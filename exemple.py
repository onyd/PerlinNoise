import numpy as np
from Perlin import Perlin
import matplotlib.pyplot as plt
import matplotlib.animation as ani

p = Perlin()
n = 40
a = 5
X, Y = np.meshgrid(np.linspace(-a, a, n), np.linspace(-a, a, n))
dt = 2
fig, ax = plt.subplots(figsize=(12, 5))


def data_gen(t=0):
    P = np.zeros((n, n))
    while t < 10:
        for i in range(n):
            for j in range(n):
                P[i, j] = (p(X[i, j], Y[i, j], dt*t))

        yield P

        t += 0.05


def run(data):
    P = data
    ax.cla()
    ax.contourf(X, Y, P, 30, alpha=0.65, cmap=plt.viridis())


ani = ani.FuncAnimation(fig, run, data_gen, blit=False,
                        interval=50, repeat=False)
plt.tight_layout()
plt.show()
