import numpy as np

from const import N, M, DT, DZ, DRHO, J1, J2, V0
from utils import get_rho


class Solver:
    def __init__(self, time: float):
        self.nt = int(time / DT)
        self.V = np.zeros((N+1, M+1))

    def set_boundary_conditions(self, t):
        self.V[1:-1, 0] = self.V[1:-1, 1]
        self.V[1:-1, -1] = self.V[1:-1, -2]
        self.V[0, 1:-1] = self.V[1, 1:-1]
        self.V[-1, :J1] = V0
        self.V[-1, J1:J2] = 0
        self.V[-1, J2:] = V0

        self.V[0, 0] = self.V[1, 1]
        self.V[0, -1] = self.V[1, -2]

    def get_next_potential(self, i, j):
        rho = get_rho(i)
        output = DRHO**(-2) * (self.V[i+1, j] + self.V[i-1, j]) + 0.5/(rho * DRHO) * (
            self.V[i+1, j] - self.V[i-1, j]) + DZ**(-2) * (self.V[i, j+1] + self.V[i, j-1])
        output /= 2 / DRHO ** 2 + 2 / DZ ** 2

        return output

    def solve(self):
        for t in range(self.nt-1):
            print(f"Solving for t = {t*DT:.2f}s", end="\r")
            self.set_boundary_conditions(t)
            for i in range(1, N):
                for j in range(1, M):
                    self.V[i, j] = self.get_next_potential(i, j)

    def save_to_file(self, filename):
        np.save(filename, self.V)

    def load_from_file(self, filename):
        self.V = np.load(filename)
