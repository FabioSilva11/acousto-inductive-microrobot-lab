import math
from dataclasses import dataclass

@dataclass
class InductionLink:
    turns: int = 18
    coil_radius_m: float = 60e-6
    frequency_hz: float = 13.56e6
    magnetic_field_t: float = 0.2e-3
    load_ohm: float = 20_000.0
    transfer_efficiency: float = 0.02

    def area(self) -> float:
        return math.pi * self.coil_radius_m**2

    def induced_vrms(self) -> float:
        """Ideal Faraday-law estimate for a tiny coil in a sinusoidal field."""
        omega = 2.0 * math.pi * self.frequency_hz
        return self.turns * self.area() * omega * self.magnetic_field_t / math.sqrt(2.0)

    def available_power_w(self) -> float:
        v = self.induced_vrms()
        return self.transfer_efficiency * (v * v) / self.load_ohm

    def summary(self) -> dict:
        return {
            "turns": self.turns,
            "coil_radius_um": self.coil_radius_m * 1e6,
            "frequency_MHz": self.frequency_hz / 1e6,
            "B_mT": self.magnetic_field_t * 1e3,
            "Vrms_mV": self.induced_vrms() * 1e3,
            "P_available_uW": self.available_power_w() * 1e6,
        }
