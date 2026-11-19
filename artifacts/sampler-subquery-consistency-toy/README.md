# Equal extension counts do not guarantee subquery consistency

**Status:** `synthetic demonstration`, `bounded derivation`, and `independently checked` (AI source-and-arithmetic challenge; no human review claimed)
**Version:** `0.1.0`
**Prepared:** 2026-11-19
**Author:** Richard George Davis
**AI assistance:** AI assisted the construction, source mapping and drafting; an independent AI reviewer checked the finite arithmetic and theorem-boundary interpretation.

## Question and intended use

Can a modified formula have the same number of satisfying extensions for two retained assignments while an input-sensitive sampler still changes their conditional probabilities? This small example is intended to help readers distinguish equal fibre sizes from the stronger sampler-behaviour assumption used by a conditional sampling argument.

## Claim supported

For the stipulated sampler family below, conditioning its distribution on the original formula to the pair `{00,11}` gives probability `5/6` to `00`, while uniform sampling over the satisfying assignments of the displayed modified formula projects to probability `1/2` for `00`. Each retained assignment has 4,095 auxiliary extensions. Equal extension counts therefore make the *uniform full-assignment projection* uniform on the pair, but do not make it equal to the original input-sensitive sampler conditioned on that pair.

This is a finite synthetic example of a known assumption boundary. It is not a contradiction of Barbarik2 or Barbarik3, a result about a deployed sampler, a general impossibility theorem, or a claim of field novelty or priority.

## Construction and exact arithmetic

Let `φ=(x∨¬x)∧(y∨¬y)`. Its satisfying assignments are `00, 01, 10, 11`. Let the target distribution `P` be uniform on these four assignments. Stipulate an input-sensitive sampler family `G` whose output on this exact input is `Q(00)=5/8` and `Q(01)=Q(10)=Q(11)=1/8`.

Choose `T={00,11}` and define this illustrative modified formula:

```text
(x OR NOT x)
AND (y OR NOT y)
AND (NOT x OR y)
AND (x OR NOT y)
AND (a1 OR a2 OR ... OR a12)
```

The equality clauses retain exactly `00` and `11`. The last clause has `2^12−1=4,095` satisfying assignments, so each retained pair member has exactly 4,095 extensions and the modified formula has 8,190 full satisfying assignments. Stipulate that `G` is uniform over those full satisfying assignments on this exact modified input. Its projection to `(x,y)` is then uniform on `T`.

On the original input, `Q(T)=5/8+1/8=3/4`, so `Q(00|T)=(5/8)/(3/4)=5/6`. The modified-input projected probability is `1/2`; the conditional-law gap is `1/3`. Relative to the uniform target on the original four assignments, `||Q−P||₁=3/4` and total variation is `3/8`.

## Relation to the cited testing results

The 2020 paper defines multiplicative closeness across all formulas and `ℓ₁` farness at a formula. Its Theorem 1 gives the close-case ACCEPT guarantee without subquery consistency; its far-case REJECT guarantee requires both `η`-farness and subquery consistency for the chosen kernel. With `ε=1/20`, `η=7/10`, this `Q` is `η`-far in the paper's `ℓ₁` convention because `3/4>7/10`, and `η>6ε`. The displayed modified input fails the analogous conditional-law equality. Since it is not a source-level reproduction of the paper's kernel output and `G`'s behaviour on that output is unspecified, this toy does not establish whether `G` satisfies the theorem's kernel-specific subquery-consistency assumption; the far-case guarantee therefore cannot be invoked from this construction. `G` already fails `ε`-closeness on the original formula, so the close-case guarantee does not apply.

The modified formula here is a simplified truth-functional teaching construction with the same retained pair and equal fibre size. It is not an execution or source-level reproduction of the paper's randomized literal-guard kernel. The numerical example stipulates the sampler's behaviour on this one modified input; it does not predict how an actual implementation responds to a kernel-generated formula.

The 2022 paper uses total variation farness and a DUAL oracle for the target plus PCOND and SAMP access for the tested sampler. Here `TV(Q,P)=3/8<7/10`, so the same `η=7/10` does not make this input far under that paper's convention. Parameters and oracle assumptions must not be transferred between the two results without checking their definitions.

## Evidence and review status

The counts and probabilities follow by enumeration of the four original assignments and the 4,095 nonzero 12-bit auxiliary assignments. The expressions above are sufficient for a reader to check the result without software. An independent AI challenge on 2026-11-19 verified the finite arithmetic, the 2020 close/far guarantee distinction and the 2022 distance/oracle distinction against the cited primary papers. It noted that representing the paper's exact randomized kernel would require additional input-specific stipulations; this artifact therefore labels its construction as a simplified toy. No human specialist review, proof-assistant verification, third-party sampler execution or complete audit of either paper is claimed.

## Sources and provenance

The [source map](../../sources/sampler-subquery-consistency-toy.md) pins the relevant primary sources and maps each claim to its definition, theorem or algorithm. The first retained private record is dated 2026-10-02; that date does not establish first conception or priority. This artifact is a reader-facing worked example and makes no field-level novelty or priority claim.

## Limitations and unresolved issues

The sampler family is stipulated rather than implemented. The example addresses one formula and one pair; it says nothing about whether a named sampler is subquery consistent on other inputs, kernels, weights, seeds or versions. It does not estimate the full tester's probability of acceptance or rejection, validate a source-code implementation, establish practical sample costs, or refute any theorem whose hypotheses remain intact.

No licence is assigned. Public visibility does not grant broader reuse permission.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-11-19 | Initial public record of the finite equal-extension example | Exact finite derivation and independent AI source-and-arithmetic challenge; no real sampler or novelty claim. |
