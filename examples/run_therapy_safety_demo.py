from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from microrobot_lab.cell_interaction import AcousticInteractionModel, proximity_score
from microrobot_lab.drug_release import DrugReservoir

out = Path('outputs')
out.mkdir(exist_ok=True)
model = AcousticInteractionModel(reference_mi=0.7, width=0.25)
reservoir = DrugReservoir(payload_mass_ug=0.5, release_rate_per_s=0.02, diffusion_radius_um=300)

# Abstract scenario only. Not a medical or lab protocol.
distance_m = 120e-6
prox = proximity_score(distance_m, 400e-6)
released = reservoir.step(dt=5.0, duty_cycle=0.6)
conc = reservoir.local_concentration_ug_per_mm3(released)
score = model.interaction_score(
    negative_pressure_mpa=0.25,
    frequency_mhz=2.0,
    exposure_s=5.0,
    proximity_0_to_1=prox,
)

report = (
    f"# Demo de segurança terapêutica simulada\n\n"
    f"Este arquivo é resultado de uma simulação abstrata.\n\n"
    f"- Proximidade: {prox:.3f}\n"
    f"- Massa liberada genérica: {released:.5f} µg\n"
    f"- Concentração local abstrata: {conc:.5f} µg/mm³\n"
    f"- Índice de interação celular abstrato: {score:.3f}\n\n"
    f"Não use estes números como protocolo biomédico.\n"
)
(out/'therapy_safety_demo.md').write_text(report, encoding='utf-8')
print(report)
print('Saved outputs/therapy_safety_demo.md')
