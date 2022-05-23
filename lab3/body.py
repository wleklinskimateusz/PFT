
import numpy as np


class Body:
    def __init__(self, r0: float, phi0: float, z0: float, pr0: float, pphi0: float, pz0: float, steps: int):
        self.vars = np.array([0, 0, 0, 0, 0])
        self.t = 0
        self.r = np.zeros(steps)
        self.phi = np.zeros(steps)
        self.z = np.zeros(steps)
        self.pr = np.zeros(steps)
        self.pphi = np.zeros(steps)
        self.pz = np.zeros(steps)   
        self.steps = steps
        
