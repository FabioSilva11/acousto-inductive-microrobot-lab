import math
from dataclasses import dataclass


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))

@dataclass
class AcousticInteractionModel:
    """Abstract ultrasound-cell interaction score.

    This intentionally does not provide clinical or wet-lab ablation parameters.
    It produces a dimensionless score for simulation and safety visualization.
    """
    reference_mi: float = 0.7
    width: float = 0.25
    max_score: float = 1.0

    def mechanical_index(self, negative_pressure_mpa: float, frequency_mhz: float) -> float:
        if frequency_mhz <= 0:
            return 0.0
        return max(0.0, negative_pressure_mpa) / math.sqrt(frequency_mhz)

    def interaction_score(
        self,
        negative_pressure_mpa: float,
        frequency_mhz: float,
        exposure_s: float,
        proximity_0_to_1: float,
    ) -> float:
        mi = self.mechanical_index(negative_pressure_mpa, frequency_mhz)
        base = sigmoid((mi - self.reference_mi) / self.width)
        exposure_factor = 1.0 - math.exp(-max(0.0, exposure_s) / 10.0)
        prox = max(0.0, min(1.0, proximity_0_to_1))
        return self.max_score * base * exposure_factor * prox


def proximity_score(distance_m: float, effect_radius_m: float) -> float:
    if effect_radius_m <= 0:
        return 0.0
    x = max(0.0, min(1.0, 1.0 - distance_m / effect_radius_m))
    return x * x * (3 - 2 * x)  # smoothstep
