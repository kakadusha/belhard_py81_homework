"""
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.
"""


def fakt(num: int):
    """
    Функция вычисляет факториал переданного числа
    """
    if num < 0:
        raise ValueError("Число не может быть отрицательным")

    return 1 if num == 0 else num * fakt(num - 1)


if __name__ == "__main__":
    print("Тесты")
    print(fakt(5))
    print(fakt(0))
    try:
        print(fakt(-1))
    except ValueError as e:
        print("Ошибка на вызове с отрицательным параметром:", e)
    print(fakt(3))
    print(fakt(70))

    print("Тесты пройдены")
