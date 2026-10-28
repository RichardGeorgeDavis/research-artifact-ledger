# A synthetic angular-scattering comparison for two sheet-response models

**Status:** `synthetic demonstration` and `bounded derivation`
**Version:** `0.1.1`
**Prepared:** 2026-10-28
**Author:** Richard George Davis
**AI assistance:** AI assisted the model formulation, derivation, calculation script and drafting; a separate AI reviewer checked the derivation and finite results.

## Question and intended use

At one fixed frequency \(\omega_0\), can a declared TE plane-wave model with an even, bounded, wavevector-dependent sheet admittance produce a different finite scattering table from a constant-admittance local-sheet comparator that agrees with it at normal incidence? This example is intended for readers inspecting model-conditional optical discriminators and their limits.

## Claim supported

For the selected dimensionless sheet response and the four stated angles, the complex reflection and transmission amplitudes agree at normal incidence by construction and differ at the three sampled oblique angles from the named angle-independent local-sheet comparator. Both declared models have a reciprocal symmetric two-port scattering matrix and satisfy the stated passivity checks over this finite table.

This is a synthetic calculation with coefficients selected during AI-assisted work solely to define the example. It is not a material measurement, fitted model, physical demonstration, unique identification of nonlocality, new theorem, or field-novelty claim.

## Model and derivation

Use identical vacuum ports, TE polarisation and the \(e^{-i\omega t}\) convention at one fixed frequency \(\omega_0\). Let \(\kappa=k_{\parallel}/k_0=\sin\theta\), restrict \(|\kappa|\leq\sqrt{3}/2\), and normalise the TE port admittance to \(y_p=\cos\theta=\sqrt{1-\kappa^2}\).

The selected wavevector-dependent response and comparator are

\[
y_s^{\mathrm{NL}}(\kappa)=\frac15+\frac{3}{10}\frac{\kappa^2}{1+\kappa^2}+\frac{i}{10},
\qquad y_s^{\mathrm{L}}=\frac15+\frac{i}{10}.
\]

The coefficients are fixed for all four angles and were not fitted to the outputs; they were selected during AI-assisted work solely to define this example. Let the incident electric-field amplitude be one, with reflection amplitude \(r\) and transmission amplitude \(t\). Tangential-field continuity gives \(t=1+r\); the sheet-current boundary condition is \(y_p(1-r)-y_pt=y_st\). Solving these two conditions gives the amplitudes

\[
r=-\frac{y_s}{2y_p+y_s},\qquad t=\frac{2y_p}{2y_p+y_s}.
\]

For these identical ports and the selected scalar response, the two-sided scattering matrix is \(S=\begin{pmatrix}r&t\\t&r\end{pmatrix}\). For \(y_s=g+ib\), set \(D=(2y_p+g)^2+b^2\); then \(R=(g^2+b^2)/D\), \(T=4y_p^2/D\), and \(A=4y_pg/D\). The symmetric and antisymmetric channel eigenvalues are \((2y_p-y_s)/(2y_p+y_s)\) and \(-1\), respectively. This symmetry follows from the selected scalar response and identical-port setup; it is not a general same-wavevector reciprocity statement for nonlocal interfaces. The accompanying script checks the identities and passivity for all eight model-angle entries to a tolerance of \(10^{-14}\).

## Finite results

| \(\theta\) | \(\kappa^2\) | Local \(r\) | Local \(t\) | Local \(A\) | Wavevector-dependent \(r\) | Wavevector-dependent \(t\) | Wavevector-dependent \(A\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0° | 0 | −0.092784−0.041237i | 0.907216−0.041237i | 0.164948 | −0.092784−0.041237i | 0.907216−0.041237i | 0.164948 |
| 30° | 0.25 | −0.105912−0.046277i | 0.894088−0.046277i | 0.185106 | −0.132704−0.043538i | 0.867296−0.043538i | 0.226397 |
| 45° | 0.5 | −0.127249−0.054067i | 0.872751−0.054067i | 0.216267 | −0.177805−0.047963i | 0.822195−0.047963i | 0.287780 |
| 60° | 0.75 | −0.172414−0.068966i | 0.827586−0.068966i | 0.275862 | −0.251552−0.056335i | 0.748448−0.056335i | 0.370200 |

The result distinguishes the selected response from this constant-admittance comparator at the three listed oblique angles. It does not show that the response is unique: a conventional multilayer, patterned resonator or another calibrated local-structure family could reproduce the same finite table. Absorption variation alone is not a nonlocality test because the local comparator also changes with angle through \(y_p\).

## Reproduction

From the repository root, run:

```sh
python3 reproduce/nonlocal-sheet-angular-toy/reproduce.py
```

The script uses only the Python standard library and requires Python 3.9 or later. It prints the four rows above and checks continuity, nonnegative absorption, \(R+T+A=1\), two-port passivity, normal-incidence agreement and oblique complex-amplitude separation. It does not model a material or establish a causal broadband constitutive law.

## Sources, provenance and prior work

The equations are derived here from the explicitly stated plane-wave and sheet-current boundary conditions. Spatially dispersive metasurfaces and their model-specific reciprocity relations are established background; for example, Pfeiffer and Grbic discuss how the reciprocal relation for their spatially dispersive metasurface connects opposite transverse wavevectors. Their paper does not validate this toy model or imply a universal same-angle symmetric scattering matrix: [Pfeiffer and Grbic, *Physical Review Letters* 117, 077401 (2016)](https://doi.org/10.1103/PhysRevLett.117.077401).

The response coefficients and finite comparison were selected during AI-assisted work solely to define this toy example. No systematic prior-art or novelty search was performed, and no priority claim is made. The first retained private record is dated 2026-10-22; that date does not establish first conception or priority.

## Review status and limitations

AI assistance was used for model formulation, derivation, code and prose. A separately dispatched AI mathematical reviewer independently derived the amplitudes, reproduced the table and absorption differences, and checked passivity for simultaneous two-port inputs on 2026-10-22. This was not a proof-assistant check, independent human specialist review, physical review or peer review. The script was run during the original private verification; this public copy is the same standard-library calculation. No new run is claimed here.

A physical discriminator would require a named material and geometry, a frequency-dependent constitutive law, appropriate reciprocal/passive/causal conditions, calibration of the permitted ordinary alternatives, uncertainty limits and frozen held-out angle/frequency measurements. None is supplied. No experiment or material selection is authorised by this artifact.

## Change history

| Version/date | Change | Reason and evidence |
|---|---|---|
| 0.1.1 / 2026-10-28 | Corrected the attribution of model selection | The coefficients were selected during AI-assisted work; no numerical result or derivation changed. |
| 0.1.0 / 2026-10-28 | Initial public record of F36-T1 | Private finite derivation and independent mathematical challenge dated 2026-10-22; no physical or novelty claim. |

This artifact has no open licence. Public visibility does not grant broader reuse permission.
