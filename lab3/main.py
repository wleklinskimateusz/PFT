import numpy as np

from const import DT, Q, B
from body import Body
from utils import make_dir
from plotter import Plotter


def ex1():
    body = Body(
        1.5,
        1.25*np.pi,
        0,
        0,
        Q * B * 1.5 ** 2 / 2, 0
    )
    body.run()
    return body


def ex2():
    body = Body(
        1, 0, 0, 0, -Q*B*1**2 / 2, 0
    )
    body.run()
    return body


def ex3():
    body = Body(
        2, 0, 0, 0, -Q*B*2**2 / 2, 0
    )
    body.run()
    return body


def ex4():
    body = Body(
        2, 0, 0, 2, -Q*B*2**2 / 2, 0
    )
    body.run()
    return body


def main():
    make_dir("output")
    bodies = {}
    bodies["ex1"] = ex1()
    bodies["ex2"] = ex2()
    bodies["ex3"] = ex3()
    bodies["ex4"] = ex4()
    p = Plotter(bodies)
    p.plot_vars()

    for ex in bodies:
        p.plot_trajectory(ex)


if __name__ == "__main__":
    main()
