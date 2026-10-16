# BFT first-event prime census: a finite descriptive comparison

**Status:** `reproduced finite comparison` (descriptive; not prospective validation)

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

For the secondary question “is any prime found in the 210-integer proposal window?”, BFT, first-survivor and same-eight median each had 807 hits; unrestricted median had 685. This window result does not distinguish BFT from the simple first-survivor rule. BFT's recorded forecasting time summed to 4,068.37 seconds, versus 0.144 seconds for comparator generation. Proposal checking shared the chronological range classifier, so a complete end-to-end cost ratio cannot be attributed.

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

The command requires Python 3.14.7, matching the frozen run. It decompresses the archived streams to a temporary directory and runs the verifier without modifying the score stream. The expected aggregate output is in `evidence/verification-summary.json`.

The public `freeze.json` is a documented derivative of the private freeze record: it changes only the manifest hash and state description to bind this public manifest. The frozen source hashes and interpreter string are retained. The private source record remains canonical.

## Sources and prior work

The BFT construction is based on Banks, Ford and Tao's probabilistic model for large prime gaps. Their paper studies large gaps; it does not claim the deterministic next-prime ranking rule evaluated here. This experiment's exact bounded claim and comparison are mapped in [`sources/bft-first-event-census.md`](../../sources/bft-first-event-census.md). A bounded search did not identify a direct equivalent first-event next-prime ranker, but that search was not comprehensive and supports no novelty claim.

## Corrections and contact

Corrections can be reported through the repository issue tracker. This record has no open licence; public visibility does not grant broader reuse permission.
