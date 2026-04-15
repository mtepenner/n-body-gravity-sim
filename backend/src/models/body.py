import numpy as np
from pydantic import BaseModel
from typing import List

class BodyState(BaseModel):
    id: str
    name: str
    mass: float
    radius: float
    position: List[float]  # [x, y, z] in meters
    velocity: List[float]  # [vx, vy, vz] in meters/second
    color: str = "#ffffff"

class CelestialBody:
    def __init__(self, id: str, name: str, mass: float, radius: float, position: List[float], velocity: List[float], color: str = "#ffffff"):
        self.id = id
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = np.array(position, dtype=np.float64)
        self.velocity = np.array(velocity, dtype=np.float64)
        self.color = color

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass,
            "radius": self.radius,
            "position": self.position.tolist(),
            "velocity": self.velocity.tolist(),
            "color": self.color
        }
