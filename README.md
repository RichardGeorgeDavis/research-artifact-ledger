# Research Artifact Ledger

**Purpose:** a small, versioned home for selected research artifacts with explicit source trails, evidence labels, reproduction notes and correction history.

**Latest tagged release:** `v0.2.0`, containing the template and one reproduced, bounded negative finding: a finite singular-series shortlist screen for immediate-next-prime retrieval. **Current `main` also contains public artifacts not included in a tagged release:** the finite BFT first-event comparison; Gaussian-moat formal endpoint and source-audit records; a conditional helix-metric application; a bounded prime-blind logarithmic-height derivation; a philosophical working paper on experiential comparison across learning; an exploratory numerical-cognition note (revised author version 2, submitted; acceptance and peer review are not established); a neutral-scalar wormhole source review; a bounded source review of matched-CMB-circle constraints on global topology; and a bounded source review of selected neutrino mass-ordering constraints. These records do not claim a new theorem, general predictor, scientific theory, empirical or physical result, or field-level novelty.

## What this repository can and cannot show

Each public commit and release records what this repository contained at that point. Source links, dated records and correction history help readers inspect provenance and changes. They do not prove when an idea was first conceived, establish priority over unpublished work, or demonstrate that a claim is correct or original.

Research artifacts added later must identify their question, bounded claim, sources, evidence class, method, reproducibility steps, limitations and review status. Established background, reproduced work, new derivations, synthetic examples, local applications, conjectures and open questions must not be blended into one verification label. For priority-sensitive records, distinguish claim-level authorship, prior work, first documented private note (if retained), first public record and the scope of any priority statement.

## Public artifacts on main

- [From Numerical Cognition to Cognitive Command](artifacts/numerical-cognition-cognitive-command/README.md) — exploratory research note; scoped `source review` and `open` questions. Updated to revised author version 2, submitted by email on 24 October 2026; submission does not establish acceptance or peer review. Preserves concept formation, the role of learned practices in standards and full AI disclosure; not independently human-reviewed. Present on `main`; not included in a tagged release.

- [When a Perspective Grows](artifacts/when-a-perspective-grows/README.md) — philosophical working paper; scoped `source review`, `synthetic demonstration` and `open` questions. Exact-arithmetic examples are reproducible; the philosophical thesis is not independently verified or peer reviewed. Meredith is cited at abstract scope only. Present on `main`; not included in a tagged release.

- [A finite screen of singular-series ranking for next-prime retrieval](artifacts/singular-series-shortlist/README.md) — `reproduced`; one fixed 10,000-origin block, with a standalone standard-library reproduction script and explicit limitations.
- [BFT first-event prime census: a finite descriptive comparison](artifacts/bft-first-event-census/README.md) — `reproduced finite comparison`; one fixed 3,111-origin frame, archived evidence and a standalone verifier. Prospective blindness was compromised, and the result shows no advantage over the first modulus-210 survivor.
- [Decimal carry states and prime-wheel phases](artifacts/carry-wheel-phase-alignment/README.md) — `bounded derivation`; exact joint periods, compatible residue states and finite checks for the mod-30 and mod-210 wheels. No new prime test or prediction claim.
- [A prime clockwork recast as an event-driven sieve](artifacts/prime-clockwork-event-sieve/README.md) — `reproduced`; one bounded Python comparison of a minimal clockwork scan, event heap and segmented sieve through 20,000. The standard segmented sieve was fastest in the retained run; no general performance or novelty claim.
- [Gaussian-moat theorem: bounded Lean endpoint check](artifacts/gaussian-moat-formal-check/README.md) — `formalised`; an OpenAI-authored theorem checked at a pinned source revision, with chronology and trust limits. Its 2026-10-12 and 2026-10-18 source-audit updates remain bounded and leave the full proof open. Present on `main`; not yet included in a tagged release.
- [Gaussian-moat bound under an address-controlled helix metric](artifacts/gaussian-moat-helix-metric-corollary/README.md) — `provisional application`; a conditional one-way graph-containment derivation from the Gaussian-moat endpoint, with zero-height and unrestricted-enumeration counterexamples. It is not Lean-formalised or a field-level novelty claim.
- [A prime-blind logarithmic height gives an infinite tail path](artifacts/prime-blind-log-height/README.md) — `bounded derivation`; one fixed spiral convention, one height function and a conclusion conditional on the stated prime-number theorem input. Exact prior art and qualified human mathematical review remain unresolved; no novelty claim is made. Present on `main`; not included in a tagged release.

- [A half-area cross-section is not a generic transmission probability](artifacts/neutral-scalar-wormhole-transmission/README.md) — `source review`; a bounded interpretation of two version-pinned theoretical papers distinguishing fixed-frequency resonance, period/all-time `A/2` observables and finite-time packet delivery. No empirical or physical claim, field-level novelty claim, human review or peer review is made. Present on `main`; not included in the latest tagged release.

- [What matched-CMB-circle nulls constrain about global topology](artifacts/cmb-matched-circle-topology/README.md) — `source review`; a bounded interpretation of two version-pinned papers distinguishing Planck's back-to-back matched-circle search and separate low-ℓ likelihood limits from Petersen et al.'s observer-centred constraints across nine orientable Euclidean families. No CMB analysis was reproduced; no global-topology verdict, novelty or priority claim, human specialist review or peer review is made. Present on `main`; not included in the latest tagged release.
- [What selected absolute-mass constraints establish about neutrino ordering](artifacts/neutrino-ordering-mass-constraints/README.md) — `source review`; a bounded comparison of endpoint, cosmological mass-sum and oscillation-ordering claims with their dataset, model, prior, statistical-method and publication-status limits. No new fit, direct ordering measurement, model-independent verdict, human specialist review or peer review is claimed. Present on `main`; not included in the latest tagged release.


## Why the repository has releases

A version tag and GitHub release give a repository state an identifier for version-specific citation and inspection. Release v0.1.0 records the initial template; v0.2.0 packages the reproduced singular-series screen. Releases are selective snapshots, not peer review or a quality certification, and later public artifacts can remain on main without a new release. These releases are not marked immutable by GitHub, so do not describe them as tamper-proof archives. Cite the tag for a released version; for a later untagged artifact, cite the relevant commit and artifact path.

## Status labels

- `source review`: sources have been inspected for the stated scope; the result is not independently reproduced.
- `bounded derivation`: an explicit mathematical derivation supports the stated claim under its assumptions and scope; this label does not imply formalisation, qualified independent review or novelty.
- `reproduced`: the stated procedure was rerun and matched the declared check.
- `independently checked`: a person not responsible for the original artifact checked the named claim or procedure; the scope of that check is stated.
- `formalised`: a specified formal system or proof assistant checks the stated formal claim; this does not validate empirical premises.
- `synthetic demonstration`: an illustrative constructed case, not evidence of real-world effectiveness.
- `provisional application`: a bounded local use whose wider effectiveness is not established.
- `open`: unresolved, incomplete or awaiting the stated check.

## Adding an artifact

1. Copy [`ARTIFACT_TEMPLATE.md`](ARTIFACT_TEMPLATE.md) and complete all applicable fields.
2. Link material claims to primary sources, data, code, derivations or prior artifacts.
3. Include enough information to reproduce or independently inspect the result, with rights and privacy reviewed.
4. State negative results, limits, unresolved objections and what evidence would change the conclusion.
5. Add a dated entry to [`HISTORY.md`](HISTORY.md) and keep citation metadata accurate. When issuing a release, provide a version tag and release entry for that snapshot; do not imply the tag is immutable unless the hosting platform confirms it. Corrections can be reported through the [repository issue tracker](https://github.com/RichardGeorgeDavis/research-artifact-ledger/issues).

## Scope and reuse

This is an artifact ledger, not a claim that its methods are novel or that its contents have peer-review status. Each artifact carries its own evidence and review limits. No open licence is assigned; no broader reuse permission should be inferred from public visibility.
