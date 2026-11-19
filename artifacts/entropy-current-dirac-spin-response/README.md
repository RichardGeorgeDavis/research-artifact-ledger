# Two derivation checks on an entropy-current emergent-gravity proposal

Status: `source review` and `bounded derivation`

Version: `0.1.2`

Last updated: `2026-11-19`

Author(s): Richard George Davis

## Question and intended use

Do two selected derivation steps in the latest public version of Yang, Yang and Mei's entropy-current/modified-Dirac proposal support the claims made from them, and what does the proposal add to the existing bounded entropy/geometry comparison?

This source review is for readers comparing emergent-gravity proposals and checking the proposal's stated spin-response route. It does not assess the whole theory, establish a physical effect, or claim novelty.

## Claim supported

In preprint v3 §6.1, the authors start with an unpolarised ensemble, state the homogeneous precession equation `d⟨S⟩/dt = ω_entropy × ⟨S⟩`, and then infer `P ≃ |ω_entropy| τ_freeze`. The stated equation preserves a zero initial ensemble mean exactly, so that equation alone cannot produce the nonzero polarisation used in the subsequent estimate. For a nonzero prepared spin `P₀` and constant `ω`, the leading vector change is `ΔP = τ(ω × P₀) + O(τ²)`; pure precession preserves the spin magnitude. Thus `|ω|τ` is a small rotation angle, not generally a polarisation.

In Appendix C.2.3, the text takes `d_a ≤ d_{a*}` because `a*` has maximal quantum dimension, then states `1/d_a ≤ 1/d_{a*}`. For positive dimensions the inequality reverses: `1/d_a ≥ 1/d_{a*}`. Consequently, the stated `q = 1/d_{a*}` is not an upper bound on all mode factors as written unless the relevant dimensions are equal. For a finite set of non-Abelian modes with each `d_a > 1`, the corrected bound `q = max_a(1/d_a) = 1/min_a(d_a)` is still below one; this local correction does not validate the manuscript's other assumptions or its fixed-point proof. The worked `D(S₃)` example immediately after Eq. (C.6) calls 2 the largest non-Abelian quantum dimension. Lou et al.'s published topological-data table lists simple-object dimensions `(1, 1, 2, 3, 3, 2, 2, 2)`, so the maximum is 3 and the minimum non-Abelian dimension is 2. Thus the example's `q=1/2` matches `1/min d_a`, not the stated `1/max d_a=1/3`; the numerical contraction factor is conditionally usable for this example, but its stated maximum-dimension rationale is inconsistent. This does not establish the ETRG map or fixed-point result.

Section 6.1 labels `8 fm/c` as approximately `40 MeV⁻¹`; the correct natural-unit conversion is approximately `40.5 GeV⁻¹`. Substituting the correctly converted time gives about `3.4 × 10⁻⁴ GeV⁻²`, consistent with the printed central estimate `3.5 × 10⁻⁴ GeV⁻²`. The printed unit label is wrong by a factor of 1,000; this check does not establish which unit was used in any unreported calculation.

## Evidence class and review status

This is a bounded source review and mathematical derivation of two local claims in the version-3 preprint, plus a natural-unit transcription check. The coordinator inspected the full version-3 text through a public text-rendering proxy and checked the original preprint's version metadata and the Frontiers abstract. One independent AI reviewer (`gpt-6.2-astra / high`) checked the public version-3 source and reached the same conclusion about the zero-mean precession equation. A second independent AI reviewer (`gpt-6.1-sol / high`) checked the spin inference, small-angle wording, natural-unit calculation and Appendix C reciprocal bound. No human specialist review or independent experimental replication is claimed.

The preprint page labels v3 as not peer reviewed. Frontiers lists the article and an acceptance date of 28 September 2026, shows two anonymous reviewers, and says the final formatted article will be published soon. The final formatted article was not available through the publisher route checked here.

## Sources and provenance

| Source or input | Version/date | Role in this artifact | Relevant claim or section | Access or rights notes |
|---|---|---|---|---|
| [Yang, Yang and Mei, *Emergent Gravity from Quantum Information Flow: A Modified Dirac-Equation Perspective*](https://www.preprints.org/manuscript/202607.1698/v3) | Preprint v3, posted 28 September 2026 | Primary source for the modified Dirac coupling, spin response, STAR estimate and gravitational claims | §§3.1–3.4, 6.1, eqs. (29)–(34), (70)–(71); Appendices B.4, C.2.3 and eq. (C.6) | Preprints.org identifies v3 as latest and marks the preprint not peer reviewed. Its direct page exposes metadata and abstract to the reader used here. Full text was inspected via the text-rendering view below; equations were checked against the original version identity and the rendered text may not preserve all layout details. |
| Lou, Shen, Chen and Hung, [*A (dummy’s) guide to working with gapped boundaries via (fermion) condensation*](https://doi.org/10.1007/JHEP02(2021)171) | JHEP 02 (2021) 171, Appendix C, D(S₃) topological-data table | Quantum dimensions of the eight simple objects | Published source table; used only to check the worked example's dimension claim. |
| [Version-3 text-rendering view of the same Preprints.org page](https://r.jina.ai/https://www.preprints.org/manuscript/202607.1698/v3) | Retrieved 19 November 2026 | Public full-text rendering used to inspect version-3 sections and equations | §§3, 6.1, Appendix B.4, Appendix C.2.3, eq. (C.6) | Rendering proxy, not an independent source or version. Captured response: 167,545 UTF-8 characters; SHA-256 `ed4d4b2ab5401975e1e32e2e4c42dc110819039c05d23d6e958b5e341073ac19`. No full source file is redistributed here. |
| [Frontiers in Physics article abstract](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2026.1945804/abstract) | DOI `10.3389/fphy.2026.1945804`; accepted 28 September 2026 | Publisher metadata and abstract comparison | Abstract and article status | The abstract page states the final formatted version will be published soon. Its displayed abstract repeats the final paragraph and loses some mathematical symbols in rendering. |
| [Preprints.org version 2](https://www.preprints.org/manuscript/202607.1698/v2) | Posted 25 August 2026 | Version-history comparison only | Abstract | v2 states `λ ∼ 10⁻⁷–10⁻⁵ GeV⁻²`, while v3 and the Frontiers abstract state `λ ∼ 10⁻⁵–10⁻³ GeV⁻²`. This records version drift; no reason for the change is inferred. |

The authors and source paper originate the model and its claims. This artifact's author is responsible only for the bounded source transcription and derivations stated here. No first-conception, priority, or originality claim is made.

## Method and derivation

### Zero-mean precession

The stated vector equation is linear and homogeneous. For a time-independent angular-velocity vector it has solution `⟨S(t)⟩ = R(t)⟨S(0)⟩`, where `R(t)` is a rotation matrix. Therefore `⟨S(0)⟩ = 0` implies `⟨S(t)⟩ = 0` for all `t`. The same result holds for time-dependent `ω(t)`: the linear evolution operator maps the zero vector to itself.

Equivalently, for a fully unpolarised spin-½ ensemble with density matrix `ρ(0) = I/2`, unitary precession gives `ρ(t) = U(t)ρ(0)U†(t) = I/2`; it does not create a preferred spin direction. For a prepared nonzero polarisation `P₀` and constant `ω`, first-order expansion gives `ΔP = τ(ω × P₀) + O(τ²)`, while `|P|` remains constant. The small-angle relation `|ω|τ` is the rotation angle; it does not follow as a generated polarisation from the specified zero-polarisation initial state. An additional mechanism beyond the stated homogeneous precession equation, with its own assumptions and calculation, is needed to derive nonzero polarisation.

The source itself notes that the conventional thermal-vorticity and electromagnetic contributions are assumed negligible or separately subtracted, and that a full joint fit is left for future work. This review does not decide what additional spin-production dynamics could yield STAR's observed polarisation.

### Natural-unit conversion and central-value check

Using `ℏc ≈ 197.326 MeV·fm`,

`8 fm/c = 8 / (197.326 MeV) ≈ 0.04054 MeV⁻¹ = 40.54 GeV⁻¹`.

With the source's illustrative values `P_Λ = 0.005`, `m_Λ ≈ 1.116 GeV`, `|∇ × s| ≈ 0.4 GeV⁴`, and the correctly converted `τ_freeze ≈ 40.54 GeV⁻¹`, the displayed estimate gives

`λ ≈ P_Λ m_Λ / (|∇ × s| τ_freeze) ≈ 3.44 × 10⁻⁴ GeV⁻²`.

This is consistent with the source's approximate `3.5 × 10⁻⁴ GeV⁻²`. It does not fix the spin-generation problem or independently validate the chosen inputs, uncertainty range, data interpretation, model, or gravitational conclusions.

### Reciprocal contraction bound

Appendix C.2.3 defines `d_{a*}` as the maximum of the participating non-Abelian quantum dimensions, so for each such `a`, `d_a ≤ d_{a*}`. Since both are positive, taking reciprocals gives `1/d_a ≥ 1/d_{a*}`, the reverse of the printed inequality. Therefore the displayed `q = 1/d_{a*}` is not established as a uniform upper bound on the claimed factors `1/d_a` from that step. If the stated per-mode factors are accepted and the participating non-Abelian set is finite with every `d_a > 1`, then `q = max_a 1/d_a = 1/min_a d_a < 1` is a valid weaker candidate bound. This check does not audit whether the normalised ETRG map has the per-mode factors the text assigns it, whether the contraction norm is correct, or whether the remaining fixed-point proof is valid.

## Results

The modified Dirac coupling and its non-relativistic spin-curl response form a distinct source-defined candidate chain: entropy-current vector → fermion coupling → curl-dependent spin precession. In the same paper, the curvature coupling and assumed nonzero entropy-field bilinear are used to write an induced Einstein–Hilbert coefficient, while Appendix B.4 assigns the spin-2 tensor degrees of freedom to an independent frame field. These are source claims, not derivations reproduced here.

The paper names Bianconi's *Gravity from Entropy* as related work, but the inspected text does not supply a matched observable, parameter map or adapter to the existing three-model entropy/geometry comparison. It therefore adds a distinct candidate to compare, but does not establish a bridge or common test. Its broad gravitational claims, STAR analysis, LIGO/Virgo constraint transfer, and companion-paper tensor-network arguments remain outside the checks performed here.

The version-2 to version-3 shift in the abstract's `λ` interval is material for any numeric reuse. It must be resolved from version-matched sections, assumptions and data before the parameter range is used in a calculation.

## Limitations and unresolved issues

- The full formatted Frontiers article was not available through the publisher route checked; source-level claims here refer to preprint v3 as identified by Preprints.org.
- The public text renderer can damage symbols, equations and table layout. The two central derivations above were independently checked from the rendered text, but no PDF byte-for-byte comparison or visual page inspection is claimed.
- No STAR data, likelihood, hydrodynamic output, uncertainty propagation, or fit was reproduced. The source's polarization range and inputs remain author-reported.
- No independent derivation of the modified Dirac equation, Proca field dynamics, induced Newton constant, graviton mass, or emergence of spacetime was performed.
- The scope is not a comprehensive review of prior work on spin transport, induced gravity, entropy currents, string-net models or emergent gravity. No field-level novelty, physical validation, or global no-go claim is made.
- The Appendix C.2.3 check covers the reciprocal inequality and the `D(S₃)` worked-example dimension claim; the ETRG construction and fixed-point proof are not audited.
- No experiment, software installation, dataset acquisition, author contact or publication activity beyond this repository artifact was performed.

## Independent review

Reviewer and date: AI subagent (`gpt-6.2-astra / high`) and AI subagent (`gpt-6.1-sol / high`), 19 November 2026.

Scope of review: the first reviewer checked public version-3 sections 3 and 6.1 and the STAR estimate's algebraic inference; the second checked the spin equation, small-angle interpretation, unit conversion and Appendix C.2.3 reciprocal bound. Both independently confirmed that zero-mean precession preserves zero; the second confirmed the reversed reciprocal inequality and its conditional weaker bound.

Findings and unresolved points: both reviewers independently confirmed that the stated homogeneous equation preserves zero-mean precession. The second reviewer also checked the small-angle interpretation, natural-unit conversion and central estimate, and the reciprocal inequality's direction and conditional finite-set bound. No human specialist assessment, independent data analysis, or full-theory review is claimed.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.2 / 2026-11-19 | Added the `D(S₃)` worked-example dimension check | The preprint calls 2 the largest non-Abelian dimension, while Lou et al.'s topological-data table includes dimensions 3; the example's factor 1/2 is the reciprocal of the minimum non-Abelian dimension. No ETRG or fixed-point assurance is added. |
| 0.1.0 / 2026-11-19 | Initial source-review artifact | Version-3 full-text source check; zero-mean precession derivation; unit conversion; independent AI review. |
| 0.1.1 / 2026-11-19 | Clarified which independent reviewer checked the unit conversion | Corrected the review summary to match the scoped reviewer records in the private item834 receipt; scientific claims and derivations are unchanged. |
