# A prime clockwork recast as an event-driven sieve

Status: `reproduced`

Version: `0.1.0`

Last updated: `2026-10-26`

Author: Richard George Davis

Preparation included AI-assisted analysis, coding and writing. No model identity is claimed where readback was unavailable.

## Question and intended use

For the workload of listing every prime through a fixed bound `N`, can a prime-clockwork scan avoid updating every discovered prime clock at every integer, and how does an event queue compare with a standard segmented sieve?

This is a bounded implementation comparison for readers studying prime enumeration or alternative representations of sieving. It is not a new prime-generation theorem or a practical speed recommendation.

## Claim supported

In one retained Python 3.14.7 run on macOS 27.0.1 arm64 through `N=20,000`, the event-heap implementation returned the same 2,262 primes as a separately implemented trial-division reference and reduced median elapsed time from about 1.005 seconds for a minimal clockwork scan to about 0.0209 seconds. The ordinary segmented sieve returned the same output in about 0.000553 seconds and used less traced Python allocation.

The measurement shows an implementation-specific improvement over the literal clockwork scan in that run. It also shows that the standard segmented sieve was substantially faster than the event queue in the same benchmark. No general performance advantage is claimed.

## Method and correctness argument

The source clockwork advances a residue for every previously discovered prime at each candidate integer. The event-queue version stores the next scheduled multiple for each prime in a priority queue. When prime `p` is emitted, its first event is `p²`. At candidate `n`, every event due at `n` is advanced by `p`; if one or more events were due, `n` is composite. Otherwise, `n` is emitted and its own event stream is added at `n²`.

If an event for `p` is due at `n`, then `n` is a multiple of `p` with quotient at least `p`, so `n` is composite. Conversely, for any composite `n`, its least prime divisor `p` satisfies `p² ≤ n`; `p` has already been emitted and its event stream marks `n`. Therefore this finite event schedule emits exactly the primes.

This is the familiar sieve-of-Eratosthenes mechanism represented as scheduled composite marks. It is not a novel sieve or predictor.

## Results

| Implementation | Counted work | Median time | Traced Python allocation peak |
|---|---:|---:|---:|
| Minimal clockwork scan | 24,068,809 clock updates | 1.004538916 s | 169,352 bytes |
| Event heap | 35,485 composite marks; 73,232 heap operations | 0.020930583 s | 193,184 bytes |
| Segmented sieve | 35,485 composite marks; 34 base primes | 0.000553250 s | 90,567 bytes |

The event heap was about 48 times faster than the minimal clockwork scan in this run. The segmented sieve was about 38 times faster than the event heap. The latter two implementations mark the same number of composites, but their implementation costs differ substantially: equal mark counts do not imply equal runtime.

The benchmark used one warm-up and five timed samples per implementation with rotated order, a segment width of 4,096, and a post-return 30-second per-run threshold. Counter-collection was disabled during timing, but its conditional branches remained in the code. The measured memory is Python allocation tracing, not resident memory. The 256 MiB traced-allocation threshold was observed after each run; the time and memory thresholds were not enforced by the operating system.

The raw environment, timings, validation flags and counters from the retained run are in [`../../reproduce/prime-clockwork-event-sieve/results.json`](../../reproduce/prime-clockwork-event-sieve/results.json). A post-packaging run on 2026-10-26 matched the three 2,262-prime outputs and all operation counts; its environment and timings are preserved separately in [`reproduction-results.json`](../../reproduce/prime-clockwork-event-sieve/reproduction-results.json). The public script writes any later run to that separate file, preserving both records.

## Evidence class and review status

This artifact is labelled `reproduced` because the retained finite run compared the three implementations against the trial-division reference, and the self-contained public script was rerun on 2026-10-26. The rerun matched the prime counts, validation flags and operation counts. Timing values differed from the retained run and are recorded separately; they remain measurements of this machine and workload, not a general performance result.

The soundness/completeness argument is a coordinator derivation of standard sieve reasoning. It has not been formalised or independently checked by a human specialist. The retained benchmark protocol has open controls described below; this is a bounded pilot report, not completion of that broader benchmark contract.

## Limitations and unresolved issues

This is one small bound, one Python version and one macOS arm64 machine, with five timed samples and no cross-machine comparison or confidence interval. The clockwork scan and event heap differ both in per-candidate updates and in when their work begins, so the timing does not isolate the causal contribution of either change. The segmented implementation uses bytearray slice operations; the experiment compares these concrete implementations, not abstract algorithms under equal low-level cost.

The full saved benchmark contract remains incomplete: resident memory was not measured, audit costs were not timed separately, thresholds were checked after runs rather than enforced, and some explicit small/segment-boundary cases were not separately recorded. The reported threshold is not a resource guarantee. A later known-horizon refinement that omits events above `√N` is a derivation only; it was not implemented or timed.

The result does not establish cross-platform or large-range performance, streaming-memory savings, repeated-query benefit, arbitrary-precision cost, field-level novelty, or portable primality certificates for isolated integers. The source clockwork may serve other representation or arithmetic-readout purposes; this prime-list benchmark does not evaluate them.

## Sources and provenance

See [`../../sources/prime-clockwork-event-sieve.md`](../../sources/prime-clockwork-event-sieve.md) for source roles and the exact benchmark record. The included script and raw results contain no third-party dataset or code. No source paper text or figures are reproduced.

## Rights and reuse

No licence is assigned. Public visibility does not itself grant reuse permission.

## Reproduction

From the repository root, using Python 3.11 or later with only the standard library:

```bash
python3 reproduce/prime-clockwork-event-sieve/benchmark.py
```

The script reruns the finite comparison and writes `reproduction-results.json` next to itself. Timing values may differ by environment. A successful run confirms output equality against that script's trial-division reference for the declared bound; it does not close the omitted benchmark controls or establish a general performance result.

## Corrections and issue reporting

Report corrections through the [repository issue tracker](https://github.com/RichardGeorgeDavis/research-artifact-ledger/issues). Changes to this untagged artifact will be identified by their commit and recorded in `HISTORY.md`.

## Independent review

Reviewer: no independent human specialist reviewer.

Prior checks: the retained local execution compared all three outputs with trial division and recorded the bounded measurements. The public reproduction copy was rerun on 2026-10-26; it matched outputs and counters, while timing results differed as expected. No peer review or novelty review is claimed.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-10-26 | Initial bounded benchmark artifact, public reproduction copy and retained raw results. | Reports the finite comparison without claiming general speed, novelty or a completed benchmark contract. |
