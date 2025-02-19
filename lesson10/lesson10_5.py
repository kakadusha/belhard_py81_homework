"""
Написать функцию счетчик которая с помощью замыкания (без глобальных переменных)
будет хранить в себе количество запусков и каждый раз возвращать число на 1 больше.
Функция должна принимать число с которого начинается отсчет.

Пример:
с1 = counter(1)
с10 = counter(10)

print(c1()) -> 2
print(c1()) -> 3
print(c1()) -> 4 

print(c10()) -> 11 
print(c10()) -> 12 
print(c10()) -> 13 

"""


def counter(call_number):
    """
    Функция счетчик запусков (хранит значение и увеличивает его каждый вызов)
    """

    def counter_ret_func():
        nonlocal call_number
        call_number += 1
        return call_number

    return counter_ret_func


def flip_counter(call_number):
    """
    Функция счетчик запусков c разворотом
    сначала наращивает значение, потом уменьшает
    """

    def counter_ret_func_1():
        nonlocal call_number
        call_number += 1
        return call_number

    yield counter_ret_func_1

    def counter_ret_func_2():
        nonlocal call_number
        call_number -= 1
        return call_number

    yield counter_ret_func_2


c2 = counter(2)

print(c2())
print(c2())
print(c2())

c7 = counter(77)
print(c7())
print(c7())

print("Flip counter")
for i in flip_counter(0):
    print(i())
    print(i())
    print(i())
    print(i())
