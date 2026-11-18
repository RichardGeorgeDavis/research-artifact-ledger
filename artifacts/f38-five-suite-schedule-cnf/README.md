# A checkable CNF encoding of a five-suite QA schedule

**Status:** `synthetic demonstration` and `independently checked`

**Version:** `0.1.1`

**Prepared:** 2026-11-16

**Record updated:** 2026-11-18

**Author:** Richard George Davis

**AI assistance:** AI assisted the formula generation, verifier code and drafting. A separately dispatched AI reviewer checked the exact encoding, model count, schedule mapping and bounded prior-art description. No independent human specialist review or peer review is claimed.

## Claim and use

This package gives one explicit DIMACS encoding of the fixed five-suite compatibility instance used in the F38 finite QA-scheduling benchmark. It translates each compatible suite–environment edge into one Boolean variable and imposes exactly one selected edge at every suite and environment. It is a small worked example for readers who want to inspect how this schedule instance becomes a parsimonious Boolean model-counting problem.

The encoding has 17 variables, 53 clauses, maximum width 5, and no auxiliary variables. Its satisfying assignments are in bijection with the 19 valid schedules recorded for this instance. This is a source-specific finite encoding, not a new general encoding method, solver result, performance comparison, or field-novelty claim.

## Frozen compatibility relation

- A: 1, 2, 3, 4, 5
- B: 1, 4, 5
- C: 1, 3, 5
- D: 1, 2, 4
- E: 2, 3, 5

A variable means that the named suite is assigned to the named environment. Variable IDs follow suite order `A` through `E`, then increasing environment number among compatible edges:

| IDs | Variables |
| --- | --- |
| 1–5 | `A1 A2 A3 A4 A5` |
| 6–8 | `B1 B4 B5` |
| 9–11 | `C1 C3 C5` |
| 12–14 | `D1 D2 D4` |
| 15–17 | `E2 E3 E5` |

For each suite and each environment, one positive clause requires at least one incident edge to be selected. Pairwise negative clauses require at most one. Together, these clauses impose exactly one edge per suite and environment. A satisfying assignment therefore selects a perfect matching in this bipartite compatibility graph, and each valid schedule selects exactly its five edge variables.

## Files and reproduction

- [`f38-schedule.cnf`](f38-schedule.cnf) is the generated DIMACS CNF. [`verify_f38_cnf.py`](../../reproduce/f38-five-suite-schedule-cnf/verify_f38_cnf.py) regenerates the clauses from the stated graph, checks byte-for-byte agreement with the DIMACS file, then checks all `2^17 = 131072` Boolean assignments and compares decoded models with the frozen 19-schedule list. [`verification.txt`](../../reproduce/f38-five-suite-schedule-cnf/verification.txt) records the result of that exhaustive check.

From the package root or the public repository root, run with Python 3 and no third-party packages:

```sh
python3 reproduce/f38-five-suite-schedule-cnf/verify_f38_cnf.py
```

Expected output:

```text
PASS: 17 variables, 53 clauses, maximum width 5, no auxiliaries
PASS: exhaustive search of 131072 assignments found exactly 19 models
PASS: decoded models equal the 19 frozen F38 schedules
```

The direct exhaustive enumeration independently checks this concrete finite formula. It does not measure SAT solver performance or establish a complexity result. Pairwise negative clauses for incident edge variables are an established matching encoding; for example, Zulkoski, Ganesh and Czarnecki describe that encoding for graph matchings in their [MATHCHECK paper](https://ijcai.org/proceedings/2016/636), §4. This package adds an at-least-one clause at every vertex to require a perfect matching and instantiates the familiar exactly-one construction on the F38 graph; it claims no novelty for the method.

## Sources, provenance and prior work

| Source or input | Date/version | Role | Rights and attribution |
| --- | --- | --- | --- |
| F38's author-created five-suite compatibility relation and its 19 listed schedules | Fixed finite instance, recorded in the F38 QA-scheduling result | Input graph and known-answer set for this encoding | The graph and schedules are stated in this package; the original F38 result is a separate finite synthetic benchmark. No third-party dataset or code is redistributed. |
| Zulkoski, Ganesh and Czarnecki, [“MATHCHECK: A Math Assistant via a Combination of Computer Algebra Systems and SAT Solvers”](https://ijcai.org/proceedings/2016/636), IJCAI 2016, §4 | Version of record | Prior work describing edge variables and pairwise incident-edge exclusions for matching constraints | Cited for the established encoding pattern; this artifact adds no novelty claim. |

The compatibility relation and known-answer schedule set come from the existing F38 finite synthetic benchmark. This package adds an explicit generated formula and a reproducible exhaustive check. The construction is derived from the graph; the package does not claim that the general encoding idea is new. The prior-art review is bounded to the cited matching encoding and the usual exactly-one translation; no broad literature or priority assessment is claimed. No external SAT solver, benchmark suite, timing, scaling study, practical QA data, human specialist review or peer review is included. The observed 19-model count applies only to this fixed graph.

The F38 question and compatibility graph are part of this research project; this reproducible package was prepared on 16 November 2026. No date or private record is offered as evidence of first conception or priority.

## Evidence status and limitations

The original F38 result compares sequential sampling laws and is not changed by this encoding. The formula does not establish the earlier F38 sampling, coverage, or completion-rate results; those remain separate evidence.

## Change history

| Version/date | Change | Reason and evidence |
| --- | --- | --- |
| 0.1.0 / 2026-11-16 | Initial standalone encoding and exhaustive verifier | Exact finite model count and frozen schedule set checked by standard-library enumeration and independent AI challenge. |
| 0.1.1 / 2026-11-18 | Clarified reviewer type in the public status record | The independent check was performed by AI; no human specialist review is claimed. Formula, verifier, finite count and evidence are unchanged. |
