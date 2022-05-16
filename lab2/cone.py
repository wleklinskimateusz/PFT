import numpy as np
from const import DT, G, ALPHA, SINA, COSA, THETA
import matplotlib.pyplot as plt

def debug(var: any, name: str):
    print(f"Variable {name} = {var}")
    print("Type:", type(var))

def cone_func(t: float, vars: np.ndarray) -> np.ndarray:
    debug(vars, "vars")
    return np.array([
        vars[2],
        vars[3],
        -G * COSA ** 2 / SINA * np.sin(vars[0]) / vars[1] - 2 * vars[2] * vars[3] / vars[1],
        SINA**2 * vars[1] * vars[2] ** 2 - G * SINA * COSA ** 2 * (1 - np.cos(vars[0]))

    ])

def get_cone(x_obj, y_obj):
    R = get_rotation_matrix()
    step = 0.05
    xlim = max([np.abs(x_obj.min()), np.abs(x_obj.max())])
    ylim = max([np.abs(y_obj.min()), np.abs(y_obj.max())])
    mlim = max([xlim, ylim])
    X = np.arange(-mlim, mlim, step)
    Y = np.arange(-mlim, mlim, step)
    num_steps = len(X)
    X, Y = np.meshgrid(X, Y)
    Z = np.sqrt(X**2 + Y**2) / np.tan(ALPHA)
    X = X.reshape((-1))
    Y = Y.reshape((-1))
    Z = Z.reshape((-1))
    t = np.array([X, Y, Z])
    X, Y, Z = np.dot(R, t)
    X = X.reshape(num_steps, num_steps)
    Y = Y.reshape(num_steps, num_steps)
    Z = Z.reshape(num_steps, num_steps)

    return X, Y, Z

def get_rho(z: np.ndarray) -> np.ndarray:
    return z * np.tan(ALPHA)

def get_x(rho: np.ndarray, phi: np.ndarray) -> np.ndarray:
    return rho * np.cos(phi)

def get_y(rho: np.ndarray, phi: np.ndarray) -> np.ndarray:
    return rho * np.sin(phi)


def rk4_solve(t, vars: np.ndarray, func) -> np.ndarray:
    k1 = func(t, vars)
    k2 = func(t + DT/2, vars + DT/2*k1)
    k3 = func(t + DT/2, vars + DT/2*k2)
    k4 = func(t + DT, vars + DT*k3)
    return DT/6*(k1 + 2*k2 + 2*k3 + k4)

def get_rotation_matrix():
    return np.array([
        [np.cos(THETA), 0, np.sin(THETA)],
        [0, 1, 0],
        [-np.sin(THETA), 0, np.cos(THETA)]
    ])

class BodyOnCone:
    def __init__(self, phi0, z, vphi, vz, max_time = 300):
        self.vars = np.array([phi0, z, vphi, vz])
        self.t = 0
        self.phi = np.zeros(max_time)
        self.z = np.zeros(max_time)
        self.vphi = np.zeros(max_time)
        self.vz = np.zeros(max_time)
        self.max_time = max_time

    def get_coordinates(self, rotate: bool = False) -> list:
        R = get_rotation_matrix()
        rho = get_rho(self.z)
        x = np.array([get_x(rho, self.phi), get_y(rho, self.phi), self.z])
        if rotate:
            return list(np.dot(R, x))
        return x

    def run(self):
        for i in range(self.max_time):
            self.t += DT
            self.vars += rk4_solve(self.t, self.vars, cone_func)
            self.phi[i] = self.vars[0]
            self.z[i] = self.vars[1]
            self.vphi[i] = self.vars[2]
            self.vz[i] = self.vars[3]

    def plot(self):
        x, y, z = self.get_coordinates(rotate=True)
        ax = plt.axes(projection='3d')
        ax.plot3D(x, y, z, 'red')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        cx, cy, cz = get_cone(x, y)
        ax.plot_surface(cx, cy, cz, color='b', alpha=0.2)
        plt.show()

if __name__ == "__main__":
    body = BodyOnCone(3.3, 5, 0, 0, 300)
    body.run()
    body.plot()
