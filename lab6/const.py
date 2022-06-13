import numpy as np

mu0 = 1
eps0 = 1
R = 1
sigma = 1
omega = 1
alpha = 0


N = 201
M = 201
L = 3
K = 41
DX = 2 * L / K
DY = DX

DTHETA = np.pi / N
DPHI = 2 * np.pi / M

w = np.array([omega * np.sin(alpha), omega * np.cos(alpha), 0])
