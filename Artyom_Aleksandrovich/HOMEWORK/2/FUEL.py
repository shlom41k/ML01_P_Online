###ПРОГРАММА РАСЧЕТА РАСХОДА ТОПЛИВА

#Определение функции расхода топлива
def calculate_fuel_consumption(distance, fuel_efficiency):
#Преобразование вводимых значений в числа с плавающей точкой
    distance = float(distance)
    fuel_efficiency = float(fuel_efficiency)
#Проверка условий
    if distance <= 0 or fuel_efficiency <= 0:
        return "Значения должны быть больше нуля."
#Расчет расхода топлива
    fuel_consumption = (distance / 100) * fuel_efficiency
    return fuel_consumption
#Ввод данных
#Запрос длительности пути
distance_input = input("Введите длину маршрута (км): ") 
#Запрос расхода топлива
fuel_efficiency_input = input("Введите расход топлива на 100 км: ")
#Расчет и вывод результата
result = calculate_fuel_consumption(distance_input, fuel_efficiency_input)
print(result)
