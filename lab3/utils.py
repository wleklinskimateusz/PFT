import numpy as np

from const import DT, M, Q, B


def rk4_solve(t, vars: np.ndarray, func) -> np.ndarray:
    k1 = func(t, vars)
    k2 = func(t + DT/2, vars + DT/2*k1)
    k3 = func(t + DT/2, vars + DT/2*k2)
    k4 = func(t + DT, vars + DT*k3)
    return DT/6*(k1 + 2*k2 + 2*k3 + k4)


def get_derrivatives(t, vars: np.ndarray) -> np.ndarray:
    return np.array([
        vars[3]/M,
        vars[4]/(M*vars[0]**2) - Q * B / (2 * M),
        vars[5]/M,
        vars[4]**2 / (M * vars[0]**3) - Q**2 * B ** 2 * vars[0] / (4*M),
        0,
        0
    ])