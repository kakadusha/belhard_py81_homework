"""
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.
"""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("Тесты\n---")
    print(factorial(5))
    print(factorial(10))
    print(factorial(0))
    print("---\nPassed")
