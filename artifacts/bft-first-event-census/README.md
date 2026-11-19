# BFT first-event prime census: a finite descriptive comparison

**Status:** `reproduced finite comparison` (descriptive; not prospective validation)

Version: `0.1.2`

Last updated: `2026-11-19`

## Question and audience

For this one fixed interval, how did the frozen Banks–Ford–Tao (BFT) first-event proposal compare with two next-prime gap-median proposals and the first integer surviving the modulus-210 sieve? This record is for readers evaluating bounded prime-ranking experiments and their comparators.

## Bounded result

The frame contains 3,111 eligible prime origins from 10,050,248 through 10,100,247. At every origin, the BFT proposal exactly matched the first modulus-210 survivor. Each proposed successor was then checked against the archived classification stream.

| Proposal | Exact next-prime hits | Rate | Mean absolute distance to next prime |
|---|---:|---:|---:|
| BFT first-event | 807 / 3,111 | 25.94% | 11.6753 |
| First modulus-210 survivor | 807 / 3,111 | 25.94% | 11.6753 |
| Median of five unrestricted mod-30 gaps | 409 / 3,111 | 13.15% | 10.8550 |
| Median of five gaps restricted to the first eight mod-210 survivors | 487 / 3,111 | 15.65% | 10.7715 |

For the secondary metric, the verifier tests whether each method's single proposed integer is prime and lies in the 210-integer window `(p, p + 210]`; it does not search the window for any prime. BFT, first-survivor and same-eight median each had 807 prime proposals; unrestricted median had 685. The largest actual successor gap was 120, so every frame window contained a prime; these are proposal-success counts, not counts of windows with any prime. This result does not distinguish BFT from the simple first-survivor rule. BFT's recorded forecasting time summed to 4,068.37 seconds, versus 0.144 seconds for comparator generation. Proposal checking shared the chronological range classifier, so a complete end-to-end cost ratio cannot be attributed.

## Evidence and method

This is a finite, fixed-frame computational comparison. The archived labels cover 10,050,211–10,100,431. The public bundle contains compressed hash-chained forecasts, labels and score events, the frozen scripts, a manifest and a verification command. The verifier independently classifies the integer interval with an Eratosthenes sieve, checks the labels, stream chains, origin coverage, chronology, historical tail, frozen source hashes and proposal/cutoff constraints, and checks the stored score events. A separate aggregate-only audit checks that the selected index is zero and equals the first modulus-210 survivor at every origin.

The verifier does not independently reconstruct the complete K=8 BFT probability law at every origin. It checks the archived forecast structure and constraints against the frozen code and records. Independent human specialist review and peer review are not claimed. Model-serving identity telemetry was not confirmed.

## Interpretation limits

A status read during execution exposed forecast-origin prime labels for sequences 208–2195 before completion. No probabilities or selected offsets were exposed, and those labels were not used to tune or stop the run. Because prospective blindness was compromised, this is not an untouched prospective validation. The exact frame and configuration were not reset or replaced.

The result does not establish statistical significance, calibration, causal explanation, asymptotic behaviour, generalisation to another range, field novelty, or a generally useful next-prime predictor. BFT's equality with the first modulus-210 survivor means this run shows no BFT-specific advantage over that simple rule. Its worse mean distance than both median comparators also matters. The result does not prove that BFT or other first-event rules cannot work elsewhere.

## Reproduce

From the repository root, run:

```sh
sh reproduce/bft-first-event-census/verify_bundle.sh
```

The command requires a Python 3.14.7 runtime whose full `sys.version` string matches the frozen value in [`evidence/freeze.json`](evidence/freeze.json), including the build date and compiler text. The verifier checks this string and a digest derived from it; it does not hash the interpreter executable. It decompresses the archived streams to a temporary directory and runs the verifier without modifying the score stream. Its default mode accepts a valid exact prefix of the archived score events; an incomplete prefix can return exit status 0 with `verification: DATA_VERIFIED_UNSCORED`. The wrapper does not compare the output with `evidence/verification-summary.json`. The wrapper prints two JSON objects. For a complete retained archive, check `"verification": "PASS"` and `"score_events": 6222` in the first, census-verifier object, then compare its totals with the saved summary. The second object's `PASS` reports proposal equivalence only. A normal process exit alone does not certify full score verification.

The public `freeze.json` is a documented derivative of the private freeze record: it changes only the manifest hash and state description to bind this public manifest. The frozen source hashes and exact interpreter version string are retained; no interpreter executable hash is claimed. The private source record remains canonical.

## Sources and prior work

The BFT construction is based on Banks, Ford and Tao's probabilistic model for large prime gaps. Their paper studies large gaps; it does not claim the deterministic next-prime ranking rule evaluated here. This experiment's exact bounded claim and comparison are mapped in [`sources/bft-first-event-census.md`](../../sources/bft-first-event-census.md). The frozen verifier/source-map scope and its 19 November 2026 clarification are documented in [`sources/bft-verification-scope.md`](../../sources/bft-verification-scope.md) and the [scope correction addendum](../../sources/bft-verification-scope-correction-20261119.md). A bounded search did not identify a direct equivalent first-event next-prime ranker, but that search was not comprehensive and supports no novelty claim.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.2 / 2026-11-19 | Clarified the frozen interpreter-version requirement and verification status | The verifier compares the full `sys.version` string and a digest derived from it; incomplete valid score prefixes return `DATA_VERIFIED_UNSCORED`, and the wrapper does not compare the saved aggregate. No benchmark was rerun. |
| 0.1.1 / 2026-11-19 | Clarified the secondary 210-integer window metric | The pinned verifier scores each method's single proposal for primality inside `(p, p + 210]`; it does not search the entire window. Counts and primary comparison are unchanged. |

## Corrections and contact

Corrections can be reported through the repository issue tracker. This record has no open licence; public visibility does not grant broader reuse permission.
