"""
Запросить 3 числа. Вывести наибольшее из них. Решить используя if.
"""

n1, n2, n3 = map(int, input("Введите через пробел три числа: ").split())

print("Наибольшее число: ", end="")
if n1 > n2:
    if n1 > n3:
        print(n1)
    else:
        print(n3)
else:
    if n2 > n3:
        print(n2)
    else:
        print(n3)
