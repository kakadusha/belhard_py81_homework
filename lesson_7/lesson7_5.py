"""
Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...
"""

DATA_LIST = ["qwertyu", "asdfggh", "zxcvbnm", "poiuytr", "dfghjkl", "0987654"]
print("Вариент 1")
for i, item in enumerate(DATA_LIST, 1):
    print(f"{i} - {item} - {item[i-1]}")

print("Вариент 2")
for i in range(len(DATA_LIST)):
    print(f"{i+1} - {DATA_LIST[i]} - {DATA_LIST[i][i]}")
