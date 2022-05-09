import numpy as np
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, x, y, params: dict={}):
        self.x = x
        self.y = y
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.params = params

    def plot(self):
        self.ax.set_xlabel(self.params.get('xlabel', 'x'))
        self.ax.set_ylabel(self.params.get('ylabel', 'y'))
        self.ax.set_title(self.params.get('title', ''))
        self.ax.set_xlim(self.params.get("xmin", -1), self.params.get("xmax", 1))
        self.ax.set_ylim(self.params.get("ymin", -1), self.params.get("ymax", 1))
        self.ax.plot(self.x, self.y)
        return self.fig.show()
    
    def show(self):
        self.fig.show()

    def save(self, filename):
        self.fig.savefig(filename)
