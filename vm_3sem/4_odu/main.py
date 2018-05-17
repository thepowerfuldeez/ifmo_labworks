import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import scipy.integrate as integrate


def f1(t, phi):
    u, udot = t
    return [udot, -u + sqrt(u)]


def f2(t, y):
    return 0.01 * y * (1 - y)


def f3(t, y):
    return y**3


def f4(t, y):
    return 1 / np.log(y)


def f5(t, y):
    return np.sin(y) ** 2


if __name__ == '__main__':
    n = input("Choose precision (n) (Enter for 2000): ")
    if not n:
        n = 2000
    else:
        n = int(n)
    i = int(input("Choose function:\n 1. -u + sqrt(u)\n 2. 0.01*y*(1-y) \n 3. y**3 \n 4. 1/log(y) \n 5. sin(y) ** 2\n"))
    tends = [7 * np.pi, 3000, 100, 100, 3]
    tend = input(f"Choose end of interpolation range (Enter for {tends[i - 1]}): ")
    if not tend:
        tend = tends[i - 1]
    else:
        tend = float(tend)
    tinits = [[1.49907, 0], 0.5, -1, 10, 0.1]
    tinit = input(f"Choose initial point (Enter for {tinits[i - 1]}): ")
    if not tinit:
        tinit = tinits[i - 1]
    else:
        float(tinit)

    if i == 1:
        sqrt = np.sqrt
        cos = np.cos
        sin = np.sin

        phi = np.linspace(0, tend, n)
        t = integrate.odeint(f1, tinit, phi)
        u, udot = t.T
        fig, ax = plt.subplots()
        ax.plot(1 / u * cos(phi), 1 / u * sin(phi))
        ax.set_aspect('equal')
        plt.grid(True)
        plt.show()
    elif i == 2:
        trange = np.linspace(0.1, tend, n)
        f = f2
    elif i == 3:
        trange = np.linspace(0.1, tend, n)
        f = f3
    elif i == 4:
        trange = np.linspace(2, tend, n)
        f = f4
    elif i == 5:
        trange = np.linspace(-3, tend, n)
        f = f5

    if i > 1:
        t = integrate.odeint(f, tinit, trange)
        plt.plot(trange, t)
        plt.show()
