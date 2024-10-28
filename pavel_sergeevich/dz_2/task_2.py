"""
Напишите программу, находящую наибольшее и наименьшее значение функции y = -26*x**2+25*x-9 на отрезке [-5,5].
Для решения и используйте while и какой то шаг (например 0.1). Найти производную и особую точку.

Решение:
    - производная: y = -52*x+25
    - особая точка: 0 = -52*x + 25 -> x = -25/(-52) = 0,4808

Комментарий: коэффициенты уравнения a, b, c расставлены следующим образом:
    y = a*x**2+b*x-c
"""

import numpy as np


def equation(a: float, b: float, c: float, x: float):
    return a * (x ** 2) + b * x + c


def special_point(a: float, b: float):
    # get derivative and calculate special point

    return a * 2 / b


if __name__ == "__main__":
    # можно построить графики онлайн: https://www.desmos.com/calculator/g6ikxtneep?lang=ru

    a = -26
    b = 25
    c = -9

    x_left = -5
    x_right = 5

    # получаем особую точку
    print("Special point (x): " + str(special_point(a, b)))

    step = 0.1
    x_points = np.linspace(x_left, x_right, int((abs(x_left) + abs(x_right))/step))
    y_points = np.array([equation(a, b, c, x) for x in x_points])

    print("Total points:", len(x_points))

    print("Min value: " + str(y_points.min()))
    print("Max value: " + str(y_points.max()))
