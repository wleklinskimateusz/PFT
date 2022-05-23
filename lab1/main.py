import os
import matplotlib.pyplot as plt
from utils import get_kinetic_energy, get_potential_energy
from pendulum import Pendulum
import numpy as np


from const import G, R, M, DT


def plot_energy(pendulum: Pendulum, times: np.ndarray, angle: float, r: np.ndarray, energy_ax: plt.Axes):
    K = get_kinetic_energy(M, pendulum.vphi * R)
    P = get_potential_energy(M, r[1, :] + R)
    E = K + P
    energy_ax.set_title(f"\u03C6 = {angle}\u00B0")
    energy_ax.set_xlabel("time [s]")
    energy_ax.set_ylabel("energy [J]")
    energy_ax.plot(times, E, label="Total Energy")
    energy_ax.plot(times, K, label="Kinetic Energy")
    energy_ax.plot(times, P, label="Potential Energy")


def plot_phase(pendulum: Pendulum, angle: float, phase_ax: plt.Axes):
    phase_ax.set_xlabel("$\u03C6$ [rad]")
    phase_ax.set_ylabel("$\dot{\u03C6} [rad/s]$")
    phase_ax.plot(pendulum.phi, pendulum.vphi, label=f"\u03C6 = {angle}\u00B0")


def teot_pendelum(A: float, times: np.ndarray) -> np.ndarray:
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
    plt.xlabel("time [s]")
    plt.ylabel("$\u03C6$ [rad]")
    plt.title(f"initial \u03C6 = {angle}\u00B0")
    plt.tight_layout()
    plt.savefig("output/ex1.png")
    plt.show()
    plt.plot(times, pendulum.phi - teot_pendelum(np.radians(angle), times))
    plt.xlabel("time [s]")
    plt.ylabel("error [rad]")
    plt.title(f"initial \u03C6 = {angle}\u00B0")
    plt.tight_layout()
    plt.savefig("output/ex1_diff.png")
    plt.show()


def second_exercise(angle: float, energy_ax: plt.Axes, phase_ax: plt.Axes):
    pendulum = Pendulum(np.radians(angle), 0, 1000)
    pendulum.run()
    r = pendulum.get_coordinates()
    times = np.linspace(0, 10, 1000)
    plot_energy(pendulum, times, angle, r, energy_ax)
    plot_phase(pendulum, angle, phase_ax)
    return pendulum.get_periods()


def handle_energy_plot(energy_plt):
    energy_plt.title = "Energy"
    handles, labels = energy_plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    energy_plt.legend(by_label.values(), by_label.keys())
    energy_plt.tight_layout()
    energy_plt.savefig("output/energy.png")


def handle_phase_plot(phase_plt):
    phase_plt.legend()
    phase_plt.tight_layout()

    phase_plt.savefig("output/phase.png")


def main() -> None:
    if not os.path.exists("output"):
        os.mkdir("output")
    first_exercise(4)
    angles = [45, 90, 135, 175]
    energy_plt, Eaxes = plt.subplots(2, 2)
    phase_plt, Pax = plt.subplots()

    T = []
    Terr = []
    for i, angle in enumerate(angles):
        period = second_exercise(angle, Eaxes[i//2, i % 2], Pax)
        T.append(period.mean())
        Terr.append(period.std())


    handle_energy_plot(energy_plt)
    handle_phase_plot(phase_plt)
    plt.show()
    plt.scatter(angles, T, label="mean period")
    plt.xlabel("initial phase [degree]")
    plt.ylabel("period of oscilation [s]")
    plt.tight_layout()
    plt.savefig("output/period.png")
    plt.show()


if __name__ == "__main__":
    main()
