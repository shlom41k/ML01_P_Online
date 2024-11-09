###ЗНАЧЕНИЯ ФУНКЦИИ
#Функция
def f(x):
    return -26*x**2 + 25*x - 9
#Задание начальных условий
start = -5
end = 5
step = 0.1
#Переменнные для хранения наибольшего и наименьшего значений
max_val = f(start)
min_val = f(start)
max_x = start
min_x = start
#Переменная для текущего значения x
x = start
#Поиск наибольшего и наименьшего значений функции на отрезке [-5,5]
while x <= end:
    y = f(x)
    if y > max_val:
        max_val = y
        max_x = x
    if y < min_val:
        min_val = y
        min_x = x
    x += step
#Вывод результатов
print(f"Максимальное значение функции на отрезке [-5, 5]: y({max_x}) = {max_val}")
print(f"Минимальное значение функции на отрезке [-5, 5]: y({min_x}) = {min_val}")
#Нахождение особой точки
special_x = 25 / 52
special_y = f(special_x)
print(f"Особая точка: x = {special_x}, y = {special_y}")
