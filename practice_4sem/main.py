import numpy as np
import matplotlib.pyplot as plt
# import sympy
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Производные решать с использованием машинного обучения, функция задается пользователем руками,
# функции линейные и нелинейные. Плюс, строить график производной и сопоставить с реальным значением.


def numeric_deriv(f, x, h=0.00001):
    """Посчитать численно производную ф-ции f на x"""

    fx = f(x)  # значение в оригинальной точке
    fxph = f(x + h)  # значение в x + h
    fxmh = f(x - h)  # значение в x - h
    grad = (fxph - fxmh) / (2 * h)  # производная
    return grad


def predict_deriv(X_train, y_train, x):
    """
    Линейная регрессия для предсказания производной
    :param f – функция
    :param X_train – данные для обучения (области X)
    :param y_train – известные ответы производной f для X_train
    :param x – данные, для которых надо предсказать зн. производной

    :returns предсказания для x
    """
    lr = LinearRegression()  # инициализация модели
    lr.fit(X_train.reshape(-1, 1), y_train)
    return lr.predict(x.reshape(-1, 1))


def predict_deriv_poly(X_train, y_train, x, p=3):
    """
    Полиномиальная регрессия для предсказания производной
    :param f – функция
    :param X_train – данные для обучения (области X)
    :param y_train – известные ответы производной f для X_train
    :param x – данные, для которых надо предсказать зн. производной
    :param p – степень полинома (большая ведет к переобучению)

    :returns предсказания для x
    """

    def gen_poly(x):
        # новый массив, в котором содержатся степени исходного
        # массива от 0 до p-1
        return np.array([np.power(x, i) for i in range(p)]).T
    X_poly = gen_poly(X_train)

    # инициализация модели
    lr = LinearRegression().fit(X_poly, y_train)
    return lr.predict(gen_poly(x))


# ЛИНЕЙНАЯ РЕГРЕССИЯ
# может улавливать только линейные зависимости,
# поэтому в примере производная x^2

def linear(f):
    # определим X
    lp = np.linspace(-2, 2)

    # посчитаем настоящий градиент
    grad = [numeric_deriv(f, x) for x in lp]

    # предсказания для этого градиента
    predicted_grad = predict_deriv(lp, grad, lp)

    plt.plot(lp, grad, label='actual')
    plt.plot(lp, predicted_grad, label='predicted')
    plt.legend()
    plt.show()
    print(f"MSE: {mean_squared_error(grad, predicted_grad)}")


# ПОЛИНОМИАЛЬНАЯ РЕГРЕССИЯ

def polynomial(f, p=3):
    # определим X
    lp = np.linspace(-2, 2)

    # посчитаем настоящий градиент
    grad = [numeric_deriv(f, x) for x in lp]

    # предсказания для этого градиента
    # регулируя p можно улучшать модель
    predicted_grad = predict_deriv_poly(lp, grad, lp, p)

    plt.plot(lp, grad, label='actual')
    plt.plot(lp, predicted_grad, label='predicted')
    plt.legend()
    plt.show()
    print(f"MSE: {mean_squared_error(grad, predicted_grad)}")


if __name__ == "__main__":
    # пусть задана функция x^2
    f = lambda x: x ** 2
    linear(f)
    # пусть задана функция x^3
    f = lambda x: x ** 2 + 3 * x ** 3
    linear(f)

    # пусть задана функция x^5
    f = lambda x: x ** 5
    polynomial(f)
    # пусть задана функция x^5
    f = lambda x: x ** 6 + np.log(x+2.1)
    polynomial(f, 5)

