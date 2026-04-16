import numpy as np
import pytest
from src.physics.integrators import step_rk4
from src.physics.forces import G

def test_rk4_circular_orbit_stability():
    # Arrange: Setup a massive central body and a small orbiting body
    M_central = 1e24  # kg (roughly Earth-ish)
    m_orbiting = 1.0  # kg
    radius = 1e6      # meters
    
    # To achieve a perfect circular orbit, velocity must be v = sqrt(G*M / r)
    v_orbit = np.sqrt(G * M_central / radius)
    
    # Body 0 is the center, Body 1 is orbiting
    positions = np.array([
        [0.0, 0.0, 0.0], 
        [radius, 0.0, 0.0]
    ])
    velocities = np.array([
        [0.0, 0.0, 0.0], 
        [0.0, v_orbit, 0.0]
    ])
    masses = np.array([M_central, m_orbiting])
    
    dt = 5.0  # 5 second time step (~154 steps/orbit for this setup)
    
    # Act: Run the simulation for 1000 steps (~83 minutes, ~6.5 orbits)
    for _ in range(1000):
        positions, velocities = step_rk4(positions, velocities, masses, dt)
        
    # Assert: Calculate the new distance from the origin
    r_vec = positions[1] - positions[0]
    new_radius = np.linalg.norm(r_vec)
    
    # The new radius should be extremely close to the original radius
    # rtol=1e-5 means we allow a 0.001% margin of error due to floating point drift
    np.testing.assert_allclose(new_radius, radius, rtol=1e-5)
