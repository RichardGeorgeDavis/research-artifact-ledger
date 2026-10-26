# Sources for decimal carry states and prime-wheel phases

| Source or input | Version/date | Role | Claim supported | Access/rights notes |
|---|---|---|---|---|
| Texas A&M Applied Algebra, [Lecture 9](https://people.tamu.edu/~yvorobets/MATH433-2023A/Lect1-09web.pdf). | Course notes accessed 2026-10-05. | Generalized Chinese remainder theorem context for compatible congruences with shared factors. | For moduli 10^k and 30 or 210, a residue pair is compatible exactly when its components agree modulo 10; compatible pairs form one class modulo the least common multiple. The artifact gives the direct proof for these moduli. | Link and attribution only; no text or figure reproduced. |
| Kevin Ford, [Sieve Methods lecture notes](https://ford126.web.illinois.edu/sieve2023.pdf). | Course notes accessed 2026-10-05. | Background on residue-class sieving and reduced-residue wheel filters. | Surviving residues are candidates after filtering selected prime divisors; this does not assert primality. | Link and attribution only; no text or figure reproduced. |
| Stanford, [Modular Arithmetic and the Chinese Remainder Theorem](https://crypto.stanford.edu/pbc/notes/numbertheory/arith.html). | Notes accessed 2026-10-05. | Modular-state background. | Interpreting each component as a finite residue state. | Link and attribution only; no text or figure reproduced. |
| [`../reproduce/carry_wheel_phase_alignment.py`](../reproduce/carry_wheel_phase_alignment.py) in this repository. | Versioned with this artifact. | Author-created finite enumeration. | Checks complete periods for `k=1,2,3`, compatibility, survivor totals, per-state counts and carry rejection. | Python standard library only; no external input. |

The artifact is a standard modular-arithmetic application. It makes no field-novelty or prime-prediction claim. The complete derivation and run provenance remain in the private research record.
