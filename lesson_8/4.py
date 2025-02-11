"""
Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
"""


def money_format(value: float, curency_suffix: str = "руб.") -> str:
    """
    Функция возвращает число в виде денежной величины в формате "1 234 567.00 руб."
    value - число для форматирования
    curency_suffix - суффикс валюты
    """
    GROUP = 3

    try:
        rub, kop = str(value).split(".")
    except ValueError:
        rub, kop = str(value), "00"
    rub = list(rub)
    if len(kop) == 1:
        kop += "0"
    # если длинна рублей больше 3, то вставляем пробелы
    if len(rub) > GROUP:
        ost = len(rub) % GROUP
        if ost:
            rub.insert(ost, " ")
        for i in range(ost * 2 + GROUP, len(rub), GROUP):
            rub.insert(i, " ")
    suff_space = " " if curency_suffix else ""
    return "".join(rub) + "." + kop + suff_space + curency_suffix


if __name__ == "__main__":
    print("Тесты\n---")
    print(money_format(1234567.00, "USD"))
    print(money_format(12567.8))
    print(money_format(123567.00))
    print(money_format(1234567))
    print(money_format(1234567.89))
    print(money_format(12.89))
    print(money_format(1.89))
    print(money_format(0), "")
    print(money_format(1234567.8))
    print(money_format(1234567.00), "")
    print("---\nPassed")
