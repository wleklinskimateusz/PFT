import numpy as np
from const import DT, N
from utils import get_starting_gaussian, rk4_solve


class Solver:
    def __init__(self, nt: float = 5000):
        self.vars = np.zeros((2*N+2, nt))
        self.t = 0
        self.nt = nt


    def initialize_gaussian(self):
        for i in range(N):
            if i == 0:
                continue
            self.vars[i, 0] = get_starting_gaussian(i)

    def calculate(self):
        for i in range(self.nt-1):
            self.t += DT
            self.vars[:, i+1] = rk4_solve(self.t, self.vars[:, i])

    def get_kinetic_energy(self):
        v = self.vars[N+2, :]
        print(v)