import os

from cone import BodyOnCone
from plotter import Plotter
from utils import make_dir


if __name__ == "__main__":
    make_dir("output")
    # body = BodyOnCone(0.1, 0.1, 0., 0.1, 500) # interesting initial conditions
    body = BodyOnCone(1.1, 1.0, 0., 0.0, 500) # original initial conditions
    p = Plotter(body)
    body.run()
    print("Finished running simulation")
    p.plot_trajectory()
    p.plot_energy()
    p.plot_vars()