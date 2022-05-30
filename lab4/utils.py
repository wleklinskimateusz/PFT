import numpy as np
import os

from const import DELTA, DT, N, ALPHA, M



def get_derrivatives(t, vars: np.ndarray) -> np.ndarray:
    k = np.zeros(2*N+2)
    for i in range(1, N):
        k[i] = vars[i+N+1]
        k[i+N+1] = ALPHA / M * (vars[i-1] - 2*vars[i] + vars[i+1])
    return k


def rk4_solve(t, vars: np.ndarray, func = get_derrivatives) -> np.ndarray:
    k1 = func(t, vars)
    k2 = func(t + DT/2, vars + DT/2*k1)
    k3 = func(t + DT/2, vars + DT/2*k2)
    k4 = func(t + DT, vars + DT*k3)
    return DT/6*(k1 + 2*k2 + 2*k3 + k4)

def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

def get_xi0(i):
    return i * DELTA

def get_starting_gaussian(i):
    x0 = get_xi0(i)
    xmax = get_xi0(N)
    print(x0, xmax)
    return x0 + DELTA / 3 * np.exp(-(x0 - xmax/2)**2 / (2 * (3 * DELTA)**2))

