import math
import numpy as np
from .constants import Fluid, RobotGeometry


def reynolds_number(speed: float, length: float, fluid: Fluid = Fluid()) -> float:
    """Compute Reynolds number for a small body in a viscous fluid."""
    return fluid.density * abs(speed) * length / fluid.viscosity


def stokes_drag(relative_velocity, radius: float, fluid: Fluid = Fluid()):
    """Stokes drag approximation. Works best for Re << 1 and sphere-like bodies."""
    v = np.asarray(relative_velocity, dtype=float)
    return -6.0 * math.pi * fluid.viscosity * radius * v


def acoustic_radiation_force(
    intensity_w_m2: float,
    area_m2: float,
    efficiency: float = 0.02,
    fluid: Fluid = Fluid(),
):
    """Simplified acoustic force scale.

    Radiation pressure for a strong reflector is approximated as 2I/c. We multiply
    by an abstract efficiency because microrobot propulsion depends on geometry,
    resonance, streaming, boundary conditions and actuator coupling.

    This is for simulation only, not device design.
    """
    radiation_pressure = 2.0 * intensity_w_m2 / fluid.sound_speed
    return efficiency * area_m2 * radiation_pressure


def terminal_velocity_from_force(force_n: float, radius: float, fluid: Fluid = Fluid()) -> float:
    """Low-Re terminal velocity from Stokes drag balance."""
    return force_n / (6.0 * math.pi * fluid.viscosity * radius)


def poiseuille_flow(y: float, vessel_radius: float, vmax: float) -> float:
    """Parabolic vessel flow along x; y=0 at centerline."""
    r = min(abs(y), vessel_radius)
    return vmax * (1.0 - (r / vessel_radius) ** 2)


def limit_norm(vec, max_norm: float):
    vec = np.asarray(vec, dtype=float)
    n = np.linalg.norm(vec)
    if n <= max_norm or n == 0:
        return vec
    return vec * (max_norm / n)
