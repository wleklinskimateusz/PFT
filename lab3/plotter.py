from locale import normalize
from turtle import color, width
import matplotlib.pyplot as plt
import numpy as np

from body import Body
from const import DT, Nt

COLOR = {
    "ex1": "red",
    "ex2": "blue",
    "ex3": "green",
    "ex4": "pink"
}


class Plotter:
    def __init__(self, bodies: dict[str, Body]):
        self.bodies = bodies

    def plot_trajectory(self, name: str):
        print("Plotting trajectory...")
        fig = plt.figure()
        x, y, z = self.body.get_coordinates()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot3D(x, y, z, color=COLOR[name])
        x2, y2, z2 = np.meshgrid(
            np.linspace(x.min(), x.max(), 10),
            np.linspace(y.min(), y.max(), 10),
            np.linspace(z.min(), z.max(), 10)
        )
        ax.quiver(x2, y2, z2, 0, 0, 0.01, length=1)
        fig.savefig(f"output/{name}.png")
        plt.show()
        


    def plot_vars(self):
        fig, axes = plt.subplots(2, 3)
        for name in self.bodies:
            t = np.linspace(0, Nt * DT, Nt)
            x, y, _ = self.bodies[name].get_coordinates()
            e = self.bodies[name].get_energy()
            if name == "ex1":
                axes[0][0].plot(x, y, "o", label=name, color=COLOR[name])
                axes[0][1].plot(t, e, ".", color=COLOR[name])
                continue
            axes[0][0].plot(x, y, label=name, color=COLOR[name])
            print(e)
            axes[0][1].plot(t, e, color=COLOR[name])
        fig.legend()
        fig.tight_layout()
            
        fig.savefig("output/vars.png")


