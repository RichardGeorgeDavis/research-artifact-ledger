# Fixed-tuple mass and conditional Main map — 26 October 2026

This update extends the 26 October scalar tuple note with an independently challenged all-`X` weighted-mass reconstruction and a source-level map of the exact caller obligations in the pinned [`Main.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/Main.lean). It is a bounded source/math review of an existing OpenAI-authored theorem. It is not a new theorem, a Lean proof, or an independent human or specialist review.

## Fixed tuple and density contract

At OpenAI Math revision [`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), let

\[
I=\frac{1427}{120030000}\frac{1431!\,2567!}{3999!},\qquad
L_0=\frac{369}{200}2^{2567},\qquad
X_{\rm res}=\max\left(4001,\frac{15L_0}{2I}\right).
\]

The reviewed construction uses `a=I/192`, `δ=I/48`, `K=5000`, and `t=I/(160000 log 4)`. The preceding [scalar tuple update](source-audit-update-20261026.md) supplies its exact elementary inequalities and factorial identity.

For real `s>1`, pinned Mathlib defines the real residue-class quantity at residue 1 modulo 4 as

\[
F(s)=\Re(\mathrm{LFunctionResidueClassAux}(1:\mathbb Z/4\mathbb Z,s))=\sum_{n\ge1}\frac{\Lambda(n)\mathbf1_{n\equiv1\pmod4}}{n^s}-\frac1{2(s-1)},\qquad s>1.
\]

See pinned Mathlib [`PrimesInAP.lean` lines 252–261](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/NumberTheory/LSeries/PrimesInAP.lean#L252-L261) and its agreement lemma at [lines 303–305](https://github.com/leanprover-community/mathlib4/blob/d13f23b723b8a846827a245b89c10fc7d3f11612/Mathlib/NumberTheory/LSeries/PrimesInAP.lean#L303-L305). The sampled points are `s_j=1+(j+1)/X`, with `1<s_j≤2`. In a reconstruction using the pinned `PrimeMass.lean` identity, writing `Z(s)=(s−1)ζ(s)` and `β(s)=L(s,χ₄)`, the same quantity is

\[
F(s)=-\frac12\left(\frac{Z'(s)}{Z(s)}+\frac{\log 2}{2^s-1}+\frac{\beta'(s)}{\beta(s)}\right),\qquad 1<s\le2.
\]

The floor integral is `J(s)=\int_1^\infty\{x\}x^{-s-1}dx`. The identities `Z=s−s(s−1)J` and `Z'=1−(2s−1)J−s(s−1)J'` give `Z≥1` and `−1/2≤Z'≤3/2`. The alternating beta series and its uniformly bounded differentiated remainder give `2/3≤β≤1` and `0≤β'≤log(3)/3<1/2`, hence `−13/8≤F(s)≤1/4`. These are reconstructed bounds, not bounds stated by the cited Mathlib declaration itself; only sampled `s_j>1` are used, so no value `F(1)` is needed. The zero-sum window coefficients bound the approximation error by `15 L₀/(16X)≤I/8` for `X≥X_res`; the residue mass is at least `IX/4`. For the non-prime terms, von Mangoldt support leaves odd prime powers `p^k`, `k≥2`, in residue `1 mod 4`, and

\[
\sum_p\frac{\log p}{p(p-1)}\le\sum_{n\ge2}\frac{\log n}{n(n-1)}\le2\sum_{n\ge2}n^{-3/2}\le4.
\]

Since `L₀>64/15`, `X_res>32/I`; subtracting this tail leaves prime-filtered mass at least `IX/8` for every real `X≥X_res`.

Set `γ=I/8`. The pinned [`DenseBins.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/DenseBins.lean#L82-L219) construction gives a finite `G_X` with `|G_X|≥IX/(32 log 4)`, the required interval-location bounds and the per-bin prime-cardinality lower bound with `δ=I/48`; its `X≥1000` guard follows from `X_res≥4001`. Fix `K=5000` before `X`. The pinned [`BatchCertificate.thin_bins`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/BatchCertificate.lean#L151-L186) partitions `G_X` by residue modulo `K`; one class gives a finite `J_X` with `|J_X|≥IX/(32K log4)=tX` and ordered distinct elements separated by at least `K`. Filtering preserves the interval and per-bin density bounds. Thus for every real `X≥X_res`, the required finite-set contract holds; only the residue class and `J_X` depend on `X`.

The decisive retrieved OpenAI raw-file SHA-256 values are: `PrimeMass.lean` (physical lines 11–24, 103–151, 198–216, 307–381) `bd5f73342ff6a9b6d25fe63746fc7f0eee2ba479c8869319bd748319877fc002`; `DenseBins.lean` (82–122, 130–219) `79895aa006aa0af75ed74bf97ce3305d8d07da67db037100eab75d65c9d36d58`; `SeparatedParameters.lean` (183–220) `14e1f6a6ab1598f92b9194e19dfe35b32eecc7d43b96a8e73f3c2ea0f3618529`; `BatchCertificate.lean` (`thin_bins`, 151–186) `d9862e913af5fb05361201428bb988f8d223512b398404bc363ec57a4d1c87a9`; and `Main.lean` (9–45) `33d31a805d14d899ea5004004ffd9bb6021d877ccdc17322695360160914e3fd`. For Mathlib at revision [`d13f23b723b8a846827a245b89c10fc7d3f11612`](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612), `PrimesInAP.lean` (86–98, 237–261, 288–294, 303–341) is `a2491d48850056b27fe6ad31cf7b210a7f6455e8e0fa4fbb714671bbffb61ca4` and `DirichletContinuation.lean` (75–85, 169–178, 338–365) is `7ef38fb53f462e19dfd6746fc1826423e55bb5e2672c2b5667e2fd4889f401b6`. All hashes identify retrieved raw bytes at the immutable revisions linked above, not independent Git-tree or cache authentication.

## Conditional source-level Main caller map

Two independent AI source-only reviews checked the exact public-source challenge packet against pinned [`Main.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/Main.lean#L9-L97) and the named component sources: [`AccurateScales.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/AccurateScales.lean), [`CommonBlocks.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/CommonBlocks.lean), [`PointEnrichment.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/PointEnrichment.lean), [`WindowParameters.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/WindowParameters.lean), [`BatchParameters.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/BatchParameters.lean), [`WindowBatch.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/WindowBatch.lean), [`Smoothing.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/Smoothing.lean) and [`SieveSmoothing.lean`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/SieveSmoothing.lean). They found no cutoff, quantifier-order, ceiling or caller-condition mismatch. The map fixes the above tuple and carries `X_res` explicitly into an alternative construction. With `H(D)=log(card(latticeBall D))`, `Q=I/(192·10^240)`, `c=Q/4`, and `r=ct/10500000`, it uses

\[
W_*(D)=\left\lceil\max\left(0,\frac{H(D)+1}{r}\right)\right\rceil^+ +1,
\]

and, for any rational `d≥D≥1`,

\[
M_*(D,d)=\max\left\{M_{\rm all}(D,W_*;d,q),\;\lceil R_s(D,W_*)\rceil^+,\;\left\lceil\max(0,X_{\rm res},5000\log2)\right\rceil^+\right\},\qquad q=\delta.
\]

The symbolic components in this expression are defined as follows; `ceil⁺(x)` is the least natural number at least `x`, `A_w=100^w`, and `T_w(R)=ceil⁺(R/A_w)` for `R>0`. For rational `d≥D≥1`, put `H_d=10200+1700d`, `C(d,w)=H_d(2A_w+1)`, `C_W=20·100^W+2`, `A_W=60W·100^W+4(W+1)+2`, and `P̄(d,W)=38+2d+2C_W`. These are sufficient majorants for the pinned `CommonBlocks.lean`, `AccurateScales.lean`, `PointEnrichment.lean` and `WindowParameters.lean` bounds. Then

\[
\begin{aligned}
M_{mid}(d,q,w)&=\max\{\lceil15360/A_w\rceil^+,15,\lceil\max(32/A_w,\sqrt{32C(d,w)/A_w})\rceil^+,\lceil8/(3qA_w)\rceil^+,\lceil2/A_w\rceil^+\},\\
M_{bot}(d,q,w)&=\max\{76800,15,\lceil\max(160,\sqrt{160C(d,w)})\rceil^+,\lceil40/(19q)\rceil^+,2\},\\
M_{tail}(d,W)&=\max\{\lceil\max(8,\sqrt{4A_W})\rceil^+,\lceil\max(400,\sqrt{400C_W})\rceil^+,\lceil800P̄(d,W)\rceil^+\},\\
M_{size}(w)&=\max\{\lceil7680/A_w\rceil^+,10\},\qquad M_{bands}(d,q,W,w)=\max\{M_{mid}(d,q,w),M_{bot}(d,q,w),M_{tail}(d,W),M_{size}(w)\}.
\end{aligned}
\]

Take `ε₀=min(1/1024,exp(−100)/(512·640000))`, `bandConstant(D)=10000+100|log D|+100|log(max(D,(card(latticeBall(4D)):ℝ)))|`, `X_top=max(2,768·10^270·bandConstant(D)/I,38400·10^246/I)`, `X_int=max(6000,(25/4)(2d²−1))`, `M_disp=ceil⁺(25·max(0,log(7680000·10^240/I)))`, and `M_err(w)=ceil⁺(max(2,log(182·100^w/ε₀)))`. The complete ten-guard component and finite maximum are

\[
M_{batch}(D,d,q,W,w)=\max\{M_{bands},M_{tail},T_w(X_{top}),T_w(X_{int}),34,50,M_{disp},0,M_{err}(w),T_w(1600)\},\qquad
M_{all}(D,W;d,q)=\max_{w\in\mathbb{N},\,w<W}M_{batch}(D,d,q,W,w).
\]

For the smoothing term, with `B=100^W`, `A=2B`, `b=19B/20`, `C=3WB`, `P=4log(4)C`, `b₁=9A−1`, `P₁=4(9A+1)`, `H=log(card(latticeBall D))`, `b₀=8A−1`, and `P₀=2(max(H,0)+2)`, the exact source-level onset is `R_s=max(2,2P/b²,2P₁/b₁²,(P₀−1)/b₀,2C)`. For any natural `m≥M_*(D,d)`, these definitions provide the source-level caller's batch, smoothing, scale and density premises for every `w<W_*(D)`: `M_all` dominates all ten batch guards on the finite nonempty range, `ceil⁺(R_s)` supplies the smoothing onset, and the final ceiling ensures `exp(m)≥X_res` and `exp(m)≥5000 log 2`. `W_*` gives the strict Main rate condition. The reviewers checked the component bounds, rational majorant for the band constant, positivity and ceilings, finite `w<W_*` range, and Main's later quantifier order. `M_*` is a symbolic sufficient bound only: no numerical `D`, rational bracket, certified transcendental evaluation, or Lean-extracted cutoff is supplied.

The source-level map is conditional on the fixed-tuple all-`X≥X_res` density contract above. It does not show that unchanged `Main.lean` selects the fixed tuple or `X_res`; no alternative Main theorem was written or elaborated.

## Review and limits

The mass/density derivation and source anchors received an independent pinned-source/math challenge. The Main/cutoff map received two independent AI source-only challenges; each found no mismatch in its bounded scope. Requested reviewer settings were `gpt-6.1-sol / high`; serving-runtime telemetry was unavailable. The exact reviewed sources and their limitations are those linked above. No Lean or Lake command was run for this update.

This evidence does not establish a Lean/Lake build of the alternative construction, selector, executable `COST`/`BATCH`, numerical or minimal cutoffs, cache/source correspondence, kernel trust, complete imported-proof closure, theorem-wide assurance, novelty, a practical application, or independent human/specialist review. The original endpoint build remains the separate bounded evidence described in the artifact record.
