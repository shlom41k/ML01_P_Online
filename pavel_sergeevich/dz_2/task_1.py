"""
Напишите программу, которая ищет корни квадратного уравнения вида a*x*x+b*x+c. На вход программы подаются a,b,c.
Результатом работы программы – действительные корни или сообщение что корней нет.
"""

"""
Решение и выводы: написана функция, реализующая решение задачи. Расчет кореней осуществлялся через дискриминант. 
Как известно, для квадратного уравнения, если дискриминант меньше нуля, то  действительных корней в уравнении нет
(есть комплексные), если равен нулю - то корень один (или, вернее, два одинаковых) и, наконец, если дискриминант
больше нуля, уравнение имеет два действительных корня. Помимо этого реализовал функцию построения графика функции
на основе библиотеки matplotlib
"""

import math

import matplotlib.pyplot as plt
import numpy as np


def get_roots(c_a: float, c_b: float, c_c: float):
    if c_a == 0:
        print("Error: invalid coefficients")
        return None

    discriminant = c_b ** 2 - 4 * c_a * c_c

    if discriminant < 0:
        print("Quadratic equation not have real roots.")
        return None
    elif discriminant == 0:
        one_root = -c_b / (2 * c_a)
        print("Quadratic equation have your one real root:", one_root)
        return one_root
    else:
        first_root = (-c_b - math.sqrt(discriminant)) / (2 * c_a)
        second_root = (-c_b + math.sqrt(discriminant)) / (2 * c_a)

        print("Quadratic equation have your two real roots:", first_root, second_root)

        return first_root, second_root


def show_equation(c_a: float, c_b: float, c_c: float):
    x = np.linspace(-10, 10, 100)
    y = c_a*x*x + c_b*x + c_c

    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=2.0)

    plt.grid()
    plt.show()


if __name__ == "__main__":
    # 2 roots
    get_roots(10, 24, 3)
    show_equation(10, 24, 3)

    # 2 roots
    get_roots(1, -6, 9)
    show_equation(1, -6, 9)

    # no roots
    get_roots(10, 1, 2)
    show_equation(10, 1, 2)

    # error
    get_roots(0, 24, 3)
