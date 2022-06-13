import numpy as np
from const import N, M, DPHI, DTHETA, w


def coef(idx: int, max_idx: int) -> int:
    if idx == 0 or idx == max_idx:
        return 1
    if idx % 2 == 0:
        return 2
    if idx % 2 == 1:
        return 4


def coefs(i: int, j: int) -> tuple[int, int]:
    return (coef(i, N), coef(j, M))


def get_phi(j: int) -> float:
    return j * DPHI


def get_theta(i: int) -> float:
    return i * DTHETA


def get_r(r, i, j):
    return np.array([
        r * np.sin(get_theta(i)) * np.cos(get_phi(j)),
        r * np.sin(get_theta(i)) * np.sin(get_phi(j)),
        r * np.cos(get_theta(i))
    ])

def get_potential_element(a: int, b: int, theta, d):
    return a * b * np.sin(theta) / (d.dot(d) ** 0.5)

def get_E_element(a, b, theta, d):
    return a * b * np.sin(theta) * d / (d.dot(d) ** 1.5)

def get_B_element(a, b, theta, d, r, R):
    return a * b * np.sin(theta) * (np.cross(d, (np.cross(w, R)))) * r / (d.dot(d) ** 1.5)
    