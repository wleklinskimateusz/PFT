from utils import get_z
from solver import Solver
import matplotlib.pyplot as plt

from const import M, N

class Plotter:
    def __init__(self, solver: Solver):
        self.solver = solver

    def plot_last_frame(self):
        plt.imshow(self.solver.V, origin="lower")
        c = plt.colorbar()
        c.set_label("V")
        plt.xlabel("z")
        plt.ylabel("rho")
        plt.show()

    def plot_Vz(self):
        plt.plot(self.solver.V[0, :].T)
        plt.ylabel("V(0, z)")
        plt.xlabel("z")
        plt.show()

    def plot_Vrho(self):
        plt.plot(self.solver.V[:, M//2].T)
        plt.ylabel("V(rho, M/2)")
        plt.xlabel("rho")
        plt.show()
