# Exact fixed-instance Main onset at D=d=1 — 5 November 2026

## Question and result

For the pinned Family-028 source-level fixed-tuple caller map, the exact sufficient threshold at the smallest geometric input is
`M_*(1,1)=6W\cdot100^W`, with `W=ceil⁺((log 5+1)/r)+1` and `r=I²/(768·160000·10500000·10^240·log 4)`. Here `I=(1427/120030000)·1431!·2567!/3999!`. This evaluates the existing sufficient construction at one exact instance; it is not a new theorem, a Lean-extracted constant or a compiled caller.

The conclusion is conditional on the separately derived pointwise density premise for every `X≥X_res` recorded in the preceding mass/Main source-audit update. That derivation is ordinary-mathematics/source replay and is not Lean elaboration or kernel certification.

## Source basis

The source is pinned at [openai/math commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb). The exact definitions and call sites are in [Main.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/Main.lean), [WindowBatch.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/WindowBatch.lean), [BatchCertificate.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/BatchCertificate.lean), [SieveSmoothing.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/SieveSmoothing.lean), and [WalkGeometry.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/WalkGeometry.lean). The earlier [26 October mass/Main update](source-audit-update-20261026-mass-main.md) provides the fixed tuple, pointwise density premise and symbolic caller map; the [28 October cutoff-scale update](source-audit-update-20261028-cutoff-scale.md) gives scale bounds and explicitly leaves complete `M_*` unevaluated.

## Derivation

The complex-norm lattice counts are `card(latticeBall 1)=5` and `card(latticeBall 4)=49`. Therefore `H=log 5`, `bandConstant(1)=10000+100log49<10400`, and `H_d=11900`.

The factorial expression obeys `10^-5733<I<1`. For the lower bound, the 1,432 denominator factors `2568,…,3999` are each below 4000, the rational prefactor exceeds `10^-5`, and `1431!>1`. For the upper bound, pair `1,…,1431` with the first 1,431 denominator factors and retain one extra denominator factor. Since `log4>1), these bounds give `0<r<10^-240), hence `W>10^240) and `B=100^W>10^8000). From the fixed `L₀=(369/200)·2^2567` and the lower bound on `I`, `X_res<10^7000<B); the exact top argument satisfies `X_top<10^6011<B).

For every integer `0≤w<W`, put `A_w=100^w`, so `A_w≤B/100), and put `U=WB). At `d=1`, `C(1,w)=11900(2A_w+1)≤357B). In `M_mid), the square-root argument is at most `32·11900·3=1,142,400<1100²), and the reciprocal-density term is at most `128/I<10^5736<B). In `M_bot), the square-root argument is at most `57,120B<B²), and its reciprocal-density term is `1920/(19I)<128/I). The remaining constants and `M_size) are below `B), so the natural ceilings preserve those bounds.

For `M_tail), the formulas give `A_W≤70U`, `C_W≤22B), and `800P̄=35,200+32,000B<67,200B<U). Thus `sqrt(4A_W)≤U` and `sqrt(400C_W)≤B≤U), including the constants inside the maxima. The top, interval and fixed guards satisfy `T_w(X_top)≤B`, `T_w(6000)≤B`, `T_w(1600)≤B), and `34,50,0≤U). Also `M_disp≤373,750<B), using `log10<5/2). Since `ε₀=exp(-100)/(512·640000)`, the logarithm in `M_err(w)` is below `128+5w); therefore `M_err(w)≤128+5w≤123+5W<6W≤U). These bounds cover the ten listed guards and yield `M_all(1,W;1,q)≤U=WB<6WB).

For the smoothing maximum, the first variable term is `(9600/361)log4·W/B<54W/B<6WB); the next is at most `152/(289B)<1); and the third is below `7/(15B)<1). The constant `2<6WB), while the final candidate is exactly `6WB). Therefore `R_s=6WB) and its natural ceiling is unchanged. The density term is at most `B), because `X_res<10^7000<B` and `5000log2<B). Taking the maximum gives the stated exact identity.

The elementary comparisons use `8/3<e<3), `(8/3)^4>49), and `(8/3)^5>100). The proof depends on the exact source-mapped component formulas; the argument above records the comparison rather than introducing a new source formula.

## Independent challenge and limitations

An independent AI reviewer requested at `gpt-6.1-sol / high` checked the corrected public-source challenge, including the complex-norm ball counts, factorial bracket, rate and width bounds, every batch guard, ceilings, smoothing maximum, density term and fixed-tuple quantifier order. The reviewer confirmed the identity and found no missing guard or ceiling issue. Serving telemetry was unavailable. This is scoped AI review, not qualified human mathematical review.

The result remains conditional on the separate pointwise density derivation. It does not establish a practical cutoff, sharpness, a Lean theorem constant, elaboration/build, cache or kernel assurance, or theorem-wide assurance. An unconditional formal caller would also require the pointwise density premise to be formalised. Values at other `D,d` remain unevaluated; no selector or executable `COST`/`BATCH` result is claimed.

## Change record

This is an untagged additive update on `main`; no open reuse licence is assigned. The exact public artifact version is `0.1.8`.
