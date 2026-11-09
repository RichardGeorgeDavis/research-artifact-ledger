# A prime-log phase orbit has the full worst-case phase-cloning domain

Status: bounded derivation

Version: 0.1.0

Last updated: 2026-11-10

Author: Richard George Davis

## Question and intended use

Does encoding a finite set of distinct primes into one real-parameter family of equal-amplitude quantum states reduce worst-case approximate-cloning difficulty because the encoding uses only one scalar parameter?

This artifact answers the question for a constructed finite-dimensional state family and deterministic channels evaluated by global fidelity.

## Claim supported

For any fixed finite set of d ≥ 2 distinct primes p₀,…,p₍d−1₎, the states

    |ψ(t)⟩ = d⁻¹ᐟ² Σⱼ exp(i t log pⱼ)|j⟩,  t ∈ ℝ,

are dense, up to global phase, in the full family of equal-amplitude d-dimensional phase states.

For fixed positive integers N and K and every deterministic CPTP channel C from N copies to N+K copies, the infimum of its squared global fidelity over this prime-log orbit equals its minimum over the full phase-state family. Optimising over the same channel class preserves that equality. Thus this encoding has no all-time worst-case fidelity advantage over the full phase family merely because it has one real parameter.

This is a bounded mathematical deduction, not a prime predictor, finite-window guarantee, physical prime-spectrum claim, new quantum mechanism or literature-priority claim.

## Evidence class and review status

This is a self-contained bounded derivation. An independent high-effort model review checked the unique-factorisation argument, continuous-time density criterion, fidelity continuity, optimisation step and finite-window limitations. It found the deduction valid at the stated scope. This is not human specialist review, peer review or formal verification.

## Sources and provenance

| Source or input | Version/date | Role | Relevant scope |
|---|---|---|---|
| Herasymenko, Lin, Verduyn Lunel and Grinko, [Approximate cloning of structured pure states](https://arxiv.org/abs/2610.06723) | arXiv:2610.06723v1, 2026-10-05 | Defines equal-amplitude phase states and proves a worst-case global-fidelity-optimal cloner for that family | Eq. 10 and Theorem X.1; their phase-state result does not claim trace-distance optimality |
| Unique prime factorisation | Standard arithmetic fact | Establishes integer independence of relative prime-log frequencies | Elementary derivation restated below |

The source paper is authored by its listed researchers. The constructed encoding and deduction here are attributed to Richard George Davis. No priority or field-level novelty claim is made.

## Method and derivation

Remove the global factor exp(i t log p₀), which does not change a quantum state. The remaining relative phases are θⱼ(t)=tωⱼ mod 2π, with ωⱼ=log(pⱼ/p₀) for 1≤j<d.

Suppose an integer vector m∈ℤ^(d−1) satisfies m·ω=0. Exponentiating gives
Πⱼ₌₁ᵈ⁻¹ pⱼ^mⱼ · p₀^(−Σmⱼ)=1.
Move negative powers to the opposite side. Unique prime factorisation forces every mⱼ=0. Thus there is no nonzero integer relation among the relative frequencies.

For each nonzero integer vector m, the torus-character time average is
(1/T)∫₀ᵀ exp(i t(m·ω))dt = (exp(iT(m·ω))−1)/(iT(m·ω)) → 0.
The zero character has average one. Finite sums of characters therefore have time averages converging to their uniform torus averages; uniform approximation extends this to every continuous function on the torus. If the trajectory missed a nonempty open subset, a nonnegative continuous function supported there with positive torus average would contradict that convergence. Hence the trajectory for t≥0, and therefore for t∈ℝ, is dense in the relative-phase torus.

For a fixed deterministic CPTP channel C, let ρθ=|φ(θ)⟩⟨φ(θ)| and define the squared global fidelity in the squared-Uhlmann convention used in the cited paper by

    |φ(θ)⟩ = d⁻¹ᐟ²(|0⟩ + Σⱼ₌₁ᵈ⁻¹ exp(iθⱼ)|j⟩),  θ ∈ 𝕋ᵈ⁻¹.
    F_C(θ) = Tr[ρθ^(⊗(N+K)) C(ρθ^(⊗N))].

This is continuous on the compact torus. Density gives
infₜ∈ℝ F_C(θ(t)) = min_θ∈𝕋ᵈ⁻¹ F_C(θ).
The infimum on the orbit need not be attained at a finite t. Since this equality holds for every fixed channel, it remains true after optimising over the same admissible channel class.

The cited paper proves a channel optimal for the full phase family in worst-case global fidelity, so that optimum carries over to this dense orbit. Its phase-state result does not establish a trace-distance optimum; this artifact makes no such claim.

## Results

The one-parameter prime-log family has the full phase torus as its closure. Its all-real-time worst-case global-fidelity cloning problem is therefore exactly the full phase-family problem. A scalar parameter count alone does not imply a reduced worst-case family dimension.

For d=1 the state family is a singleton. For d=2 the relative phase covers the circle periodically; any interval at least 2π/|log(p₁/p₀)| long covers the full relative-phase circle. For d≥3 the entire real-time image is a proper dense subset of the torus; every bounded time segment is a compact smooth curve and cannot fill it.

For d≥3, properness also follows because the real-time image is a countable union of bounded smooth curve segments, each of zero (d−1)-dimensional Haar measure; it cannot equal the positive-measure torus.

## Limitations and unresolved issues

The density argument alone gives no equality for a prescribed bounded time interval and no quantitative convergence rate. A finite-window cloning study must specify its interval, primes, channel class and fidelity criterion. If the question instead concerns recurrence or sidelobe statistics, define those outcomes separately and compare with matched frequency controls.

The conclusion assumes a fixed deterministic channel that receives no classical label revealing t. It concerns global fidelity for the joint output, not single-copy or marginal fidelity. Conditional postselection at zero success probability would require a separate model. The same density argument applies to any continuous phase-invariant score, but no numerical trace-distance optimum is imported.

This construction does not predict primes, show that prime logarithms are physically encoded in a quantum system, explain prime occurrence, establish a connection to cosmology, or imply that prime prediction is impossible. The result depends only on rational independence of the relative frequencies and is not unique to primes.

No literature-priority claim is made. A bounded web search for related phrases is not an exhaustive prior-art review.

## Independent review

Reviewer and date: independent high-effort model review, 2026-11-10.

Scope: arithmetic independence of the relative log frequencies; continuous-time torus density; continuity and the infimum/minimum equality for fixed channels; optimisation over the same channel class; finite-window and score limitations.

Findings: no mismatch found in the stated derivation. The reviewer distinguished continuous time from the discrete-time Kronecker condition, noted that the all-time infimum need not be attained, and confirmed that the result gives no prime-prediction claim. No human specialist review is claimed.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-11-10 | Initial public bounded derivation | Independent model challenge found the deduction valid at its stated mathematical scope; no finite-window calculation or human review is claimed |
