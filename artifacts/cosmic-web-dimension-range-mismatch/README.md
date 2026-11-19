# An arithmetic mismatch in a stated cosmic-web dimension range

Status: `source review`

Version: `0.1.2`

Last updated: `2026-11-19`

Author: Richard George Davis, with AI-assisted source analysis and writing.

This note checks one printed dimension-range calculation and distinguishes it from nearby primary-source definitions. It does not review the wider theory in the preprint or claim a dimension for the universe.

## Question

Does the dimension range printed in the inspected Authorea preprint follow from its stated exponent and equation, and what do the named primary sources establish about related dimension measures?

## Claim supported

The inspected Authorea v1 text gives `γ≈1.7–1.9`, states `D=3−γ`, and then reports `D≈2.1–2.3`. Substituting the stated endpoints gives `D≈1.1–1.3`: `3−1.9=1.1` and `3−1.7=1.3`. The printed range does not follow from the equation and exponent range as written. This identifies an internal arithmetic mismatch; it does not establish which input, equation or reported range the author intended to change.

Related primary sources use distinct measures. Einasto et al. define a scale-dependent local effective dimension from the signed logarithmic slope of `1+ξ(r)` and distinguish it from a correlation dimension calculated using an averaged structure function. Cautun et al. use grid-cell box counts on identified filament and wall networks and report scale-dependent behaviour, including a filament example near `d≈2.2`. These values and estimators cannot be substituted for one another or read as a single dimension of the universe.

## Evidence class and review status

Evidence class: `source review`, with a direct arithmetic check on the named version's indexed text. The initial review and a separate public-source review on 19 November 2026 reported matching the Authorea v1 passage; the second review located the indexed text at the exact hosted PDF URL and checked its cover metadata and §3 equations. The coordinator's direct DOI/PDF fetch remains unsuccessful. No downloaded or visually rendered PDF is claimed. This review does not reproduce a cosmological calculation, analyse data or assess the wider model.

One independent public-source challenge requested `gpt-6.1-sol / high`; serving telemetry was unavailable. The reviewer confirmed the arithmetic mismatch and distinguished the selected primary-source estimators. The Authorea DOI destination returned an access challenge; its indexed v1 PDF text was available to the reviewer. A PDF screenshot attempt failed, so no visual page inspection is claimed. No human specialist review or peer review is claimed.

## Sources and provenance

| Source | Version and locator | Contribution and boundary |
|---|---|---|
| Haci Sogukpinar, “A Fractal Universe: Observational Evidence from the Cosmos to the Quantum Vacuum in the Unified Fractal Quantum Field Theory,” [Authorea DOI](https://doi.org/10.22541/au.176901880.04316314/v1) ([hosted v1 PDF](https://d197for5662m48.cloudfront.net/documents/publicationstatus/302617/preprint_pdf/1b70f1b7ec409263498cbff9083f6637.pdf)) | v1, 21 January 2026; §3, Eqs. (3)–(4) | The inspected text states `γ≈1.7–1.9`, `D=3−γ`, and `D≈2.1–2.3`. The source labels itself not peer reviewed. The cited range is not entailed by the printed equation and exponent. No author intent or validity of the broader theory is inferred. |
| Einasto, Hütsi, Kuutma and Einasto, “Correlation function: biasing and fractal properties of the cosmic web,” [arXiv:2002.02813v2](https://arxiv.org/abs/2002.02813v2) | v2; §2.1, Eqs. (3)–(4), §§4.2–4.3 and §5 | Defines `g(r)=1+ξ(r)` and a signed local slope `γ(r)=d log g(r)/d log r`, with local effective `D(r)=3+γ(r)`. It distinguishes this from correlation dimension `D₂` calculated using an averaged structure function. Reported values depend on scale and sample. |
| Cautun et al., “Evolution of the cosmic web,” [arXiv:1401.7866v1](https://arxiv.org/abs/1401.7866v1) | v1; §8.4, Eqs. (17)–(19), Figs. 41–42 | Uses grid-cell counts for identified filament and wall networks. The fitted box-counting behaviour changes with scale and has a redshift-dependent break; one filament example is near `d≈2.2`. This is not Einasto's local correlation-function dimension. |
| Aragón-Calvo et al., “The Spine of the Cosmic Web,” [arXiv:0809.5104v1](https://arxiv.org/abs/0809.5104v1) | v1; §§2–4 | Describes watershed-based identification of voids, walls and the filamentary spine and tests segmentation with a Voronoi model. This version supplies no box-counting estimate and is not used to support a numerical dimension. A later published version is a distinct text and is outside this review. |

Only links and short mathematical expressions are reproduced; no source figures, tables, data or substantial text are included. Public visibility does not grant general reuse rights, and this artifact adds no licence.

## Method and reproduction

For the arithmetic check, evaluate the stated function at both endpoints of the stated interval: `3−1.9=1.1` and `3−1.7=1.3`. No code is needed. For each related dimension claim, inspect the source's object, estimator, sign convention, scale range and sample before comparing its reported value with another source.

No dimension was recalculated from observations or simulations. No dataset, likelihood, source code, figure or model output was accessed or reproduced. The arithmetic check establishes only that the printed inputs and output disagree.

## What this does not establish

- It does not identify the author's intended correction or explain the mismatch.
- It does not validate or refute the preprint's broader theory.
- It does not establish a universal fractal dimension, effective dimension or topology of the universe.
- It does not make the local effective fractal dimension, averaged-structure-function correlation dimension, network box-counting exponent and segmentation method interchangeable.
- It does not correct or change any cited primary study.
- It does not establish novelty, priority, empirical evidence, peer review or qualified human specialist review.

## Authorship and chronology

This is a bounded source-to-claim comparison authored by Richard George Davis with AI-assisted source analysis and writing. The underlying authors retain credit for their sources and results. The public Ledger commit records when this version appeared in the repository; it does not establish first conception, originality or priority.

## Independent review

An earlier independent AI public-source challenge, requested at `gpt-6.1-sol / high`, reported confirming the arithmetic against indexed Authorea v1 text and distinguishing the selected primary-source estimators; serving telemetry was unavailable. A later review requested at `gpt-6.2-astra / high` could not retrieve the DOI or hosted PDF and checked only the related primary-source definitions. On 19 November 2026, a separate public-only review requested at `gpt-6.2-astra / high` found indexed full text at the exact hosted v1 PDF URL and matched the cover metadata and §3 equations (3)–(4), including the printed exponent and dimension range; serving telemetry was unavailable. This freshly supports the source-text attribution at the indexed-text level. The coordinator still could not retrieve the DOI destination or download/render the PDF, so no visual PDF inspection is claimed. No private notes, study reproduction, broader theory assessment, human specialist review or peer review is claimed.

## Change history

| Version/date | Change | Evidence |
|---|---|---|
| 0.1.2 / 2026-11-19 | Reverified the named Authorea v1 passage using indexed text at the exact hosted PDF URL; clarified that the coordinator still could not download or visually inspect the PDF. | Separate public-only review matched the cover metadata and §3 equations (3)–(4); serving telemetry unavailable. |
| 0.1.1 / 2026-11-19 | Qualified current source-access status; retained the earlier source-attributed arithmetic discrepancy as historical pending a fresh version-matched copy. | Independent and coordinator rechecks could not retrieve Authorea v1; the earlier review record is preserved and its serving telemetry remains unavailable. |
| 0.1.0 / 2026-11-19 | Initial bounded source-review note. | Authorea v1 indexed text as reported in the initial independent challenge; version-pinned primary-source records and direct arithmetic substitution. |
