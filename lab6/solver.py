import numpy as np
from const import DX, DY, L, sigma, mu0, eps0, R, N, M, DPHI, DTHETA
from utils import coefs, get_B_element, get_E_element, get_potential_element, get_r, get_theta


class Solver:
    def __init__(self):
        self.potential = np.zeros((N, M))
        self.electric_field = np.zeros((N, M, 3))
        self.magnetic_field = np.zeros((N, M, 3))

    def calculate_step(self, r: np.ndarray) -> float:
        A = sigma * R ** 2 / (4 * np.pi * eps0) * DPHI * DTHETA / 9
        AB = - sigma * R ** 2 * mu0 / (4 * np.pi) * DPHI * DTHETA / 9
        potential = 0
        E = np.zeros(3)
        B = np.zeros(3)
        for i in range(N):
            for j in range(M):
                d = r - get_r(R, i, j)
                a, b = coefs(i, j)
                theta = get_theta(i)
                potential += get_potential_element(a, b, theta, d)
                # E += get_E_element(a, b, theta, d)
                # B += get_B_element(a, b, theta, d, r, R)

        return A * potential, A * E, AB * B

    def solve(self) -> None:
        print("Solving...")
        x_arr = np.arange(-L, L, DX)
        y_arr = np.arange(-L, L, DY)
        for xi, x in enumerate(x_arr):
            for yi, y in enumerate(y_arr):
                print(f"{x} {y}", end="\r")
                r = np.array([x, y, 0])
                self.potential[xi, yi], self.electric_field[xi, yi], self.magnetic_field[xi, yi] = self.calculate_step(r)
        print("Solved.")

    def save_to_file(self) -> None:
        np.save('potential.npy', self.potential)
        np.save('electric_field.npy', self.electric_field)
        np.save('magnetic_field.npy', self.magnetic_field)

    def load_from_file(self) -> None:
        self.potential = np.load('potential.npy')
        self.electric_field = np.load('electric_field.npy')
        self.magnetic_field = np.load('magnetic_field.npy')
