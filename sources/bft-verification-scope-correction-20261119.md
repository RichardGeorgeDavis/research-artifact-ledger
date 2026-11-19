# BFT verification-scope clarification

Date: 2026-11-19

This addendum corrects two overstatements in the frozen BFT verification-scope description. It does not change the archived data, verifier, runner, freeze record, or the source-map file pinned by the public manifest.

## Environment identity

The frozen record retains the complete Python `sys.version` string. The verifier requires an exact string match and checks a digest derived from that string. It does not hash the Python interpreter executable. The source map's phrase “interpreter hashes” therefore overstates what the verifier establishes.

## Complete score verification

The verifier validates any existing score stream that is an exact prefix of independently computed score events. In its default mode, when a valid prefix is incomplete, it reports `DATA_VERIFIED_UNSCORED` and can exit normally. The public wrapper does not compare its output to the saved aggregate summary. For the retained complete archive, a full verification result has status `PASS` and 6,222 score events; a successful process exit alone is insufficient to establish that condition.

The frozen source map and manifest remain unchanged. This note supplies a versioned clarification while preserving their recorded hashes.

## Pinned sources

- [Verifier environment and source checks](https://github.com/RichardGeorgeDavis/research-artifact-ledger/blob/77fa77d3fa4890db40883b7f77e4976783c8e242/reproduce/bft-first-event-census/bft_census_verifier.py#L227-L234)
- [Verifier score-prefix and completion status](https://github.com/RichardGeorgeDavis/research-artifact-ledger/blob/77fa77d3fa4890db40883b7f77e4976783c8e242/reproduce/bft-first-event-census/bft_census_verifier.py#L331-L349)
- [Public wrapper invocation](https://github.com/RichardGeorgeDavis/research-artifact-ledger/blob/77fa77d3fa4890db40883b7f77e4976783c8e242/reproduce/bft-first-event-census/verify_bundle.sh#L12-L17)
- [Frozen Python version](https://github.com/RichardGeorgeDavis/research-artifact-ledger/blob/77fa77d3fa4890db40883b7f77e4976783c8e242/artifacts/bft-first-event-census/evidence/freeze.json)
- [Artifact integrity list](https://github.com/RichardGeorgeDavis/research-artifact-ledger/blob/77fa77d3fa4890db40883b7f77e4976783c8e242/artifacts/bft-first-event-census/SHA256SUMS)
