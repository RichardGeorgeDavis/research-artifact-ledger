# Additional bounded source-review coverage — 2026-10-16

Status: `source review`. This note reports additional AI-assisted source reviews recorded on 15–16 October. It is a summary of private review records, not a fresh proof audit or reproduction. It helps readers locate reviewed interfaces and distinguish them from the still-open full proof assurance.

## Sources and reviewed interfaces

The OpenAI source revision is [fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb). The Mathlib revision is [d13f23b723b8a846827a245b89c10fc7d3f11612](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).

1. **Endpoint conversion (refinement overlapping earlier coverage):** the recorded review traced the displayed finite-sieve premise to the main and uniform endpoint interfaces in `Model.lean`, `Main.lean` and `LatticeComponents.lean`. It found no local invalid inference under the inspected premises. This does not establish the finite-sieve construction or identify an evaluated uniform bound.
2. **Inverse-limit application:** the review read Mathlib `Mathlib/Order/KonigLemma.lean`, `exists_seq_forall_proj_of_forall_finite`, alongside its use in `LatticeComponents.lean`. It mapped nonempty finite prefix types, restriction maps and their identity/composition obligations to the compatible-sequence conclusion. The recorded source challenge found no concrete indexing or coherence mismatch. Finiteness of each prefix type is stronger than the imported finite-fibre requirement.
3. **First accurate-band application:** the review traced `AccurateScales.eventually_accurate_band` through the first application in `CommonBlocks.eventually_window_bands` to `WindowBatch.eventually_window_batch`. The record maps parameter and local hypotheses to the first returned entropy-band witness. Its source challenge found no concrete mismatch in that map. The second application and remaining guards were outside this review.

The GaussianMoat files are under `lean/OAI/NumberTheory/GaussianMoat/` at the pinned OpenAI revision. Publication-time retrieval of the pinned raw files located the inverse-limit call at LatticeComponents.lean:277, the accurate-band declaration at AccurateScales.lean:219, and the named callers at CommonBlocks.lean:137 and WindowBatch.lean:28. This locator check corrects inconsistent historical references; it is not a fresh derivation review. Inspect the named declarations and callers together; reading a statement alone does not reproduce a caller-contract review.

## Evidence and limits

These are recorded source-level observations, not a new theorem, numerical component bound, or independent certification. The full working reports remain private. AI review passes provide a challenge to the argument map; they are not independent human specialist review. Requested reviewer settings were not confirmed by runtime telemetry.

No new Lean/Lake build, comparator run or numerical experiment was performed for these slices or this publication. The earlier build and axiom-query evidence remains separate. These reviews do not authenticate cached dependencies, close the transitive proof graph, review all imported foundations, establish the full sieve construction or determine novelty. Absence of a detected local mismatch is not proof of whole-theorem correctness.

This adds coverage to the earlier 12 October source-review note without replacing its dated findings. Public history records publication of this summary, not first conception or scientific priority. Only original summary prose and technical identifiers are included; no private working records or third-party source bodies are reproduced.
