def function(L, V):
    return (L*V) / 100

def main():
    try:
        L = float(input("Введите длину маршрута в километрах: "))
        if L <= 0:
            raise ValueError("Длина маршрута должна быть больше 0.")

        V = float(input("Введите расход топлива на 100 километров: "))
        if V <= 0:
            raise ValueError("Расход топлива должен быть больше 0.")

        V1 = function(L, V)
        print(f"Общий расход топлива на маршруте составит: {V1:.2f} литров.")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
if __name__ == "__main__":
    main()