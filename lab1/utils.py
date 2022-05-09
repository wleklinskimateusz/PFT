import numpy as np
from const import G

def get_kinetic_energy(m: float, v: np.ndarray) -> np.ndarray:
    return 0.5 * m * v**2

def get_potential_energy(m: float, h: np.ndarray) -> np.ndarray:
    return m * G * h