"""Chronological C12 runner with separate immutable forecast/score chains.

This is cooperative process separation, not an OS sandbox. Do not use with an
unfrozen frame or an input history manifest other than the approved C12 packet.
"""

import argparse
import hashlib
import json
import math
import os
import subprocess
import sys
import time
from pathlib import Path

FRAME_START = 10_050_248
FRAME_END = 10_100_247
LABEL_START = 10_050_211
GENESIS = "0" * 64


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def is_prime_trial(n):
    """Odd trial division, used only by this evaluator process."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = math.isqrt(n)
    d = 3
    while d <= limit:
        if n % d == 0:
            return False
        d += 2
    return True


def append_chained(path, body, previous_hash):
    body = dict(body)
    body["previous_hash"] = previous_hash
    digest = sha256_bytes(canonical(body).encode())
    record = dict(body, record_hash=digest)
    payload = (canonical(record) + "\n").encode()
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    try:
        with os.fdopen(fd, "ab", closefd=False) as out:
            out.write(payload)
            out.flush()
            os.fsync(out.fileno())
    finally:
        os.close(fd)
    return digest


def read_chain(path):
    previous = GENESIS
    rows = []
    p = Path(path)
    if not p.exists():
        return rows, previous
    for line_no, line in enumerate(p.read_text().splitlines(), 1):
        row = json.loads(line)
        digest = row.pop("record_hash")
        if row.get("previous_hash") != previous:
            raise ValueError(f"broken chain predecessor at {p}:{line_no}")
        expected = sha256_bytes(canonical(row).encode())
        if digest != expected:
            raise ValueError(f"broken chain digest at {p}:{line_no}")
        row["record_hash"] = digest
        rows.append(row)
        previous = digest
    return rows, previous


def worker_call(worker, request):
    proc = subprocess.run(
        [sys.executable, str(worker)], input=canonical(request) + "\n",
        text=True, capture_output=True, check=True,
    )
    lines = proc.stdout.splitlines()
    if len(lines) != 1:
        raise ValueError("worker must return exactly one JSON line")
    result = json.loads(lines[0])
    if result.get("request_id") != request["request_id"]:
        raise ValueError("worker response request_id mismatch")
    return result


def primary_score(forecast, successor):
    bft = forecast["payload"]["bft"]["origin"] + forecast["payload"]["bft"]["selected_offset"]
    comps = forecast["payload"]["comparators"]
    p = forecast["payload"]["bft"]["origin"]
    predicted = {"bft": bft, **{k: p + v for k, v in comps.items()}}
    return {
        "event": "primary_scored",
        "forecast_hash": forecast["record_hash"],
        "origin": p,
        "successor": successor,
        "outcomes": {key: int(value == successor) for key, value in predicted.items()},
        "proposal_minus_successor": {key: value - successor for key, value in predicted.items()},
        "absolute_offset_error": {key: abs(value - successor) for key, value in predicted.items()},
    }


def secondary_score(forecast, classified):
    payload = forecast["payload"]
    p = payload["bft"]["origin"]
    proposals = {"bft": payload["bft"]["origin"] + payload["bft"]["selected_offset"]}
    proposals.update({k: p + v for k, v in payload["comparators"].items()})
    outcomes = {}
    for key, value in proposals.items():
        outcomes[key] = int(0 < value - p <= 210 and classified.get(value) is True)
    return {
        "event": "secondary_scored",
        "forecast_hash": forecast["record_hash"],
        "origin": p,
        "outcomes": outcomes,
        "classified_through": max(classified),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--prepare", action="store_true", help="freeze source and empty journals; classifies no integers")
    parser.add_argument("--activate", action="store_true", help="start/resume C12 after independent pre-run review")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    data_dir = Path(args.data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = Path(args.manifest)
    manifest = json.loads(manifest_path.read_text())
    if manifest.get("frame_start") != FRAME_START or manifest.get("frame_end") != FRAME_END:
        raise ValueError("manifest does not match frozen C12 frame")
    if manifest.get("label_start") != LABEL_START or manifest.get("history_watermark") != LABEL_START - 1:
        raise ValueError("manifest does not match frozen historical watermark")
    historical = manifest.get("last_six_primes")
    if type(historical) is not list or len(historical) != 6 or any(type(x) is not int for x in historical):
        raise ValueError("manifest must contain exactly six integer historical primes")
    if any(a >= b for a, b in zip(historical, historical[1:])):
        raise ValueError("historical manifest inputs must be strictly increasing")
    if historical[-1] > manifest["history_watermark"]:
        raise ValueError("historical prime exceeds the frozen watermark")
    for key in ("contract", "verification"):
        source = Path(manifest["historical_source"][key])
        if sha256_bytes(source.read_bytes()) != manifest["historical_source"][key + "_sha256"]:
            raise ValueError(f"historical source changed since manifest creation: {source}")
    worker = root / "bft_forecaster_worker.py"
    forecast_path = data_dir / "forecasts.jsonl"
    score_path = data_dir / "scores.jsonl"
    label_path = data_dir / "labels.jsonl"
    freeze = data_dir / "freeze.json"
    forecasts, forecast_tip = read_chain(forecast_path)
    scores, score_tip = read_chain(score_path)
    labels, label_tip = read_chain(label_path)
    if args.prepare:
        if freeze.exists() or forecasts or scores or labels:
            raise ValueError("preparation requires a fresh directory; preserve existing records")
        source_hashes = {
            name: sha256_bytes((root / name).read_bytes())
            for name in ("bft_exact_law.py", "bft_forecaster_worker.py", "bft_census_runner.py", "bft_census_verifier.py")
        }
        freeze_data = {
            "frame_start": FRAME_START,
            "frame_end": FRAME_END,
            "label_start": LABEL_START,
            "history_watermark": manifest["history_watermark"],
            "manifest_sha256": sha256_bytes(manifest_path.read_bytes()),
            "source_sha256": source_hashes,
            "python_version": sys.version,
            "journal_schema": "C12-jsonl-chain-v1",
            "forecasts_genesis": GENESIS,
            "scores_genesis": GENESIS,
            "labels_genesis": GENESIS,
            "state": "prepared-awaiting-independent-review",
        }
        temp = freeze.with_suffix(".tmp")
        temp.write_text(canonical(freeze_data) + "\n")
        with temp.open("rb") as handle:
            os.fsync(handle.fileno())
        os.replace(temp, freeze)
        for path in (forecast_path, score_path, label_path):
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            os.fsync(fd)
            os.close(fd)
        print(json.dumps({"preparation": "PASS", "frame": [FRAME_START, FRAME_END], "source_sha256": source_hashes, "manifest_sha256": freeze_data["manifest_sha256"], "target_labels_opened": False}, sort_keys=True))
        return
    if not args.activate:
        print(json.dumps({"preflight": "PASS", "frame": [FRAME_START, FRAME_END], "label_start": LABEL_START, "existing_forecasts": len(forecasts), "existing_scores": len(scores), "existing_labels": len(labels)}, sort_keys=True))
        return

    if not freeze.exists():
        raise ValueError("activation requires a prepared freeze")
    freeze_data = json.loads(freeze.read_text())
    if freeze_data.get("state") != "prepared-awaiting-independent-review":
        raise ValueError("freeze state is not prepared for activation")
    current_hashes = {
        name: sha256_bytes((root / name).read_bytes())
        for name in ("bft_exact_law.py", "bft_forecaster_worker.py", "bft_census_runner.py", "bft_census_verifier.py")
    }
    if current_hashes != freeze_data["source_sha256"] or sha256_bytes(manifest_path.read_bytes()) != freeze_data["manifest_sha256"] or sys.version != freeze_data["python_version"]:
        raise ValueError("frozen source or manifest changed; create a new version and review it")
    if scores:
        raise ValueError("score chain already exists; resume scoring only with the independent verifier")

    # This runner currently creates forecasts and labels prospectively. Scoring
    # is performed only by the separate verifier after the frame is fully sealed.
    # It never computes a future origin list or target outcome in advance.
    primes = list(historical)
    last_n = LABEL_START - 1
    if labels:
        last_n = labels[-1]["payload"]["n"]
        if labels[-1]["payload"]["n"] < LABEL_START - 1:
            raise ValueError("label checkpoint precedes frozen watermark")
        for row in labels:
            entry = row["payload"]
            if entry["n"] != LABEL_START + entry["sequence"] or type(entry["is_prime"]) is not bool:
                raise ValueError("label sequence is not contiguous or its value is not Boolean")
            if entry["n"] >= LABEL_START and entry["is_prime"]:
                primes.append(entry["n"])
        if [row["payload"]["n"] for row in labels] != list(range(LABEL_START, last_n + 1)):
            raise ValueError("label chain is not a contiguous integer prefix")
    # Forecast chain must be a prefix of prime labels already sealed at each
    # origin, with no duplicate or skipped forecast sequence numbers.
    known_forecast_origins = {row["origin"] for row in forecasts}
    if len(known_forecast_origins) != len(forecasts):
        raise ValueError("duplicate forecast origin in journal")
    if any(row["sequence"] != i for i, row in enumerate(forecasts)):
        raise ValueError("forecast sequence is not contiguous")
    if any(row["origin"] > last_n for row in forecasts):
        raise ValueError("forecast exists beyond the durable classification watermark")
    started = time.time()
    label_hash_by_n = {row["payload"]["n"]: row["record_hash"] for row in labels}

    current_forecast_tip = GENESIS
    existing_forecasts = iter(forecasts)
    next_forecast = next(existing_forecasts, None)
    for label_row in labels:
        label = label_row["payload"]
        if label.get("forecast_tip_at_classification") != current_forecast_tip:
            raise ValueError(f"classification at {label['n']} does not bind the preceding forecast tip")
        if next_forecast is not None and next_forecast["origin"] == label["n"]:
            if next_forecast.get("origin_label_hash") != label_row["record_hash"] or next_forecast.get("previous_hash") != current_forecast_tip:
                raise ValueError(f"forecast at {label['n']} is not sealed against its label and prior tip")
            current_forecast_tip = next_forecast["record_hash"]
            next_forecast = next(existing_forecasts, None)
    if next_forecast is not None:
        raise ValueError("forecast chain contains an origin absent from the label prefix")
    for row in forecasts:
        origin = row["origin"]
        if origin not in label_hash_by_n or not labels[origin - LABEL_START]["payload"]["is_prime"]:
            raise ValueError(f"forecast origin {origin} lacks a corresponding prime label")
        if row.get("origin_label_hash") != label_hash_by_n[origin] or row["history_watermark"] != origin:
            raise ValueError(f"forecast origin {origin} is not bound to its label/watermark")
        if row.get("source_sha256") != freeze_data["source_sha256"] or row.get("environment_sha256") != sha256_bytes(freeze_data["python_version"].encode()):
            raise ValueError(f"forecast source/environment binding mismatch at {origin}")

    # Refuse to advance past any eligible prime whose forecast is absent. The
    # sole repairable gap is an eligible final prime label with no later label.
    for row in labels:
        n = row["payload"]["n"]
        if FRAME_START <= n <= FRAME_END and row["payload"]["is_prime"]:
            z, _, _ = __import__("bft_exact_law").certified_cutoff(n)
            if z >= 7 and n not in known_forecast_origins and n != last_n:
                raise ValueError(f"eligible origin {n} lacks a sealed forecast before later labels")

    def seal_if_eligible(n):
        nonlocal forecasts, forecast_tip
        if n < FRAME_START or n > FRAME_END or n in known_forecast_origins:
            return
        z, _, _ = __import__("bft_exact_law").certified_cutoff(n)
        if n < 8 or z < 7:
            return
        request = {
            "request_id": f"C12-{n}",
            "origin": n,
            "history_watermark": n,
            "past_primes": primes[-6:],
        }
        payload = worker_call(worker, request)
        forecast_body = {
            "sequence": len(forecasts),
            "origin": n,
            "history_watermark": n,
            "origin_label_hash": label_hash_by_n[n],
            "payload": payload,
            "source_sha256": freeze_data["source_sha256"],
            "environment_sha256": sha256_bytes(sys.version.encode()),
        }
        forecast_tip = append_chained(forecast_path, forecast_body, forecast_tip)
        forecasts, forecast_tip = read_chain(forecast_path)
        known_forecast_origins.add(n)
        print(json.dumps({"sealed_forecast": n, "sequence": len(forecasts)-1, "elapsed_seconds": round(time.time()-started, 3)}, sort_keys=True), flush=True)

    # If interrupted immediately after classifying an origin but before its
    # forecast was durably sealed, finish that forecast before any new label.
    if last_n >= FRAME_START and labels and labels[-1]["payload"]["is_prime"]:
        seal_if_eligible(last_n)

    for n in range(max(LABEL_START, last_n + 1), FRAME_END + 1):
        prime = is_prime_trial(n)
        label_body = {"payload": {"kind": "classification", "n": n, "is_prime": prime, "method": "odd_trial_division", "sequence": n - LABEL_START, "forecast_tip_at_classification": forecast_tip}}
        label_tip = append_chained(label_path, label_body, label_tip)
        label_hash_by_n[n] = label_tip
        last_n = n
        if prime:
            primes.append(n)
            seal_if_eligible(n)

    # Once every in-frame origin forecast is sealed, continue classification
    # until every secondary window and the final-origin successor are known.
    forecasts, forecast_tip = read_chain(forecast_path)
    if forecasts:
        max_origin = max(row["origin"] for row in forecasts)
        saw_successor = any(p > max_origin for p in primes)
        n = max(FRAME_END + 1, last_n + 1)
        while n <= max_origin + 210 or not saw_successor:
            prime = is_prime_trial(n)
            label_body = {"payload": {"kind": "classification", "n": n, "is_prime": prime, "method": "odd_trial_division", "sequence": n - LABEL_START, "forecast_tip_at_classification": forecast_tip}}
            label_tip = append_chained(label_path, label_body, label_tip)
            last_n = n
            if prime:
                primes.append(n)
                if n > max_origin:
                    saw_successor = True
            n += 1
    else:
        last_n = FRAME_END
    print(json.dumps({"frame_forecast_pass": "COMPLETE", "forecasts": len(known_forecast_origins), "labels_through": last_n, "forecast_tip": forecast_tip, "label_tip": label_tip, "seconds": round(time.time()-started,3), "next_step": "independent verifier reclassifies, validates completeness, and writes append-only score events"}, sort_keys=True))


if __name__ == "__main__":
    main()
