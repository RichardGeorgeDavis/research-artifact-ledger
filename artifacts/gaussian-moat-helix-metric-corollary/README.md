# Gaussian-moat bound under an address-controlled helix metric

Status: `provisional application` — conditional derivation, AI-challenged, not Lean-formalised.

Version: `0.1.0`

Last updated: `2026-10-12`

Artifact author: Richard George Davis. The mathematical derivation was AI-assisted and independently challenged by an AI reviewer; no independent human review is claimed.

Underlying theorem author: OpenAI, as named on the source manuscript. This artifact records a project-level application of that existing theorem and does not claim authorship of it.

## Evidence class and review status

This is a `provisional application`: an elementary source-derived argument applying the Gaussian `UniformEndpoint` to a changed adjacency rule. An AI reviewer reconstructed and challenged the derivation against the pinned graph model and endpoint declaration on 2026-10-12; no defect was identified under the stated assumptions. The reviewer’s runtime model identity was unavailable. There was no human review, Lean formalisation, independent reproduction or exhaustive prior-art search.

## Question and intended use

Does the family-028 Gaussian-prime component bound also say something if we redefine adjacency using distance on the programme's indexed helix?

The answer is conditional. For a helix with nonzero linear height and an enumeration whose consecutive steps have one global bound, every helix edge is also an edge in a Gaussian-prime graph at a calculable cutoff. The Gaussian theorem then bounds the helix components. This is an application to a changed graph; simply relabelling the original graph would preserve its edges by definition and would prove no new consequence.

## Claim supported

Let `A={1,2,...}` and let `S:A→Z[i]` be a bijection. Assume one finite real `L≥0` satisfies `|S(k+1)-S(k)|≤L` for every address `k`. Define the helix, for finite real `R` and `h`, by

`H(n)=(R cos(2πn/10), R sin(2πn/10), hn/10)`.

Let `P` be the Gaussian irreducibles, retaining identities as distinct vertices (including associates). Map `z∈P` to `H(S⁻¹(z))`. For a fixed finite real `δ≥0`, connect distinct vertices when their three-dimensional helix distance is at most `δ`.

If `h≠0`, every edge of this graph is an edge of the original Gaussian-prime graph at distance cutoff

`D*=10Lδ/|h|`.

Therefore, conditional on the source theorem's `UniformEndpoint` at this finite cutoff, every helix component is finite and has a common size bound independent of its starting vertex. This conclusion is for each fixed `S,L,R,h,δ` satisfying the assumptions. It does not assert one bound uniformly over all cutoffs or heights.

## Method and reproduction

For addresses `n,m`, telescoping the consecutive-step bound gives `|S(n)-S(m)|≤L|n-m|`. The helix chord is at least its vertical-coordinate difference, so

`||H(n)-H(m)||₂ ≥ |h||n-m|/10`.

A helix edge of length at most `δ` therefore has `|n-m|≤10δ/|h|`; its Gaussian-plane distance is at most `L|n-m|≤D*`. The identity on Gaussian-prime vertices maps every helix edge to an edge of the source graph. Each finite helix path is consequently a source path, and each target component is contained in the corresponding Gaussian component. Applying the source uniform-component bound gives the result.

The proof uses a one-way edge inclusion. It does not show that the two metrics are equivalent or that the helix drawing preserves Gaussian distances. The global step bound is sufficient for this transfer; bijectivity and nonzero height alone are insufficient.

There is no computational experiment to reproduce. A reader can inspect the argument using the linked pinned model and endpoint declarations; all inequalities and assumptions are stated here.

The exact chord formula for an integer address gap `d≥1` is

`||H(n+d)-H(n)||² = 4R² sin²(πd/10) + h²d²/100`.

For fixed `R,h,δ` with `h≠0`, let `K` be the largest nonnegative integer gap whose squared chord is at most `δ²`, with `K=0` when no positive gap qualifies. The source cutoff can then be sharpened to `D_phase=LK≤D*`. This may improve the bound for some parameter values, but no useful parameter range or finite-graph effect has been selected or tested. Small nonzero `|h|` can still make the cutoff weak.

## Results and boundary cases

When `h=0`, `H` repeats every ten addresses. There are infinitely many Gaussian irreducibles: if a finite list existed, take their nonzero product `P`; for sufficiently large integer `a`, `1+aP` has norm greater than one and hence an irreducible divisor by norm descent. That divisor also divides `aP`, so it would divide `1`, a contradiction. The infinite address set of irreducibles splits across ten residue classes, so one class is infinite. Retaining identities makes all vertices in that class coincide in the display and form an infinite clique for every `δ≥0`. This is a counterexample for the altered identity-retaining graph, not for the source theorem.

If the finite list were empty, `1+i` itself is irreducible because its norm is two. Otherwise, the product argument above yields the contradiction. Norm descent uses multiplicativity of the Gaussian norm. In a factorisation `u=vw` with both factors nonunits and `u≠0`, multiplicativity gives `N(v),N(w)≥2`, so both norms are positive and strictly smaller than `N(u)`. Repeatedly choosing a nonunit factor therefore terminates at an irreducible.

If the global step bound is removed, bijectivity and nonzero height do not suffice. The complement of the irreducibles is countably infinite; it contains the distinct reducible integers `2k` for `k≥2`. Choose a bijection that puts an enumeration `p₁,p₂,…` of all Gaussian irreducibles at addresses `10k`, filling the other addresses bijectively with the complement. Then `H(10k)=(R,0,hk)`, so consecutive irreducibles form an infinite path at cutoff `δ=|h|`. This arbitrary enumeration is not the square spiral; it shows why some global address-control condition is needed for the stated transfer argument.

For the actual unit-step square spiral, `L=1`. This establishes the sufficient condition used by the application, not that the same bound is necessary for every possible enumeration or proof.

## Limitations and unresolved issues

This is an elementary conditional corollary from an existing uniform-component theorem. Its value is a concrete example of how changing a representation can create a new graph question, then how a simple map and inequality can transfer a known bound. It does not establish a new theorem in prime theory, an Infinity or odometer connection, an ordinary-prime prediction, a physical result, or improved reader understanding. No empirical display test was run.

The derivation was reconstructed and challenged against the pinned model and endpoint declarations by an AI reviewer. It was not formalised in Lean. The source theorem's full transitive proof closure and cache-source authentication remain open under the separate family-028 evidence record. The challenge is not a human sign-off or a fresh proof of that theorem.

## Authorship, chronology and prior work

No exhaustive prior-art search for this corollary or field-level novelty claim is made. The source theorem remains attributed to OpenAI. The private research record documents the derivation on 2026-10-12; this repository's file history documents when this artifact was first made public. Neither date establishes first conception or priority over unpublished work.

| Event | Date/time and zone | Evidence and identifier | What this date establishes |
|---|---|---|---|
| Source manuscript date | 2026-09-26 | Title page in the [pinned manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/main.tex) | Date printed on the OpenAI theorem manuscript. |
| Pinned source revision | 2026-10-08 05:20 UTC | [OpenAI Math commit](https://github.com/openai/math/commit/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb) | Public history of the source snapshot used; not an exhaustive search for earlier postings. |
| Private derivation and AI challenge | 2026-10-12, Africa/Johannesburg; exact time not retained | Private execution record and source-challenge report | A dated research record of this project application, not first conception or priority. |
| First public appearance of this artifact | See [GitHub file history](https://github.com/RichardGeorgeDavis/research-artifact-ledger/commits/main/artifacts/gaussian-moat-helix-metric-corollary/README.md) | Commit adding this file | Public repository chronology only. |

## Independent review

Reviewer and date: AI reviewer, 2026-10-12; runtime model identity unavailable.

Scope of review: reconstructed the graph definitions, source endpoint use, constants, quantifiers, component containment, identity convention, zero/negative cutoffs, zero height and weakened-enumeration counterexample from the pinned source model and the frozen derivation.

Findings and unresolved points: conditionally accepted under the recorded source endpoint and stated hypotheses; no defect identified. This was not Lean formalisation, full source-theorem review, independent human review or a novelty assessment.

## What this means

The result shows how a changed representation can create a separate graph question and how a simple map plus inequality can transfer a known bound. It does not establish a new theorem in prime theory, an Infinity or odometer connection, an ordinary-prime prediction, a physical result or improved reader understanding. No empirical display test was run.

## Sources and provenance

| Source | Version | Use and limit |
|---|---|---|
| [OpenAI Math family 028 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/main.tex) | Pinned commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` | Source uniform-component theorem. This artifact does not claim authorship or priority for that theorem. |
| [Formal graph model](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/Model.lean) | Same source commit | Vertex identity, adjacency and endpoint definitions used for alignment. |
| [Formal endpoint](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/Main.lean#L99-L103) | Same source commit | Declares `fullMain : MainEndpoint ∧ UniformEndpoint`; the corollary uses `UniformEndpoint`. |
| [Family-028 evidence record](../gaussian-moat-formal-check/README.md) | Public record, version 0.1.3 | Build/axiom output and trust boundary; this artifact does not extend its proof audit. |

## Chronology

The private research record dates the derivation and AI challenge to 2026-10-12 (Africa/Johannesburg); an exact time is not retained. The first public appearance is the commit shown in this file's [GitHub history](https://github.com/RichardGeorgeDavis/research-artifact-ledger/commits/main/artifacts/gaussian-moat-helix-metric-corollary/README.md). That repository timestamp establishes public-record chronology only.

## Change history

| Version/date | Change | Evidence and limit |
|---|---|---|
| 0.1.0 / 2026-10-12 | Added the conditional helix-metric graph application | AI-challenged derivation; no Lean formalisation, exhaustive novelty review or human sign-off. |
