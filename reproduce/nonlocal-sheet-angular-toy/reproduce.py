#!/usr/bin/env python3
"""Reproduce the declared finite F36-T1 angular-scattering toy table."""

from math import cos, radians, sin


ANGLES_DEG = (0, 30, 45, 60)


def amplitudes(theta_deg: int, spatially_dispersive: bool) -> tuple[complex, complex, float, float, float]:
    theta = radians(theta_deg)
    kappa = sin(theta)
    y_port = cos(theta)  # TE wave admittance, normalised to vacuum admittance.
    y_sheet = 0.2 + 0.1j
    if spatially_dispersive:
        y_sheet += 0.3 * kappa**2 / (1.0 + kappa**2)

    denominator = 2.0 * y_port + y_sheet
    reflection = -y_sheet / denominator
    transmission = 2.0 * y_port / denominator
    reflectance = abs(reflection) ** 2
    transmittance = abs(transmission) ** 2
    absorption = 4.0 * y_port * y_sheet.real / abs(denominator) ** 2
    return reflection, transmission, reflectance, transmittance, absorption


def check_two_port_passivity(reflection: complex, transmission: complex, y_port: float, y_sheet: complex) -> None:
    """Check S†S <= I using the two symmetric-channel eigenvalues."""
    denominator = 2.0 * y_port + y_sheet
    lambda_symmetric = reflection + transmission
    lambda_antisymmetric = reflection - transmission
    expected_symmetric = (2.0 * y_port - y_sheet) / denominator
    assert abs(lambda_symmetric - expected_symmetric) < 1e-14
    assert abs(lambda_antisymmetric + 1.0) < 1e-14
    assert abs((1.0 - abs(lambda_symmetric) ** 2) - 8.0 * y_port * y_sheet.real / abs(denominator) ** 2) < 1e-14
    assert abs(lambda_symmetric) <= 1.0 + 1e-14
    assert abs(lambda_antisymmetric) <= 1.0 + 1e-14


def main() -> None:
    for angle in ANGLES_DEG:
        kappa2 = sin(radians(angle)) ** 2
        local = amplitudes(angle, spatially_dispersive=False)
        spatial = amplitudes(angle, spatially_dispersive=True)
        for response in (local, spatial):
            reflection, transmission, reflectance, transmittance, absorption = response
            assert abs(transmission - (1.0 + reflection)) < 1e-14
            assert absorption >= 0.0
            assert abs(reflectance + transmittance + absorption - 1.0) < 1e-14
        for model_is_spatially_dispersive, response in ((False, local), (True, spatial)):
            reflection, transmission, *_ = response
            theta = radians(angle)
            y_port = cos(theta)
            kappa2 = sin(theta) ** 2
            y_sheet = 0.2 + 0.1j
            if model_is_spatially_dispersive:
                y_sheet += 0.3 * kappa2 / (1.0 + kappa2)
            check_two_port_passivity(reflection, transmission, y_port, y_sheet)
        if angle == 0:
            assert abs(local[0] - spatial[0]) < 1e-14
            assert abs(local[1] - spatial[1]) < 1e-14
        else:
            assert abs(local[0] - spatial[0]) + abs(local[1] - spatial[1]) > 1e-3

        print(
            f"{angle:2d}  {kappa2:.6f}  "
            f"{local[0].real:+.6f}{local[0].imag:+.6f}i  "
            f"{local[1].real:+.6f}{local[1].imag:+.6f}i  {local[4]:.6f}  "
            f"{spatial[0].real:+.6f}{spatial[0].imag:+.6f}i  "
            f"{spatial[1].real:+.6f}{spatial[1].imag:+.6f}i  {spatial[4]:.6f}"
        )


if __name__ == "__main__":
    main()
