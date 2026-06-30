from dataclasses import dataclass, field
import numpy as np
from .constants import Fluid, RobotGeometry
from .physics import acoustic_radiation_force, stokes_drag, poiseuille_flow, limit_norm

@dataclass
class RobotState:
    position: np.ndarray
    velocity: np.ndarray
    heading: np.ndarray
    payload: float = 1.0

@dataclass
class MotionConfig:
    dt: float = 0.05
    max_speed: float = 250e-6
    acoustic_intensity_w_m2: float = 5_000.0
    actuator_efficiency: float = 0.02
    vessel_radius_m: float = 500e-6
    flow_vmax_m_s: float = 1.5e-3
    steering_gain: float = 6.0
    thrust_gain: float = 1.0

class MotionSimulator:
    def __init__(self, geometry=RobotGeometry(), fluid=Fluid(), config=MotionConfig()):
        self.geometry = geometry
        self.fluid = fluid
        self.config = config

    def step(self, state: RobotState, target: np.ndarray) -> RobotState:
        cfg = self.config
        pos = np.asarray(state.position, dtype=float)
        vel = np.asarray(state.velocity, dtype=float)
        heading = np.asarray(state.heading, dtype=float)
        target = np.asarray(target, dtype=float)

        to_target = target - pos
        dist = np.linalg.norm(to_target)
        desired = to_target / dist if dist > 1e-12 else heading

        # Smooth heading update
        heading = heading + cfg.steering_gain * cfg.dt * (desired - heading)
        n = np.linalg.norm(heading)
        if n > 0:
            heading = heading / n

        # Fluid flow along x, with parabolic profile in y for 2D/3D vectors
        y = pos[1] if len(pos) > 1 else 0.0
        flow = np.zeros_like(pos)
        flow[0] = poiseuille_flow(y, cfg.vessel_radius_m, cfg.flow_vmax_m_s)

        # Acoustic thrust along heading
        force_mag = acoustic_radiation_force(
            cfg.acoustic_intensity_w_m2,
            self.geometry.cross_section_area,
            cfg.actuator_efficiency,
            self.fluid,
        ) * cfg.thrust_gain
        thrust = heading * force_mag

        drag = stokes_drag(vel - flow, self.geometry.radius, self.fluid)
        acc = (thrust + drag) / self.geometry.mass
        vel = vel + acc * cfg.dt
        vel = limit_norm(vel, cfg.max_speed)
        pos = pos + vel * cfg.dt

        # Keep inside vessel boundary in y dimension
        if len(pos) > 1:
            r = abs(pos[1])
            limit = cfg.vessel_radius_m * 0.95
            if r > limit:
                pos[1] = np.sign(pos[1]) * limit
                vel[1] *= -0.2

        return RobotState(position=pos, velocity=vel, heading=heading, payload=state.payload)

    def run(self, start, target, steps=1000):
        dim = len(start)
        state = RobotState(
            position=np.array(start, dtype=float),
            velocity=np.zeros(dim),
            heading=np.array([1.0] + [0.0]*(dim-1)),
        )
        history = []
        for _ in range(steps):
            history.append((state.position.copy(), state.velocity.copy(), state.heading.copy()))
            state = self.step(state, np.array(target, dtype=float))
        return state, history
