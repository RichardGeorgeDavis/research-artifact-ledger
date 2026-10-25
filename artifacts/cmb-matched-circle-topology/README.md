# What matched-CMB-circle nulls constrain about global topology

Status: `source review`

Version: `0.1.0`

Last updated: `2026-10-26`

Artifact author: Richard George Davis, with AI-assisted source analysis and writing.

Underlying source authors: the Planck Collaboration; the authors of the COMPACT Collaboration study by Petersen et al. This artifact interprets selected claims from their papers and does not claim authorship of the underlying cosmological analyses.

Two independent AI source-only checks reviewed the named public sources and a bounded public-source packet. Neither was a human specialist review or peer review. No human review is claimed.

## Question and intended use

What do the selected Planck and Petersen et al. matched-circle analyses constrain about compact spatial topology, and what do their null results leave unresolved?

This note is for readers comparing CMB matched-circle limits with claims about the universe's global topology. Its scope is the evidence and assumptions in two version-pinned papers, not a new cosmological analysis.

## Claim supported

These papers support observer-centred, model-specific constraints from matched CMB-circle non-detections. The Planck matched-circle analysis constrains detectable back-to-back circle pairs in a specified flat cubic-torus model under its stated assumptions; Petersen et al. translate earlier WMAP/Planck temperature-circle nulls into constraints across nine orientable Euclidean manifold families. Neither result identifies the actual global topology of our universe or excludes every shorter loop away from our location.

Planck reports no statistically significant matched-circle correlation in its temperature or E-mode maps. Its T3 polarization matched-circle result gives a lower bound of approximately `R_i = L/2 ≥ 0.97 χ_rec` at 99% confidence, conditional on the fiducial flat ΛCDM setting, a minimum detectable circle radius near 15°, and the fundamental-domain orientation and mask permitting detection. The search considers antipodal (back-to-back) circle centres.

Planck's separate low-ℓ likelihood analysis must be kept distinct. The authors use a likelihood fall-off `Δln L ≈ -5` as a convenient approximation to a 3σ/99% contour, not a Bayesian posterior constraint without an upper-size prior. The marginalized limits use combined low-resolution temperature and polarization data: `R_i > 0.97 χ_rec` for T3 and `R_i > 0.56 χ_rec` for T1. The T3 profile-likelihood limit is weaker, `R_i > 0.79 χ_rec`. These are not the same statistic or data subset as the 99% polarization-only matched-circle result.

Petersen et al. do not rerun the WMAP/Planck map search. They translate earlier temperature-circle non-detections across nine orientable Euclidean topology families. Their headline 98.5% bound concerns the shortest non-contractible loop through our location, relative to the comoving diameter of the last-scattering surface, and inherits the earlier search's finite detection thresholds. The authors show that shorter loops can avoid our location and, for many of the examined families, be factors of roughly 2–6 shorter than the last-scattering-surface diameter while remaining compatible with that observer-centred bound.

## Evidence class and review status

The evidence class is `source review`. The analysis is a close reading and source-to-claim comparison of two public papers. No CMB map, likelihood, source code or numerical result was independently reproduced.

Two separate AI source-only checks reviewed the bounded claims against the cited papers. The first checked the search restrictions, statistical labels, observer-location ceiling and topology scope. The second additionally confirmed that the 99% matched-circle result uses polarization alone, while the separate low-ℓ likelihood contour uses combined temperature and polarization data. The requested settings were `gpt-6.1-sol / high` and `gpt-5.6-luna / low`; serving telemetry was not available. These checks are not specialist human review, peer review, data reanalysis or validation of the cosmological models.

## Sources and provenance

| Source | Version/date | Role | Exact locators | Access and rights |
|---|---|---|---|---|
| Planck Collaboration, [*Planck 2015 results. XVIII. Background geometry and topology of the Universe*](https://arxiv.org/abs/1502.01593v2) | arXiv:1502.01593v2, 2016-06-06; *Astronomy & Astrophysics* 594, A18 | Matched-circle search and separate low-ℓ likelihood limits for T3 and T1 | §§4.1–4.2, Eq. (5), §§5.1.1–5.1.2; official [full text](https://arxiv.org/html/1502.01593v2) | Public arXiv source; linked and paraphrased, no figures, tables, maps or extended text redistributed. |
| Petersen et al. (COMPACT Collaboration), [*Cosmic topology. Part I. Limits on orientable Euclidean manifolds from circle searches*](https://arxiv.org/abs/2211.02603v4) | arXiv:2211.02603v4, 2024-11-27; *Journal of Cosmology and Astroparticle Physics* 01 (2023) 030 | Translation of previous temperature-circle nulls through nine orientable Euclidean families; observer-position dependence | Abstract, §§1, 3–5 and §3 footnote 6; official [full text](https://arxiv.org/html/2211.02603v4) | Public arXiv source; v3 corrected Figs. 3–5 under an erratum and v4 added an omitted author. The v4 text is used here; no figures, tables, maps or code redistributed. |

## Method and reproduction

To inspect the source claims, read Planck §§4.1–4.2 and §§5.1.1–5.1.2, preserving the distinction between the back-to-back circle search and the separate low-ℓ likelihood analysis. Then read Petersen et al. §§1, 3–5 and §3 footnote 6 to trace the prior-map nulls, detection thresholds and observer-position calculation. This is a manual source-inspection procedure; it does not reproduce either paper's data analysis or code.

## Results and interpretation

The circle null is informative for the topologies, circle configurations, data masks and detection thresholds studied. It is not a certificate that the universe is simply connected. In the Petersen et al. analysis, an observer-centred bound need not bound the shortest loop at every point in a manifold because the loop length can vary with observer position.

Petersen et al.'s observer fraction `p` is an approximate exclusion p-value under their stated uniform sampling and interpretation; it is not a posterior probability that a topology is true. The 98.5% value is a threshold-dependent constraint derived from an existing map null, not a deterministic theorem about every global topology.

Other signatures may probe surviving models. Petersen et al. discuss off-diagonal correlations of CMB harmonic coefficients as one example of a statistic beyond matched circles.

## Limitations and unresolved issues

- The Planck direct circle search is restricted to antipodal/back-to-back circle centres and depends on the assumed fiducial background, mask, orientation and detectable radius.
- The matched-circle 99% T3 result uses polarization alone; the separate low-ℓ likelihood limits use combined temperature and polarization data and have distinct marginal/profile labels.
- The Petersen et al. analysis is a translation of prior temperature-circle nulls through nine orientable Euclidean families; it is not a new search of the CMB maps.
- The 98.5% loop bound is through our location and inherits the prior search's detection thresholds and false-negative limits. Shorter loops elsewhere remain possible in many of the studied families.
- The selected papers do not classify the actual topology of our universe, establish a bound for every global topology, cover non-flat or non-orientable spaces in the Petersen analysis, or rule out other signatures.
- No likelihood, map search, numerical limit or topology code was rerun. The paper-reported limits are not independently reproduced here.
- This is not a new cosmological result, empirical discovery, novelty or priority claim, physical claim about Infinity Research, or evidence that surviving topology is permanently inaccessible.
- There is no human specialist review or peer review. The two AI checks cover only the listed source interpretation.
- Public availability of the sources does not grant broad reuse rights. The Ledger has no open licence; this artifact links and paraphrases the papers and includes no third-party figures, tables, data or code.

## Authorship, chronology and prior work

This artifact is authored by Richard George Davis with AI-assisted source analysis and writing. The Planck and COMPACT Collaboration authors retain attribution for the published analyses. The source papers predate this note. The artifact records a bounded source interpretation and does not make a field-level novelty, originality or priority claim; it is not an exhaustive literature search.

| Event | Date | Evidence | What the date establishes |
|---|---|---|---|
| Planck version used | 2016-06-06 | arXiv:1502.01593v2 record | Version date for the source text checked. |
| Petersen et al. version used | 2024-11-27 | arXiv:2211.02603v4 record | Version date for the source text checked. |
| Coordinator source review and AI challenges | 2026-10-26 | Bounded source review and two source-only checks | Date of the documented source review, not first conception or priority. |
| First appearance of this artifact in the Ledger | Ledger commit history | The public commit adding this file | Repository chronology only; not first conception, originality or priority. |

## Independent review

Reviewers: two independent AI source-only checks; requested settings `gpt-6.1-sol / high` and `gpt-5.6-luna / low`. Date: 2026-10-26.

Scope: statistical and method labels for Planck's circle-search and low-ℓ likelihood results; the distinction between an observer-centred loop bound and global topology constraints; and the nine-family scope and residual signatures in Petersen et al.

Findings: no major numerical claim error was identified. The checks required the polarization-only versus combined-temperature/polarization distinction, and narrower wording for Planck's search family, Petersen et al.'s inherited detection thresholds, observer-position dependence and the absence of a global topology verdict. No human specialist or peer review was performed.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-10-26 | Initial bounded source-review artifact | Two version-pinned primary sources, coordinator source reading and two independent AI source-only checks. |
