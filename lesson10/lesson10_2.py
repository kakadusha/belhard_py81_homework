"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""


def factorial(last_number=10):
    """
    Генератор факториала
    :param last_number: последнее число факториала
    :return: генератор
    """
    f = 1
    for j in range(1, last_number + 1):
        f *= j
        yield f


if __name__ == "__main__":
    MAX_NUMBER = 10
    factorial_gen = factorial(MAX_NUMBER)

    for i in range(1, MAX_NUMBER + 1):
        print(f"Шаг {i} факториал {next(factorial_gen)}")

    print("А тут должен упасть на StopIteration")
    try:
        print(next(factorial_gen))
    except StopIteration:
        print("Уппс StopIteration")

    print("Тест пассед")
