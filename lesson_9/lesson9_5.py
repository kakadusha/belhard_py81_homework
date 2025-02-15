"""
*
Написать рекурсивную функцию, которая принимает список 
и печатает каждых элемент на новой строке. 
Если элемент списка - список, то его элементы должны выводиться 
с отступом относительно родительского на 2 символа. 
Символ для отступа передать дополнительными необязательным параметром.

** написать такую же функцию но без рекурсии

Пример1: some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
1
2
3
--4
----5
----6
--7
8
9

Пример2: some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
1
--2
------3
----4
5
------6
------7
8
--------9
--------10
----11
12

"""


def wave_rec(li: list, prefix: str = ""):
    """
    Рекурсивная функция для вывода элементов списка
    """
    for element in li:
        if isinstance(element, list):
            wave_rec(element, prefix + "--")
        else:
            print(f"{prefix}{element}")


def wave_rec_no_for(li: list, prefix: str = ""):
    """
    Рекурсивная функция для вывода элементов списка не использует цикл
    """
    if li:
        element = li[0]
        if isinstance(element, list):
            # вызов функции для погружения на новый уровень
            wave_rec_no_for(element, prefix + "--")
        else:
            print(f"{prefix}{element}")
        # вызов функции для оставшейся части списка (натом же уровне)
        wave_rec_no_for(li[1:], prefix)


def wave_no_rec(li: list):
    """
    Функция для вывода элементов списка без рекурсии
    - преобразуем список к строке
    - убираем пробелы и запятые кроме тех запятых которые внутри списка
    - далее идем посимвольно
        [ - увеличиваем префикс на --,
        ] - уменьшаем префикс на --,
        9 - выводим элемент с префиксом
        , - переходим на следующий элемент
        при печати префикс печанаем на 2 символа меньше
    """
    li_str = str(li)
    li_str = li_str.replace(", [", "[").replace("], ", "]").replace(", ", ",")
    # print(li_str)
    prefix = "\n"
    in_digit = False
    for char in li_str:
        if char == "[":
            in_digit = False
            prefix += "--"
        elif char == "]":
            in_digit = False
            prefix = prefix[:-2]
        elif char.isdigit():
            if in_digit:
                print(char, end="")
            else:
                in_digit = True
                print(prefix[:-2] + char, end="")
        elif char == ",":
            in_digit = False
        else:
            print(f"Error: {char}")

    print()


# some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
some_list = [1, [2, [[3], 4]], 5, [[[6, 7]]], 8, [[[[9, 10]], 11]], 12]

print("Рекурсия и цикл")
wave_rec(some_list)

print("Рекурсия без цикла")
wave_rec_no_for(some_list)

print("Без рекурсии только цикл")
wave_no_rec(some_list)
