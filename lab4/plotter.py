from matplotlib import pyplot as plt
import numpy as np
from const import DT, N
from solver import Solver


class Plotter:
    def __init__(self, s: Solver):
        self.solver = s



    def plot_energy(self):
        plt.plot(self.solver.get_kinetic_energy(), label="Kinetic")
        plt.plot(self.solver.get_potential_energy(), label="Potential")
        plt.plot(self.solver.get_total_energy(), label="Total")
        plt.legend()
        plt.show()

    def plot_xmap(self):
        dx = self.solver.get_diffs()
        x = np.linspace(0, N, N+1)
        t = np.linspace(0, self.solver.nt * DT, self.solver.nt)
        plt.pcolormesh(t, x, dx, cmap="RdBu")
        plt.show()
