#!/usr/bin/env python3
"""Regenerate and exhaustively count the F38 five-suite DIMACS encoding."""
from itertools import combinations
from pathlib import Path

COMPATIBILITY = {
    "A": (1, 2, 3, 4, 5),
    "B": (1, 4, 5),
    "C": (1, 3, 5),
    "D": (1, 2, 4),
    "E": (2, 3, 5),
}
EXPECTED_SCHEDULES = {
    (1, 4, 3, 2, 5), (1, 4, 5, 2, 3), (1, 5, 3, 4, 2),
    (2, 1, 3, 4, 5), (2, 1, 5, 4, 3), (2, 4, 3, 1, 5),
    (2, 4, 5, 1, 3), (2, 5, 1, 4, 3), (3, 1, 5, 4, 2),
    (3, 4, 1, 2, 5), (3, 4, 5, 1, 2), (3, 5, 1, 4, 2),
    (4, 1, 3, 2, 5), (4, 1, 5, 2, 3), (4, 5, 1, 2, 3),
    (4, 5, 3, 1, 2), (5, 1, 3, 4, 2), (5, 4, 1, 2, 3),
    (5, 4, 3, 1, 2),
}


def build_cnf():
    edges = [(suite, env) for suite in "ABCDE" for env in COMPATIBILITY[suite]]
    var = {edge: i + 1 for i, edge in enumerate(edges)}
    clauses = []
    for suite in "ABCDE":
        ids = [var[suite, env] for env in COMPATIBILITY[suite]]
        clauses.append(ids)
        clauses.extend([[-a, -b] for a, b in combinations(ids, 2)])
    for env in range(1, 6):
        ids = [var[suite, env] for suite in "ABCDE" if env in COMPATIBILITY[suite]]
        clauses.append(ids)
        clauses.extend([[-a, -b] for a, b in combinations(ids, 2)])
    return edges, var, clauses


def dimacs(clauses, nvars):
    return (
        "c F38 five-suite QA schedule compatibility encoding\n"
        "c Variables are x_(suite,environment), IDs in README.md order.\n"
        f"p cnf {nvars} {len(clauses)}\n"
        + "\n".join(" ".join(map(str, clause)) + " 0" for clause in clauses)
        + "\n"
    )


def main():
    edges, var, clauses = build_cnf()
    if len(edges) != 17:
        raise SystemExit(f"expected 17 variables, found {len(edges)}")
    if len(clauses) != 53:
        raise SystemExit(f"expected 53 clauses, found {len(clauses)}")
    if max(map(len, clauses)) != 5:
        raise SystemExit(f"expected maximum clause width 5, found {max(map(len, clauses))}")
    repo = Path(__file__).resolve().parents[2]
    cnf_path = repo / "artifacts" / "f38-five-suite-schedule-cnf" / "f38-schedule.cnf"
    if cnf_path.read_bytes() != dimacs(clauses, len(edges)).encode("ascii"):
        raise SystemExit("DIMACS bytes do not match the regenerated clauses")

    model_count = 0
    decoded_models = set()
    for mask in range(1 << len(edges)):
        if all(any((literal > 0) == bool(mask & (1 << (abs(literal) - 1)))
                   for literal in clause) for clause in clauses):
            model_count += 1
            schedule = []
            for suite in "ABCDE":
                chosen = [env for env in COMPATIBILITY[suite]
                          if mask & (1 << (var[suite, env] - 1))]
                if len(chosen) != 1:
                    raise SystemExit(f"satisfying assignment decodes ambiguously for suite {suite}: {chosen}")
                schedule.append(chosen[0])
            decoded_models.add(tuple(schedule))

    if model_count != 19:
        raise SystemExit(f"expected 19 satisfying assignments, found {model_count}")
    if len(decoded_models) != model_count:
        raise SystemExit("distinct decoded schedule count differs from raw satisfying-assignment count")
    if decoded_models != EXPECTED_SCHEDULES:
        raise SystemExit("decoded models differ from the frozen F38 schedule list")
    print("PASS: 17 variables, 53 clauses, maximum width 5, no auxiliaries")
    print("PASS: exhaustive search of 131072 assignments found exactly 19 models")
    print("PASS: decoded models equal the 19 frozen F38 schedules")


if __name__ == "__main__":
    main()
