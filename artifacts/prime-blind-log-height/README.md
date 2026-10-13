# A prime-blind logarithmic height gives an infinite tail path

Status: `bounded derivation`

Version: `0.1.0`

Last updated: `2026-10-13`

Artifact editor: Richard George Davis

Preparation included AI-assisted mathematical analysis and review. The candidate height profile was proposed by an AI reviewer in a private research run; its host model identity was not available for readback.

## Question and intended use

For the fixed square-spiral address convention and fixed ten-phase circular display below, does the prime-blind height `z(n)=log(n+1)` produce an infinite connected component among Gaussian-prime addresses at every positive edge cutoff?

This is a bounded mathematical result about one declared display map. It helps distinguish a prime-dependent construction from a fixed height chosen without reference to prime membership. It is not a prime predictor, a statement about the original two-dimensional prime graph, or a classification of other height functions.

## Claim supported

Let `S: {1,2,3,...} → Z[i]` be the square spiral starting at `S(1)=0`, moving right, up, left and down in turn, with segment lengths `1,1,2,2,3,3,...`. For a fixed finite radius `R ≥ 0`, map each positive integer address `n` to

`H_R(n) = (R cos(2πn/10), R sin(2πn/10), log(n+1))`.

Form a graph whose vertices are the addresses `n` for which `S(n)` is a Gaussian prime, joining distinct vertices when their Euclidean distance after applying `H_R` is at most `δ`. For every `δ > 0`, this graph contains an infinite connected component.

The claim is conditional on the stated spiral convention and the fixed-modulus prime-number-theorem input identified below. The same height function and phase map work for every positive cutoff; the starting point of the connected tail may depend on the cutoff.

## Method and derivation

1. **Address on the positive real axis.** Write `n(p)` for the address of `(p,0)` when `p` is a positive integer. The ring of radius `p−1` ends at `(p−1,−(p−1))` with address `(2p−1)^2`. From that corner, `p` moves reach `(p,0)`: one step right, followed by `p−1` steps up. Therefore `n(p)=(2p−1)^2+p=4p^2−3p+1`. This formula is for the convention stated above; a changed starting index or turn order needs a new mapping.
2. **An infinite same-phase Gaussian-prime subsequence.** Take the increasing sequence `p_1<p_2<...` of rational primes congruent to `3 mod 20`. The prime-number theorem for this fixed reduced residue class gives infinitely many such primes. Each is `3 mod 4`. If such a rational prime factored into two nonunits in `Z[i]`, multiplicativity of the Gaussian norm would force both factors to have norm `p`; but `p` is not a sum of two squares because squares modulo `4` are `0` or `1`. Thus `p` is irreducible, and since `Z[i]` is Euclidean, it is a Gaussian prime. Therefore `(p_k,0)` is a vertex. Since `p_k ≡ 3 mod 10`,

   `n(p_k) ≡ 4·3^2−3·3+1 ≡ 8 (mod 10)`.

   All selected addresses consequently have identical first two display coordinates.
3. **Successive selected heights become arbitrarily close.** The cited fixed-modulus result gives a weighted prime-counting asymptotic; by partial summation it yields `π(x;20,3) ~ x/(φ(20) log x)=x/(8 log x)`. For every fixed `ε>0`, the number of primes in this class between `x` and `(1+ε)x` tends to infinity as `x` grows. In particular, for sufficiently large `k`, `p_{k+1} ≤ (1+ε)p_k`; hence `p_{k+1}/p_k → 1`. As `n(p) ~ 4p^2`, it follows that `n(p_{k+1})/n(p_k) → 1`, and therefore

   `log(n(p_{k+1})+1) − log(n(p_k)+1) → 0`.

4. **Connect a tail.** Given any `δ>0`, choose `K` large enough that every successive selected-height difference after `K` is less than `δ`. The selected addresses have equal circular coordinates, so the Euclidean distance between the images of `n(p_k)` and `n(p_{k+1})` is exactly their positive height difference. Each successive pair for `k≥K` is therefore an edge. The infinite sequence `n(p_K), n(p_{K+1}), ...` is an infinite path, which lies in an infinite connected component.

No numerical value for `K` is derived. No computation is needed to establish this asymptotic argument, and no finite numerical check is presented as proof.

## Evidence class and review status

The fixed-modulus prime input was checked against Thorner and Zaman, Theorem 1.1, Corollary 1.4 and Remark 1.5, including the fixed `(q,a)=(20,3)` specialisation. The derivation was reconstructed by the research coordinator and received a separate AI challenge of the formula, phase, asymptotic implication and graph argument. The independent challenge accepted it only at the stated conditional scope.

No qualified human mathematical review, formalisation, numerical cutoff, or independent reproduction is claimed. The cited analytic-number-theory source's proof was not replayed. The displayed proof is included so readers can inspect the finite chain of implications directly.

## Prior work and contribution boundary

The prime-number-theorem input is established mathematics, not a contribution of this artifact. The inspected Cilleruelo–Tesoro result uses Gaussian-prime and arithmetic-progression methods for a different additive-sequence construction. The inspected Lacasa et al. work treats prime sequences and spiral representations. The bounded comparison did not identify either as an exact antecedent for the complete fixed-height graph statement, but the search and source coverage are incomplete.

A targeted zbMATH Open retrieval attempt returned no inspectable record and a direct-open HTTP 403. This is an access failure, not evidence that the index lacks a relevant result. Exact prior art remains unresolved. No claim is made that the derivation is new to mathematics, that the project application is original, or that this is a new theorem.

## Limitations and what this does not establish

- It treats one address convention, one ten-phase map and the single height `log(n+1)`; it classifies no other height profiles.
- It proves existence of an infinite component containing the selected tail; it does not show that the component contains only these vertices or describe every component.
- It gives no effective threshold for a given `δ`, finite-cutoff estimate, density statement or rate of convergence.
- It does not preserve the original square-spiral adjacency relation under the display map.
- It does not establish a useful prime-generation or retrieval method, a physical interpretation, a broad Infinity framework claim, field novelty or priority.
- The proof uses the cited established prime-number theorem for a fixed arithmetic progression; it assumes no additional unproved prime-distribution conjecture.

## Sources and provenance

See [`../../sources/prime-blind-log-height.md`](../../sources/prime-blind-log-height.md) for source versions, exact roles, source-to-claim mapping and access limits. The full derivation, prior-art packets and review history remain in the private research record and are not included here.

## Authorship, chronology and prior work

This public artifact was prepared by Richard George Davis from a private, dated research record. The candidate height profile was suggested by an AI reviewer; the host did not expose that reviewer's model identity. The mathematical claim is presented with the derivation and evidence status above, not as a claim about who first conceived an equivalent idea.

| Event | Date | Evidence and what it establishes |
|---|---|---|
| First retained project record | 2026-10-13 | Private research record documents the candidate and its bounded derivation; it is not public evidence of global priority. |
| Prior-art review | 2026-10-13 | Bounded source comparison and a later inaccessible specialist-index attempt; exact prior art remains unresolved. |
| First public appearance of this artifact | Recorded in this file's Git history | Establishes when this repository first contained this version, not first conception, originality or correctness. |

No licence is assigned by this repository. This artifact paraphrases and cites sources; it does not reproduce third-party text, figures, code or data.

## Independent review

Reviewer: separate AI reviewer in the research workflow; host model identity unavailable. Date: 2026-10-13.

Scope: address formula, residue-class phase, use of the fixed-modulus prime theorem, logarithmic height limit and resulting graph path.

Outcome: accepted at the stated conditional scope. This is not qualified human specialist review, formal verification or an independent proof audit by a human mathematician.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-10-13 | Initial bounded derivation | Coordinator reconstruction and separate AI challenge; prior-art limits and review status stated explicitly. |
