###ПОИСК КОРНЕЙ КВАДРАТНОГО УРАВНЕНИЯ

import math
#Функция для поиска корней квадратного уравнения
def find_roots(a, b, c):
#Дискриминант
    discriminant = b**2 - 4*a*c
#Условия по значению дискриминанта
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Два действительных корня: {root1} и {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"Один действительный корень: {root}"
    else:
        return "Действительных корней нет"
#Ввод данных
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
#Вывод
result = find_roots(a, b, c)
print(result)
