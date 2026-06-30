import numpy as np
from dataclasses import dataclass
from .physics import limit_norm

@dataclass
class SwarmConfig:
    neighbor_radius: float = 400e-6
    separation_radius: float = 140e-6
    cohesion_gain: float = 0.8
    alignment_gain: float = 0.6
    separation_gain: float = 1.4
    target_gain: float = 1.8
    wall_gain: float = 1.2
    max_command: float = 1.0
    vessel_radius_m: float = 500e-6


def swarm_commands(positions, velocities, target, cfg=SwarmConfig()):
    """Return dimensionless command vectors for each robot in a safe boids-like swarm."""
    positions = np.asarray(positions, dtype=float)
    velocities = np.asarray(velocities, dtype=float)
    target = np.asarray(target, dtype=float)
    n = len(positions)
    commands = np.zeros_like(positions)

    for i in range(n):
        p = positions[i]
        v = velocities[i]
        cohesion = np.zeros_like(p)
        alignment = np.zeros_like(p)
        separation = np.zeros_like(p)
        count = 0

        for j in range(n):
            if i == j:
                continue
            delta = positions[j] - p
            d = np.linalg.norm(delta)
            if d < cfg.neighbor_radius:
                cohesion += positions[j]
                alignment += velocities[j]
                count += 1
            if 1e-12 < d < cfg.separation_radius:
                separation -= delta / (d*d)

        cmd = np.zeros_like(p)
        if count > 0:
            center = cohesion / count
            avg_v = alignment / count
            cmd += cfg.cohesion_gain * (center - p)
            cmd += cfg.alignment_gain * avg_v
        cmd += cfg.separation_gain * separation

        to_target = target - p
        dtarget = np.linalg.norm(to_target)
        if dtarget > 1e-12:
            cmd += cfg.target_gain * (to_target / dtarget)

        # wall avoidance in y dimension
        if len(p) > 1:
            y = p[1]
            margin = cfg.vessel_radius_m * 0.85
            if abs(y) > margin:
                cmd[1] += -cfg.wall_gain * np.sign(y) * (abs(y)-margin) / max(1e-12, cfg.vessel_radius_m-margin)

        commands[i] = limit_norm(cmd, cfg.max_command)
    return commands
