"""
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44

    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44 
"""

input_1 = input("Введите нескольких чисел через пробел, 1: ")
input_2 = input("Введите нескольких чисел через пробел, 2: ")
input_3 = input("Введите нескольких чисел через пробел, 3: ")

set_int_1 = set(map(int, input_1.split()))
set_int_2 = set(map(int, input_2.split()))
set_int_3 = set(map(int, input_3.split()))

all_set = set_int_1 | set_int_2 | set_int_3
print("Все уникальные числа по возрастанию: ", sorted(all_set))

common_set = set_int_1 & set_int_2 & set_int_3
print("Числа что есть в каждой строке: ", common_set)

unique_set = (
    all_set
    - (set_int_1 & set_int_2)
    - (set_int_1 & set_int_3)
    - (set_int_2 & set_int_3)
)
print("Числа что есть только в одной из трех строк: ", unique_set)
