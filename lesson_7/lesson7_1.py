"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""

marks_list = []
while True:
    input_str = input("Введите оценку ученика (для завершения 0): ")
    if input_str == "0":
        break
    marks_list = marks_list + list(map(int, input_str.split(" ")))

if len(marks_list) != 0:
    print(f"Средний бал ученика: {sum(marks_list) / len(marks_list)}")
else:
    print("Вы не ввели оценок")
