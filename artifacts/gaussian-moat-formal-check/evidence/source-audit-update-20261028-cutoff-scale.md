# Fixed-tuple cutoff scale — 28 October 2026

This update evaluates the scale of the existing fixed-tuple sufficient construction from the 26 October mass/Main review. It is a bounded arithmetic consequence, not a new theorem, Lean result or complete numerical Main cutoff.

## Derived density onset scale

At pinned OpenAI Math revision [`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb), the 26 October ordinary-mathematics reconstruction derives a pointwise prime-mass and finite-set-density premise for every real `X≥X_res`, where

$
I=\frac{1427}{120030000}\frac{1431!\,2567!}{3999!},\qquad
L_0=\frac{369}{200}2^{2567},\qquad
X_{\rm res}=\max\left(4001,\frac{15L_0}{2I}\right).
$

An 80-digit Decimal log-factorial calculation gives `log10(I)≈−1139.0970383684459743`, `log10(L₀)≈773.0099952399348073`, and `log10(15L₀/(2I))≈1912.9820948717724816`. Thus `X_res≈9.59610236×10^1912`; the analytic term dominates 4001. A separate `math.lgamma` calculation agrees on `log10(I)` within about `1.2×10^-12`.

This `X_res` is derived in the 26 October bounded ordinary-mathematics/source-replay update from pinned analytic identities and explicit error bounds. It is not a literal Lean constant or a Lean-certified effective cutoff. The pinned Lean declarations retain their existential/limit form; see the [mass and conditional Main update](source-audit-update-20261026-mass-main.md) for the derivation and its exact evidence ceiling.

## Lower scale of the prescribed finite window

The fixed-tuple caller map uses

$
r=\frac{I^2}{768\cdot160000\cdot10500000\cdot10^{240}\log 4},\quad
H(D)=\log(\operatorname{card}(\operatorname{latticeBall}(D))),\quad
W_*(D)=\left\lceil\max\left(0,\frac{H(D)+1}{r}\right)\right\rceil^+ +1.
$

The pinned [`WalkGeometry.lean` definition](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/GaussianMoat/WalkGeometry.lean#L429-L433) identifies `latticeBall(D)` with Gaussian integers whose complex norm is at most `D`. For every `D≥1`, it contains the five distinct points `0, ±1, ±i`; therefore `H(D)≥log 5`. It follows that

$
W_*(D)\ge\left\lceil\frac{\log 5+1}{r}\right\rceil^+ +1.
$

The positive argument has `log10((log 5+1)/r)≈2533.8631496633029212`, or a scale of about `7.29708934×10^2533`. The prescribed window width is therefore at least 2,534 decimal digits, even before evaluating the other components of the common Main onset.

## Review and limits

An independent AI challenge recomputed the factorial-based scales and checked the logarithm bases, Gaussian-ball lower bound, ceiling implication and claim limits. It found no arithmetic error. The challenge treated the item379 pointwise cutoff as an assumed premise and did not re-review that derivation; that separate derivation has its own bounded independent review, recorded in the 26 October update. Reviewer serving telemetry is unavailable. No independent human or specialist review is claimed.

This quantifies the scale of one explicit sufficient fixed-tuple construction. It does not show the bounds are sharp, refute the theorem, establish universal practical impossibility, or exclude another proof. The full `M_all`, `R_s` and `M_*` remain symbolic; no selector, executable `COST`/`BATCH`, alternative Main lemma, Lean/build, cache/kernel assurance or theorem-wide result is established.
