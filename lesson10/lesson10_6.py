"""
Написать генератор triangular_numbers, который возвращает подряд 
треугольные числа

Формула:
Tn = 1 / 2 * n * (n + 1)

Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21

Решение
 - делаем функцию замыкание, которая помнит n и каждый раз считает по формуле
 - вызываем её в цикле и дополнительно через next(), нарываемся на исключение
"""


def tn_gen(n=0, max_value=10000):
    """
    Генератор треугольных чисел
    :param n: начальное значение
    :param max_value: максимальное значение
    :return: следующее треугольное число
    """
    while True:
        n += 1
        yield int(1 / 2 * n * (n + 1))
        if n > max_value:
            break


tn = tn_gen()
# спросим с какого начать
start = int(input("С какого по порядку начать? "))
tg = tn_gen(start, 100)
for i in tg:
    try:
        # тут мы обязательно превысим максимальное значение
        print(i)
        print(next(tg))
    except StopIteration:
        print("Got StopIteration")
        break
