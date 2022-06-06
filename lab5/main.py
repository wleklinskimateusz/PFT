import os
import numpy as np
from const import DT
from plotter import Plotter
from solver import Solver

def main():
    s = Solver(25)
    if os.path.exists("V.npy"):
        s.load_from_file("V.npy")
    else:
        s.solve()
        s.save_to_file("V.npy")
    p = Plotter(s)
    p.plot_last_frame()
    p.plot_Vz()
    p.plot_Vrho()


if __name__ == "__main__":
    main()