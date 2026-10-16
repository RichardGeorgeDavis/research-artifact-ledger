"""Line-oriented forecast worker; it receives no verifier or future labels."""

import json
import sys
from time import perf_counter

def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


for line in sys.stdin:
    request = json.loads(line, object_pairs_hook=reject_duplicate_keys)
    expected_keys = {
        "request_id",
        "origin",
        "history_watermark",
        "past_primes",
    }
    if not isinstance(request, dict) or set(request) != expected_keys:
        raise ValueError("request must contain exactly the frozen input fields")
    if type(request.get("request_id")) is not str or not request["request_id"]:
        raise ValueError("request_id must be a non-empty string")
    if type(request.get("origin")) is not int:
        raise TypeError("origin must be a JSON integer")
    if type(request.get("history_watermark")) is not int:
        raise TypeError("history_watermark must be a JSON integer")
    past_primes = request.get("past_primes")
    if (
        not isinstance(past_primes, list)
        or len(past_primes) != 6
        or any(type(value) is not int for value in past_primes)
    ):
        raise TypeError("past_primes must contain exactly six JSON integers")
    if past_primes[-1] != request["origin"]:
        raise ValueError("historical input must end at the current origin")
    if past_primes[0] < 2:
        raise ValueError("historical prime inputs must be at least two")
    if request["history_watermark"] != request["origin"]:
        raise ValueError("history watermark must equal the origin")
    if any(a >= b for a, b in zip(past_primes, past_primes[1:])):
        raise ValueError("historical prime inputs must be strictly increasing")
    past_gaps = [b - a for a, b in zip(past_primes, past_primes[1:])]
    started = perf_counter()
    law = __import__("bft_exact_law").bft_distribution(request["origin"])
    bft_seconds = perf_counter() - started
    comparator_started = perf_counter()
    comparators = __import__("bft_exact_law").comparator_offsets(
        request["origin"], past_gaps, law["candidate_offsets"]
    )
    comparator_seconds = perf_counter() - comparator_started
    result = {"bft": law, "comparators": comparators}
    result["request_id"] = request["request_id"]
    result["history_watermark"] = request["history_watermark"]
    result["past_primes"] = past_primes
    result["bft_seconds"] = bft_seconds
    result["comparator_seconds"] = comparator_seconds
    result["forecast_seconds"] = perf_counter() - started
    print(json.dumps(result, separators=(",", ":"), sort_keys=True), flush=True)
