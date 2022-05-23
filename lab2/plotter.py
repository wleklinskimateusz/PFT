from matplotlib import pyplot as plt
import numpy as np

from cone import BodyOnCone
from const import DT
from utils import get_cone


class Plotter:
    def __init__(self, body: BodyOnCone):
        self.body = body

    def plot_trajectory(self):
        x, y, z = self.body.get_coordinates(rotate=True)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot3D(x, y, z, 'red')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        # cx, cy, cz = get_cone(x, y)
        # ax.plot_surface(cx, cy, cz, color='b', alpha=0.2)
        fig.savefig('output/trajectory.png')

    def plot_energy(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(np.linspace(0, self.body.steps * DT, self.body.steps), self.body.energies)
        ax.set_xlabel("time [s]")
        ax.set_ylabel("energy [J]")
        fig.savefig("output/energy.png")

    def plot_var(self, var: np.ndarray, var_name: str, unit: str, ax: plt):
        ax.plot(np.linspace(0, self.body.steps * DT, self.body.steps), var)
        ax.set_xlabel("time [s]")
        ax.set_ylabel(f"{var_name} [{unit}]")

    def plot_vars(self):
        fig, axes = plt.subplots(2, 2)
        self.plot_var(self.body.phi, "phi", "rad", axes[0][0])
        self.plot_var(self.body.z, "z", "m", axes[0][1])
        self.plot_var(self.body.vphi, "vphi", "rad/s", axes[1][0])
        self.plot_var(self.body.vz, "vz", "m/s", axes[1][1])
        fig.tight_layout()
        fig.savefig("output/vars.png")
