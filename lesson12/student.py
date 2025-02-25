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
"""


class Student:
    """
    Класс Student определяет студента и его свойства
    """

    def __init__(self, surname: str, name: str, group: int, grads: list[int]):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads

    def add_grade(self, grade: int):
        if 1 <= grade <= 10:
            self.grads.append(grade)
        else:
            raise ValueError("Grade must be between 1 and 10")

    def average_grade(self) -> float:
        return sum(self.grads) / len(self.grads)

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __str__(self):
        return f"{self.surname} {self.name} - {self.average_grade()}"
