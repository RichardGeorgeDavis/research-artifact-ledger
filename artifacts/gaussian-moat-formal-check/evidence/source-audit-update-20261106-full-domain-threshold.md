# Exact all-domain source-level sufficient Main threshold

Status: Bounded derivation; source-level; corrected copy independently AI-reviewed

Date: 2026-11-06

Artifact: [Gaussian-moat theorem: bounded Lean endpoint check](../README.md), version 0.1.9.

## Question and scope

For the fixed scalar tuple already recorded in the [mass/Main source update](source-audit-update-20261026-mass-main.md) and [cutoff-scale update](source-audit-update-20261028-cutoff-scale.md), can the source-defined sufficient Main threshold be evaluated exactly for every real D >= 1 and rational d >= D?

Yes, at ordinary source-mapped mathematical scope, the defined expression is:

    M*(D,d) = max(6 W 100^W, ceil+(X_int(d)))

Here H = log(card(latticeBall(D))), W = ceil+((H+1)/r)+1, B = 100^W, and X_int(d) = max(6000, (25/4)(2d^2 - 1)). The symbol ceil+ means natural ceiling. This exactly evaluates the prescribed sufficient expression; it does not establish that the upstream formal caller compiles with this expression or that the theorem has a new formal constant.

The fixed tuple has I = (1427/120030000)·1431!·2567!/3999! and r = I^2/(768·160000·10500000·10^240·log 4). Its already recorded bounds include 10^-5733 < I < 1, r < 10^-240, W > 10^240, B > 10^8000, and X_res < 10^7000 < B. The result remains conditional on the separate pointwise density premise for every real X >= X_res.

## Source-mapped comparison

The pinned caller is [WindowBatch.lean, lines 43–52](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/WindowBatch.lean#L43-L52); the source-defined lattice ball is [WalkGeometry.lean, lines 429–433](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/WalkGeometry.lean#L429-L433). The corresponding smoothing and density definitions are in the pinned [SieveSmoothing.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/SieveSmoothing.lean) and [AccurateScales.lean](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/AccurateScales.lean). The pinned revision is [OpenAI Math commit fd4aeeb](https://github.com/openai/math/commit/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb).

For every D >= 1, the axis points give D <= card(latticeBall(D)) = e^H. The lattice-square count gives card(latticeBall(4D)) <= (8D+1)^2 <= 81D^2, hence log(max(D, card(latticeBall(4D)))) < log 81 + 2H. With the fixed rate, the source band constant is below 10500 + 300H < 10800W, and the top cutoff satisfies X_top < 10^6011 W < B.

For each integer 0 <= w < W, let A_w = 100^w and E = max(B,d). The source bounds give A_w <= B/100, C(d,w)/A_w <= 35700E, and C(d,w) <= 357BE. The middle and bottom square-root terms are therefore below 1100E and 240E. When d <= B, these and the corresponding tail terms fit below the smoothing bound 6WB; when d > B, their d-dependent terms are bounded by d^2 <= X_int(d). The tail bounds use A_W <= 70WB, C_W <= 22B, and 800Pbar <= 67200E. The remaining reciprocal, fixed, size, displacement and error guards are also below 6WB; in particular M_err(w) <= 128+5w <= 123+5W < 6W <= 6WB. Thus every non-interval guard is below 6WB when d <= B; when d > B, each d-dependent guard is bounded by X_int(d), while the fixed guards remain below 6WB. Including the interval candidate T_0(X_int(d)) = ceil+(X_int(d)), the pinned caller therefore gives M_all(D,d) <= max(6WB, ceil+(X_int(d))) uniformly over the stated domain. Some d-dependent guards need not be below WB.

In the source smoothing maximum, the final candidate is exactly 6WB; each other candidate is smaller, using H < W and the fixed-tuple bounds. Hence R_s(D) = 6WB. The density term is at most B, conditional on the separate pointwise density result. Conversely, the interval term at w=0 is exactly ceil+(X_int(d)). These upper and lower bounds give the stated exact maximum.

The raw crossing X_int(d) = 6WB occurs at d^2 = (12/25)WB + 1/2. Because the interval term is naturally rounded, its tie band is (12/25)WB + 1/2 - 2/25 < d^2 <= (12/25)WB + 1/2. For the diagonal d = ceil(D), the count bound gives d <= e^H < e^W < 3^W, which implies X_int(d) < B and therefore ceil+(X_int(d)) <= B < 6WB. At the other extreme, d = 2B gives ceil+(X_int(d)) = 50B^2 - 6, so the interval term can dominate. The earlier D=d=1 result is recovered as the special case in the [5 November exact-onset update](source-audit-update-20261105-main-onset.md).

## Corrected-copy independent review and limits

After the release-copy correction, a separate source-only review checked the public caller map, all ten non-interval guards across `d <= B` and `d > B`, the `w=0` interval candidate, smoothing and density bounds, lower-bound attainments, diagonal case, and rounded crossing/tie statements. It confirmed the corrected `M_*` identity and found no remaining mismatch in that bounded scope. An earlier challenge outcome is recorded separately in the private run history and is not used to verify this corrected copy. No independent human or qualified specialist review is claimed.

This is an exact evaluation of a source-defined sufficient expression, conditional on the separate pointwise density premise and the branch bounds above. It does not establish sharpness, a practical cutoff, an executable COST or BATCH result, Lean elaboration/build, cached-source authentication, kernel trust or theorem-wide assurance. The underlying Gaussian-moat theorem remains attributed to OpenAI. This update makes no novelty claim and establishes no connection to ordinary-prime prediction or the Infinity Research framework.

## Change record

Added 2026-11-06 as a bounded extension of the D=d=1 evaluation. This public evidence note contains no local paths, private records, third-party source text or copied source code. No open reuse licence is assigned.
