
import numpy as np

from const import B, DT, M, Q, Nt
from utils import get_derrivatives, rk4_solve


class Body:
    def __init__(self, r0: float, phi0: float, z0: float, pr0: float, pphi0: float, pz0: float):
        self.vars = np.array([
            r0, phi0, z0, pr0, pphi0, pz0
        ])
        self.t = 0
        self.r = np.zeros(Nt)
        self.phi = np.zeros(Nt)
        self.z = np.zeros(Nt)
        self.pr = np.zeros(Nt)
        self.pphi = np.zeros(Nt)
        self.pz = np.zeros(Nt)

    def run(self):
        print("Running Simulation")
        for i in range(Nt):
            self.t += DT
            self.r[i] = self.vars[0]
            self.phi[i] = self.vars[1]
            self.z[i] = self.vars[2]
            self.pr[i] = self.vars[3]
            self.pphi[i] = self.vars[4]
            self.pz[i] = self.vars[5]
            self.vars += rk4_solve(self.t, self.vars, get_derrivatives)
        print("Finished running")

    def get_energy(self):
        return 1 / (2 * M) * (self.pr**2 + self.pphi**2 / self.r ** 2 + self.pz ** 2) - Q * B / (2 * M) * self.pphi + Q**2 * B ** 2 / (8*M) * self.r**2

    def get_coordinates(self) -> list:
        print("Calculating coordinates...")
        x = self.r * np.cos(self.phi)
        y = self.r * np.sin(self.phi)
        return np.array([x, y, self.z])
