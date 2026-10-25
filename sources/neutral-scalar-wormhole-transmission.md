# Source map: neutral-scalar wormhole transmission

This map supports [*A half-area cross-section is not a generic transmission probability*](../artifacts/neutral-scalar-wormhole-transmission/README.md). The source review is bounded to two version-pinned primary papers and makes no empirical, universal-traversability, novelty or priority claim.

## Source identities and read scope

| ID | Source and version | Exact locators read | Claim role | Relationship and limit |
|---|---|---|---|---|
| S1 | Maldacena, Milekhin and Popov, [arXiv:1807.04726v3](https://arxiv.org/abs/1807.04726v3), 2020-11-03; [v2](https://arxiv.org/abs/1807.04726v2) compared | §5.3.2, Eqs. (5.31)–(5.42) | C1: scalar ODE and symmetry; C2: asymptotic matching of length and binding energy | Version comparison is limited to the displayed equations used by this derivation. The full §5.5 validity regime and all background-stability conditions were not audited. |
| S2 | Freivogel, Fumagalli and Tomašević, [arXiv:2606.12528v2](https://arxiv.org/abs/2606.12528v2), 2026-09-14 | §§2–3, Eqs. (3.1)–(3.54) | C3: cross-section setup; C4: fixed-frequency resonance and off-resonance behaviour; C5: period average and all-time packet integral; C6: finite-time packet result | Source-reported theory for neutral massless scalar s-wave scattering under the paper's boundary conditions and approximations. No computation was reproduced. |

Accessed and inspected for the stated locators on 2026-10-25. Versioned arXiv records are linked; no PDF or figure is republished.

## Claim-to-source map

| Claim | Evidence and derivation | Evidence status | Limit |
|---|---|---|---|
| C1 — the displayed MMP scalar solution satisfies Eq. (5.36) | S1 Eq. (5.36) gives `ρφ′ − φ = −α/(1+ρ²)` and Eq. (5.37) gives `φ = α(1+ρ arctanρ)`. Differentiate: `φ′ = α(arctanρ + ρ/(1+ρ²))`; substitution yields `α(ρ²/(1+ρ²) − 1) = −α/(1+ρ²)`. The homogeneous solution is `Cρ`; the even `Z₂` solution imposes `C=0`. | Coordinator algebra; independently source-challenged. | Verifies this equation chain, not the full geometry or model. |
| C2 — the matched length and energy agree with Eq. (5.31) | S1 Eqs. (5.39)–(5.40): `φ∼παρ/2` and `2(r−r_e)/r_e∼φ` give `r−r_e∼πα r_eρ/4`, so `ℓ=4r_e/(πα)`. With `α=qG_N/(4πr_e²)`, `ℓ=16r_e³/(qG_N)`. The constant term in Eqs. (5.41)–(5.42) gives `E_min=−G_Nq²/(256r_e³)`. | Coordinator derivation; independently source-challenged. | Asymptotic match in the paper's stated coordinate/parameter regime; not an exact finite-`ρ` identity. |
| C3 — the 2026 paper's cross-section is conditional on a defined near-mouth incoming current | S2 Eq. (3.1) and surrounding text define transmitted particle number relative to current from flux sent near one mouth; bypassing particles and ambient-reflected paths are excluded. | Source reading. | A cross-section has area units and is not itself the dimensionless traversal probability for an arbitrary incident particle. |
| C4 — fixed-frequency results differ by resonance | S2 Eqs. (3.18)–(3.23): `|T|²=1` at exact `ω=n/ℓ` resonances; low-frequency off-resonance conditions with `sin²(πℓω)=O(1)` yield near-total reflection and suppressed cross-section. | Source reading and direct scaling check. | The off-resonance expression is a scaling statement with an order-one detuning factor, not an exact equality at every frequency. |
| C5 — the period-averaged and all-time packet results each yield `A/2` | S2 Eqs. (3.24)–(3.27) average cross-section over one frequency oscillation period; Eqs. (3.45)–(3.47) separately integrate a packet over all time and interpret half the trapped signal as eventually exiting the other mouth. | Source reading. | Equal values do not make these observables identical to a fixed-frequency probability or a short-time signal. All-time accumulation is not rapid delivery. |
| C6 — finite-time transmission remains separately suppressed | S2 Eqs. (3.48)–(3.54) define a finite-time packet quantity distinct from a standard asymptotic cross-section; the paper reports no early through-signal and first-arrival suppression by `4ω₀²r_e²≪1` relative to horizon-area scale. | Source reading. | Applies to the paper's stated setup/approximations; not measured transmission. |

## Independent challenge

An independent AI source-only challenge, requested setting `gpt-5.6-luna / low` (serving telemetry unavailable), confirmed C1, C2 and the C3–C6 distinction at the packet's bounded source scope. It noted that the MMP match is asymptotic and coordinate/parameter dependent. It did not independently review the full papers, reproduce a scattering calculation, inspect an experiment, or provide human specialist review.

## Reopening condition

Reopen this source map if a material source-version change, correction, or contrary equation reading affects S1 or S2; if the receiving claim expands beyond neutral massless scalar s-wave transmission; or if an empirical/physical claim is proposed. Then pin the changed source, trace affected claims and outputs, and use the separate evidence/authority required for the expanded scope.
