from sympy.physics.vector import ReferenceFrame
from sympy.physics.vector import curl, divergence
from sympy.physics.mechanics import cross
import matplotlib.pyplot as plt
import numpy as np
import sympy as sm

R = ReferenceFrame('R')


def vector_mul(a, b):
    return cross(a, b)


def div(a):
    return divergence(a, R)


def rot(a):
    return curl(a, R)


if __name__ == '__main__':
    # базис пространства
    R = ReferenceFrame('R')

    # (y^2*z,-xy,z^3) – вектор, функции в координатах
    a = R[1] ** 2 * R[2] * R.x - R[0] * R[1] * R.y + R[2] ** 3 * R.z
    # (x^2*z,-xy,z)
    b = R[0] ** 2 * R[2] * R.x - R[0] * R[1] * R.y + R[2] * R.z
    # (y*z,-xy,xy)
    c = R[1] * R[2] * R.x - R[0] * R[1] * R.y + R[0] * R[1] * R.z

    # [a, b] x rot(C)
    res1 = cross(a, b).dot(rot(c))
    res1 = res1.expand().simplify()

    # b x (div A) * c - a x (div B) * c
    res2 = b.dot(div(a) * c) - a.dot(div(b) * c)
    res2 = res2.expand().simplify()

    # выражения, которые получились
    print(res1.evalf(subs={"R_x": 1, "R_y": 1, "R_z": 1}),
          res2.evalf(subs={"R_x": 1, "R_y": 1, "R_z": 1}))

    # составление python функций из выражения
    f1 = sm.lambdify(res1.free_symbols, res1, "numpy")
    f2 = sm.lambdify(res2.free_symbols, res2, "numpy")

    # генерация данных
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    Z = np.arange(-5, 5, 0.25)

    # разница значений функций
    print(f1(X, Y, Z) - f2(X, Y, Z))
