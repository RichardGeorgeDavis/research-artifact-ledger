# Decimal carry states and prime-wheel phases

Status: `bounded derivation`

Version: `0.1.0`

Last updated: `2026-10-26`

Author: Richard George Davis

Preparation included AI-assisted mathematical analysis, code and writing. No model identity is claimed where readback was unavailable.

## Question and intended use

How do the repeating states of a base-10 odometer align with the residue filters modulo 30 and 210, and what does that alignment establish about prime candidates?

This is a compact mathematical and visual explanation for readers studying place-value cycles, modular arithmetic or prime wheels. It does not propose a prime predictor.

## Claim supported

For each integer `k ≥ 1`, the joint state `(t mod 10^k, t mod M)`, with `M=30` or `210`, has respective period `3·10^k` or `21·10^k`. A pair of component residues is reachable exactly when both agree modulo 10. Across one joint period, the wheel-survivor counts are `8·10^(k−1)` for `M=30` and `48·10^(k−1)` for `M=210`.

Every carry endpoint through `j ≥ 1` decimal places is divisible by 2 and 5 and is therefore rejected by either wheel. A surviving wheel state is only a candidate: it need not be prime.

## Derivation

Let `t` be the integer label after an increment. Define the product state

`S_(k,M)(t) = (t mod 10^k, t mod M)`.

The two moduli share exactly the factor 10 for `k ≥ 1`. A compatible pair `(a mod 10^k, r mod M)` therefore comes from an integer precisely when `a ≡ r (mod 10)`. The generalized Chinese remainder theorem gives one representing class modulo `lcm(10^k,M)`.

The least period of the product state is this least common multiple. It is `3·10^k` for modulus 30 and `21·10^k` for modulus 210. Each joint period contains `10^(k−1)` full wheel cycles, so the number of surviving states is the number of reduced residues, `φ(M)`, multiplied by `10^(k−1)`.

A carry through `j` decimal places occurs at `t ≡ 0 (mod 10^j)`. Such a label shares factors 2 and 5 with either wheel modulus. It cannot be coprime to 30 or 210, so no carry endpoint survives.

| Wheel modulus | Reduced residues per wheel cycle | Joint period | Survivors per joint period |
|---:|---:|---:|---:|
| 30 | 8 | `3·10^k` | `8·10^(k−1)` |
| 210 | 48 | `21·10^k` | `48·10^(k−1)` |

For a concrete example, track two decimal places and the mod-30 wheel. The joint period is 300. Decimal state `37 mod 100` is compatible with wheel phases 7, 17 and 27 modulo 30; labels 37 and 137 survive, while 237 is removed because it is divisible by 3.

## Finite check

The included standard-library script enumerates each full joint period for `k=1,2,3` and both wheels. It checks the number of reachable state pairs, the compatibility condition, the survivor totals, the final-digit distribution and the rejection of every carry endpoint. The proof above supplies the general formulas; enumeration is a finite cross-check.

Expected output:

```text
PASS: k=1..3; moduli=30,210; joint periods, compatibility, survivor counts and carry rejection
```

The original 5 October check covered aggregate last-digit counts. A 19 October recheck added explicit per-decimal-state assertions and the incompatible-pair control; it confirmed that eligible fixed decimal states have 2 surviving mod-30 phases or 12 surviving mod-210 phases. This public script includes those per-state checks.

## Evidence class and review status

This is a `bounded derivation` of standard modular and sieve facts applied to a particular pair of decimal and wheel cycles. It is not a new theorem, prime test, sieve method, prediction result or priority claim. Finite assertions check the declared small periods; the all-`k` conclusions follow from the derivation.

The original project run compared the result with standard modular arithmetic, generalized CRT and sieve references. No independent human specialist review, formal proof-assistant check, exhaustive literature review or measured reader-learning benefit is claimed.

## Limitations

The computational check covers only `k=1,2,3`; it does not establish the general formulas, which are derived algebraically. Only base 10 and wheels 30 and 210 are treated. A wheel's filtering primes require separate handling, and 1 passes coprimality filters without being prime. No 3D model is needed to verify this finite state result; a visualisation would display the same arithmetic in different coordinates.

## Sources and provenance

See [`../../sources/carry-wheel-phase-alignment.md`](../../sources/carry-wheel-phase-alignment.md) for the source-to-claim map and evidence roles. The original private derivation and run record remain outside this repository. No third-party text, data, figure or code is reproduced here.

## Rights and reuse

No licence is assigned. Public visibility does not itself grant reuse permission.

## Reproduction

From the repository root, using Python 3.11 or later with only the standard library:

```bash
python3 reproduce/carry_wheel_phase_alignment.py
```

The script prints the expected `PASS` line and exits nonzero if any finite assertion fails. It uses no external data or network access.

## Corrections and issue reporting

Report corrections through the [repository issue tracker](https://github.com/RichardGeorgeDavis/research-artifact-ledger/issues). Changes to this untagged artifact will be identified by their commit and recorded in `HISTORY.md`.

## Independent review

Reviewer: no independent human reviewer for this public artifact.

Prior checks: the private run performed finite enumerations through `k=1,2,3`, including a later per-state audit. Those checks are reproduced by the included script. The algebra is stated for direct inspection; no formalisation or specialist human review is claimed.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-10-26 | Initial bounded derivation and finite-check script. | Exact state formulas and their limits are made inspectable; no novelty or prediction claim is made. |
