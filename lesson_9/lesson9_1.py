"""
Написать функцию print_n() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
кокай раз по счету выполняется эта функция. 
"""


def print_n(text, counter):
    """рекурсивная функция печати текста с номером"""
    if counter > 0:
        # нужен еще один вызов
        print_n(text, counter - 1)
        # печатаем текст
        print(f"[{counter}] {text}")
    elif counter < 0:
        raise ValueError(f"counter must be greater than 0, got: {counter}")


if __name__ == "__main__":
    print("Test print_n()")
    print_n("Hello, Recursive World 5!", 5)
    print()
    print_n("Hello, Recursive World 3!", 3)
    print()
    print_n("Hello, Recursive World 1!", 1)
    print()
    print_n("Hello, Recursive World 0!", 0)
    print()
    try:
        print_n("Hello, World -1!", -10)
    except ValueError as e:
        print(f"Got error on negative count: {e}")

    print("Test print_n() done")
