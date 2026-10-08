#!/usr/bin/env python3
"""Reproduce the published finite singular-series shortlist screen."""
from bisect import bisect_left
from decimal import Decimal, ROUND_FLOOR, localcontext
from fractions import Fraction
from math import gcd, isqrt
import json

START_ORIGIN = 1_743_433
ORIGIN_COUNT = 10_000
POOL_SIZE = 8
OUTPUT_SIZE = 5
WHEEL = 210
SIEVE_LIMIT = 2_000_000


def primes_to(limit: int) -> tuple[list[int], bytearray]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [n for n, flag in enumerate(flags) if flag], flags


def candidate_pool(origin: int) -> list[int]:
    pool = []
    n = origin + 1
    while len(pool) < POOL_SIZE:
        if gcd(n, WHEEL) == 1:
            pool.append(n)
        n += 1
    return pool


def singular_score(offset: int) -> Fraction:
    """Variable part of the even-gap two-prime singular series."""
    remaining = offset
    while remaining % 2 == 0:
        remaining //= 2
    score = Fraction(1, 1)
    factor = 3
    while factor * factor <= remaining:
        if remaining % factor == 0:
            score *= Fraction(factor - 1, factor - 2)
            while remaining % factor == 0:
                remaining //= factor
        factor += 2
    if remaining > 2:
        score *= Fraction(remaining - 1, remaining - 2)
    return score


def rounded_log_gap(origin: int) -> int:
    with localcontext() as ctx:
        ctx.prec = 80
        value = Decimal(origin).ln()
        lower = int((value / 2).to_integral_value(rounding=ROUND_FLOOR)) * 2
        lower = max(2, lower)
        boundary = Decimal(lower + 1)
        if value == boundary or abs(value - boundary) < Decimal("1e-70"):
            raise ArithmeticError("log value too close to a rounding boundary")
        return lower if value < boundary else lower + 2


def ranked_lists(origin: int, pool: list[int]) -> dict[str, list[int]]:
    density_gap = rounded_log_gap(origin)
    singular = sorted(pool, key=lambda n: (-singular_score(n - origin), n))
    density = sorted(pool, key=lambda n: (abs((n - origin) - density_gap), n))
    return {
        "singular_series": singular[:OUTPUT_SIZE],
        "wheel_order": pool[:OUTPUT_SIZE],
        "rounded_log_density": density[:OUTPUT_SIZE],
    }


def main() -> None:
    primes, is_prime = primes_to(SIEVE_LIMIT)
    start = bisect_left(primes, START_ORIGIN)
    if start == len(primes) or primes[start] != START_ORIGIN:
        raise AssertionError("declared first origin is absent from the prime sieve")
    if start == 0 or primes[start - 1] >= START_ORIGIN:
        raise AssertionError("origin anchor is not the first prime at or above the declared start")
    if start + ORIGIN_COUNT >= len(primes):
        raise AssertionError("sieve bound does not contain all origins and successors")

    hits = {name: 0 for name in ("singular_series", "wheel_order", "rounded_log_density")}
    conditional_hits = dict.fromkeys(hits, 0)
    prime_slots = dict.fromkeys(hits, 0)
    rank_one_hits = dict.fromkeys(hits, 0)
    rank_one_distance = dict.fromkeys(hits, 0)
    paired = {"SS_only": 0, "wheel_only": 0, "density_only": 0,
              "SS_and_wheel_only": 0, "SS_and_density_only": 0,
              "wheel_and_density_only": 0, "all_hit": 0, "none_hit": 0}
    in_pool_count = 0
    maximum_classified = 0
    final_target = None

    for i in range(ORIGIN_COUNT):
        origin = primes[start + i]
        target = primes[start + i + 1]
        pool = candidate_pool(origin)
        ranked = ranked_lists(origin, pool)
        in_pool = target in pool
        in_pool_count += int(in_pool)
        final_target = target
        maximum_classified = max(maximum_classified, target, pool[-1])
        outcomes = {}
        for name, selected in ranked.items():
            hit = target in selected
            outcomes[name] = hit
            hits[name] += int(hit)
            conditional_hits[name] += int(hit and in_pool)
            rank_one_hits[name] += int(selected[0] == target)
            rank_one_distance[name] += abs(selected[0] - target)
            prime_slots[name] += sum(bool(is_prime[n]) for n in selected)
        mask = (outcomes["singular_series"], outcomes["wheel_order"], outcomes["rounded_log_density"])
        key = {(1, 0, 0): "SS_only", (0, 1, 0): "wheel_only", (0, 0, 1): "density_only",
               (1, 1, 0): "SS_and_wheel_only", (1, 0, 1): "SS_and_density_only",
               (0, 1, 1): "wheel_and_density_only", (1, 1, 1): "all_hit", (0, 0, 0): "none_hit"}[mask]
        paired[key] += 1

    result = {
        "status": "REPRODUCED",
        "origins": ORIGIN_COUNT,
        "first_origin": primes[start],
        "final_target": final_target,
        "maximum_candidate_or_target_classified": maximum_classified,
        "successor_in_pool": in_pool_count,
        "successor_out_of_pool": ORIGIN_COUNT - in_pool_count,
        "recall_at_5_hits": hits,
        "recall_at_5_rates": {name: round(value / ORIGIN_COUNT, 4) for name, value in hits.items()},
        "conditional_recall_at_5_hits": conditional_hits,
        "conditional_denominator": in_pool_count,
        "rank_one_exact_hits": rank_one_hits,
        "rank_one_absolute_distance_sum": rank_one_distance,
        "prime_output_slots_of_50000": prime_slots,
        "paired_outcome_cells": paired,
        "singular_minus_wheel_hits": hits["singular_series"] - hits["wheel_order"],
        "singular_minus_density_hits": hits["singular_series"] - hits["rounded_log_density"],
    }

    expected = {
        "recall_at_5_hits": {"singular_series": 5579, "wheel_order": 8400, "rounded_log_density": 7973},
        "successor_in_pool": 9505,
        "rank_one_exact_hits": {"singular_series": 694, "wheel_order": 2889, "rounded_log_density": 1508},
        "prime_output_slots_of_50000": {"singular_series": 14643, "wheel_order": 14628, "rounded_log_density": 14634},
        "paired_outcome_cells": {"SS_only": 573, "wheel_only": 508, "density_only": 0,
                                  "SS_and_wheel_only": 0, "SS_and_density_only": 81,
                                  "wheel_and_density_only": 2967, "all_hit": 4925, "none_hit": 946},
        "singular_minus_wheel_hits": -2821,
        "singular_minus_density_hits": -2394,
    }
    for key, value in expected.items():
        if result[key] != value:
            raise AssertionError(f"reproduction mismatch for {key}: expected {value}, got {result[key]}")
    if result["first_origin"] != START_ORIGIN or final_target != 1_886_993:
        raise AssertionError("block endpoint mismatch")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: all declared result checks match.")


if __name__ == "__main__":
    main()
