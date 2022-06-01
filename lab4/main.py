from matplotlib import pyplot as plt
import numpy as np
from animator import Animator
from const import N
from utils import show_frame
from plotter import Plotter
from solver import Solver


def main():
    s = Solver(1000)
    s.initialize_gaussian()

    s.calculate()
    # a = Animator(s)
    # a.animate()
    p = Plotter(s)
    p.plot_energy()

if __name__ == "__main__":
    main()