import numpy as np
import numpy.random as rd


class Perlin:
    def __init__(self, d=3):
        self.d = d

        # Compute gradient vector
        #self.GV = self.gradientVector()
        self.sigma = self.shuffle(256, 400)
        self.GV = np.array([
            [1, 1, 0], [1, -1, 0], [1, 0, 1], [1, 0, -1],
            [-1, 1, 0], [-1, -1, 0], [-1, 0, 1], [-1, 0, -1],
            [0, 1, 1], [0, 1, -1], [0, -1, 1], [0, -1, -1],
            [1, 1, 0], [-1, 1, 0], [0, -1, 1], [0, -1, -1]

        ])

    def __call__(self, x, y, z):
        L = self.dotGrad(x, y, z)
        dx = x-self.int_fl(x)
        dy = y-self.int_fl(y)
        dz = z-self.int_fl(z)

        # Interpolation
        a = self.interp(L[0], L[1], dx)
        b = self.interp(L[2], L[3], dx)
        v1 = self.interp(a, b, dy)
        c = self.interp(L[4], L[5], dx)
        d = self.interp(L[6], L[7], dx)
        v2 = self.interp(c, d, dy)

        v = self.interp(v1, v2, dz)

        return v

    def norme(self, x):
        return np.vdot(x, x)

    def shuffle(self, n, N):
        L = [i for i in range(n)]
        for k in range(N):
            aux = rd.randint(0, n)
            aux2 = rd.randint(0, n)
            L[aux], L[aux2] = L[aux2], L[aux]
        return L

    def interp(self, a, b, t):
        c = 6*t**5-15*t**4+10*t**3  # (1-np.cos(np.pi*t))/2
        return (1-c)*a + c*b

    def int_fl(self, x):
        if x > 0:
            return int(x)
        else:
            return int(x)-1

    def getGrad(self, X, Y, Z):

        i = self.sigma[(self.sigma[(self.sigma[X % 255] + Y) % 255] + Z) % 255]
        return self.GV[i % 15]

    def dotGrad(self, x, y, z):
        L = []
        xi = self.int_fl(x)
        yi = self.int_fl(y)
        zi = self.int_fl(z)
        X = np.array([[x], [y], [z]])
        for l in range(0, 2):
            for j in range(0, 2):
                for i in range(0, 2):
                    X0 = np.array([[xi+i], [yi+j], [zi+l]])
                    G = self.getGrad(xi+i, yi+j, zi+l)
                    dX = X-X0
                    L.append(G[0]*dX[0, 0]+G[1]*dX[1, 0]+G[2]*dX[2, 0])
        return L
