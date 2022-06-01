import numpy as np
from const import ALPHA, DELTA, DT, M, N
from utils import get_starting_gaussian, rk4_solve, show_frame


class Solver:
    def __init__(self, nt: float = 5000):
        self.vars = np.zeros((2*N+2, nt))
        self.t = 0
        self.nt = nt


    def initialize_gaussian(self):
        for i in range(1, N+1):
            self.vars[i, 0] = get_starting_gaussian(i)
        # show_frame(self.vars[:, 0])

    def calculate(self):
        for i in range(self.nt-1):
            self.t += DT
            self.vars[:, i+1] = rk4_solve(self.t, self.vars[:, i])
            # show_frame(self.vars[:, i], "before")
            # show_frame(self.vars[:, i+1], "after")

    def get_kinetic_energy(self):
        Ek=np.zeros(self.nt)
        for i in range(N+1):
            Ek[i] = 0.5 * M * np.sum(self.vars[N+2:,i]**2)
        return Ek

    def get_potential_energy(self):
        Ep = np.zeros(self.nt)
        for i in range(1, N+1):
            Ep[i] = 0.5 * ALPHA * np.sum((self.vars[i+1, :] - self.vars[i, :] + DELTA)**2)
        return Ep
    def get_total_energy(self):
        return self.get_kinetic_energy() + self.get_potential_energy()
