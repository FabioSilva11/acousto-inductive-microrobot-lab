from dataclasses import dataclass
import math

@dataclass
class DrugReservoir:
    payload_mass_ug: float = 0.5
    release_rate_per_s: float = 0.01
    diffusion_radius_um: float = 300.0
    remaining_ug: float | None = None

    def __post_init__(self):
        if self.remaining_ug is None:
            self.remaining_ug = self.payload_mass_ug

    def step(self, dt: float, duty_cycle: float) -> float:
        """Release an abstract payload mass in micrograms.

        This is not a real drug dosing model.
        """
        duty = max(0.0, min(1.0, duty_cycle))
        released = self.remaining_ug * (1.0 - math.exp(-self.release_rate_per_s * duty * dt))
        self.remaining_ug -= released
        return released

    def local_concentration_ug_per_mm3(self, released_ug: float) -> float:
        r_mm = self.diffusion_radius_um / 1000.0
        volume_mm3 = (4.0 / 3.0) * math.pi * r_mm**3
        if volume_mm3 <= 0:
            return 0.0
        return released_ug / volume_mm3
