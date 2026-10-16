#!/usr/bin/env python3
"""Aggregate-only audit that the BFT selected proposal is the first mod-210 survivor."""
import json
import math
import sys

path = sys.argv[1]
records = 0
mismatches = 0
selected_zero = 0
for line in open(path, encoding="utf-8"):
    row = json.loads(line)
    p = row["origin"]
    payload = row["payload"]
    law = payload["bft"]
    expected = []
    h = 1
    while len(expected) < 8:
        if math.gcd(p + h, 210) == 1:
            expected.append(h)
        h += 1
    if law["candidate_offsets"] != expected:
        mismatches += 1
    if law["selected_index_zero_based"] == 0:
        selected_zero += 1
    if law["selected_index_zero_based"] != 0 or law["selected_offset"] != expected[0]:
        mismatches += 1
    if payload["comparators"]["first_mod210"] != expected[0]:
        mismatches += 1
    records += 1
print(json.dumps({
    "audit": "first-mod210-proposal-equivalence",
    "records": records,
    "selected_index_zero_records": selected_zero,
    "mismatches": mismatches,
    "verification": "PASS" if records == 3111 and selected_zero == 3111 and mismatches == 0 else "FAIL"
}, sort_keys=True))
if records != 3111 or selected_zero != 3111 or mismatches != 0:
    raise SystemExit(1)
