import numpy as np
from utils import fit_curve, get_z, square
from solver import Solver
import matplotlib.pyplot as plt

from const import DRHO, DZ, M, N

class Plotter:
    def __init__(self, solver: Solver):
        self.solver = solver

    def plot_last_frame(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        im = ax.matshow(self.solver.V, origin="lower")
        c = fig.colorbar(im, ax=ax)
        c.set_label("V")
        ax.set_xlabel("z")
        ax.set_ylabel("rho")
        fig.savefig("last_frame.png")

    def plot_Vz(self):
        x = np.linspace(0, 1, M+1)
        y = self.solver.V[0, :]
        xmin = int(0.4 * M)
        xmax = int(0.6 * M)
        a, b, c = fit_curve(x[xmin:xmax], y[xmin:xmax])
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x, self.solver.V[0, :].T, label="numeric")
        ax.plot(x[xmin-20:xmax+20], square(x[xmin-20:xmax+20], a, b, c), label="fit")
        ax.set_ylabel("V(0, z)")
        ax.set_xlabel("z")
        fig.savefig("Vz.png")

    def plot_Vrho(self):
        x = np.linspace(0, 1, N+1)
        y = self.solver.V[:, M//2]
        a, b, c = fit_curve(x, y)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x, self.solver.V[:, M//2].T, label="numeric")
        ax.plot(x, square(x, a, b, c), label="fit")
        ax.set_ylabel("V(rho, M/2)")
        ax.set_xlabel("rho")
        fig.savefig("Vrho.png")

    def plot3d_V(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        Z, RHO = np.meshgrid(np.linspace(0, 1, M+1), np.linspace(0, 1, N+1))
        ax.plot_surface(RHO, Z, self.solver.V, cmap="viridis")
        ax.set_xlabel("z")
        ax.set_ylabel("rho")
        ax.set_zlabel("V")
        fig.savefig("V.png")