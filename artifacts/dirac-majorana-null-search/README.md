# What a neutrinoless double-beta null search can establish about neutrino nature

Status: `source review`

Version: `0.1.0`

Last updated: `2026-10-27`

Author: Richard George Davis, with AI-assisted source analysis and writing.

Underlying source authors retain credit for the experiment, oscillation analysis and physical interpretations discussed here. This note reports a bounded source comparison; it does not claim a new particle-physics result, measurement, likelihood analysis, or claim about authorship of those results.

## Question and intended use

What does the KamLAND-Zen complete-dataset search establish about the Dirac/Majorana question, and which assumptions connect its half-life limit to an effective Majorana mass?

This note is for readers distinguishing a null neutrinoless double-beta-decay search from a particle-nature verdict. It follows one experiment's reported limit and its conditional effective-mass translation, then checks how the relevant phase dependence relates to neutrino oscillations. It is a source review, not a new fit or an exhaustive survey of lepton-number-violating mechanisms.

## Bounded conclusion

KamLAND-Zen reports no signal excess and a 90% confidence lower limit on the neutrinoless double-beta half-life from its combined 400+800 datasets. Under dominant light-Majorana-neutrino exchange and the paper's stated axial-coupling, phase-space and nuclear-matrix-element choices, the half-life limit maps to a range of upper bounds on the effective Majorana mass. The range is not a measured mass interval, and a null result at finite sensitivity does not establish that neutrinos are Dirac or exclude Majorana neutrinos.

The combined 400+800 half-life limit is `T₁/₂⁰ν > 3.8 × 10²⁶ yr` at 90% CL. It is distinct from the KamLAND-Zen 800-only profile-likelihood limit `>3.5 × 10²⁶ yr` and its separate Feldman–Cousins limit `>4.3 × 10²⁶ yr`. The latter pair differs by statistical construction; neither is the combined result.

For light-Majorana exchange, the paper reports `mββ < 28–122 meV` at 90% CL across its listed phenomenological nuclear matrix elements. This translation assumes `g_A≈1.27` and the stated phase-space factor. Nuclear-model and interaction uncertainties remain material; the paper discusses quenching/contact contributions, and the listed interval is not a model-independent experimental mass measurement.

NuFIT 6.0 states that its Majorana phase matrix does not enter oscillations and defines the neutrinoless double-beta effective mass as `mₑₑ=|Σᵢ mᵢ Uₑᵢ²|`. Under the same phase labels printed for its mixing matrix, direct substitution gives phase factors that appear sign-inconsistent with NuFIT's later expanded Eq. (5.4). The discrepancy is an apparent internal phase-label/convention mismatch: the paper does not announce a relabelling between the equations. The free phases span the same full effective-mass envelope after relabelling, so this notation issue does not change the stated oscillation result or the allowed envelope. The invariant `mₑₑ` definition avoids the ambiguity.

## Evidence class and review status

The evidence class is `source review`. The coordinator checked the final published KamLAND-Zen paper and versioned NuFIT source, including a visual inspection of the relevant NuFIT PDF equations. An independent AI public-source challenge reviewed the named public packet and source links at the requested setting `gpt-6.1-sol / high`; serving telemetry was unavailable. The challenge confirmed the combined and 800-only limit distinctions, the conditional mass conversion, the non-inference from a null result, and the apparent NuFIT phase-label sign mismatch. No human specialist review or peer review of this synthesis is claimed.

No experimental fit, detector-data analysis, likelihood, nuclear-matrix-element conversion, mass-ordering analysis, or physical particle-nature verdict was reproduced. This note establishes no field-level novelty, priority or Infinity Research connection.

## Sources and provenance

| Source | Version/date | Role and locator | Access and rights |
|---|---|---|---|
| KamLAND-Zen Collaboration, “Search for Majorana Neutrinos with the Complete KamLAND-Zen Dataset,” *Phys. Rev. Lett.* 135, 262501 (2025), DOI [10.1103/jkf6-48j8](https://doi.org/10.1103/jkf6-48j8), [arXiv:2406.11438v2](https://arxiv.org/abs/2406.11438v2) | Final published version; 29 December 2025 | Summed-electron search region and best fit (printed pp. 262501-2, -4); 800-only profile-likelihood and Feldman–Cousins bounds (p. -4); combined 400+800 Eq. (1) and mass translation Eq. (2), Table II (p. -5) | Linked and paraphrased. The institutional repository copy identifies the final published version and CC BY 4.0: [University of Amsterdam PDF](https://pure.uva.nl/ws/files/297309160/jkf6-48j8.pdf). No data, table or figure is reproduced. |
| Esteban et al., “NuFit-6.0: Updated global analysis of three-flavor neutrino oscillations,” *JHEP* 12 (2024) 216, [arXiv:2410.05380v2](https://arxiv.org/abs/2410.05380v2) | v2, 28 October 2025 | Mixing-matrix convention and Majorana phase statement (printed p. 3, Eq. (2.1) and following paragraph); invariant `mₑₑ` (printed p. 21, Eq. (5.2)); expanded phase expression (printed p. 21, Eq. (5.4)) | Linked and paraphrased. The v2 PDF was visually inspected at pp. 5 and 23 of the downloaded file; no figure or table is reused. |

Public visibility does not grant general reuse rights. This note quotes no substantial source text and redistributes no source data, table or figure. The Ledger assigns no open licence; no broader reuse permission is implied.

## Observable-to-claim map

1. The experimental observable is the summed energy of the two electrons. Under the assumed 0νββ decay, a peak is expected at 2.458 MeV in the KamLAND-Zen search. In the complete-dataset fit, the best-fit 0νββ signal is zero events, so the paper reports no excess over its background expectation.
2. The combined KamLAND-Zen 400+800 analysis reports a lower half-life bound of `3.8 × 10²⁶ yr` at 90% CL (Eq. (1)). It does not report a positive decay signal.
3. To infer `mββ`, the collaboration assumes light-Majorana-neutrino exchange and applies the stated `g_A`, phase-space factor and nuclear matrix elements. Across the listed nuclear calculations, it reports upper limits from 28 to 122 meV (Eq. (2), Table II). These assumptions make the translation conditional.
4. In the three-neutrino mixing framework, oscillation probabilities use products of mixing-matrix elements in which the column Majorana phase factors cancel. NuFIT therefore states that the phase matrix `P` does not affect oscillations. Its Eq. (5.2) effective-mass definition instead contains the squared electron-row elements, so relative phases can affect `mₑₑ` through interference.
5. Directly substituting the NuFIT Eq. (2.1) first-row elements into Eq. (5.2) yields an apparent sign-convention mismatch with the expanded Eq. (5.4). Because the two Majorana phase labels are freely variable, changing their labels by the corresponding Dirac-phase shift leaves the complete allowed envelope invariant. The equations should be read with that convention caveat; the source does not specify an explicit relabelling.

## Limitations and unresolved issues

- A null search means no signal was established at the reported sensitivity. It does not distinguish Dirac from Majorana neutrinos.
- The `28–122 meV` range is a set of conditional upper limits across nuclear-matrix-element calculations, not a measured interval or probability that neutrinos are Majorana.
- The light-Majorana-exchange relation does not survey every possible lepton-number-violating mechanism. No alternative mechanism is evaluated here.
- The NuFIT phase-sign issue is an apparent convention inconsistency between its displayed equations under identical phase labels. It is not evidence that Majorana phases affect oscillations, and it does not change the full free-phase `mₑₑ` envelope.
- The AI challenge is not a human specialist review, peer review, independent experimental analysis or reproduction of underlying data.
- No laboratory data, fit, likelihood, nuclear calculation, ordering test, or new physical conclusion was produced. This is not a full literature review.

## Authorship and chronology

This bounded note is authored by Richard George Davis with AI-assisted source analysis and writing. The underlying research, measurements and interpretations remain attributed to their source authors. All sources predate this note. No originality, priority or first-discovery claim is made.

## Independent review

Reviewer: one independent AI public-source challenge; requested setting `gpt-6.1-sol / high`; serving telemetry unavailable. Date: 2026-10-27.

Scope: distinguish the combined and 800-only limits; verify the light-Majorana mass conversion assumptions; check the non-inference from a null result; verify Majorana-phase independence in oscillations; and check the displayed NuFIT effective-mass equations and phase conventions.

Findings: the reviewer confirmed the combined 400+800 limit and separate 800-only profile-likelihood/Feldman–Cousins values, the conditional mass-limit range, and that the null result does not determine particle nature. It identified that NuFIT Eq. (5.4) uses `αᵢ−δCP` whereas substitution from Eq. (2.1) into invariant Eq. (5.2) yields `αᵢ+δCP` after factoring out a common phase. The reviewer and coordinator found the complete free-phase envelope unchanged. No fit or human specialist review occurred.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-10-27 | Initial bounded source-review artifact | Version-pinned public sources, coordinator source inspection and an independent AI public-source challenge; conditional interpretation and equation-convention limits are stated above. |
