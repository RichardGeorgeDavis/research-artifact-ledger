# A half-area cross-section is not a generic transmission probability

Status: `source review`

Version: `0.1.0`

Last updated: 2026-10-25

Artifact author: Richard George Davis

Underlying source authors: Juan Maldacena, Alexey Milekhin and Fedor Popov; Ben Freivogel, Benjo Fumagalli and Anja Tomašević. This note interprets selected equations from their papers; it does not claim authorship of their models or results.

AI-assisted source analysis and an independent AI source-only challenge were used. The challenge checked the listed equation chain and observable distinction; it was not peer review or a human specialist review. No independent human review is claimed.

## Question and intended use

Does a reported half-horizon-area (`A/2`) neutral-scalar transmission cross-section show that particles generically pass through a four-dimensional traversable wormhole with high probability or in a short time?

This note is for readers comparing the frequency-averaged and wave-packet results with fixed-frequency transmission and finite-time signal delivery.

## Claim supported

In the cited theoretical neutral massless scalar s-wave setup, exact resonances have unit transmission, generic low-frequency off-resonance transmission is suppressed, and the paper's period-averaged and all-time packet-integrated cross-sections are different observables from a fixed-frequency transmission probability and a finite-time delivered signal. Therefore `A/2` does not establish generic high-probability or rapid traversal. The first expected finite-time arrival is suppressed relative to the horizon-area scale by `4 ω₀² r_e² ≪ 1` under the paper's stated regime.

This is a bounded interpretation of two theoretical papers, not a new wormhole model, an experimental result, or evidence about a physical wormhole.

## Evidence class and review status

The evidence class is `source review`, supported by an explicit algebraic check of the geometry matching and a source-to-claim comparison of the scattering observables. The work was performed after an initial coordinator read; it was not blind or preregistered.

A separate AI reviewer checked the public source packet and confirmed the ODE solution, symmetry restriction, asymptotic length and energy matching, and the distinctions among resonant, off-resonant, averaged, all-time and finite-time quantities. The requested reviewer setting was `gpt-5.6-luna / low`; actual serving telemetry was unavailable. The reviewer did not inspect a physical system, rerun a scattering simulation, or perform peer review.

## Method and source checks

For Maldacena, Milekhin and Popov (MMP), differentiating `φ = α(1 + ρ arctan ρ)` gives `ρφ′ − φ = −α/(1 + ρ²)`, matching Eq. (5.36). The homogeneous solution is `Cρ`; the paper's even `Z₂` solution sets `C = 0`. At large positive `ρ`, `φ ∼ παρ/2`; combining this with Eq. (5.39) gives `r − r_e ∼ πα r_eρ/4`. Substitution into Eq. (5.40) yields `ℓ = 4r_e/(πα)`. With `α = qG_N/(4πr_e²)`, this agrees with `ℓ = 16r_e³/(qG_N)` in Eq. (5.31). Matching the constant term in Eqs. (5.41)–(5.42) likewise yields `E_min = −G_Nq²/(256r_e³)`, as in Eq. (5.31). This is asymptotic matching in the paper's stated coordinate and parameter regime, not an exact finite-`ρ` identity.

For the 2026 scattering paper, Eq. (3.1) defines a cross-section from transmitted particle number relative to incoming current, with incoming flux sent near one mouth. It excludes bypassing particles and reflected particles that travel through ambient space. A cross-section is an area; it is not itself a dimensionless probability that an arbitrary incident particle traverses the throat.

At fixed frequency, Eqs. (3.18)–(3.23) give unit transmission at exact resonances `ω = n/ℓ`; away from resonance at low frequency they give almost total reflection. The suppressed off-resonance cross-section is a scaling statement with an order-one detuning factor, not an exact equality for every frequency. Equations (3.24)–(3.27) average the cross-section over one oscillation period in frequency and obtain `A/2`. Equations (3.45)–(3.47) separately integrate a wave packet over all time and obtain the same cross-section value, interpreting it as half the trapped signal eventually exiting the other mouth after sufficiently long waiting. Equations (3.48)–(3.54) define a finite-time packet quantity separately: there is no through-signal at the early short timescale, and the first expected arrival is suppressed by `4ω₀²r_e² ≪ 1` relative to the horizon-area scale.

The full claim-to-source map is in [`sources/neutral-scalar-wormhole-transmission.md`](../../sources/neutral-scalar-wormhole-transmission.md).

## Result and contribution

The equations support a probe-, frequency- and time-dependent transmission picture. The `A/2` values are valid within their stated average or all-time definitions; they do not turn into a generic fixed-frequency probability or a rapid-delivery guarantee. Exact resonances and later accumulated leakage remain part of the same source account, so the conclusion is not that transmission never occurs.

The public contribution is a compact, checked map from the source's frequency-averaged and all-time quantities to its separate fixed-frequency and finite-time results. The underlying papers already report these results. No field-level novelty or priority claim is made, and no systematic novelty search was performed.

## Authorship, chronology and prior work

This artifact is authored by Richard George Davis with AI-assisted source analysis and writing. The underlying wormhole geometry and scalar-scattering claims belong to the authors of the cited papers; the AI reviewer is not a co-author or human specialist. The note's contribution is a bounded source map and interpretation of already published equations, not a new theorem or field result.

| Event | Date | Evidence | What the date establishes |
|---|---|---|---|
| MMP version checked | 2020-11-03 | arXiv:1807.04726v3 record | Date of the version used for the stated source check. |
| Scattering paper version checked | 2026-09-14 | arXiv:2606.12528v2 record | Date of the version used for the stated source check. |
| Coordinator source review | 2026-10-25 | Bounded source audit and derivation described in this artifact | Date of this documented review, not necessarily the first private mention. |
| Independent AI source challenge | 2026-10-25 | Challenge of the listed public-source packet | Date and scope of the AI challenge; not human review or peer review. |
| First appearance of this artifact in the Ledger | See [file history](https://github.com/RichardGeorgeDavis/research-artifact-ledger/commits/main/artifacts/neutral-scalar-wormhole-transmission/README.md) | The public commit that adds this file | Repository chronology only; not first conception, originality or priority. |

The 2018 and 2026 papers predate this note and report the underlying geometry and scattering results. This note does not make a novelty or priority claim and does not perform an exhaustive prior-art search.

## Limitations and unresolved issues

- The conclusion applies only to the cited neutral massless scalar s-wave setup and the equations' stated approximations and boundary conditions.
- The MMP matching check is asymptotic and coordinate/parameter dependent; this note does not audit the paper's full §5.5 validity analysis or all background stability conditions.
- The finite-time factor and resonant/off-resonant limits are source-reported; no numerical scattering calculation was reproduced here.
- The separate charged-fermion claim is outside scope. No claim about all probes, all wormhole models, physical realizability, empirical transmission, or a universal traversability property follows.
- This is a two-source source review, not an exhaustive literature or priority search. It does not independently establish the truth of the papers' theoretical assumptions.
- No third-party PDF, figure, dataset or extended passage is redistributed. The note paraphrases the source argument and links to versioned papers.

## Sources and provenance

| Source | Version/date | Role | Locators | Access and rights |
|---|---|---|---|---|
| [Maldacena, Milekhin and Popov, *Traversable wormholes in four dimensions*](https://arxiv.org/abs/1807.04726v3) | arXiv:1807.04726v3, 2020-11-03; compared with v2 | Wormhole geometry, scalar solution and matching | §5.3.2, Eqs. (5.31)–(5.42); v2 comparison | Public arXiv versioned source; linked, not redistributed. |
| [Freivogel, Fumagalli and Tomašević, *How traversable is a traversable wormhole?*](https://arxiv.org/abs/2606.12528v2) | arXiv:2606.12528v2, 2026-09-14 | Neutral massless scalar s-wave cross-section and finite-time packet results | §§2–3, Eqs. (3.1)–(3.54) | Public arXiv versioned source; linked, not redistributed. |

The full source-to-claim locators and read scope are recorded in [`sources/neutral-scalar-wormhole-transmission.md`](../../sources/neutral-scalar-wormhole-transmission.md). A public commit dates this note's appearance in this repository only; it does not establish first conception, originality or priority.

## Independent review

Reviewer: independent AI source-only challenge, requested setting `gpt-5.6-luna / low`; serving telemetry was unavailable. Date: 2026-10-25.

Scope: MMP ODE solution, symmetry-selected homogeneous term, asymptotic length/energy matching, and whether the `A/2` average/all-time values support generic rapid or high-probability neutral-scalar transmission.

Finding: no concrete mismatch was identified in that scope. The challenge qualified the geometry match as asymptotic and dependent on the source's coordinate and parameter regime. It did not certify the full MMP validity conditions, reproduce scattering calculations, or provide human specialist or peer review.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.0 / 2026-10-25 | Initial source-review artifact | Two version-pinned primary sources; coordinator derivation and bounded independent AI source challenge. |
