# Third-party exact-pin Comparator replay records — 2026-11-06

## Bounded finding

Three public audit records report a Comparator replay of OpenAI Math's `GaussianMoat` challenge at upstream revision [`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb). Toledo's [pinned cert-machine census row](https://github.com/carlostoledo1891/cert-machine/blob/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-kernel.json#L6168-L6202) identifies family 028, records Comparator exit 0, and says Lean's default kernel and stock nanoda accept the solution. MathVet's [challenge-status row](https://github.com/mathvet/mathvet/blob/14c7f918cd336d0da03a02aae5a0eed4a429d4db/reviews/openai-math/challenge-status.csv#L150) records a `comparator-sandboxed-pass` for `OAI.GaussianMoat.fullMain` at that pin using `landrun` in real best-effort mode. Reilly's [corpus replay row](https://github.com/jmreilly1113/siegel-zeros-audit/blob/main/results/2026-10-20-corpus-summary-final.tsv#L96) records `GaussianMoat` as `ACCEPT_BOTH`, with Lean and nanoda accepting and exit 0.

These are three publicly inspectable records, not three independent mathematical proof audits; the records may derive from overlapping challenge runs. They support external replay of the encoded endpoint at the named revision, not paper-to-Lean equivalence, correctness of every imported proof, cache-to-source authentication, theorem novelty or full proof validity. The existing local build remains a distinct run. Its own Comparator harness was not executed.

## Scope and trust boundary

Toledo's corpus-level [method and trust description](https://raw.githubusercontent.com/carlostoledo1891/cert-machine/9814e4c06281e34a113ce853d7d99ccce160b750/certs/openai-math-kernel.json) explains that the challenge statement/configuration bytes are hash-checked and replayed with Lean and nanoda, while its trust base includes both kernels, exporter/comparator, fetched Mathlib cache and GitHub runner. It reports Landlock sandboxing as best-effort and notes the recommended systemd AF_UNIX restriction was unavailable on those runners. The row therefore documents an external toolchain replay with a stated trust base; it does not replace our separate source/cache assessment.

## Impact on this artifact

This evidence strengthens the record of independent formal endpoint acceptance at the exact source pin. It does not change the theorem, its parameters, the project-derived `M_*(D,d)` source-level threshold, or any prime-prediction receiver. The exact threshold remains conditional on its separate pointwise density premise and is not a Lean theorem or compiled caller. No new result in ordinary rational-prime prediction, RH, or the Infinity/odometer programme follows.

No local Lean or Comparator run was performed for this update. The existing claims and labels remain bounded by the evidence above and the artifact's other limitations. No external text, data, code, proof or figures are reproduced here; this note paraphrases public records and provides direct links.

## Sources

- Toledo, cert-machine exact-pin row, commit `9814e4c06281e34a113ce853d7d99ccce160b750`, lines 6168–6202.
- MathVet, challenge-status source snapshot, commit `14c7f918cd336d0da03a02aae5a0eed4a429d4db`, line 150.
- Reilly, corpus summary, line 96; repository snapshot as accessed 2026-11-06.
- OpenAI Math source pin `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.
