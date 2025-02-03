"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.
"""

d = {"one": 11, "two": 22, "hello": "python", True: False}
print(d)
key = input("Введите порядковый номерэлемента для удаления (номера с единицы): ")
del d[list(d.keys())[int(key) - 1]]
print(d)
