# Bounded manuscript–formal endpoint statement comparison

Date: 2026-11-19

Artifact: [Gaussian-moat theorem: bounded Lean endpoint check](../README.md), version 0.1.12.

## Result

At the pinned [OpenAI Math source commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/commit/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), a bounded comparison found no mismatch between the manuscript's theorem statement and the Lean endpoint's top-level statement and parameters.

The comparison covered the manuscript's [Gaussian-prime vertex and distance definitions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/main.tex#L54-L75), its [uniform component conclusion](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/main.tex#L63-L75), and the Lean [model and endpoint definitions](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/Model.lean#L7-L34). Both use irreducible Gaussian integers, distinct vertices joined at Euclidean distance at most a real cutoff `D`, and a finite component bound independent of the starting prime. The Lean endpoint quantifies over every real `D`; its bridge applies the finite-sieve premise at `max(D,1)` and restores the finite exceptional neighbourhood. The finite-walk conclusion bounds the number of vertices/terms, including the empty finite-walk case.

The manuscript's sufficient-bound expression and Lean's witness `period² + ncard(restored)` are different expressions; no equality between them is asserted or needed for the existential statement. The manuscript's fixed-ratio prime batches and Lean's selected dense, separated bins are different proof architectures.

## Evidence ceiling

This is a source-level statement, hypothesis and parameter comparison. It does not establish proof-route identity, equality or evaluation of witness constants, an effective general `B(D)`, complete paper-to-proof correspondence, a fresh build or replay, cache-to-source authentication, complete imported-proof correctness, theorem-wide assurance, novelty, or specialist/human review.

A separate AI challenge examined the pinned source comparison and its endpoint bridge; the requested reviewer setting was `gpt-6.1-sol / high`, but serving identity and effort were not available for telemetry readback. This is not external or human specialist review. No Lean/Lake command was run for this comparison.

## Impact

The sources are the same immutable pin already recorded by this artifact. No scientific premise, formula, dataset, figure, calculation or saved result changed. The existing formal endpoint and its trust limits are unchanged; restart is `UNAFFECTED`.
