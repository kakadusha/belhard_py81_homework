"""
Создать класс Student.

Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""

from student import Student
import random

names = [
    "Иван Иванов",
    "Петр Петров",
    "Сидор Сидоров",
    "Михаил Михайлов",
    "Саша Александрова",
]


def r_grade() -> int:
    """функция возвращает случайную оценку [1-10]"""
    return random.randint(1, 10)


# студенты со случайным баллом из группы 13
students = [
    Student(names[i].split()[0], names[i].split()[1], 13, [r_grade() for _ in range(5)])
    for i in range(5)
]

# сортировка по возрастанию через лямбду от среднего балла
students.sort(key=lambda x: x.average_grade())
print("Сортировка по возрастанию:")
for student in students:
    print(f"{student.surname} {student.name} - {student.average_grade()}")
print()

print(
    "Сравним пару студентов",
    students[0],
    " и ",
    students[1],
    "по среднему баллу: ",
    students[0] > students[1],
)

# сортируем без лямбды
students.sort(reverse=True)
print("Сортировка по убыванию:")
for student in students:
    print(f"{student.surname} {student.name} - {student.average_grade()}")

# фильтруем с функцией filter у кого балл больше 8
print("Студенты с баллом больше 8:")
for student in filter(lambda x: x.average_grade() > 8, students):
    print(f"{student.surname} {student.name} - {student.average_grade()}")
else:
    print("  Извините, студентов с баллом больше 8 нет")
