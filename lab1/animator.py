from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


class Animator:
    def __init__(self, x, y, params: dict = {}):
        self.x = x
        self.y = y
        self.fig = plt.figure()
        self.axis = plt.axes(xlim=(params.get("xmin", -1), params.get("xmax", 1)),
                             ylim=(params.get("ymin", -1), params.get("ymax", 1)))
        self.point, = self.axis.plot([], [], 'ro', lw=3)
        self.line, = self.axis.plot([], [], '-', lw=3)
        self.params = params

    def setup(self):
        self.point.set_data([], [])
        self.line.set_data([], [])
        return self.line,

    def animate(self, i):
        self.line.set_data([0, self.x[i]], [0, self.y[i]])
        self.point.set_data(self.x[i], self.y[i])
        return self.point, self.line

    def run(self):
        print("siema")
        anim = FuncAnimation(self.fig, self.animate, init_func=self.setup, frames=self.params.get(
            "frames", 100), interval=self.params.get("interval", 20), blit=True)
        anim.save('pendulum.gif', writer='imagemagick')
