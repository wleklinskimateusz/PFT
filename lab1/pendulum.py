import numpy as np
from animator import Animator

from plotter import Plotter
from const import G, R, DT, M



def pendulum_func(_: float, vars: np.ndarray) -> np.ndarray:
    return np.array([vars[1], -G/R*np.sin(vars[0])])

def rk4_solve(t, vars: np.ndarray, func) -> np.ndarray:
    k1 = func(t, vars)
    k2 = func(t + DT/2, vars + DT/2*k1)
    k3 = func(t + DT/2, vars + DT/2*k2)
    k4 = func(t + DT, vars + DT*k3)
    return DT/6*(k1 + 2*k2 + 2*k3 + k4)

    

class Pendulum:
    def __init__(self, phi0, vphi0, max_time = 300):
        self.vars = np.array([phi0, vphi0])
        self.t = 0
        self.phi = np.zeros(max_time)
        self.vphi = np.zeros(max_time)
        self.max_time = max_time

    def get_coordinates(self) -> np.ndarray:
        return np.array([R * np.sin(self.phi), -R * np.cos(self.phi)])

    def get_periods(self):
        counter = 0
        amps = []
        is_positive = False
        for i in range(self.max_time):
            if self.vphi[i] > 0 and not is_positive:
                amps.append(i)
                is_positive = True
            elif self.vphi[i] < 0 and is_positive:
                is_positive = False
        periods = [amps[i+1] - amps[i] for i in range(len(amps)-1)]
        return np.array(periods) * DT

    def run(self):
        for i in range(self.max_time):
            self.t += DT
            self.vars += rk4_solve(self.t, self.vars, pendulum_func)
            self.phi[i] = self.vars[0]
            self.vphi[i] = self.vars[1]

    def plot(self, filename: str):
        cord = self.get_coordinates()
        plotter = Plotter(cord[0], cord[1], {
            "xlabel": "x",
            "ylabel": "y",
            "title": "Pendulum",
            "xmin": -1,
            "xmax": 1,
            "ymin": -1.5,
            "ymax": 0.5
        })
        plotter.plot()
        if filename:
            plotter.save("output/tor.png")

    def animate(self):
        coordinates = self.get_coordinates()
        animator = Animator(coordinates[0, :],coordinates[1, :], {
            "frames": self.max_time,
            "xmin": -1,
            "xmax": 1,
            "ymin": -1.5,
            "ymax": 0.,
            "interval": 30,
            })
        animator.run()




        