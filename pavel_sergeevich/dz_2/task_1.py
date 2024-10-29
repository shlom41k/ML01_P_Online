"""
Напишите программу, которая ищет корни квадратного уравнения вида a*x*x+b*x+c. На вход программы подаются a,b,c.
Результатом работы программы – действительные корни или сообщение что корней нет.
"""

import math


def get_roots(c_a: float, c_b: float, c_c: float):
    if c_a == 0:
        print("Error: invalid coefficients")
        return None

    discriminant = c_b**2 - 4*c_a*c_c

    if discriminant < 0:
        print("Quadratic equation not have real roots.")
        return None
    elif discriminant == 0:
        one_root = -c_b/(2*c_a)
        print("Quadratic equation have your one real root:", one_root)
        return one_root
    else:
        first_root = (-c_b - math.sqrt(discriminant))/(2*c_a)
        second_root = (-c_b + math.sqrt(discriminant))/(2*c_a)

        print("Quadratic equation have your two real roots:", first_root, second_root)

        return first_root, second_root


if __name__ == "__main__":
    # можно построить графики онлайн: https://www.desmos.com/calculator/g6ikxtneep?lang=ru

    # 2 roots
    get_roots(10, 24, 3)

    # 2 roots
    get_roots(1, -6, 9)

    # no roots
    get_roots(10, 1, 2)

    # error
    get_roots(0, 24, 3)