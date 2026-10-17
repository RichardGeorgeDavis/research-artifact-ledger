# Bounded Mathlib source-audit update — 2026-10-18

## Finding

Three additional bounded source reviews examined selected Mathlib declarations connected with the Family-028 confidence review and its compatible-basis construction at revision [`d13f23b723b8a846827a245b89c10fc7d3f11612`](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612). The reviews found no concrete mismatch in the exact signatures, proof steps and caller maps listed below. This is conditional source-level evidence for these slices only; it does not certify the full theorem or its transitive proof environment.

The complete working derivations remain in the private research record. This public note identifies the sources, bounded claim and limits; it is not a replacement for a formal proof audit. Separate AI technical challenges checked the frozen source maps. One challenge caught and corrected a reversed prose description of the rank-induction step in the first coordinator draft; the corrected map received no further mismatch report. Reviewer model-serving identity and effort were unavailable for readback. No independent human review is claimed.

## Audited slices

### PID basis reduction

The review inspected [`Submodule.basis_of_pid_aux`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/FreeModule/PID.lean#L152-L269), with its displayed commutative PID-domain, finite-basis, nonzero-submodule and inclusion assumptions. The source chooses a maximal image of a linear functional, uses its principal generator to split off a direction, forms nested kernel submodules, and constructs compatible basis-extension data. The review found no concrete mismatch in the statement, coefficient-separation argument, spanning step or basis-extension map within that declaration and its directly inspected interfaces.

This does not authenticate the imported maximality, principal-ideal, basis or module proof bodies, establish the complete Smith-normal-form theorem, or certify the Gaussian-moat theorem.

### Rank-induction consumer assembly

The review mapped [`Submodule.inductionOnRank`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/Dimension/StrongRankCondition.lean#L393-L404) to its uses in [`nonempty_basis_of_pid`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/FreeModule/PID.lean#L279-L292) and [`exists_smith_normal_form_of_le`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/FreeModule/PID.lean#L487-L503). The displayed recursive submodule direction, one-vector separation premise, zero cases, generalisation over the nested submodule, basis extensions and coefficient transport align with those theorem statements. The theorem returns a diagonal coefficient relation and a dimension inequality; it does not assert divisibility ordering among the coefficients.

A separate AI challenge caught and corrected a reversed prose description of the induction step in the first coordinator draft; it found no further mismatch in the corrected map. This source-assembly review does not inspect the auxiliary induction engine's full foundation or certify imported proofs.

### `inductionOnRankAux` foundation

The exact auxiliary declaration [`Submodule.inductionOnRankAux`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/Basis/Submodule.lean#L79-L109) was reviewed against the wrapper contract above. Its base case derives the motive for the bottom submodule from the separation condition; its zero-rank branch reduces the submodule to bottom; and its successor branch adjoins the separated vector to an independent family, then uses the finite-family bound to establish the smaller recursive bound for each eligible residual submodule. A separately dispatched AI challenge found no concrete mismatch in the base case, recursive bound, vector extension, separation condition, motive direction or distinction between the auxiliary's assumptions and the wrapper's additional assumptions.

The conclusion is positive only for alignment of this exact declaration with its wrapper contract. The review did not inspect imported `Basis.eq_bot_of_rank_eq_zero` or `LinearIndependent.finCons'` proof bodies, run Lean/Lake, authenticate cached artifacts, replay the kernel, or audit the transitive Mathlib dependency graph.

## What this adds

These reviews extend the named source-coverage record for one existing formalised theorem and its lower basis-construction dependency. They found no defect in the listed slices and add no new theorem, build result, theorem-wide verdict, novelty claim or connection to ordinary-prime prediction, infinity or the other Infinity Research streams. The theorem and the public endpoint check retain their prior authorship, chronology and trust boundaries.

## Verification boundary

The source files were pinned to the exact Mathlib revision above and retained with hashes in the private execution record. The public summaries are derived from those source reviews; the full working notes and source copies are not reproduced here. The PID review also read the directly used helper bodies and interfaces for [`generator_submoduleImage_dvd_of_mem`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/RingTheory/PrincipalIdealDomain.lean#L151-L155) and [`mkFinCons` / `mkFinConsOfLE`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/Basis/Fin.lean#L41-L80) at the same pin; their lower-level dependencies remain trusted. No complete audit of imported proofs, Lean or Lake command, comparator harness, proof-kernel replay, or cache authentication was performed for these additions. The same-cluster AI challenges are source-map checks, not independent scientific evidence or human specialist review. The existing formal endpoint run and its declared environment boundary remain unchanged.

## Sources and provenance

- [`Mathlib/LinearAlgebra/FreeModule/PID.lean`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/FreeModule/PID.lean) — `basis_of_pid_aux` and the two named consumers.
- [`Mathlib/LinearAlgebra/Dimension/StrongRankCondition.lean`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/Dimension/StrongRankCondition.lean) — public rank-induction wrapper.
- [`Mathlib/LinearAlgebra/Basis/Submodule.lean`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/Basis/Submodule.lean) — bounded auxiliary induction foundation.
- [`Mathlib/RingTheory/PrincipalIdealDomain.lean`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/RingTheory/PrincipalIdealDomain.lean#L151-L155) — directly used principal-ideal helper body and interface inspected for the PID basis reduction.
- [`Mathlib/LinearAlgebra/Basis/Fin.lean`](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/LinearAlgebra/Basis/Fin.lean#L41-L80) — directly used finite-basis extension helper bodies and interfaces inspected for the PID basis reduction.
- Upstream theorem and existing endpoint-check context remain as cited in the parent artifact; these source reviews do not change its authorship or theorem claim.
