import os
import numpy as np
from const import DT, G, ALPHA, SINA, COSA, M
import matplotlib.pyplot as plt

from utils import cone_func, get_rho, get_rotation_matrix, get_x, get_y, rk4_solve


class BodyOnCone:
    def __init__(self, phi0, z, vphi, vz, steps=500):
        self.vars = np.array([phi0, z, vphi, vz])
        self.t = 0
        self.phi = np.zeros(steps)
        self.z = np.zeros(steps)
        self.vphi = np.zeros(steps)
        self.vz = np.zeros(steps)
        self.steps = steps
        self.energies = np.zeros(steps)

    def get_coordinates(self, rotate: bool = False) -> list:
        R = get_rotation_matrix()
        rho = get_rho(self.z)
        x = np.array([get_x(rho, self.phi), get_y(rho, self.phi), self.z])
        if rotate:
            return list(np.dot(R, x))
        return x

    def get_energy(self):
        return 0.5 * M *((SINA/COSA)**2 * self.vars[1]**2*self.vars[2]**2 + (self.vars[3]**2 / COSA ** 2)) + G * self.vars[1] * SINA * (1 - np.cos(self.vars[0]))

    def run(self):
        self.energies[0] = self.get_energy()
        for i in range(self.steps):
            self.t += DT
            self.vars += rk4_solve(self.t, self.vars, cone_func)
            self.phi[i] = self.vars[0]
            self.z[i] = self.vars[1]
            self.vphi[i] = self.vars[2]
            self.vz[i] = self.vars[3]
            self.energies[i] = self.get_energy()


    
