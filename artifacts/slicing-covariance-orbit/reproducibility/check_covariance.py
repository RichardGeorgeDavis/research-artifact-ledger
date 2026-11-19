"""Own deterministic finite-map checks; synthetic, not a GR/NR solver.

Run: python3 -B artifacts/slicing-covariance-orbit/reproducibility/check_covariance.py
No external dependencies, file writes, observed data or fitted QNM constants.
"""
import cmath
import json
import math


def close(a, b, tol=2e-12):
    assert abs(a - b) <= tol * max(1.0, abs(a), abs(b)), (a, b)


def vector(values):
    return [x for z in values for x in (z.real, z.imag)]


def projection(z, a):
    """Euclidean local unwrapped-log diagnostic; not a likelihood."""
    if not z or len(z) != len(a):
        raise ValueError("projection requires equally sized, non-empty vectors")
    zv, av = vector(z), vector(a)
    norm2 = sum(x * x for x in av)
    assert norm2 > 0
    d = sum(x * y for x, y in zip(zv, av)) / norm2
    residual = math.sqrt(sum((x - d * y) ** 2 for x, y in zip(zv, av)))
    return d, residual


def global_check(ratios, a):
    """Exact orbit criterion without complex-log phase branch choices.

    Requires nonzero ratios and a[0].real != 0; no noise threshold inferred.
    """
    if not ratios or len(ratios) != len(a):
        raise ValueError("global_check requires equally sized, non-empty vectors")
    assert all(abs(x) > 0 for x in ratios)
    assert a[0].real != 0
    d = math.log(abs(ratios[0])) / a[0].real
    residual = max(abs(r - cmath.exp(x * d)) for r, x in zip(ratios, a))
    return d, residual


def main():
    # Dimensionless synthetic frequencies, NOT Schwarzschild spectral values.
    # Slots correspond to the proposed two distinct direct-branch mode labels.
    c = 1.0
    omega = [0.4 - 0.1j, 0.7 - 0.15j]
    q = [-2j * c * w for w in omega]
    qm = [x.conjugate() for x in q]
    a = [-x for x in q]
    H = [1.1 + 0.3j, -0.7 + 0.2j]
    F = [0.5 - 0.2j, 0.8 + 0.1j]  # Synthetic nonzero transfer constants.
    O = [f * h for f, h in zip(F, H)]
    Hm = [h.conjugate() for h in H]
    Fm = [f.conjugate() for f in F]
    Om = [f * h for f, h in zip(Fm, Hm)]
    checks = []
    cases = [(0.0, 0.0), (0.2, 0.2), (-0.1, 0.3), (0.4, -0.2)]
    worst_field_error = 0.0
    for f0, f1 in cases:
        d = f1 - f0
        hh = [h * cmath.exp(x * f1) for h, x in zip(H, q)]
        oo = [o * cmath.exp(x * f0) for o, x in zip(O, q)]
        ff = [f * cmath.exp(x * d) for f, x in zip(F, a)]
        hmm = [h * cmath.exp(x * f1) for h, x in zip(Hm, qm)]
        omm = [o * cmath.exp(x * f0) for o, x in zip(Om, qm)]
        fmm = [f * cmath.exp(-x * d) for f, x in zip(Fm, qm)]
        for j in range(2):
            close(oo[j], ff[j] * hh[j])
            close(omm[j], fmm[j] * hmm[j])
            for tau_hat in [-0.4, 0.0, 1.0, 3.0]:
                for sigma in [0.0, 0.1, 0.5, 0.9, 1.0]:
                    # Smooth radial interpolation with endpoint-preserving bump.
                    f_sigma = f0 + (f1 - f0) * sigma + 0.07 * sigma * (1 - sigma)
                    # Match both boundary amplitudes: R(1)=1, R(0)=F.
                    # This interpolation is NOT a GR radial eigenfunction.
                    radial = F[j] + (1 - F[j]) * sigma + 0.2j * sigma * (1 - sigma)
                    old = H[j] * radial * cmath.exp(q[j] * (tau_hat + f_sigma + 1))
                    new = (H[j] * radial * cmath.exp(q[j] * f_sigma)
                           * cmath.exp(q[j] * (tau_hat + 1)))
                    old_mirror = (Hm[j] * radial.conjugate()
                                  * cmath.exp(qm[j] * (tau_hat + f_sigma + 1)))
                    new_mirror = (Hm[j] * radial.conjugate()
                                  * cmath.exp(qm[j] * f_sigma)
                                  * cmath.exp(qm[j] * (tau_hat + 1)))
                    close(old, new)
                    close(old_mirror, new_mirror)
                    if sigma == 1.0:
                        close(new, hh[j] * cmath.exp(q[j] * (tau_hat + 1)))
                        close(new_mirror, hmm[j] * cmath.exp(qm[j] * (tau_hat + 1)))
                    elif sigma == 0.0:
                        close(new, oo[j] * cmath.exp(q[j] * (tau_hat + 1)))
                        close(new_mirror, omm[j] * cmath.exp(qm[j] * (tau_hat + 1)))
                    worst_field_error = max(worst_field_error, abs(old - new))
                    worst_field_error = max(worst_field_error, abs(old_mirror - new_mirror))
        ratios = [oo[j] / (F[j] * hh[j]) for j in range(2)]
        d_global, res_global = global_check(ratios, a)
        close(d_global, d)
        close(res_global, 0)
        d_local, res_local = projection([cmath.log(r) for r in ratios], a)
        close(d_local, d)  # These small shifts remain on the selected log chart.
        close(res_local, 0)
    checks.append("direct and mirror covariance with synthetic field recovery: 4 cases, 160 points each")
    # Fixed endpoints permit an interior reparametrisation without amplitude change.
    close(cmath.exp(a[0] * 0), 1)
    checks.append("endpoint-fixed and common-shift transfer unchanged")
    d = 0.4
    factor = cmath.exp(a[0] * d)
    close(abs(factor), math.exp(2 * c * (-omega[0].imag) * d))
    assert abs(abs(factor) - 1) > 0.05
    checks.append("relative shift changes magnitude despite unchanged represented field")
    # Failure control: horizon coordinate changed while infinity/transfer frozen.
    bad_h = [h * cmath.exp(x * d) for h, x in zip(H, q)]
    bad_error = max(abs(O[j] - F[j] * bad_h[j]) for j in range(2))
    assert bad_error > 0.05
    checks.append("non-covariant one-sided update produces a false raw residual")
    # A changed synthetic map outside the one-real-parameter time orbit.
    ratios = [1.1 * cmath.exp(a[0] * d), cmath.exp(a[1] * d)]
    d_local, local_residual = projection([cmath.log(r) for r in ratios], a)
    d_global, global_residual = global_check(ratios, a)
    assert local_residual > 0.05 and global_residual > 0.1
    checks.append("mode-specific 10 percent map change survives declared time nuisance")
    # Principal complex logs fail outside a chart; the global criterion still works.
    large_d = 8.0
    large_ratios = [cmath.exp(x * large_d) for x in a]
    d_exact, global_large_residual = global_check(large_ratios, a)
    close(d_exact, large_d)
    close(global_large_residual, 0, 1e-10)
    _, false_local = projection([cmath.log(r) for r in large_ratios], a)
    assert false_local > 1
    checks.append("large-shift log-branch false positive avoided by global orbit criterion")
    # Waveform-only no-separator: arbitrary d is absorbed into unobserved H.
    for trial in [-3.0, 0.0, 2.0, 8.0]:
        inferred_h = [O[j] / (F[j] * cmath.exp(a[j] * trial)) for j in range(2)]
        for j in range(2):
            close(F[j] * cmath.exp(a[j] * trial) * inferred_h[j], O[j])
    checks.append("waveform-only family exactly fits all four arbitrary alignments")
    # Mirror branch uses conjugate time dependence, not the direct factor unchanged.
    for j in range(2):
        close(cmath.exp(-qm[j] * d), cmath.exp(a[j] * d).conjugate())
    checks.append("mirror sign/conjugation covariance")
    # Refuse mismatched or empty vectors rather than silently truncating zip.
    for operation, args in [
        (projection, ([1 + 1j], [1 + 1j, 2 + 2j])),
        (global_check, ([1 + 1j], [1 + 1j, 2 + 2j])),
        (projection, ([], [])),
        (global_check, ([], [])),
    ]:
        try:
            operation(*args)
        except ValueError:
            pass
        else:
            raise AssertionError(f"{operation.__name__} accepted invalid vector shape")
    checks.append("projection/orbit helpers reject mismatched and empty vector shapes")
    # P=a a^T/(a^T a): rank one, complementary projection rank three.
    av = vector(a)
    norm2 = sum(x*x for x in av)
    P = [[x*y/norm2 for y in av] for x in av]
    for i in range(4):
        for j in range(4):
            close(sum(P[i][k] * P[k][j] for k in range(4)), P[i][j])
    close(sum(P[i][i] for i in range(4)), 1)
    checks.append("real nuisance projector idempotent, trace 1; quotient dimension 3")
    print(json.dumps({"status": "PASS", "synthetic_only": True,
                      "checks": checks, "worst_field_error": worst_field_error,
                      "relative_shift_magnitude_factor": abs(factor),
                      "one_sided_raw_residual": bad_error,
                      "map_change_local_residual": local_residual,
                      "map_change_global_residual": global_residual,
                      "large_shift_principal_log_false_residual": false_local}, indent=2))


if __name__ == "__main__":
    main()
