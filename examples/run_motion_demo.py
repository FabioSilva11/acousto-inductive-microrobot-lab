from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import numpy as np
import matplotlib.pyplot as plt
from microrobot_lab.motion_sim import MotionSimulator, MotionConfig
from microrobot_lab.physics import reynolds_number
from microrobot_lab.constants import Fluid, RobotGeometry

out = Path("outputs")
out.mkdir(exist_ok=True)
fluid = Fluid(viscosity=3.5e-3)
geom = RobotGeometry()
cfg = MotionConfig(flow_vmax_m_s=1.5e-3, acoustic_intensity_w_m2=5000)
sim = MotionSimulator(geom, fluid, cfg)
state, hist = sim.run(start=[-1.5e-3, -250e-6], target=[1.5e-3, 150e-6], steps=900)
positions = np.array([h[0] for h in hist])
speeds = np.linalg.norm(np.array([h[1] for h in hist]), axis=1)

plt.figure(figsize=(8, 4.5))
plt.plot(positions[:,0]*1e3, positions[:,1]*1e6)
plt.axhline(cfg.vessel_radius_m*1e6, linestyle='--')
plt.axhline(-cfg.vessel_radius_m*1e6, linestyle='--')
plt.scatter([1.5], [150], marker='x')
plt.xlabel('x (mm)')
plt.ylabel('y (µm)')
plt.title('Trajetória simulada em fluido viscoso')
plt.tight_layout()
plt.savefig(out/'motion_demo.png', dpi=180)

print('Final position (m):', state.position)
print('Mean speed (um/s):', speeds.mean()*1e6)
print('Approx Reynolds:', reynolds_number(speeds.mean(), geom.length, fluid))
print('Saved outputs/motion_demo.png')
