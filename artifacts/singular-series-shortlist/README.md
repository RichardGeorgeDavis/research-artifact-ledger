# A finite screen of singular-series ranking for next-prime retrieval

Status: `reproduced`

Version: `0.2.0`

Last updated: `2026-10-08`

Author: Richard George Davis

Preparation included AI-assisted analysis and coding. No model identity is claimed where readback was unavailable.

## Question and intended use

On one fixed block of 10,000 consecutive prime origins, did ranking the first eight integers coprime to 210 by the variable factor of the two-prime Hardy–Littlewood singular series retrieve the immediate next prime in a five-candidate shortlist more often than ascending wheel order or a rounded-log-density ranking?

This is a bounded methods result for readers evaluating a particular prime-ranking heuristic. It is not a practical prime-generation recommendation.

## Claim supported

On the declared block and under the exact rules below, singular-series ranking retrieved the immediate successor in 5,579 of 10,000 shortlists (55.79%). Wheel order did so in 8,400 (84.00%), and rounded-log density in 7,973 (79.73%). The singular-series shortlist therefore recorded 2,821 fewer hits than wheel order and 2,394 fewer than rounded-log density on this block. Under the predeclared strict-improvement rule, this tested singular-series shortlist family stops.

The script in [`../../reproduce/singular_series_screen.py`](../../reproduce/singular_series_screen.py) regenerates the block with a sieve and asserts the reported outcome counts.

## Method

The first origin is `1,743,433`. The test uses 10,000 consecutive prime origins, each paired with its immediate successor. For each origin `p`, it forms the first eight integers `n > p` with `gcd(n, 210) = 1`. It scores each positive even offset `h = n - p` by

`S(h) = product over distinct odd prime q dividing h of (q - 1)/(q - 2)`.

The empty product is 1. Exact rational arithmetic ranks candidates by descending score, with smaller integers breaking ties. The method emits the top five. It does not test candidate primality while ranking.

The wheel-order control emits the first five candidates in ascending order. The rounded-log-density control rounds `ln(p)` to the nearest positive even integer `r`, breaking exact rounding ties downwards, then ranks the same eight candidates by increasing `|h-r|`, with smaller integers breaking ties. It emits five candidates. All methods use the same pool and output budget.

The primary measure is paired exact-successor inclusion at five outputs, counted over all 10,000 origins. The 495 cases where the successor falls outside the eight-candidate pool remain misses. The rounded-log control is a fixed density-inspired reference; neither it nor the singular-series score is a calibrated probability for a fixed endpoint.

## Results

| Method | Immediate successors in top five | Rate | Rank-one exact hits | Prime-valued output slots |
|---|---:|---:|---:|---:|
| Singular-series ranking | 5,579 / 10,000 | 55.79% | 694 | 14,643 / 50,000 |
| Wheel order | 8,400 / 10,000 | 84.00% | 2,889 | 14,628 / 50,000 |
| Rounded-log density | 7,973 / 10,000 | 79.73% | 1,508 | 14,634 / 50,000 |

The immediate successor was in the common eight-candidate pool 9,505 times and outside it 495 times. Paired outcome cells were: all three methods hit, 4,925; none hit, 946; singular series only, 573; wheel only, 508; density only, 0; singular series plus density only, 81; singular series plus wheel only, 0; wheel plus density only, 2,967. These counts sum to 10,000.

## Evidence class and review status

This artifact is labelled `reproduced`: its included standalone procedure was run and matched the reported counts and block endpoints. The original private run also passed a separate verifier over its sealed journal, frozen contract, implementation hashes and outcome calculations. A pre-run implementation review and mathematical review were recorded. Those reviewers were AI-based; their model identities were not available for readback. This release does not claim independent human specialist review, formal proof, statistical significance, asymptotic performance or external validation.

The tested implementation used a cooperative forecast/reveal process boundary, not adversarial operating-system isolation. That limitation is retained in the private execution record; the public reproduction script directly computes the declared finite comparison and makes no isolation claim.

## Limitations and what would change the claim

This is one contiguous finite block and one fixed rule, window and output budget. The result does not establish a general failure of singular-series methods, disprove the Hardy–Littlewood prime-tuple conjecture, estimate prime probabilities, or support a conclusion about other blocks, score variants or candidate budgets. The pair singular series concerns average translated prime-pair structure; it does not model the absence of intervening primes required for an immediate-successor claim. The observed output counts also do not establish statistical significance.

Changing the block, score, window, budget or claim would require a new predeclared contract and a fresh exposure audit. No follow-on test is implied by this result.

## Sources and provenance

See [`../../sources/singular-series-screen.md`](../../sources/singular-series-screen.md) for the source-to-claim map and access details. No third-party dataset or code is bundled. The full research record, event journal, exposure audit, review packets and provenance remain in the private research record and are not part of this public artifact.

## Rights and reuse

No licence is assigned by this release. Public visibility does not itself grant reuse permission. No third-party text, image, dataset or code is reproduced here; the mathematical formula is stated in the artifact and the source is cited.

## Reproduction

From the repository root, using Python 3.11 or later with only the standard library:

```bash
python3 reproduce/singular_series_screen.py
```

The script prints a JSON summary and exits successfully only if the result counts and endpoints match the recorded values. It computes primes locally up to the declared sieve limit and includes no external data download.

## Corrections and issue reporting

Report corrections through the [repository issue tracker](https://github.com/RichardGeorgeDavis/research-artifact-ledger/issues). Released changes are recorded in the repository `HISTORY.md` and versioned by tag.

## Independent review

Reviewer: no independent human reviewer for this public release.

Prior checks: a separate implementation verifier passed on the private run; pre-run mathematical and implementation reviews are recorded in the private research record. Model identity readbacks were unavailable. No claim of peer review is made.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.2.0 / 2026-10-08 | Published the bounded negative screen and standalone reproduction script. | Reproduction matched all declared outcome checks; limitations and evidence status are stated above. |
