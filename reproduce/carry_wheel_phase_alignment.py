#!/usr/bin/env python3
"""Finite checks for decimal carry and mod-30/mod-210 wheel alignment."""
from math import gcd, lcm


for modulus, phi, period_multiplier in ((30, 8, 3), (210, 48, 21)):
    for digits in (1, 2, 3):
        decimal_modulus = 10**digits
        period = lcm(decimal_modulus, modulus)
        states = {(t % decimal_modulus, t % modulus) for t in range(period)}
        compatible = {
            (decimal_residue, wheel_residue)
            for decimal_residue in range(decimal_modulus)
            for wheel_residue in range(modulus)
            if (decimal_residue - wheel_residue) % 10 == 0
        }
        survivor_count = sum(gcd(t, modulus) == 1 for t in range(period))

        assert period == period_multiplier * decimal_modulus
        assert len(states) == len(compatible) == period
        assert survivor_count == phi * 10 ** (digits - 1)

        for carry_places in range(1, digits + 1):
            carry_period = lcm(10**carry_places, modulus)
            wheel_phases = {
                t % modulus for t in range(0, carry_period, 10**carry_places)
            }
            assert len(wheel_phases) == period_multiplier
            assert all(gcd(phase, modulus) > 1 for phase in wheel_phases)
            assert not any(
                gcd(t, modulus) == 1
                for t in range(0, period, 10**carry_places)
            )

        per_decimal_state = {}
        for t in range(period):
            if gcd(t, modulus) == 1:
                key = (t % decimal_modulus, t % 10)
                per_decimal_state[key] = per_decimal_state.get(key, 0) + 1

        for decimal_residue in range(decimal_modulus):
            expected = phi // 4 if decimal_residue % 10 in (1, 3, 7, 9) else 0
            assert per_decimal_state.get((decimal_residue, decimal_residue % 10), 0) == expected

        if digits == 2:
            assert (37, 8) not in states

print(
    "PASS: k=1..3; moduli=30,210; joint periods, compatibility, "
    "survivor counts and carry rejection"
)
