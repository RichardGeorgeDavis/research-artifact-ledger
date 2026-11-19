# Source map — finite slicing-covariance orbit test

This source map supports the author-created finite derivation and synthetic verifier in [`artifacts/slicing-covariance-orbit/README.md`](../artifacts/slicing-covariance-orbit/README.md). The cited paper supplies the slicing convention and perturbative transfer relation, not the quotient test, synthetic inputs or their outputs.

## Primary source

Ariadna Ribes Metidieri, Béatrice Bonga and Badri Krishnan, [“Black Hole Tomography: Unveiling Black Hole Ringdown via Gravitational Wave Observations”](https://arxiv.org/abs/2501.08964v2), arXiv:2501.08964v2, 21 January 2025.

| Locator | Source statement used | Bounded role and limit |
|---|---|---|
| Eq. (13), printed p. 6 | `c=1/(2κ)=R₀=2M` for the Schwarzschild background | Sets the geometrical length scale; does not supply the synthetic frequencies. |
| Eqs. (132), (142), printed pp. 24–26 | Hyperboloidal coordinates and a real regular slicing function with finite endpoint values | Supports `d=f(1)-f(0)` as the endpoint difference in the stated coordinate family; does not prove arbitrary functions define admissible spacelike foliations. |
| Eqs. (136)–(140), printed p. 25 | Horizon and null-infinity `Ψ̃₄` coefficients, leading rescaled infinity coefficient, and relation to other Weyl amplitudes | Supports the matched coefficient convention; a horizon `Ψ₀` or detector strain requires a separate conversion. |
| Eqs. (143)–(145), printed pp. 25–26 | Direct and mirror boundary factors and the slicing-dependent transfer change | Direct transfer factor is `exp(2icωd)`; mirror factor is `exp(-2ic\bar{ω}d)`. The paper does not state the exact-orbit test or local log diagnostic. |
| Discussion after Eq. (145), printed p. 26 | Different slicings connect different horizon and infinity cross-sections | Supports the stated interpretation boundary; no detector or empirical conclusion follows. |

## Author-created derivation and controls

The mode ratio, shared real nuisance parameter, magnitude-based unique candidate, direct substitution criterion, local log projection, and output-only inversion are derived in the artifact README. Synthetic frequencies, coefficients, `d=8` branch-cut example, perturbation control and output-only fits come from the included standard-library script. These are not paper outputs, evaluated QNM values, observational results or calibrated quantities.

## Review

An independent AI source-and-arithmetic challenge on 19 November 2026 checked equation signs, units, coefficient conventions, exact-orbit assumptions and synthetic outputs. It identified that the direct-branch exponent and shifted versus baseline data must be labelled explicitly; the artifact follows those corrections. No human scientist review, physical-data check, full paper audit, novelty search or priority claim is made.
