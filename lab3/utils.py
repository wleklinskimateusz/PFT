from matplotlib import pyplot as plt
import numpy as np
import os

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

def make_dir(dir_name):
    if not os.path.exists(dir_name):
        print("Creating directory: {}".format(dir_name))
        os.mkdir(dir_name)

def legend_without_duplicate_labels(figure):
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    figure.legend(by_label.values(), by_label.keys(), loc='lower right')