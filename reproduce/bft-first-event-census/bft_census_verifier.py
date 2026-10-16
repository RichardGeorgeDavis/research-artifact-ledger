"""Independent end-of-run C12 label, forecast, and score-chain verifier.

This uses a sieve implementation separate from the runner's trial division
and from the BFT forecast module. Run only after all forecasts and required
label windows have been durably sealed.
"""

import argparse
from bisect import bisect_left, bisect_right
import hashlib
import json
import os
import sys
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

FRAME_START = 10_050_248
FRAME_END = 10_100_247
LABEL_START = 10_050_211
HISTORY_FRONTIER = 10_050_210
GENESIS = "0" * 64


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sieve(limit):
    bits = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        bits[0] = 0
    if limit >= 1:
        bits[1] = 0
    for p in range(2, isqrt(limit) + 1):
        if bits[p]:
            start = p * p
            bits[start:limit + 1:p] = b"\x00" * (((limit - start) // p) + 1)
    return bits


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
        if digest != sha256_bytes(canonical(row).encode()):
            raise ValueError(f"broken chain digest at {p}:{line_no}")
        row["record_hash"] = digest
        rows.append(row)
        previous = digest
    return rows, previous


def append_chain(path, body, previous):
    body = dict(body, previous_hash=previous)
    digest = sha256_bytes(canonical(body).encode())
    record = dict(body, record_hash=digest)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    try:
        with os.fdopen(fd, "ab", closefd=False) as out:
            out.write((canonical(record) + "\n").encode())
            out.flush()
            os.fsync(out.fileno())
    finally:
        os.close(fd)
    return digest


def rational_log_bounds_independent(n, terms):
    """Separate exact-rational implementation of the Taylor log enclosure."""
    exponent = n.bit_length() - 1
    reduced = Fraction(n, 1 << exponent)

    def atanh_log_bounds(value):
        u = (value - 1) / (value + 1)
        total = Fraction(0)
        for k in range(terms):
            total += u ** (2 * k + 1) / (2 * k + 1)
        lower = 2 * total
        tail = 2 * u ** (2 * terms + 1) / ((2 * terms + 1) * (1 - u * u))
        return lower, lower + tail

    ln2_lower, ln2_upper = atanh_log_bounds(Fraction(2))
    reduced_lower, reduced_upper = atanh_log_bounds(reduced)
    return (
        exponent * ln2_lower + reduced_lower,
        exponent * ln2_upper + reduced_upper,
    )


def cutoff_independent(n, primes, bracket):
    """Certify a recorded cutoff with independent Fraction log bounds."""
    accepted, first_rejected, terms = bracket
    if accepted is None:
        if first_rejected != 2:
            raise ValueError(f"first rejected prime must be 2 when no cutoff is accepted for n={n}")
    else:
        index = bisect_left(primes, accepted)
        if index >= len(primes) or primes[index] != accepted:
            raise ValueError(f"accepted cutoff is absent from prime stream for n={n}")
        if index + 1 >= len(primes) or primes[index + 1] != first_rejected:
            raise ValueError(f"reported cutoff primes are not consecutive for n={n}")
    lower, upper = rational_log_bounds_independent(n, terms)
    inverse_theta = Fraction(1)
    accepted_verified = None
    for q in primes:
        inverse_theta *= Fraction(q, q - 1)
        if q == accepted:
            if inverse_theta > lower:
                raise ValueError(f"accepted cutoff not below independent lower bound for n={n}")
            accepted_verified = q
        if q == first_rejected:
            if inverse_theta <= upper:
                raise ValueError(f"rejected cutoff not above independent upper bound for n={n}")
            if accepted_verified != accepted:
                raise ValueError(f"accepted cutoff prime missing before rejection for n={n}")
            return accepted, first_rejected
    if accepted is not None:
        raise ValueError(f"accepted cutoff {accepted} is absent from prime stream")
    raise ValueError(f"first rejected cutoff {first_rejected} is absent from prime stream")


def derive_cutoff_independent(n, primes):
    """Derive z(n) with independently computed exact rational enclosures."""
    terms = 2
    while True:
        lower, upper = rational_log_bounds_independent(n, terms)
        inverse_theta = Fraction(1)
        accepted = None
        unresolved = False
        for q in primes:
            inverse_theta *= Fraction(q, q - 1)
            if inverse_theta <= lower:
                accepted = q
            elif inverse_theta <= upper:
                unresolved = True
                break
            else:
                return accepted, q
        if unresolved:
            terms += 1
            continue
        raise ArithmeticError(f"independent cutoff stream ended for n={n}")


def validate_forecast_payload(row, primes):
    payload = row["payload"]
    p = row["origin"]
    law = payload["bft"]
    if law["origin"] != p:
        raise ValueError(f"BFT law origin mismatch at {p}")
    offsets = []
    h = 1
    while len(offsets) < 8:
        if gcd(p + h, 210) == 1:
            offsets.append(h)
        h += 1
    if law["candidate_offsets"] != offsets:
        raise ValueError(f"candidate sequence mismatch at origin {p}")
    if law["candidate_numbers"] != [p + h for h in offsets] or len(law["candidate_cutoffs"]) != 8:
        raise ValueError(f"candidate number/cutoff record mismatch at origin {p}")
    probabilities = [
        Fraction(int(x["numerator"]), int(x["denominator"]))
        for x in law["first_event_probabilities"]
    ]
    if len(probabilities) != 9 or any(x < 0 for x in probabilities) or sum(probabilities, Fraction(0)) != 1:
        raise ValueError(f"invalid exact probability law at origin {p}")
    selected = max(range(8), key=lambda i: (probabilities[i], -i))
    if law["selected_index_zero_based"] != selected or law["selected_offset"] != offsets[selected]:
        raise ValueError(f"argmax/tie rule mismatch at origin {p}")
    if law["outside_probability"] != law["first_event_probabilities"][-1]:
        raise ValueError(f"outside probability mismatch at origin {p}")
    # Verify all reported cutoff brackets independently. The BFT module uses
    # rational Taylor bounds; this verifier uses Decimal logarithms.
    origin_bracket = law["origin_cutoff"]
    z, next_q = cutoff_independent(p, primes, origin_bracket)
    if origin_bracket[:2] != [z, next_q]:
        raise ValueError(f"origin cutoff disagreement at {p}")
    for number, bracket in zip(law["candidate_numbers"], law["candidate_cutoffs"]):
        cz, cn = cutoff_independent(number, primes, bracket)
        if bracket[:2] != [cz, cn]:
            raise ValueError(f"candidate cutoff disagreement at {number}")
    past = payload["past_primes"]
    gaps = [b-a for a,b in zip(past,past[1:])]
    median = sorted(gaps)[2]
    unrestricted_candidates = [h for h in range(1, median + 31) if gcd(p + h, 30) == 1]
    unrestricted = min(unrestricted_candidates, key=lambda h: (abs(h-median), h))
    restricted = min(offsets, key=lambda h: (abs(h-median), h))
    expected_comparators = {
        "median5_unrestricted_mod30": unrestricted,
        "median5_restricted_first8_mod210": restricted,
        "first_mod210": offsets[0],
    }
    if payload["comparators"] != expected_comparators:
        raise ValueError(f"frozen comparator mismatch at origin {p}")
    if type(payload.get("bft_seconds")) not in (int, float) or payload["bft_seconds"] < 0:
        raise ValueError(f"missing BFT timing at origin {p}")
    return probabilities


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--score", action="store_true", help="append verified score events after all checks pass")
    args = parser.parse_args()
    directory = Path(args.data_dir)
    manifest_path = Path(args.manifest)
    freeze = json.loads((directory / "freeze.json").read_text())
    manifest = json.loads(manifest_path.read_text())
    if sha256_bytes(manifest_path.read_bytes()) != freeze["manifest_sha256"]:
        raise ValueError("historical manifest differs from frozen hash")
    if freeze["frame_start"] != FRAME_START or freeze["frame_end"] != FRAME_END or freeze["label_start"] != LABEL_START:
        raise ValueError("frozen frame does not match C12")
    root = Path(__file__).resolve().parent
    current_hashes = {
        name: sha256_bytes((root / name).read_bytes())
        for name in ("bft_exact_law.py", "bft_forecaster_worker.py", "bft_census_runner.py", "bft_census_verifier.py")
    }
    if current_hashes != freeze["source_sha256"] or sys.version != freeze["python_version"]:
        raise ValueError("source or interpreter differs from frozen run")
    repo_root = Path.cwd()
    for key in ("contract", "verification"):
        source = repo_root / manifest["historical_source"][key]
        if sha256_bytes(source.read_bytes()) != manifest["historical_source"][key + "_sha256"]:
            raise ValueError(f"historical source changed since manifest creation: {source}")
    labels, label_tip = read_chain(directory / "labels.jsonl")
    forecasts, forecast_tip = read_chain(directory / "forecasts.jsonl")
    scores, score_tip = read_chain(directory / "scores.jsonl")
    if not labels:
        raise ValueError("no label stream exists")
    first_n = labels[0]["payload"]["n"]
    last_n = labels[-1]["payload"]["n"]
    if first_n != LABEL_START or [x["payload"]["n"] for x in labels] != list(range(LABEL_START, last_n + 1)):
        raise ValueError("label chain is not a complete contiguous integer interval")
    bits = sieve(last_n)
    primes = [n for n in range(2, last_n + 1) if bits[n]]
    historical = manifest["last_six_primes"]
    historical_tail = [n for n in range(max(2, HISTORY_FRONTIER - 400), HISTORY_FRONTIER + 1) if bits[n]][-6:]
    if historical_tail != historical:
        raise ValueError("historical manifest tail does not match independent sieve")
    classified = {row["payload"]["n"]: row["payload"]["is_prime"] for row in labels}
    label_hash_by_n = {row["payload"]["n"]: row["record_hash"] for row in labels}
    if any(type(row["payload"]["is_prime"]) is not bool for row in labels):
        raise ValueError("label stream contains non-Boolean result")
    disagreements = [n for n, value in classified.items() if value != bool(bits[n])]
    if disagreements:
        raise ValueError(f"independent sieve disagrees with evaluator labels at {disagreements[:5]}")
    all_primes = historical + [n for n, value in classified.items() if value]
    all_primes.sort()
    expected_origins = []
    exclusions = []
    for p in range(FRAME_START, FRAME_END + 1):
        if bits[p]:
            z, _ = derive_cutoff_independent(p, primes)
            if p < 8 or z is None or z < 7:
                exclusions.append(p)
            else:
                expected_origins.append(p)
    if [row["origin"] for row in forecasts] != expected_origins:
        raise ValueError("forecast origins are not the complete eligible prime stream in the frozen frame")
    forecast_tip = GENESIS
    remaining_forecasts = iter(forecasts)
    next_forecast = next(remaining_forecasts, None)
    for label_row in labels:
        label = label_row["payload"]
        if label.get("forecast_tip_at_classification") != forecast_tip:
            raise ValueError(f"label {label['n']} does not bind the preceding sealed-forecast tip")
        if next_forecast is not None and next_forecast["origin"] == label["n"]:
            if next_forecast.get("origin_label_hash") != label_row["record_hash"] or next_forecast.get("previous_hash") != forecast_tip:
                raise ValueError(f"forecast at {label['n']} is not sealed against its origin label and prior tip")
            forecast_tip = next_forecast["record_hash"]
            next_forecast = next(remaining_forecasts, None)
    if next_forecast is not None or forecast_tip != (forecasts[-1]["record_hash"] if forecasts else GENESIS):
        raise ValueError("not every forecast is represented in chronological label order")
    for sequence, row in enumerate(forecasts):
        if row["sequence"] != sequence or row["history_watermark"] != row["origin"]:
            raise ValueError(f"forecast sequence or watermark mismatch at {row['origin']}")
        if row.get("source_sha256") != freeze["source_sha256"] or row.get("environment_sha256") != sha256_bytes(freeze["python_version"].encode()):
            raise ValueError(f"forecast source/environment binding mismatch at {row['origin']}")
        p = row["origin"]
        prior = all_primes[:bisect_right(all_primes, p)]
        if row["payload"]["past_primes"] != prior[-6:]:
            raise ValueError(f"forecast historical input is not the six-prime tail at {p}")
        validate_forecast_payload(row, primes)
    if forecasts:
        max_origin = forecasts[-1]["origin"]
        if last_n < max_origin + 210 or not any(n > max_origin and bits[n] for n in range(max_origin + 1, last_n + 1)):
            raise ValueError("label stream lacks a full secondary window or terminal successor")
    expected_score_bodies = []
    for row in forecasts:
        p = row["origin"]
        successor = next((n for n in range(p + 1, last_n + 1) if bits[n]), None)
        if successor is None:
            raise ValueError(f"missing successor for origin {p}")
        law = row["payload"]["bft"]
        candidates = law["candidate_numbers"]
        successor_rank = candidates.index(successor) + 1 if successor in candidates else "outside"
        proposals = {"bft": p + law["selected_offset"]}
        proposals.update({k: p + v for k, v in row["payload"]["comparators"].items()})
        expected_score_bodies.append({
            "event": "primary_scored",
            "forecast_hash": row["record_hash"],
            "origin": p,
            "successor": successor,
            "actual_successor_candidate_rank": successor_rank,
            "classification_watermark_hash": label_hash_by_n[successor],
            "outcomes": {key: int(value == successor) for key, value in proposals.items()},
            "proposal_minus_successor": {key: value - successor for key, value in proposals.items()},
            "absolute_offset_error": {key: abs(value - successor) for key, value in proposals.items()},
        })
        expected_score_bodies.append({
            "event": "secondary_scored",
            "forecast_hash": row["record_hash"],
            "origin": p,
            "classification_watermark_hash": label_hash_by_n[p + 210],
            "outcomes": {key: int(0 < value - p <= 210 and bool(bits[value])) for key, value in proposals.items()},
            "classified_through": last_n,
        })
    # Existing events must be an exact prefix; only then append missing ones.
    existing_bodies = []
    for row in scores:
        body = {k: v for k, v in row.items() if k not in ("record_hash", "previous_hash")}
        existing_bodies.append(body)
    if existing_bodies != expected_score_bodies[:len(existing_bodies)]:
        raise ValueError("existing score chain is not an exact prefix of independently verified outcomes")
    if args.score:
        for body in expected_score_bodies[len(existing_bodies):]:
            score_tip = append_chain(directory / "scores.jsonl", body, score_tip)
        scores, score_tip = read_chain(directory / "scores.jsonl")
    primary = [row for row in scores if row.get("event") == "primary_scored"]
    secondary = [row for row in scores if row.get("event") == "secondary_scored"]
    score_totals = {key: sum(row["outcomes"][key] for row in primary) for key in ("bft", "median5_unrestricted_mod30", "median5_restricted_first8_mod210", "first_mod210")}
    scores_complete = len(scores) == len(expected_score_bodies)
    if args.score and not scores_complete:
        raise ValueError("score event chain incomplete after scoring pass")
    summary = {
        "verification": "PASS" if scores_complete else "DATA_VERIFIED_UNSCORED",
        "independent_classifier": "Eratosthenes sieve; separate from runner trial division and BFT forecast module",
        "labels": len(labels),
        "label_interval": [first_n, last_n],
        "independent_label_disagreements": len(disagreements),
        "frame_prime_origins_eligible": len(expected_origins),
        "frame_prime_origins_excluded": len(exclusions),
        "forecasts": len(forecasts),
        "bft_candidates_enumerated": 8 * len(forecasts),
        "proposal_targets_within_secondary_window": sum(
            1
            for row in forecasts
            for offset in [row["payload"]["bft"]["selected_offset"], *row["payload"]["comparators"].values()]
            if 0 < offset <= 210
        ),
        "unique_integers_classified": len(labels),
        "score_events": len(scores),
        "primary_hit_totals": score_totals if scores_complete else None,
        "secondary_any_prime_hit_totals": {
            key: sum(row["outcomes"][key] for row in secondary)
            for key in ("bft", "median5_unrestricted_mod30", "median5_restricted_first8_mod210", "first_mod210")
        } if scores_complete else None,
        "primary_rates": {key: value / len(primary) for key, value in score_totals.items()} if scores_complete and primary else None,
        "primary_bft_minus_unrestricted_median": score_totals["bft"] - score_totals["median5_unrestricted_mod30"] if scores_complete else None,
        "bft_seconds_sum": sum(float(row["payload"]["bft_seconds"]) for row in forecasts),
        "comparator_seconds_sum": sum(float(row["payload"]["comparator_seconds"]) for row in forecasts),
        "proposal_verification_compute": "shared with the chronological range classifier; no per-proposal compute attribution is available",
        "forecast_tip": forecast_tip,
        "label_tip": label_tip,
        "score_tip": score_tip,
        "data_sha256": {name: sha256_bytes((directory / name).read_bytes()) for name in ("forecasts.jsonl", "labels.jsonl", "scores.jsonl")},
        "note": "Finite fixed-frame result only; no asymptotic, causal, calibrated-probability, or generalisation claim."
    }
    (directory / "verification-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
