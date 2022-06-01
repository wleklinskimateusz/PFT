from matplotlib import pyplot as plt
import numpy as np
import os

from const import DELTA, DT, N, ALPHA, M



def get_derrivatives(t, vars: np.ndarray, k):
    for i in range(1, N):
        k[i] = vars[i+N+1]
        k[i+N+1] = (ALPHA / M) * (vars[i-1] - 2*vars[i] + vars[i+1])
    k[0] = 0
    k[N] = 0
    k[N+1] = 0
    k[2*N+1] = 0



def rk4_solve(t, vars: np.ndarray, func = get_derrivatives) -> np.ndarray:
    s = vars.copy()
    n = len(vars)
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    k4 = np.zeros(n)
    w = np.zeros(n)
    for i in range(n):
        w[i] = s[i]
    func(t, w, k1)
    for i in range(n):
        w[i] = s[i] + DT/2 * k1[i]
    func(t + DT/2, w, k2)
    for i in range(n):
        w[i] = s[i] + DT/2 * k2[i]
    func(t + DT/2, w, k3)
    for i in range(n):
        w[i] = s[i] + DT * k3[i]
    func(t + DT, w, k4)
    for i in range(n):
        s[i] += DT/6 * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i])
    return s

def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

def get_xi0(i):
    return i * DELTA

def get_starting_gaussian(i):
    x0 = get_xi0(i)
    xmax = get_xi0(N)
    print(x0, xmax)
    return x0 + (DELTA / 3) * np.exp(-((x0 - xmax/2)**2) / (2 * (3 * DELTA)**2))

def show_frame(vars, title: str = ""):
    plt.plot(vars[:N+2], np.zeros(N+2), 'ro')
    plt.title(title)
    plt.show()

