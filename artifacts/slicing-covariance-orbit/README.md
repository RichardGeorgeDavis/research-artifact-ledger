# A finite slicing-covariance orbit test for two boundary modes

**Status:** `synthetic demonstration`, `bounded derivation`, and `independently checked` (AI source-and-arithmetic challenge; no human review claimed)
**Version:** `0.1.0`
**Prepared:** 2026-11-19
**Author:** Richard George Davis
**AI assistance:** AI assisted the derivation, source mapping, synthetic verifier and drafting. An independent AI reviewer checked source signs, units, assumptions and synthetic arithmetic against the pinned paper.

## Question and intended use

Can a two-boundary mode comparison reject only one declared real time-alignment nuisance without mistaking a principal-log branch cut for a physical mismatch? This finite example distinguishes a local log-chart residual from an exact global exponential-orbit check and shows why output-only reconstruction cannot identify an independent horizon amplitude.

For a reader-facing explanation of the finite example, see [When a time shift looks like a mismatch](https://rgd.cx/articles/when-a-time-shift-looks-like-a-mismatch) on RGD.cx.

## Claim supported

Let `H_j` denote the horizon coefficient and `O_j` the leading rescaled null-infinity coefficient for the same direct-branch `Ψ̃₄` mode in the tested representation. Let `F_j` be the fixed, nonzero baseline transfer before applying a relative endpoint shift `d=f(1)-f(0)`. With matched nonzero coefficients, fixed conventions and one shared real `d`, define the direct-branch exponent `a_j=2icω_j` and ratio `R_j=O_j/(F_jH_j)`. The declared alignment orbit is `R_j=exp(a_jd)` for every mode. If at least one reference mode has `Re(a_k)≠0`, its magnitude fixes the only possible real offset, `d*=log|R_k|/Re(a_k)`. Direct substitution in every complex ratio, including the reference, is then a necessary-and-sufficient exact membership check for this one-parameter orbit.

A principal complex logarithm is local, not a global phase-unwrapping rule. In the supplied synthetic example a valid large shift passes the magnitude-and-substitution test while the principal-log least-squares residual is positive. If only the asymptotic output coefficients are supplied and horizon coefficients are inferred using the same map, every tested real offset can be fitted exactly; that construction supplies no independent separator.

This is a conditional finite algebra result. It is not a black-hole simulation, a QNM calculation, an observed horizon measurement, a GR test, or a calibrated physical inference.

## Source relation and conventions

The [source map](../../sources/slicing-covariance-orbit.md) pins the paper’s [arXiv v2](https://arxiv.org/abs/2501.08964v2). It writes the slicing family in hyperboloidal coordinates and shows that the horizon-to-infinity transfer changes by an exponential of the endpoint difference `f(1)-f(0)`; it describes this as connecting different boundary cross-sections. For the direct branch its transfer factor is `exp(2icωd)`. For the mirror branch it is `exp(-2ic\bar{ω}d)`, so the corresponding transfer baseline must be conjugated. Equation (13) sets `c=2M` for the Schwarzschild case. The exponent is dimensionless because `c` has length units, `ω` inverse-length units, and the slicing function is dimensionless.

The quotient uses matched `Ψ̃₄` coefficients: the horizon coefficient and the leading rescaled `Ψ̃₄` coefficient at null infinity. A horizon `Ψ₀` amplitude or detector strain requires a separate conversion. The source derivation is perturbative and includes its own gauge, mode and boundary assumptions; the algebra below does not independently validate those physical assumptions.

## Exact orbit check

Under the fixed assumptions, `|R_k|=exp(Re(a_k)d)`. If `Re(a_k)≠0`, then

```text
d* = log(abs(R_k)) / Re(a_k)
accept iff R_j = exp(a_j d*) for every j
```

A zero `R_k` is outside this nonzero-ratio criterion; a zero `H_k` or `F_k` makes the quotient undefined. An undamped mode has `Re(a)=0` and cannot determine `d` by magnitude, though it can check phase after a damped reference determines the offset. If all references are undamped, one must solve simultaneous phase congruences instead. Unknown transfer, free per-mode complex gain, mode-dependent boundary time offsets, frame or tetrad changes, angular mixing, mass/frequency changes, mode-label errors, extraction changes or noise require new nuisance models. This criterion rejects only the stipulated single real offset.

In the local log chart, stack real and imaginary parts of `z_j=Log(R_j)` and `a_j` into real vectors; the local diagnostic projects `z` onto the one-dimensional real span of `a`. Two complex modes leave a three-dimensional linear complement in `R⁴` under these assumptions. A branch cut can make this local residual positive even for an exact global orbit point.

## Reproduction

From the repository root, run:

```sh
python3 -B artifacts/slicing-covariance-orbit/reproducibility/check_covariance.py
```

Verifier SHA-256: `fb33a2bd25ba705aa3ba4d9515373401f22775cb28f69491efd1cd9c2f2d723e`. The standard-library script uses synthetic dimensionless inputs `c=1`, `ω=(0.4−0.1i,0.7−0.15i)`, `F=(0.5−0.2i,0.8+0.1i)` and `H=(1.1+0.3i,−0.7+0.2i)`. These are not evaluated Schwarzschild QNMs or calibrated transfer constants; the two slots stand in for mode labels `(2,0,0)` and `(3,0,0)` only. It checks direct and mirror endpoint covariance, 160 synthetic field points per branch over four alignment cases, the one-sided failure control, a mode-specific map perturbation, a valid `d=8` orbit point, output-only fits at `d∈{-3,0,2,8}`, shape guards, and the rank-one nuisance projector.

The d=8 direct exponential ratios give zero global discrepancy by construction; recomputing them as `O^(8)/(FH)` has maximum floating-point discrepancy `1.83×10⁻¹⁵`. The principal-log local residual is `3.158806988771255`. Output-only baseline fits have maximum reconstruction error at most `1.48×10⁻¹⁶`. The script's equality tolerance is `2×10⁻¹²×max(1,|x|,|y|)`; this checks floating-point identities, not observational data.

## Evidence and review status

The derivation and synthetic values are author-created. An independent AI challenge checked the direct and mirror source signs, dimensions, coefficient meaning, damped-reference uniqueness, substitution sufficiency, principal-log counterexample and output-only inversion against the pinned v2 source, and independently recomputed the stated residual and reconstruction errors. No human specialist review, proof-assistant check, numerical-relativity run, actual horizon/infinity data, statistical threshold, novelty or priority search, peer review or field-level novelty is claimed.

## Limits and reopening condition

The test concerns one exactly specified real alignment parameter under fixed conventions. A free relative time origin of the two extractions is the same nuisance and therefore cannot be separately identified from it. Additional physical or numerical nuisance directions may absorb the quotient. Reopen empirical work only when a named compatible public product or expressly authorised dataset supplies independently usable same-case horizon and asymptotic coefficients, exact mode/revision, common time/frame/tetrad conventions, extraction and rescaling, perturbative-regime basis, and error estimates. The existing bounded search found no qualifying independent pair; this synthetic artifact does not change that access result.

No licence is assigned. Public visibility does not grant broader reuse permission.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-11-19 | Initial finite source-mapped orbit test and reproducibility script | Pinned arXiv v2 equations 13, 132, 136–145; independent AI source-and-arithmetic challenge; no empirical claim. |
