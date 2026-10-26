#!/usr/bin/env python3
"""Bounded comparative implementations for prime enumeration through N."""
import heapq
import json
import math
import platform
import statistics
import sys
import time
import tracemalloc
from pathlib import Path

N = 20_000
SEGMENT = 4096
REPEATS = 5
MEMORY_CAP = 256 * 1024 * 1024


def clockwork(n, count_ops=True):
    primes, residues = [], []
    updates = 0
    for value in range(2, n + 1):
        ringing = False
        for i, p in enumerate(primes):
            r = residues[i] + 1
            if r == p:
                r = 0
                ringing = True
            residues[i] = r
            if count_ops:
                updates += 1
        if not ringing:
            primes.append(value)
            residues.append(0)
    return primes, ({"clock_updates": updates} if count_ops else {})


def event_heap(n, count_ops=True):
    primes = []
    events = []
    marks = 0
    for value in range(2, n + 1):
        marked = False
        while events and events[0][0] == value:
            multiple, p = heapq.heappop(events)
            heapq.heappush(events, (multiple + p, p))
            if count_ops:
                marks += 1
            marked = True
        if not marked:
            primes.append(value)
            heapq.heappush(events, (value * value, value))
    return primes, (
        {"composite_marks": marks, "heap_pushes_pops": 2 * marks + len(primes)}
        if count_ops else {}
    )


def segmented(n, count_ops=True):
    limit = math.isqrt(n)
    base = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        base[0] = 0
    if limit >= 1:
        base[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if base[p]:
            base[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    base_primes = [p for p in range(2, limit + 1) if base[p]]
    out, marks = [], 0
    for low in range(2, n + 1, SEGMENT):
        high = min(low + SEGMENT, n + 1)
        flags = bytearray(b"\x01") * (high - low)
        for p in base_primes:
            start = max(p * p, ((low + p - 1) // p) * p)
            if start >= high:
                continue
            count = ((high - 1 - start) // p) + 1
            if count_ops:
                marks += count
            flags[start - low : high - low : p] = b"\x00" * count
        out.extend(low + i for i, flag in enumerate(flags) if flag)
    return out, (
        {"composite_marks": marks, "segment_width": SEGMENT, "base_prime_count": len(base_primes)}
        if count_ops else {}
    )


def reference(n):
    out = []
    for value in range(2, n + 1):
        prime = True
        for divisor in range(2, math.isqrt(value) + 1):
            if value % divisor == 0:
                prime = False
                break
        if prime:
            out.append(value)
    return out


def main():
    funcs = {"clockwork": clockwork, "event_heap": event_heap, "segmented": segmented}
    expected = reference(N)
    validation = {}
    for name, fn in funcs.items():
        out, _ = fn(N)
        validation[name] = {
            "equal_to_independent_trial_division": out == expected,
            "prime_count": len(out),
        }
        if out != expected:
            raise SystemExit(f"validation failed: {name}")
    timings = {name: [] for name in funcs}
    counters, peaks = {}, {}
    names = list(funcs)
    for name, fn in funcs.items():
        _, counters[name] = fn(N, count_ops=True)
        fn(N, count_ops=False)
    for shift in range(REPEATS):
        order = names[shift % len(names) :] + names[: shift % len(names)]
        for name in order:
            start = time.perf_counter()
            funcs[name](N, count_ops=False)
            elapsed = time.perf_counter() - start
            timings[name].append(elapsed)
            if elapsed > 30:
                raise SystemExit(f"per-run time cap exceeded: {name}")
    timing_summary = {
        name: {"seconds": samples, "median_seconds": statistics.median(samples)}
        for name, samples in timings.items()
    }
    for name, fn in funcs.items():
        tracemalloc.start()
        fn(N, count_ops=False)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        peaks[name] = peak
        if peak > MEMORY_CAP:
            raise SystemExit(f"memory threshold exceeded: {name}")
    result = {
        "N": N,
        "segment_width": SEGMENT,
        "repeats": REPEATS,
        "per_run_time_cap_seconds": 30,
        "tracemalloc_memory_threshold_bytes": MEMORY_CAP,
        "python": sys.version,
        "platform": platform.platform(),
        "validation": validation,
        "counters": counters,
        "timings": timing_summary,
        "tracemalloc_peak_bytes": peaks,
    }
    output_path = Path(__file__).with_name("reproduction-results.json")
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
