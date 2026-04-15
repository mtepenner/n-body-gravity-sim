import numpy as np
from typing import List, Dict
from src.models.body import CelestialBody
from src.physics.integrators import step_rk4

class Universe:
    def __init__(self):
        self.bodies: List[CelestialBody] = []
        self.time: float = 0.0

    def add_body(self, body: CelestialBody):
        self.bodies.append(body)

    def clear(self):
        self.bodies = []
        self.time = 0.0

    def step(self, dt: float):
        if not self.bodies:
            return

        # 1. Extract and stack states into NumPy arrays for the physics engine
        positions = np.array([b.position for b in self.bodies])
        velocities = np.array([b.velocity for b in self.bodies])
        masses = np.array([b.mass for b in self.bodies])

        # 2. Run RK4 Integration
        new_pos, new_vel = step_rk4(positions, velocities, masses, dt)

        # 3. Apply new states back to objects
        for i, body in enumerate(self.bodies):
            body.position = new_pos[i]
            body.velocity = new_vel[i]

        self.time += dt

    def get_state(self) -> Dict:
        return {
            "time": self.time,
            "bodies": [b.to_dict() for b in self.bodies]
        }
