"""
**
задание для самых  любопытных ))

сделать анимацию снежинок елки с выводом в консоль
образец и описание в файле example\elka_animate.py

"""

from random import Random
from rich.console import Console

random = Random()
console = Console()


def new_sky_line(columns):
    """Создаёт строку неба из columns символов случайно заполненных пробелами, точками, звездочками"""
    return "".join(random.choice("   ..   ''   \"   * ") for _ in range(columns))


# функция замыкание которая помнит небо из rows строк
# и каждый раз возвращает полное небо
def sky(rows, columns):
    """
    Создаёт замыкание которое помнит небо из rows строк
    и каждый раз возвращает полное небо как то модифицированное (зависит от inner_sky)
    """
    all_sky = [new_sky_line(columns) for _ in range(rows)]
    wind = 0

    # каждый раз сдвижает небо на одну строку вверх (снег летит наверх)
    def inner_sky_up():
        all_sky.pop(0)
        all_sky.append(new_sky_line(columns))
        return "\n".join(all_sky)

    # каждый раз сдвижает небо на одну строку вниз
    def inner_sky_down():
        all_sky.pop(-1)
        all_sky.insert(0, new_sky_line(columns))
        return "\n".join(all_sky)

    # каждый раз сдвигает небо на одну строку вниз и все строки на один символ вправо
    def inner_sky_down_right():
        nonlocal all_sky, wind

        all_sky.pop(-1)
        all_sky.insert(0, new_sky_line(columns))
        wind = int(wind / 2 + random.randint(-1, 2))
        # склеиваем строки сдвинутые на x символов вправо
        all_sky = [all_sky[i][wind:] + all_sky[i][:wind] for i in range(rows)]
        return "\n".join(all_sky)

    # # стабильное небо, стоит на месте
    # def inner_sky():
    #     return "\n".join(all_sky)

    return inner_sky_down_right


def add_tree(all_sky: list, tree_height):
    """
    Получает небо в виде списка строк и добавляет на него елку
    в крайнюю правую часть,
    заменяя символы неба на ▲
    """
    for i in range(tree_height):
        all_sky[i] = (
            all_sky[i][: tree_height - i - 1]
            + "▲" * (i * 2 + 1)
            + all_sky[i][tree_height + i + 1 :]
        )

    return all_sky


def print_rastr(rastr_list: list):
    """
    Выводит список строк в консоль и стирает их
    """
    for i in rastr_list:
        print(i)
    print("\b" * len(rastr_list), end="", flush=True)


import time


sky = sky(30, 80)

while 1:
    rastr = sky().split("\n")
    rastr = add_tree(rastr, 30)
    print_rastr(rastr)
    time.sleep(0.1)
