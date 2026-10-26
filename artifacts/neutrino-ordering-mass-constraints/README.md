# What selected absolute-mass constraints establish about neutrino ordering

Status: `source review`

Version: `0.1.0`

Last updated: `2026-10-26`

Author: Richard George Davis, with AI-assisted source analysis and writing.

Underlying source authors: the NuFIT collaboration, KATRIN Collaboration, Elbers et al., Ivanov et al., Jimenez et al., Bari Group, and Chudaykin, Ivanov and Philcox. This note compares selected published claims; it does not claim authorship of their measurements, likelihood analyses or cosmological models.

## Question and intended use

What do selected tritium-endpoint and cosmological absolute-mass results establish about neutrino mass ordering, and which distinctions must be kept when comparing them?

This note is for readers comparing laboratory mass limits, cosmological mass-sum constraints and ordering claims. It is a source-to-claim comparison, not a new fit or a review of every neutrino-mass analysis.

## Claim supported

The selected sources constrain different quantities and support conditional, dataset- and model-dependent statements. KATRIN’s direct endpoint result constrains an effective electron-flavour mass. Cosmological analyses constrain or compare the sum of masses under specified datasets, cosmologies, priors and statistical procedures. A mass-sum limit may be compared with an oscillation-implied ordering floor, while a Bayesian ordering odds result additionally depends on parameterisation, priors and likelihood construction. These are not interchangeable forms of direct ordering measurement.

Several selected peer-reviewed cosmological analyses report tension with the inverted-ordering mass floor under their stated assumptions. The selected papers do not provide a model-independent ordering determination or a new combined fit. The selected 2026 preliminary Bari oscillation release reports differing ordering preferences across overlapping data combinations. One unreviewed preprint reports much larger combined odds but contains an unresolved arithmetic inconsistency in its oscillation contribution; its odds are not repaired or independently validated here.

## Evidence class and review status

The evidence class is `source review`. The coordinator inspected the version-pinned sources and compared each reported claim with its stated quantity, dataset, model, statistical method and publication status. One independent AI source-only challenge reviewed the named public packet and the linked source claims at the requested setting `gpt-6.1-sol / high`; serving telemetry was unavailable. The reviewer confirmed the key dataset attachments, Bari overlap qualification and the Jimenez arithmetic discrepancy. It could not retrieve the NuFIT 6.1 release PDF. No human specialist review or peer review is claimed. No likelihood, code, chain, experimental data, or cosmological result was reproduced.

## Sources and provenance

| Source | Version/date | Role and locator | Access and rights |
|---|---|---|---|
| Esteban et al., NuFIT 6.0, JHEP 12 (2024) 216, [arXiv:2410.05380v2](https://arxiv.org/abs/2410.05380v2) | v2, 28 October 2025 | §5, Eqs. (15), (17)–(20): oscillation mass-squared differences, effective tritium mass and cosmological mass sum | Linked and paraphrased. The later [NuFIT 6.1 release notes](https://www.nu-fit.org/sites/default/files/v61.release-notes.pdf) are listed for context; that PDF was not retrieved in the independent review. |
| KATRIN Collaboration, Science 388 (2025), [arXiv:2406.13516](https://arxiv.org/abs/2406.13516) | 2025; 259 measurement days | Abstract and reported endpoint result: effective electron-antineutrino mass limit `mν < 0.45 eV` at 90% CL | Linked and paraphrased; no data or figures reused. |
| Elbers et al., Phys. Rev. D 112, 083513 (2025), DOI [10.1103/w9pk-xsk7](https://doi.org/10.1103/w9pk-xsk7), [APS record](https://journals.aps.org/prd/abstract/10.1103/w9pk-xsk7), [arXiv:2503.14744v3](https://arxiv.org/abs/2503.14744v3) | v3, 2025 | Separate cosmological mass-sum bound and ordering comparison, including its data, model, parameterisation and prior qualifications | Linked and paraphrased; no tables or figures reused. |
| Ivanov et al., Phys. Rev. D 114, 063526 (2026), DOI [10.1103/sjff-yj2t](https://doi.org/10.1103/sjff-yj2t), [APS record](https://journals.aps.org/prd/abstract/10.1103/sjff-yj2t), [arXiv:2601.16165v3](https://arxiv.org/abs/2601.16165v3) | v3 / published 2026 | §4.3 and §5: mass-sum limits and posterior-derived comparison with ordering floors | Linked and paraphrased; no tables or figures reused. |
| Jimenez et al., [arXiv:2606.18987v1](https://arxiv.org/abs/2606.18987v1) | v1, 2026; preprint not peer reviewed | §§2.1, 3.3 and 5: combined odds, prior sensitivity and an unresolved `Δχ²` arithmetic discrepancy | Linked and paraphrased; the discrepancy is left unresolved and the reported odds are not reproduced. |
| Bari Group, [public results page](https://global-nu.org/results.html) | Preliminary release dated 15 October 2026 | “Key numbers” and combination tables: source-specific oscillation ordering comparisons and the authors’ `sqrt(Δχ²)` convention | Preliminary web release, not a peer-reviewed publication; overlapping combinations are not treated as independent. |
| Chudaykin, Ivanov and Philcox, Phys. Rev. D 114, 063527 (2026), [arXiv:2602.18554v2](https://arxiv.org/abs/2602.18554v2), [APS record](https://journals.aps.org/prd/abstract/10.1103/lg1n-k1rl) | v2; published 17 September 2026 | §2.2, §3.3, Table 4, Fig. 5 and §4: simulation-based prior mass-sum limits, dataset/model choices and systematics | Linked and paraphrased; no table, figure, data or code redistributed. |

Public visibility does not grant general reuse rights. No third-party figure, table, dataset or substantial text is reproduced. The Research Artifact Ledger does not assign an open licence.

## Method and reproduction

Read the exact versions and locators in the source table. For each numerical limit or ordering statement, identify the observable, data combination, cosmological model, mass parameterisation, prior, confidence or posterior interpretation, and publication status before comparing it with another row. Check that an endpoint effective-mass limit is not presented as a cosmological mass-sum limit and that a comparison with an ordering floor is not described as a direct mass-ordering measurement.

This is a manual source-inspection method. No fit, posterior, Bayes factor, confidence limit or experimental result was recalculated. The arithmetic check of `exp(9.4/2)` is a direct calculator-level check of the printed expression only; it does not identify which input the preprint authors used.

## Results

| Source and result | Quantity and method | What it supports | What it does not support |
|---|---|---|---|
| KATRIN: `mν < 0.45 eV` at 90% CL | Effective electron-antineutrino mass from the beta-decay endpoint, first five campaigns / 259 measurement days | A direct kinematic bound on an absolute-mass combination | A cosmological mass-sum bound, a direct ordering selection, or a sensitivity ratio against `Σmν` limits |
| Elbers et al.: `Σmν < 0.0642 eV` (95%) | DESI DR2 BAO + baseline CMB including Planck/ACT lensing; three degenerate masses | A conditional cosmological mass-sum limit under the stated dataset and model | Their separate ordering fit or a model-independent ordering verdict |
| Elbers et al.: `m_l < 0.023 eV`, `P(NO)=0.91`, `K=10` | Separate analysis including NuFIT 6.0; equal ordering priors and stated lightest-mass parameterisation; alternate CMB choices give `K=6/8` | A conditional Bayesian ordering comparison under that setup | A direct laboratory ordering measurement or a prior-free result |
| Ivanov et al.: `Σmν < 0.049 eV` (ΛCDM), `<0.077 eV` (`w0wa`CDM), 95% | Three-degenerate-mass limits; posterior comparisons with ordering floors | A conditional cosmological mass-sum result and author-reported floor tensions, including an approximately 2.3σ tension with the normal floor under ΛCDM | A joint NuFIT ordering likelihood or an independent frequentist ordering test from the quoted 3.5σ/2.4σ translations |
| Jimenez et al.: large combined Bayesian ordering odds | Unreviewed preprint combines oscillation evidence with DESI cosmological likelihoods taken at face value; truncated-Gaussian/KDE reconstruction and several priors | A report of the authors’ conditional analysis and a strong dependence on prior measure | Validated odds: §2.1 states `Δχ²=9.4` while §3.3 says `exp(Δχ²/2)≈21`; `exp(9.4/2)≈110`. The input or intended correction is unresolved. |
| Bari Group: `Δχ²=15.34` (labelled 3.92σ), 2.00σ NO for one JUNO combination and 1.62σ IO for a listed combination without JUNO | Preliminary oscillation-only public release; it labels significance using `sqrt(Δχ²)` | A source-specific comparison showing reported preference depends on the selected combination | Cosmological mass-sum evidence or additive independent significance; the combinations overlap and are preliminary |
| Chudaykin, Ivanov and Philcox: `Σmν<0.0730 eV` for ΛCDM; `<0.0903 eV` for `w0wa`CDM, 95% | Three degenerate masses, `Mν>0`; CMB + DR2 BAO + DR1 power for the first; CMB + BAO + power + bispectrum monopole + Pantheon+ for the second; simulation-based priors | Conditional model- and prior-dependent limits; the authors say 0.090 eV formally disfavors the inverted floor by about 2σ | A joint oscillation-ordering likelihood or a claim that simulation-based priors universally tighten limits. The ΛCDM result is weaker than their conservative-prior comparison, and HOD/systematics caveats remain. |

Together the selected sources support conditional, dataset-specific preference or tension statements. They do not establish a model-independent consensus ordering result. They do not determine the CP phase or whether neutrinos are Dirac or Majorana particles.

## Limitations and unresolved issues

- The quoted `mν` endpoint and `Σmν` cosmological values describe different observables and inference procedures; their numerical values should not be compared as if they measured the same parameter.
- Cosmological limits depend on data selection, cosmological model, mass parameterisation, priors, likelihood construction, nuisance treatment and systematics.
- Mass-sum comparisons against ordering floors are conditional and distinct from a joint ordering likelihood or direct ordering measurement.
- The Jimenez preprint’s `Δχ²`/Bayes-factor arithmetic discrepancy is unresolved. No correction or presumed author intent is supplied.
- Bari Group results remain preliminary; their listed data combinations overlap and should not be combined as independent evidence.
- The independent review could not retrieve the NuFIT 6.1 release PDF. This artifact uses NuFIT 6.0 §5 for the displayed observable equations and treats 6.1 only as contextual release-note information.
- No analysis code, likelihood, chain, cosmological dataset, CMB map or laboratory data was reproduced. Paper-reported limits and odds are source-reported, not independently recalculated.
- No specialist human or peer review, new physical result, new fit, field-level novelty or priority claim is made. This is not an Infinity Research result or a full literature review.

## Authorship, chronology and prior work

This artifact is authored by Richard George Davis with AI-assisted source analysis and writing. Underlying authors retain credit for their papers, datasets, analyses and interpretations. All selected sources predate this bounded comparison. The artifact does not claim to be first, novel, original or exhaustive.

| Event | Date | Evidence | What it establishes |
|---|---|---|---|
| Source versions checked | As listed above | Linked versioned records and publication metadata | Identity of the cited texts used for this comparison, within the stated source-access limits |
| Coordinator source review and independent AI challenge | 2026-10-26 | Dated source-review record and bounded challenge result | Date and scope of this documented review, not first conception or priority |
| First public appearance of this artifact | Ledger commit history | Commit that adds this artifact | Public repository chronology only; not priority or originality |

## Independent review

Reviewer: one independent AI source-only challenge; requested setting `gpt-6.1-sol / high`; serving telemetry unavailable. Date: 2026-10-26.

Scope: observable mapping; dataset/model/statistical interpretation in selected 2025–2026 analyses; Bari source status and overlapping combinations; Jimenez preprint arithmetic; and the bounded conclusion without reproducing underlying fits.

Findings: the observable comparison is descriptive only when the quantities and methods remain distinct. The reviewer verified the Elbers and PRD IV/V dataset details, the Bari values and overlap caveat, and the Jimenez arithmetic mismatch. It did not retrieve the NuFIT 6.1 release PDF. No likelihood was independently reproduced; no human specialist review occurred.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-10-26 | Initial bounded source-review artifact | Version-pinned public sources, coordinator source review and an independent AI public-source challenge; unresolved limits are stated above. |
