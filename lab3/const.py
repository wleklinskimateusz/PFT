from numpy import pi

N = 6
Nt = 5000
Q = 1  # C
B = 1  # T
M = 1  # kg
Wc = Q * B / M
T = 2 * pi / Wc
DT = 5 * T / Nt
