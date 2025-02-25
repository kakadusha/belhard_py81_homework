"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать красным "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать зеленым "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать желтым "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать белым "----- лук ------"

Написать функцию beef, которая:
 - печатает красным "### говядина ###"

Написать функцию chicken, которая:
 - печатает серым "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""

from rich.console import Console

console = Console()


def bread_upper(func):
    def wrapper(*args, **kwargs):
        print("/------------\\")
        func(*args, **kwargs)

    return wrapper


def bread_lower(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("\\____________/")

    return wrapper


def tomato(func):
    def wrapper(*args, **kwargs):
        console.print("***помидоры***", style="red")
        func(*args, **kwargs)

    return wrapper


def salad(func):
    def wrapper(*args, **kwargs):
        console.print("~~~ салат ~~~-", style="green")
        func(*args, **kwargs)

    return wrapper


def cheese(func):
    def wrapper(*args, **kwargs):
        console.print("^^^^^ сыр ^^^\\", style="yellow")
        func(*args, **kwargs)

    return wrapper


def onion(func):
    def wrapper(*args, **kwargs):
        console.print("-----лук------", style="rgb(95,30,145)")
        func(*args, **kwargs)

    return wrapper


def beef(func):
    def wrapper(*args, **kwargs):
        console.print("###говядина###", style="rgb(145,30,45)")
        func(*args, **kwargs)

    return wrapper


def chicken(func):
    def wrapper(*args, **kwargs):
        console.print("||||курица||||", style="rgb(185,180,155)")
        func(*args, **kwargs)

    return wrapper


@bread_upper
@onion
@tomato
@beef
@bread_lower
def hamburger():
    pass


@bread_upper
@cheese
@salad
@chicken
@bread_lower
def chickenburger():
    pass


if __name__ == "__main__":
    print("\nСборка гамбургера")
    hamburger()
    print("\nСборка чикенбургера")
    chickenburger()
    print("\nСборка чикенбургер экстра сыр")
    chickenburger_extra_cheese = cheese(cheese(chickenburger))
    chickenburger_extra_cheese()
