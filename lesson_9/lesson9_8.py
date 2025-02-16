"""
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип. 
"""

data = [1, 22, 333, "aw", "bh", "c", True, False, 1, 22, 33]
# остались только строки
string = list(filter(lambda x: isinstance(x, str), data))
# остался только логический тип
booleans = list(filter(lambda x: isinstance(x, bool), data))
# остался только числовой тип
numbers = list(filter(lambda x: isinstance(x, int), data))


print("Остались только строки")
print(string)
print("Остался только логический тип")
print(booleans)
print("Остался только числовой тип")
print(numbers)
print(">> Интересно что логический - тоже числовой тип")
