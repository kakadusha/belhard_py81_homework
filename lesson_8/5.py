"""
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!
"""

from pprint import pprint


def count_char(text: str):
    """
    Функция принимает строку и возвращает словарь вида {'буква': 'количество-вхождений-в-строку'}
    text - строка для подсчета
    """
    # удалим пробелы точки и запятые
    text = text.lower()
    text = text.replace(" ", "").replace(".", "").replace(",", "")

    result = {}
    for ch in text:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result


if __name__ == "__main__":
    pprint("Тесты\n---")
    pprint(count_char("hello world"))
    pprint(count_char("the QUICK brown fox jumps over the LAZY dog"))
    pprint(count_char("съешь ещё ЭТИХ мягких французских булок да выпей чаю"))
    pprint(count_char("a" * 1000))
    pprint(count_char(""))
    pprint("---\nPassed")
