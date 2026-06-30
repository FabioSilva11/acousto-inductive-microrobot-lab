from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import numpy as np
import matplotlib.pyplot as plt
from microrobot_lab.swarm_control import swarm_commands, SwarmConfig

out = Path('outputs')
out.mkdir(exist_ok=True)
rng = np.random.default_rng(42)
N = 24
positions = np.column_stack([
    rng.uniform(-1.8e-3, -1.0e-3, N),
    rng.uniform(-250e-6, 250e-6, N),
])
velocities = np.zeros_like(positions)
target = np.array([1.5e-3, 0.0])
cfg = SwarmConfig()
dt = 0.08
speed = 120e-6
history = []

for step in range(500):
    history.append(positions.copy())
    cmds = swarm_commands(positions, velocities, target, cfg)
    velocities = 0.85 * velocities + 0.15 * cmds * speed
    positions = positions + velocities * dt

history = np.array(history)
plt.figure(figsize=(8, 4.5))
for i in range(N):
    plt.plot(history[:,i,0]*1e3, history[:,i,1]*1e6, alpha=0.7)
plt.scatter([target[0]*1e3], [target[1]*1e6], marker='x')
plt.axhline(cfg.vessel_radius_m*1e6, linestyle='--')
plt.axhline(-cfg.vessel_radius_m*1e6, linestyle='--')
plt.xlabel('x (mm)')
plt.ylabel('y (µm)')
plt.title('Enxame: coesão, separação e atração ao alvo')
plt.tight_layout()
plt.savefig(out/'swarm_demo.png', dpi=180)
print('Saved outputs/swarm_demo.png')
