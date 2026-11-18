# A sample-size factor missing from a displayed relative-lift variance

Status: `source review`

Version: `0.1.0`

Last updated: `2026-11-18`

Author: Richard George Davis, with AI-assisted source analysis and writing.

## Question and intended use

Are the sample-size terms in the relative-lift variance printed in Jonathan Fulton’s currently accessible “AB Testing 101” consistent with the definitions in the preceding figure and with a first-order delta-method calculation for independent treatment and control sample means?

This note is a reader-facing correction and comparison for people consulting the displayed formula. It addresses the currently accessible article figures only.

## Claim supported

The article’s first relative-lift figure labels `s_T` and `s_C` as sample standard deviations and separately defines `n_T` and `n_C` as the treatment and control sample counts. The next figure prints a relative-lift variance expression with neither sample-size divisor. Under the ordinary independent-groups model and the stated sample-standard-deviation definitions, the first-order variance estimate includes both divisors:

`Var(Δ̂) ≈ s_T²/(n_T m_C²) + m_T² s_C²/(n_C m_C⁴)`

Equivalently, when `m_T` and `m_C` are nonzero:

`Var(Δ̂) ≈ (m_T²/m_C²) [s_C²/(n_C m_C²) + s_T²/(n_T m_T²)]`.

This is the first-order delta-method variance for `Δ = m_T/m_C − 1`, using the sample means and variances as plug-in estimates. It assumes a nonzero control mean, a ratio approximation suitable for the data, independent treatment and control means, and the stated unclustered sample-mean variance model. Dependence between the means requires the covariance term from the gradient calculation; other assignment, clustering, weighting or repeated-measure designs require their corresponding variance and covariance estimates.

## Evidence class and review status

The evidence class is `source review`, with independent mathematical challenges. The coordinator checked the current article text and current Eppo documentation; independent reviewers visually checked the two figures served by the article. Two AI public-source challenges checked the figure transcription and derivation: one dated 26 October 2026 requested `gpt-6.1-sol / high`, and one dated 18 November 2026 requested `gpt-6.2-astra / high`. Serving-model telemetry was unavailable. This is not human specialist review, peer review, an audit of Eppo’s historical documentation, or an assessment of any experiment or implementation.

## Sources and provenance

| Source | Version/date | Role and locator | Access and rights |
|---|---|---|---|
| Jonathan Fulton, [“AB Testing 101”](https://medium.com/jonathans-musings/ab-testing-101-5576de6466b), Jonathan’s Musings | Published 25 August 2023; accessed 18 November 2026 | The relative-lift section quotes Eppo documentation. The first figure gives the lift definition, sample-standard-deviation labels and sample counts; the next figure prints the disputed variance expression. | Public webpage and externally hosted figures; linked and paraphrased. No image or substantial source text is redistributed. |
| Fulton article’s [notation figure](https://miro.medium.com/v2/resize:fit:1100/1*TknxbBFmyIuIa2A9jzWnaQ.png) and [variance figure](https://miro.medium.com/v2/resize:fit:1100/1*uTmyveR7mlzvC5uoKMF6dA.png) | Currently served figures, accessed 18 November 2026 | Direct visual evidence for the labels and printed expression described above. | Linked only; no image copy is included. |
| Eppo, [“Statistical nitty-gritty”](https://docs.geteppo.com/statistics/confidence-intervals/statistical-nitty-gritty) | Current page accessed 18 November 2026 | Defines group means, sample variances and sample sizes; its frequentist relative-lift formula includes `n_C` and `n_T`. It is a current comparator, not proof of the historical Eppo wording quoted by Fulton. | Public documentation; linked and paraphrased. |

The Ledger assigns no open licence. Public visibility does not grant general reuse permission.

## Method and result

For `f(x,y)=x/y−1`, the gradient is `(1/y,−x/y²)`. First-order propagation for independent treatment and control sample means gives `Var(f) ≈ Var(m_T)/m_C² + m_T² Var(m_C)/m_C⁴`. Substituting `Var(m_T)≈s_T²/n_T` and `Var(m_C)≈s_C²/n_C` yields the expression above.

For equal group sizes `n`, the variance printed in the article figure is `n` times this first-order estimate when `s_T` and `s_C` are interpreted as sample standard deviations. When the quantities are positive, the corresponding standard-error factor is `√n`. Interpreting `s_T` and `s_C` as standard errors could remove the divisors, but that conflicts with the definitions in the preceding figure.

Eppo’s currently accessible documentation includes both sample-size factors in its independent-groups relative-lift formula. This comparison does not establish what an earlier Eppo documentation version contained.

## Limitations and unresolved issues

- The conclusion concerns the currently accessible Fulton article figures. It does not establish that those figures are unchanged from the article’s 2023 publication or from a separately archived course PDF.
- A separately archived course PDF was not available for byte-identity verification or inspection. No claim is made about its contents or pagination.
- This review does not determine the author’s intent, the editing history of the figures, or the wording of historical Eppo documentation.
- The result does not show that an experiment, software implementation, estimate or decision used the displayed expression.
- The delta-method approximation may be poor when the control mean is near zero or the ratio distribution is poorly approximated by a normal distribution. Dependence, clustering, weighting and repeated measures can change the variance formula.
- No data, code, experiment, estimator implementation, uncertainty interval, novelty, priority, field-level contribution or new statistical theorem is claimed. No human specialist review or peer review occurred.

## Authorship, chronology and prior work

This artifact records a bounded source comparison and a standard first-order derivation. Jonathan Fulton authored the article examined; Eppo authored its current documentation. The article and statistical method predate this note. No originality or priority claim is made. The artifact’s initial public appearance is the commit that adds this file to the Ledger; that date records repository chronology only.

## Independent review

Reviewers: two independent AI public-source challenges; requested settings `gpt-6.1-sol / high` on 26 October 2026 and `gpt-6.2-astra / high` on 18 November 2026. Serving-model telemetry was unavailable.

Scope: verify the currently served figure transcription, the delta-method expression under the displayed definitions, the equal-allocation comparison and the limits imposed by the unrecovered frozen PDF.

Findings: the reviewers confirmed that the article figure separately labels sample standard deviations and sample counts, that the displayed variance omits both count divisors, and that the independent-means plug-in expression includes them. The reviewers agreed that this supports a source-specific correction only; it does not establish author intent, historical Eppo wording, frozen-PDF identity or downstream use.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-11-18 | Initial bounded source-review artifact | Current article figures, current Eppo documentation, coordinator derivation and two independent AI public-source challenges. |
