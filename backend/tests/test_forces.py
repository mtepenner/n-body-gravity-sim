import numpy as np
import pytest
from src.physics.forces import calculate_accelerations, G

def test_gravitational_force_two_bodies():
    # Arrange: Two 1kg masses, exactly 1 meter apart on the X-axis
    positions = np.array([
        [0.0, 0.0, 0.0], 
        [1.0, 0.0, 0.0]
    ])
    masses = np.array([1.0, 1.0])
    
    # Act: Calculate the accelerations
    accelerations = calculate_accelerations(positions, masses)
    
    # Assert: 
    # Body 0 should accelerate in the +X direction by exactly G
    # Body 1 should accelerate in the -X direction by exactly G
    expected_a0 = np.array([G, 0.0, 0.0])
    expected_a1 = np.array([-G, 0.0, 0.0])
    
    # We use np.testing because comparing floats directly (==) is dangerous
    np.testing.assert_almost_equal(accelerations[0], expected_a0)
    np.testing.assert_almost_equal(accelerations[1], expected_a1)

def test_three_body_equilibrium():
    # Arrange: Three equal masses in an equilateral triangle around the origin
    # The net force on a body exactly in the center (origin) should be zero.
    positions = np.array([
        [0.0, 1.0, 0.0],
        [np.sqrt(3)/2, -0.5, 0.0],
        [-np.sqrt(3)/2, -0.5, 0.0],
        [0.0, 0.0, 0.0]  # The test body in the center
    ])
    masses = np.array([1.0, 1.0, 1.0, 1.0])

    # Act
    accelerations = calculate_accelerations(positions, masses)

    # Assert: The central body (index 3) should have zero acceleration
    np.testing.assert_almost_equal(accelerations[3], np.array([0.0, 0.0, 0.0]))
