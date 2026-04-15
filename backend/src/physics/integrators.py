import numpy as np
from typing import Tuple
from src.physics.forces import calculate_accelerations

def step_euler(positions: np.ndarray, velocities: np.ndarray, masses: np.ndarray, dt: float) -> Tuple[np.ndarray, np.ndarray]:
    """Simple integration (Included for comparison, but not recommended for orbits)."""
    accelerations = calculate_accelerations(positions, masses)
    new_positions = positions + velocities * dt
    new_velocities = velocities + accelerations * dt
    return new_positions, new_velocities

def step_rk4(positions: np.ndarray, velocities: np.ndarray, masses: np.ndarray, dt: float) -> Tuple[np.ndarray, np.ndarray]:
    """Runge-Kutta 4th Order numerical integration for stable orbits."""
    # k1 (Current state)
    k1_v = calculate_accelerations(positions, masses)
    k1_p = velocities

    # k2 (State at halfway point using k1)
    k2_v = calculate_accelerations(positions + k1_p * dt / 2.0, masses)
    k2_p = velocities + k1_v * dt / 2.0

    # k3 (State at halfway point using k2)
    k3_v = calculate_accelerations(positions + k2_p * dt / 2.0, masses)
    k3_p = velocities + k2_v * dt / 2.0

    # k4 (State at end point using k3)
    k4_v = calculate_accelerations(positions + k3_p * dt, masses)
    k4_p = velocities + k3_v * dt

    # Weighted average of slopes
    new_positions = positions + (dt / 6.0) * (k1_p + 2*k2_p + 2*k3_p + k4_p)
    new_velocities = velocities + (dt / 6.0) * (k1_v + 2*k2_v + 2*k3_v + k4_v)

    return new_positions, new_velocities
