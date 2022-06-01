from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from const import DELTA, N
from solver import Solver


class Animator:
    def __init__(self, solver: Solver):
        self.solver = solver
        self.fig = plt.figure()
        self.axis = plt.axes(xlim=(0, N*DELTA), ylim=(-1, 1))
        self.ln, = self.axis.plot([], [], 'o')
        self.xdata = []
        self.ydata = []

    def init(self):
        self.xdata = [i * DELTA for i in range(N+2)]
        self.ydata = np.zeros((N+2))
        return self.ln,

    def update(self, i):

        if i % 100 == 0:
            print(f"Frame: {i}, {200*i/self.solver.nt}%")
            # print(self.solver.vars[:, 2*i])
        self.xdata = self.solver.vars[:N+2, 2*i]
        self.ln.set_data(self.xdata, self.ydata)
        return self.ln

    def animate(self):
        ani = FuncAnimation(self.fig, self.update,
                            frames=self.solver.nt//2, init_func=self.init)
        print("Saving animation...")
        ani.save("atoms.gif", fps=30)
        print("Saved!")
