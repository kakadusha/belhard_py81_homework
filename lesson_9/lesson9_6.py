"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.
"""

dict_temp = {"day1": 18, "day2": 22, "day3": 7, "day4": 11, "day5": 14}

print("сортировка по возрастанию температуры")
dict_temp = dict(sorted(dict_temp.items(), key=lambda x: x[1]))
# печатаем каждый день на новой строке
for key, value in dict_temp.items():
    print(key, value)

print("сортировка по убыванию температуры")
dict_temp_rev = dict(sorted(dict_temp.items(), key=lambda x: x[1], reverse=True))
# печатаем каждый день на новой строке
for key, value in dict_temp_rev.items():
    print(key, value)
