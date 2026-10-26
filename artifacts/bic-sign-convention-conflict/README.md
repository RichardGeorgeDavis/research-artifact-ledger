# A source-text conflict in one cosmological BIC comparison

Status: `source review`

Version: `0.1.0`

Last updated: `2026-10-26`

Author: Richard George Davis, with AI-assisted source analysis and writing.

Underlying source authors: Wang and Mota authored the cosmology paper examined here; Gideon Schwarz introduced the model-dimension criterion cited for the conventional comparison. This note does not claim authorship of the source paper, its cosmological analyses, or the BIC method.

## Question and intended use

Does the Version of Record of Wang and Mota’s 2025 article use a consistent sign convention when interpreting its reported Bayesian Information Criterion (BIC) differences, and what can a reader infer from the printed text alone?

This bounded source review is for readers assessing the article’s wording about support for dynamical dark energy. It flags a conflict between two statements in the same paper and explains what the text does not determine.

## Claim supported

The publisher Version of Record and the inspected arXiv v2 text both contain a sign-direction inconsistency. Section 6 interprets positive `ΔBIC` values as evidence for dynamical dark energy. Note 49 defines `ΔBIC = BIC_model − BIC_ΛCDM` and describes positive differences as evidence against the reference model, `ΛCDM`. Under the conventional comparison in which lower BIC is preferred, that definition makes positive `ΔBIC` favour `ΛCDM`, in conflict with the Section 6 interpretation.

This source-text inconsistency does not establish whether the printed definition, reported signs or prose interpretation is wrong; it does not identify the authors’ intended correction, the signs used in code, or which model is empirically preferred. No likelihood result is accepted here.

## Evidence class and review status

The evidence class is `source review`. The coordinator compared the publisher VOR and arXiv v2 at the listed passages and checked the stated subtraction direction against the conventional lower-is-better BIC comparison. One independent AI source-only challenge cross-checked the sign logic against both public versions. It confirmed the conflict and found the same text in both versions. This is not a human specialist review, peer review, correction-history audit, fit reproduction, code review or empirical model comparison.

## Sources and provenance

| Source | Version/date | Role and locator | Access and rights |
|---|---|---|---|
| Wang and Mota, “Did DESI DR2 truly reveal dynamical dark energy?”, *European Physical Journal C* 85, 1356 (2025), [DOI 10.1140/epjc/s10052-025-15076-y](https://doi.org/10.1140/epjc/s10052-025-15076-y), [publisher Version of Record](https://link.springer.com/article/10.1140/epjc/s10052-025-15076-y) | VOR published 25 November 2025 | §6, pp. 3–4, reports positive `ΔBIC` values as evidence for DDE; note 49, p. 6, defines the subtraction and interprets positive differences against `ΛCDM` | Publicly readable VOR. Linked and paraphrased; no table, figure or substantial text reproduced. |
| Wang and Mota, [arXiv:2504.15222v2](https://arxiv.org/abs/2504.15222v2) | v2 dated 20 November 2025 | “Solution”, p. 4 and note [49], pp. 6–7, preserve the same sign/interpretation conflict | Public arXiv author version; no figures or tables reused. |
| Schwarz, “Estimating the Dimension of a Model,” *The Annals of Statistics* 6(2), 461–464 (1978), [DOI 10.1214/aos/1176344136](https://doi.org/10.1214/aos/1176344136) | 1978 | Primary methodological context for BIC model comparison; the comparison convention used here prefers the lower BIC | Linked for method context; no text redistributed. |

No open licence is assigned by the Research Artifact Ledger. Public visibility does not grant general reuse permission.

## Method and reproduction

Read §6 and note 49 in both linked Wang–Mota versions. Copy the defined subtraction direction, identify which model is first, and compare it with the adjacent prose. For conventional BIC model comparison, smaller BIC is preferred; therefore if `ΔBIC` is model minus reference, a positive value means the model has the larger BIC and the reference has the smaller one. This is a sign-logic check from the printed definition, not a calculation of the paper’s reported BIC values.

No likelihood, code, chain, covariance, cosmological dataset or fitted parameter was accessed or rerun. No reported BIC value was recomputed and no alternate correction was selected.

## Results

The VOR §6 reports positive differences `2.25`, `25.63`, `3.92` and `11.49` as favouring dynamical dark energy. Note 49 defines `ΔBIC = BIC_model − BIC_ΛCDM` but says positive differences are evidence against `ΛCDM`. Under lower-is-better BIC, the stated definition instead favours `ΛCDM` when the difference is positive. The arXiv v2 version contains the same conflict in “Solution” and note [49].

The bounded conclusion is that these printed passages cannot all support the same sign interpretation. The sources inspected here do not identify which statement is erroneous or which sign was used in the analyses. The conflict is not evidence, by itself, that either cosmological model fits the data better.

## Limitations and unresolved issues

- The comparison checks the VOR and arXiv v2 only; it is not a full correction-history or all-version audit.
- The sign conflict does not identify the intended correction. Neither reversing the definition nor negating the values is justified by the checked text alone.
- An independent reviewer noted a possible additional bound: if the relevant fits use identical likelihoods and CPL adds exactly two parameters, then `ΔBIC ≤ 2 ln N`; for `N=1701` this is about `14.88`, below one reported `+25.63`. This is not accepted as an additional inconsistency because the checked text does not establish that this particular reported value uses that exact sample size, the same likelihood, and exactly two additional parameters under otherwise identical conditions. The entry-specific data mapping, likelihood minima and parameter counts would be needed.
- Resolving the sign and any value-level discrepancy requires per-dataset likelihood minima, parameter counts, sample size and the implemented subtraction, or an attributable authoritative correction.
- No model ranking, parameter estimate, new cosmological result, empirical conclusion, novelty, priority or field-level claim is made. No human specialist or peer review occurred.
- No third-party table, figure, dataset, code or substantial text is reproduced. The Ledger has no open licence.

## Authorship, chronology and prior work

This artifact is authored by Richard George Davis with AI-assisted source analysis and writing. Wang and Mota retain credit for their article and its cosmological analyses; Schwarz is credited for the cited model-dimension criterion. Both examined Wang–Mota versions predate this source review. This note records a bounded reading of those texts, not first conception, originality, priority or an exhaustive literature search.

| Event | Date | Evidence | What it establishes |
|---|---|---|---|
| Wang–Mota source versions checked | 2025-11-20 (arXiv v2); 2025-11-25 (VOR) | arXiv version record and publisher metadata | Identity/dates of the checked source versions |
| Coordinator source reading and independent AI challenge | 2026-10-26 | Dated source comparison and independent public-source challenge | Date and scope of this source review, not priority |
| First public appearance of this artifact | Ledger commit history | Commit adding this file | Repository chronology only; not first conception or priority |

## Independent review

Review: one independent AI source-only challenge. Date: 2026-10-26.

Scope: compare VOR §6 with note 49, compare the same passages in arXiv v2, and assess what follows from the sign definition under lower-is-better BIC. The reviewer confirmed the source-text conflict, the matching passages across the two versions, and the bounded inference. It also supplied the conditional `2 ln N` lead above; no dataset/value mapping was verified for that lead. No likelihood or code was reviewed and no cosmological fit was reproduced.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-10-26 | Initial bounded source-review artifact | Publisher VOR and arXiv v2 source comparison plus an independent public-source sign-logic challenge. |
