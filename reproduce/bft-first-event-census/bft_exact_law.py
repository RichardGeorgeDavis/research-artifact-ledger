"""Pure exact BFT first-event law and frozen one-proposal comparators.

This module never classifies integers as prime and does not read evaluation
labels. Actual-origin classification belongs to the separate verifier.
"""

from fractions import Fraction
from math import gcd, isqrt

WHEEL = 210
WHEEL_PRIMES = {2, 3, 5, 7}
K = 8


def prime_stream():
    """Yield primes incrementally; no fixed search ceiling is imposed."""
    yield 2
    found = [2]
    candidate = 3
    while True:
        for divisor in found:
            if divisor * divisor > candidate:
                found.append(candidate)
                yield candidate
                break
            if candidate % divisor == 0:
                break
        candidate += 2


def log_bounds(n, terms):
    """Rational lower and upper bounds for log(n), n >= 2."""
    exponent = n.bit_length() - 1
    reduced = Fraction(n, 2**exponent)

    def series(value):
        u = (value - 1) / (value + 1)
        partial = sum(
            (u ** (2 * k + 1) / (2 * k + 1) for k in range(terms)),
            Fraction(0),
        ) * 2
        remainder = 2 * u ** (2 * terms + 1) / (
            (2 * terms + 1) * (1 - u * u)
        )
        return partial, partial + remainder

    ln2_lo, ln2_hi = series(Fraction(2))
    lnr_lo, lnr_hi = series(reduced)
    return exponent * ln2_lo + lnr_lo, exponent * ln2_hi + lnr_hi


def certified_cutoff(n):
    """Certify max q with product_{r<=q}(1-1/r)^-1 <= log(n).

    Return (accepted prime, first rejected prime, Taylor terms). Refine the
    rational logarithm interval until the next threshold is resolved.
    """
    if n < 2:
        raise ValueError("cutoff requires n >= 2")
    terms = 2
    while True:
        lower, upper = log_bounds(n, terms)
        inverse_theta = Fraction(1)
        accepted = None
        unresolved = False
        for q in prime_stream():
            inverse_theta *= Fraction(q, q - 1)
            if inverse_theta <= lower:
                accepted = q
            elif inverse_theta <= upper:
                unresolved = True
                break
            else:
                if accepted is None:
                    return None, q, terms
                return accepted, q, terms
        if unresolved:
            terms += 1
            continue
        raise ArithmeticError("prime stream ended before a cutoff was resolved")


def first_wheel_offsets(p, count=K):
    if gcd(p, WHEEL) != 1:
        raise ValueError("origin must survive the mod-210 wheel")
    found = []
    h = 1
    while len(found) < count:
        if gcd(p + h, WHEEL) == 1:
            found.append(h)
        h += 1
    return found


def primes_up_to(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for n in range(2, isqrt(limit) + 1):
        if sieve[n]:
            start = n * n
            sieve[start:limit + 1:n] = b"\x00" * (
                ((limit - start) // n) + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def allowed_residues(q, p, origin_cutoff):
    if q in WHEEL_PRIMES:
        return (0,)
    if q <= origin_cutoff:
        return tuple(r for r in range(q) if r != p % q)
    return tuple(range(q))


def first_event_probabilities(p, offsets, cutoffs, primes, origin_cutoff):
    k = len(offsets)
    if k != len(cutoffs):
        raise ValueError("each candidate needs one cutoff")
    numbers = [p + h for h in offsets]
    max_cutoff = max(cutoffs)
    joint = [Fraction(1)] * (1 << k)
    for q in primes:
        if q > max_cutoff:
            break
        allowed = allowed_residues(q, p, origin_cutoff)
        active = [i for i, z in enumerate(cutoffs) if q <= z]
        residue_bits = {}
        for i in active:
            residue = numbers[i] % q
            if residue in allowed:
                residue_bits[residue] = residue_bits.get(residue, 0) | (1 << i)
        for mask in range(1, 1 << k):
            distinct_relevant = sum(
                1 for bits in residue_bits.values() if mask & bits
            )
            if distinct_relevant:
                joint[mask] *= Fraction(
                    len(allowed) - distinct_relevant, len(allowed)
                )

    first = []
    for i in range(k):
        value = Fraction(0)
        for subset in range(1 << i):
            mask = 1 << i
            for j in range(i):
                if subset & (1 << j):
                    mask |= 1 << j
            value += (-1) ** subset.bit_count() * joint[mask]
        first.append(value)
    outside = Fraction(0)
    for mask in range(1 << k):
        outside += (-1) ** mask.bit_count() * joint[mask]
    outcomes = first + [outside]
    if any(value < 0 for value in outcomes) or sum(outcomes, Fraction(0)) != 1:
        raise ArithmeticError("first-event distribution failed exact checks")
    return outcomes


def bft_distribution(p):
    offsets = first_wheel_offsets(p)
    candidate_numbers = [p + h for h in offsets]
    cutoff_records = [certified_cutoff(n) for n in candidate_numbers]
    origin_record = certified_cutoff(p)
    origin_cutoff = origin_record[0]
    cutoffs = [record[0] for record in cutoff_records]
    if origin_cutoff is None or any(z is None for z in cutoffs):
        raise ArithmeticError("one or more BFT cutoffs were unresolved")
    if origin_cutoff < 7:
        raise ValueError("origin cutoff does not activate the wheel primes")
    primes = primes_up_to(max(cutoffs))
    probabilities = first_event_probabilities(
        p, offsets, cutoffs, primes, origin_cutoff
    )
    model_index = max(range(K), key=lambda i: (probabilities[i], -i))
    return {
        "origin": p,
        "candidate_offsets": offsets,
        "candidate_numbers": candidate_numbers,
        "origin_cutoff": origin_record,
        "candidate_cutoffs": cutoff_records,
        "prime_moduli_count": len(primes),
        "first_event_probabilities": [
            {"numerator": str(value.numerator), "denominator": str(value.denominator)}
            for value in probabilities
        ],
        "selected_index_zero_based": model_index,
        "selected_offset": offsets[model_index],
        "outside_probability": {
            "numerator": str(probabilities[-1].numerator),
            "denominator": str(probabilities[-1].denominator),
        },
    }


def comparator_offsets(p, past_gaps, candidates):
    if len(past_gaps) != 5 or any(g <= 0 for g in past_gaps):
        raise ValueError("exactly five positive historical gaps are required")
    median = sorted(past_gaps)[2]
    unrestricted = None
    h = 1
    while True:
        if gcd(p + h, 30) == 1:
            if unrestricted is None or (abs(h - median), h) < (
                abs(unrestricted - median), unrestricted
            ):
                unrestricted = h
        if unrestricted is not None and h > median and h - median > abs(
            unrestricted - median
        ):
            break
        h += 1
    restricted = min(candidates, key=lambda h: (abs(Fraction(h) - median), h))
    return {
        "median5_unrestricted_mod30": unrestricted,
        "median5_restricted_first8_mod210": restricted,
        "first_mod210": candidates[0],
    }


def forecast(p, past_gaps):
    law = bft_distribution(p)
    comparators = comparator_offsets(p, past_gaps, law["candidate_offsets"])
    return {"bft": law, "comparators": comparators}
