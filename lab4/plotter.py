from matplotlib import pyplot as plt
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
