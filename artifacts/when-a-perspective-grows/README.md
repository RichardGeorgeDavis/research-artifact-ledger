# When a Perspective Grows — final author release

Status: `source review`, `synthetic demonstration`, `open`

Paper version: **2.6** · Artifact record: **0.3.0** · Released: **5 November 2026** · Author: Richard George Davis

This is the final author release of the combined manuscript, not a journal-accepted or peer-reviewed article. “Final” identifies this released edition; it does not close the research questions or prevent a documented correction. No field-level novelty or historical-priority claim is made.

## Question and intended use

What warrants comparing experience across learning, and what kind of understanding has increased? The paper is intended for readers of objective phenomenology and measurement methodology. It combines a critical synthesis, stipulated mathematical examples, a worked interpretation of a published learning experiment and a conditional formal clarification.

## Claim supported

A common phenomenal target and adequate joint evidence can support a local endpoint comparison without first establishing complete phenomenal identity. Uncertainty about a metric or response process need not defeat a weaker ordering supported across the relevant accounts; agreement alone cannot supply a missing phenomenal interpretation. Whole-character change does not by itself establish the failure of every partial comparison.

The Goldstone application retains a published discrimination result and identifies why correct category-label identity alone is insufficient to explain within-category discrimination. It does not establish a pre/post-learning phenomenal ordering or the hypothetical model’s numerical parameters. Pauen’s replay discussion illustrates a possible indirect calibration standard, with its assumptions and transfer limits retained.

Appendix A distinguishes eliminating candidate characterisations from adding uniform instance consequences. Its separator condition is conditional on the stated representation; phenomenal eligibility and the exact OR-inheritance assumptions remain open.

## Files and provenance

- [Final manuscript v2.6](paper.md): self-contained main argument, Appendix A, thirty references and AI assistance disclosure.
- [Supporting sensitivity analysis](sensitivity-analysis.md): separate self-contained treatment of the conditional model’s parameter bounds.
- [Reproduction script](reproduce.py): exact finite geometry and rational baseline checks.
- [Sensitivity checker](check_sensitivity.py): exact rational endpoint and separation checks for the supporting analysis.
- [Source-to-claim map](../../sources/when-a-perspective-grows.md): source roles and access boundaries.
- [Artifact citation metadata](CITATION.cff).
- [Earlier public v2.4](https://github.com/RichardGeorgeDavis/research-artifact-ledger/blob/b22476e6b33459bff7d525ef60fb6f3ca10a4ea1/artifacts/when-a-perspective-grows/paper.md).
- [Earlier public v1](https://github.com/RichardGeorgeDavis/research-artifact-ledger/tree/cf61260a820c0ecb325473badc77874eaac44017/artifacts/when-a-perspective-grows).

Paper SHA256: `60d706d97bd79c0d6802fe726059e25bef2a16ff45c90968ba87b710163451f3`

Supporting analysis SHA256: `8a325536d5fcc4da8558377f5dc7a796739b09b6739e10028c6c55b6f388765e`

The release copy changes the private manuscript’s local-status metadata removes its local companion hyperlink and uses GitHub-compatible display-math delimiters. It does not publish private review logs, correspondence, supplied source copies or submission materials.

## Evidence and review status

`source review` covers the bounded source interpretation, not a systematic literature review. `synthetic demonstration` covers the stipulated geometry and response model, not observed experience. `open` covers actual phenomenal calibration, common-content correspondence, Appendix domain eligibility, historical novelty and external editorial judgement.

Separate AI reviews checked source interpretation, argumentative scope, context retention and the final reader journey. These are not independent human philosopher review or peer review. No qualified independent human philosophical review is recorded. The calculations are reproducible; successful execution does not verify the philosophical premises.

## Method and reproduction

Python 3, standard library only:

```sh
python3 reproduce.py
python3 check_sensitivity.py
```

The geometry script enumerates 120 ordered injective placements, obtaining one metric-preserving and sixteen ordinal placements. It checks the equal old-reference squared-distance profiles `(4, 5, 13)` and distinct new-reference distances `(10, 18)`. Baseline choice ranges are `0.90–0.91` and `0.10–0.19`. The sensitivity checker verifies endpoint extrema and strict-separation thresholds with exact fractions. These are checks of stipulated mathematics only.

For the noncomputational argument, inspect §§1–4 against their cited sources, §6.3 against Goldstone’s Experiment 4, §7 against Spener/Pauen and the stated objections, and Appendix A against its explicit assumptions and Lee-domain qualifications. No new empirical study or raw-data reanalysis was performed.

## Limitations

The manuscript does not establish an actual longitudinal phenomenal ordering, validate the numerical calibration or prove that the proposed common target survives a particular learning transition. Goldstone’s comparison is between post-training groups, not each learner’s before/after experience. The replay standard is indirect and does not establish transfer to that learning task. Appendix A does not establish phenomenal eligibility or exact compositional inheritance. Nagel-style intelligibility without the relevant experiential capacities remains a stronger, unproved achievement.

Meredith’s full text was unavailable; other abstract/draft access limits are identified in the paper and source map. The contribution is a critical synthesis and bounded application, not a new validation method or established original theory.

## Authorship, chronology and prior work

Richard George Davis is the author. Material OpenAI GPT assistance is disclosed in the manuscript and supporting analysis. The scripts were developed with AI assistance. Nagel, Lee, Negro and the cited measurement/calibration literature supply the underlying questions and methods; this paper does not claim to originate them.

| Version/date | Change |
|---|---|
| Paper 2.6 / artifact 0.3.0 / 5 November 2026 | Final combined author release; worked Goldstone application, developed calibration argument, retained earlier examples and self-contained formal appendix; separate sensitivity support. |
| Paper 2.4 / artifact 0.2.0 / 26 October 2026 | Public memory and response-shift synthesis; preserved in the linked commit. |
| Paper 1 / artifact 0.1.0 / 24 October 2026 | First public paper and exact-arithmetic companion; preserved in the introducing commit. |

These dates establish public versions, not first conception, correctness or priority. The artifact-specific release tag is `when-a-perspective-grows-v2.6`; it identifies a repository snapshot, but the release claim concerns this artifact, not validation of unrelated repository contents.

## Publication, corrections and reuse

The author authorised this Ledger release on 5 November 2026. Third-party papers are cited, not redistributed. No open licence is assigned; public visibility does not grant broader reuse rights. Corrections should identify the version and passage through the [issue tracker](https://github.com/RichardGeorgeDavis/research-artifact-ledger/issues). Earlier releases remain available in version history.
