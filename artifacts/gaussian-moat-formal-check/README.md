# Gaussian-moat theorem: bounded Lean endpoint check

Status: `formalised`

Version: `0.1.4`

Last updated: `2026-10-16`

Artifact author: Richard George Davis

Underlying theorem author: OpenAI, as named on the source manuscript. This record reports a bounded check of that existing result; it does not claim authorship of the theorem.

AI-assisted source review and challenge were used. Reviewer runtime model identities were not available for readback. No independent human review is claimed.

## Question and intended use

What does the formal endpoint in OpenAI Math family 028, *Bounded-Step Walks on Gaussian Primes*, claim, and did the exact pinned Lean project build and report the expected endpoint axioms?

This record helps readers distinguish the source theorem, our local formal-build check, earlier work credited by the paper, and possible future applications. It is a bounded verification record, not a new theorem or a novelty claim.

## The theorem in plain language

Treat each Gaussian prime a + bi as a point in the square lattice, and join two different points when they are within a fixed distance D. The theorem says that, for every fixed finite D, every connected group in this graph has a finite maximum size B_D, and the same bound works no matter where the group starts. So a person cannot keep walking through new Gaussian primes forever if every step must stay at most D; eventually that connected region runs out.

The bound depends on D, is not made explicit by the paper, and the claim concerns Gaussian primes in the Gaussian integers, not the ordinary primes on the number line.

See the [evidence bundle and claim map](evidence/README.md) for retained outputs, integrity checks, reproduction instructions and missing receipts.

## Claim supported by this artifact

At upstream source revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, Lean 4.34.1 successfully built `OAI.NumberTheory.GaussianMoat.Main`. In a separate offline rerun, Lean reported:

```
OAI.GaussianMoat.fullMain : OAI.GaussianMoat.MainEndpoint ∧ OAI.GaussianMoat.UniformEndpoint
'OAI.GaussianMoat.fullMain' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The pinned comparator configuration names the same theorem and permits the same three axioms. This is a configuration match; the comparator harness itself was not run.

The evidence supports the labels `formalised` and `source review` for the stated scope, conditional on the imported environment and trust limits below. It does not authenticate every cached dependency against source, establish a complete independent proof audit, or determine novelty.

Three further bounded source reviews and a report-level challenge are recorded in the [2026-10-12 source-audit update](evidence/source-audit-update-20261012.md). They found no defect in their listed declaration bodies, interfaces and caller substitutions; they did not run Lean/Lake or verify the entire theorem dependency chain.

## Authorship, chronology and prior work

| Event | Date/time and zone | Evidence | What the date establishes |
|---|---|---|---|
| Manuscript date | 2026-09-26 | Date on the OpenAI manuscript title page | The date printed on this manuscript version |
| Pinned upstream commit | 2026-10-08 05:20 UTC | [GitHub commit fd4aeeb](https://github.com/openai/math/commit/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb) | Public repository history for this exact source snapshot; this artifact does not search exhaustively for earlier postings |
| Bounded source-crosswalk work | 2026-10-11, Africa/Johannesburg | Private research execution record | The documented source-review checkpoint, not necessarily the first private mention |
| Endpoint build and axiom query | 2026-10-12, Africa/Johannesburg | Private research execution record and retained outputs | The documented local formal-check run |
| First public appearance of this ledger entry | See [GitHub file history](https://github.com/RichardGeorgeDavis/research-artifact-ledger/commits/main/artifacts/gaussian-moat-formal-check/README.md) | The commit that first adds this file | When this version entered this public repository, not when the idea was conceived |

The manuscript says the Gaussian moat problem traces to Basil Gordon in 1962 and recounts later attribution involving Motzkin and Erdős. This artifact records the manuscript's historical attribution; it does not independently establish that history. The manuscript discusses earlier work by Gethner and Stark and Vardi, and a methodological comparison with Tao. Our source crosswalk checked selected antecedents within a bounded scope; it did not perform an exhaustive priority search.

For this theorem, the checked OpenAI source snapshot predates this documented Lean check. That comparison is limited to the cited manuscript and the recorded check. A public commit establishes when its contents appeared in repository history; it does not establish when an idea was first conceived or prove priority over unpublished work.

## Method and reproduction

The run used the exact upstream revision above, Lean 4.34.1, a Linux ARM64 container with network access disabled, read-only pinned package-cache inputs, and a 7 GiB guest-memory limit. The initial source/dependency audit checked 42 dependency revision/origin pairs. The offline Lake build completed all 8,964 jobs, including the requested `Main` target.

The build wrapper then exited non-zero because its follow-on check referenced a mistyped file path. The successful `Main` target was retained, and a separate fresh offline container ran the endpoint check and axiom query against the persistent built project. Eleven Lake warnings reported local changes in cached dependency checkouts. A later scoped audit matched all eleven tracked dependency diffs to their configured pinned compatibility patches; see the [patch audit](evidence/dependency-patch-audit-20261012.md). The cache review and the 42 revision/origin checks support a qualified run report; they do not bind every cached artifact byte to its declared source.

To reproduce the project check, use the exact upstream revision and its declared toolchain in a reviewed contained environment:

```bash
lake build OAI.NumberTheory.GaussianMoat.Main
```

Then run the following in the same Lake environment:

```lean
import OAI.NumberTheory.GaussianMoat.Main

#check OAI.GaussianMoat.fullMain
#print axioms OAI.GaussianMoat.fullMain
```

Expected result: the endpoint type and three-axiom list shown above. The project has Lake hooks and a broad dependency graph; the command should be run with its writes and network route reviewed. The [retained evidence bundle](evidence/README.md) includes the build log, axiom output, check input and runtime outputs. It does not include a standalone environment image.

## Relation to the Infinity Research programme

This theorem is about a graph on Gaussian primes. The run found no formal map or discriminating consequence connecting it to the programme's ordinary-prime, infinity, odometer, Möbius or Berry-phase questions. Sharing the word “infinity”, or both topics involving primes, is not a mathematical connection.

One transferable idea is methodological: the proof combines prime supply across many scales, selects dense separated batches, accumulates information costs, and uses a finite periodic obstruction. An abstract supply-and-sparsification lemma could be investigated elsewhere if a specific receiving theorem, structure-preserving map and testable consequence are identified. That is a future research question; this run did not establish the lemma or an application of that lemma.

A distinct project-level corollary that applies the source endpoint to an indexed helix graph is recorded in the [separate helix-metric artifact](../gaussian-moat-helix-metric-corollary/README.md). Its conditional derivation does not validate the source theorem beyond the endpoint already recorded here.

## AI-assisted consistency review

Review scope: bounded source audits of selected geometry/entropy, information/telescope, certificate/endpoint and dependency-trust obligations; a separate AI challenge of eight integrated records; and mechanical verification of the output and comparator configuration.

Findings: reviewers found no concrete issue in the portions they inspected. Their reviews were resource-bounded and conditional on stated premises and imports. The challenger did not rerun Lean or the comparator. Reviewer model/effort readback was unavailable. No independent human review or full transitive proof audit is claimed.

The later [2026-10-12 source-audit update](evidence/source-audit-update-20261012.md) adds bounded reviews of finite entropy/accounting, quotient/lattice/component interfaces and analytic weighted prime-mass extraction. A separate AI challenge checked report consistency and claim wording only; it did not reopen source or verify the reported source hashes/read coverage.

## Limitations and unresolved issues

- The source manuscript's historical attributions have not all been independently checked against their original sources in this artifact.
- The official cache's artifact bytes were not authenticated against every source body; complete transitive source closure remains unproved.
- The comparator JSON was inspected, but its harness was not executed; `enable_nanoda` is false.
- The listed entropy/support, ordered-accounting, quotient/lattice/component and analytic prime-mass source slices have bounded AI source reviews with no defect identified in the inspected scope. Imported dependencies, uninspected portions and downstream implications remain outside complete independent review; see the dated source-audit update for exact boundaries.
- The build and axiom output do not establish theorem novelty, a defect in the theorem, an Infinity or ordinary-prime connection, or a practical application.
- The retained build and axiom logs are published in the evidence bundle. The full container packet and numeric exit-status receipts are not included. The tracked compatibility-patch inventory is included, but no complete cache-byte manifest or authentication of cached artifacts against source is claimed.

## Sources and provenance

| Source or input | Version/date | Role in this artifact | Relevant claim or section | Access or rights notes |
|---|---|---|---|---|
| [OpenAI Math family 028 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/main.tex) | Manuscript dated 2026-09-26; pinned repository commit above | Statement, authorship and historical claims | Theorem statement, title-page date, introduction | Public source |
| [Lean Main module](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/Main.lean) | Same source commit | Formal endpoint declaration | `OAI.GaussianMoat.fullMain` | Public source |
| [Comparator configuration](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/GaussianMoat.json) | Same source commit | Expected theorem and permitted axiom set | Target, permitted axioms and checker setting | Public configuration; harness not run |
| Local execution record and outputs | Dated 2026-10-11 to 2026-10-12 (Africa/Johannesburg) | Run evidence, bounded reviews and trust disposition | Build and axiom result | Selected machine outputs are published in the evidence bundle; full working record remains private |

No third-party text, data or code is reproduced here beyond short technical identifiers and the minimal Lean output needed to identify the check. The theorem is paraphrased and attributed to its named source author.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-10-12 | Initial bounded formal endpoint record | Pinned offline build, separate endpoint/axiom query, bounded challenge and mechanical review; claim limits stated above. |
| 0.1.1 / 2026-10-12 | Published retained evidence bundle | Original output hashes match earlier receipts; packaging did not rerun Lean. |
| 0.1.2 / 2026-10-12 | Added a scoped inventory of all eleven configured compatibility patches and corrected the warning explanation | Each retained tracked package diff matches its pinned patch and passes reverse-check; cache artifact authenticity and missing exit receipts remain unresolved. |
| 0.1.3 / 2026-10-12 | Added a public summary of three bounded source-audit reports and a separate report-level challenge | No defect was identified in the listed slices; the full reports remain private and full dependency/proof closure remains open. |
| 0.1.4 / 2026-10-16 | Added three bounded source-review coverage summaries | Records the inspected interfaces and unchanged full-proof/cache limits; no new formal run. |

Additional endpoint, inverse-limit and first accurate-band review coverage is summarised in the [16 October note](evidence/source-audit-update-20261016.md). These remain source reviews with no new build or full proof assurance.
