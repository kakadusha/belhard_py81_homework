"""
запросить число и вывести на экран сколько номиналов в этом числе:
	 - тысячи
	 - сотни
	 - десятки
	 - единицы
     
пример: # знак >>> значит что ввели что-то через input
    >>>21234 
    тысяч - 21
    сотни - 2
    десятки - 3
    еденицы - 4
     
"""

# 12345
number = int(input("Введите число: "))
print("десятки тысяч: ", number // 10000)
print("тысячи: ", number // 1000 % 10)
print("сотни: ", number // 100 % 10)
print("десятки: ", number // 10 % 10)
print("единицы: ", number % 10)
