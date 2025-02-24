"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""


def log_decorator(func):
    """
    Декоратор для логирования
    :param func: функция
    :return: обернутая функция
    """

    def wrapper(*args, **kwargs):
        print(f"#Выполняется функция {func.__name__} с аргументами {args}")
        func(*args, **kwargs)
        print(f"#{func.__name__} - завершена")

    return wrapper


@log_decorator
def hello(name, surname):
    """
    Функция приветствия
    :param name: имя
    :param surname: фамилия
    """
    print(f" Привет, {name} {surname}")


# функция без декоратора
hello_no_decorateor = hello.__closure__[0].cell_contents

if __name__ == "__main__":
    print("> Декор")
    hello("Петр", "Петров")
    print("> А теперь без декоратора")
    hello_no_decorateor("Иван", "Бездекораторовский")
    print("> А теперь без сахара")
    hello_sugar_free = log_decorator(hello_no_decorateor)
    hello_sugar_free("Сидор", "Безсахарный")
    print("> А теперь декорируемое без сахара ")
    hello_dec_sugar_free = log_decorator(hello)
    hello_dec_sugar_free("Порфирий", "Петрович")
