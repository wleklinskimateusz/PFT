
from turtle import pendown
import matplotlib.pyplot as plt
from utils import get_kinetic_energy, get_potential_energy
from pendulum import Pendulum
import numpy as np

from const import G, R, M, DT

def plot_energy(pendulum: Pendulum, times: np.ndarray, angle: float, r: np.ndarray):
    K = get_kinetic_energy(M, pendulum.vphi * R)
    P = get_potential_energy(M, r[1, :] + R)
    E = K + P
    plt.plot(times, E, label="Total Energy")
    plt.plot(times, K, label="Kinetic Energy")
    plt.plot(times, P, label="Potential Energy")
    plt.xlabel("Time [s]")
    plt.ylabel("Energy [J]")
    plt.legend()
    plt.savefig(f"output/ex2_{angle}.png")
    plt.show()


def plot_phase(pendulum: Pendulum, angle: float):
    plt.plot(pendulum.phi, pendulum.vphi)
    plt.savefig(f"output/ex2_phase{angle}.png")
    plt.show()

def teot_pendelum(A: float, times: np.ndarray)->np.ndarray:
    return A*np.cos(times * (G / R)**0.5)


def first_exercise(angle: float, animate: bool = False):
    pendulum = Pendulum(np.radians(angle), 0, 1000)
    pendulum.run()
    if animate:
        pendulum.animate()
    times = np.linspace(0, 10, 1000)
    plt.plot(times, pendulum.phi, label="numeric")
    plt.plot(times, teot_pendelum(np.radians(angle), times), label="analytic")
    plt.legend()
    plt.savefig("output/ex1.png")
    plt.show()
    plt.plot(times, pendulum.phi - teot_pendelum(np.radians(angle), times))
    plt.savefig("output/ex1_diff.png")
    plt.show()

def second_exercise(angle: float):
    pendulum = Pendulum(np.radians(angle), 0, 1000)
    pendulum.run()
    r = pendulum.get_coordinates()
    times = np.linspace(0, 10, 1000)
    plot_energy(pendulum, times, angle, r)





def main() -> None:
    first_exercise(4, animate=False)
    angles = [45, 90, 135, 175]
    # energy_plt, axes = plt.subplots(len(angles), 1)

    for angle in angles:

        second_exercise(angle)


if __name__ == "__main__":
    main()
