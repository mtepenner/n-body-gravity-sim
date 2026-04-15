import numpy as np

G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)

def calculate_accelerations(positions: np.ndarray, masses: np.ndarray) -> np.ndarray:
    """
    Calculates the acceleration of each body due to gravity from all other bodies.
    positions: (N, 3) array of positions
    masses: (N,) array of masses
    Returns: (N, 3) array of accelerations
    """
    N = len(masses)
    accelerations = np.zeros((N, 3), dtype=np.float64)

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            
            # Vector from body i to body j
            r_vec = positions[j] - positions[i]
            r_mag_sq = np.sum(r_vec**2)
            r_mag = np.sqrt(r_mag_sq)
            
            # Avoid division by zero in case of an exact collision
            if r_mag > 0:
                # a = G * m_j / r^2 * (r_vec / r)
                accelerations[i] += G * masses[j] * r_vec / (r_mag_sq * r_mag)
                
    return accelerations
