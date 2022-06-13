
import numpy as np
from const import DRHO, DZ


def get_rho(i):
    return i * DRHO

def get_z(i):
    return i * DZ

def square(x, a, b, c):
    return a * x**2 + b * x + c

def fit_curve(x, y):
    a, b, c = np.polyfit(x, y, 2)
    return a, b, c