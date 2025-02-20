"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""


def catch_error(output="console"):
    """
    Декоратор для перехвата ошибок в функции
    :param func: функция
    :param output: вывод в консоль ("console") или в файл (путь к файлу)
    :return: обернутая функция
    """

    def _catch_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if output == "console":
                    print(f"О ужас: ошибка в функции {func.__name__}: {e}")
                else:
                    with open(output, "a", encoding="utf-8") as f:
                        f.write(f"О ужас: ошибка в функции {func.__name__}: {e}\n")

        return wrapper

    return _catch_error


@catch_error(output="./error.log")
def func1(x, y):
    """
    Функция деления
    :param x: делимое
    :param y: делитель
    :return: результат деления
    """
    return x / y


if __name__ == "__main__":
    func1(0, 0)
