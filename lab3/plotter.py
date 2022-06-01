import matplotlib.pyplot as plt
import numpy as np

from body import Body
from const import DT, Nt
from utils import legend_without_duplicate_labels

COLOR = {
    "ex1": "#F55D3E",
    "ex2": "#878E88",
    "ex3": "#F7CB15",
    "ex4": "#76BED0"
}


class Plotter:
    def __init__(self, bodies: dict[str, Body]):
        self.bodies = bodies

    def plot_trajectory(self, name: str):
        print("Plotting trajectory...")
        fig = plt.figure()
        x, y, z = self.bodies[name].get_coordinates()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot3D(x, y, z, color=COLOR[name])
        x2, y2, z2 = np.meshgrid(
            np.linspace(x.min(), x.max(), 10),
            np.linspace(y.min(), y.max(), 10),
            np.linspace(z.min(), z.max(), 10)
        )
        ax.quiver(x2, y2, z2, 0, 0, 0.01, length=1)
        fig.savefig(f"output/{name}.png")

    def plot_vars(self):
        fig, axes = plt.subplots(2, 3)
        for name in self.bodies:
            t = np.linspace(0, Nt * DT, Nt)
            x, y, _ = self.bodies[name].get_coordinates()
            e = self.bodies[name].get_energy()
            if name == "ex1":
                axes[0][0].plot(x, y, "o", label=name, color=COLOR[name])
                axes[0][1].plot(t, e, ".", color=COLOR[name])
                axes[0][2].plot(
                    t, self.bodies[name].r,
                    ".", color=COLOR[name])
                axes[1][0].plot(t, self.bodies[name].phi, ".", color=COLOR[name])
                axes[1][1].plot(t, self.bodies[name].pr, ".", color=COLOR[name])
                axes[1][2].plot(t, self.bodies[name].pphi, ".", color=COLOR[name])
                continue
            axes[0][0].plot(x, y, color=COLOR[name])

            axes[0][1].plot(t, e, label=name, color=COLOR[name])
            axes[0][2].plot(
                t, self.bodies[name].r, color=COLOR[name]
            )
            axes[1][0].plot(t, self.bodies[name].phi, color=COLOR[name])
            axes[1][1].plot(t, self.bodies[name].pr, color=COLOR[name])
            axes[1][2].plot(t, self.bodies[name].pphi, color=COLOR[name])
        axes[0][0].set_xlabel("x(t)")
        axes[0][0].set_ylabel("y(t)")
        axes[0][1].set_xlabel("t")
        axes[0][1].set_ylabel("E")
        axes[0][2].set_xlabel("t")
        axes[0][2].set_ylabel("r")
        axes[1][0].set_xlabel("t")
        axes[1][0].set_ylabel(u"\u03C6")
        axes[1][1].set_xlabel("t")
        axes[1][1].set_ylabel("Pr")
        axes[1][2].set_xlabel("t")
        axes[1][2].set_ylabel("P\u03C6")

        fig.legend()
        legend_without_duplicate_labels(fig)

        fig.tight_layout()

        fig.savefig("output/vars.png")
