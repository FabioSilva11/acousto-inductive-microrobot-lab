from dataclasses import dataclass

@dataclass(frozen=True)
class Fluid:
    density: float = 1060.0        # kg/m^3, blood-like
    viscosity: float = 3.5e-3      # Pa*s, blood-like order of magnitude
    sound_speed: float = 1540.0    # m/s, soft tissue/blood-like order

@dataclass(frozen=True)
class RobotGeometry:
    length: float = 300e-6         # m
    diameter: float = 120e-6       # m
    mass: float = 80e-9            # kg, conceptual effective mass

    @property
    def radius(self) -> float:
        return self.diameter / 2

    @property
    def cross_section_area(self) -> float:
        import math
        return math.pi * self.radius**2
