# Research Artifact Ledger

**Purpose:** a small, versioned home for selected research artifacts with explicit source trails, evidence labels, reproduction notes and correction history.

**Current release:** repository structure and an artifact-record template only. No Infinity Research findings, scientific theory, novelty claim or validation result are included in this release.

## What this repository can and cannot show

Each public commit and release records what this repository contained at that point. Source links, dated records and correction history help readers inspect provenance and changes. They do not prove when an idea was first conceived, establish priority over unpublished work, or demonstrate that a claim is correct or original.

Research artifacts added later must identify their question, bounded claim, sources, evidence class, method, reproducibility steps, limitations and review status. Established background, reproduced work, new derivations, synthetic examples, local applications, conjectures and open questions must not be blended into one verification label.

## Status labels

- `source review`: sources have been inspected for the stated scope; the result is not independently reproduced.
- `reproduced`: the stated procedure was rerun and matched the declared check.
- `independently checked`: a person not responsible for the original artifact checked the named claim or procedure; the scope of that check is stated.
- `formalised`: a specified formal system or proof assistant checks the stated formal claim; this does not validate empirical premises.
- `synthetic demonstration`: an illustrative constructed case, not evidence of real-world effectiveness.
- `provisional application`: a bounded local use whose wider effectiveness is not established.
- `open`: unresolved, incomplete or awaiting the stated check.

## Adding an artifact

1. Copy [`ARTIFACT_TEMPLATE.md`](ARTIFACT_TEMPLATE.md) and complete all applicable fields.
2. Link material claims to primary sources, data, code, derivations or prior artifacts.
3. Include enough information to reproduce or independently inspect the result, with rights and privacy reviewed.
4. State negative results, limits, unresolved objections and what evidence would change the conclusion.
5. Add a dated entry to [`HISTORY.md`](HISTORY.md) and update citation metadata when making a release.

Kaggle scores, medals and competition placements are task-specific benchmark outcomes. They do not establish scientific validity or show that a research method caused an improvement. Competition rules, dataset rights and attribution requirements apply to any shared Kaggle material.

## Scope and reuse

This is an artifact ledger, not a claim that its methods are novel or that its contents have peer-review status. Each artifact carries its own evidence and review limits. The initial release does not include an open licence; no broader reuse permission should be inferred from public visibility.
