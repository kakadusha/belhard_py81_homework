"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    """
    Функция принимает
    """
    args_sum = 0
    kwargs_max_len = 0
    # с помощью all() проверяем, что все элементы в args - целые числа
    if not args:
        args_sum = None
    else:
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError("Все позиционные аргументы должны быть целыми")
        args_sum = sum(args)

    # с помощью all проверяем что все ключи в kwargs - строки
    if not kwargs:
        kwargs_max_len = None
    else:
        if not all(isinstance(key, str) for key in kwargs.keys()):
            raise TypeError("Все аргументы - ключевые слова должны быть строками")
        kwargs_max_len = max(map(len, kwargs.keys()))

    return {"args_sum": args_sum, "kwargs_max_len": kwargs_max_len}


if __name__ == "__main__":
    print(
        dict_from_args(
            1,
            222,
            322,
            444,
            5,
            a="aw",
            b="bh",
            c="c",
        )
    )
    print(dict_from_args(1, a="aw"))
    print(dict_from_args(1))
    print(dict_from_args(a=1))
