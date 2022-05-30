from matplotlib import pyplot as plt
import numpy as np
from animator import Animator
from const import N
from solver import Solver


def main():
    s = Solver()
    s.initialize_gaussian()
    plt.scatter(s.vars[:N+2, 0], np.zeros(N+2))
    plt.show()
    s.calculate()
    a = Animator(s)
    a.animate()

if __name__ == "__main__":
    main()