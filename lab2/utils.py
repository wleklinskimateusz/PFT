import os
import numpy as np

from const import COSA, DT, SINA, G, ALPHA, THETA

def get_rho(z: np.ndarray) -> np.ndarray:
    return z * np.tan(ALPHA)


def get_x(rho: np.ndarray, phi: np.ndarray) -> np.ndarray:
    return rho * np.cos(phi)


def get_y(rho: np.ndarray, phi: np.ndarray) -> np.ndarray:
    return rho * np.sin(phi)


def rk4_solve(t, vars: np.ndarray, func) -> np.ndarray:
    k1 = func(t, vars)
    k2 = func(t + DT/2, vars + DT/2*k1)
    k3 = func(t + DT/2, vars + DT/2*k2)
    k4 = func(t + DT, vars + DT*k3)
    return DT/6*(k1 + 2*k2 + 2*k3 + k4)


def get_rotation_matrix():
    return np.array([
        [np.cos(THETA), 0, np.sin(THETA)],
        [0, 1, 0],
        [-np.sin(THETA), 0, np.cos(THETA)]
    ])


def debug(var: any, name: str):
    print(f"Variable {name} = {var}")
    print("Type:", type(var))


def cone_func(t: float, vars: np.ndarray) -> np.ndarray:
    debug(vars, "vars")
    return np.array([
        vars[2],
        vars[3],
        -G * COSA ** 2 / SINA *
        np.sin(vars[0]) / vars[1] - 2 * vars[2] * vars[3] / vars[1],
        SINA**2 * vars[1] * vars[2] ** 2 - G *
        SINA * COSA ** 2 * (1 - np.cos(vars[0]))

    ])


def get_cone(x_obj: np.ndarray, y_obj: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    R = get_rotation_matrix()
    step = 0.05
    xlim = max([np.abs(x_obj.min()), np.abs(x_obj.max())])
    ylim = max([np.abs(y_obj.min()), np.abs(y_obj.max())])
    mlim = max([xlim, ylim]) / 2
    X = np.arange(-mlim, mlim, step)
    Y = np.arange(-mlim, mlim, step)
    num_steps = len(X)
    X, Y = np.meshgrid(X, Y)
    Z: np.ndarray = np.sqrt(X**2 + Y**2) / np.tan(ALPHA)
    X = X.reshape((-1))
    Y = Y.reshape((-1))
    Z = Z.reshape((-1))
    t = np.array([X, Y, Z])
    X, Y, Z = np.dot(R, t)
    X = X.reshape(num_steps, num_steps)
    Y = Y.reshape(num_steps, num_steps)
    Z = Z.reshape(num_steps, num_steps)

    return X, Y, Z

def make_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)