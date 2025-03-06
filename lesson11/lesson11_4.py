"""
Открыть и обработать файл students_grades.txt
собрать все данные в словарь ниже приведенного формата
записать в файл "excellent_students.txt" по 1 ученику из класса с наибольшим балом
{
    "9A":[
        {'fio':'fio', 
         'objects':{
            'mathematics':[4, 9, 7],
            'physics':[8, 9, 8, 6],
            ...:...
            }
        },
        ...        
    ],
    "9Б":[
        ...
    ]
}
---
Сергей Ерофеевич Кононов, 9А, Математика (6, 6, 8, 9, 4, 9), Русский язык (9, 7, 9, 5, 10, 8), Физика (9, 6, 4, 7), Химия (10, 7, 7, 3, 7, 6, 3), История (4, 7, 9, 7, 9, 4, 8, 10)
Суханов Мефодий Харитонович, 9Б, Математика (8, 3, 5, 8, 4, 8, 3, 3), Русский язык (7, 4, 10), Физика (4, 5, 3, 5, 9, 4, 10), Химия (6, 3, 6, 7, 7, 5, 3), История (7, 6, 5, 7, 8, 9, 9, 5, 4)
---
"""

import os
from pprint import pprint
from copy import deepcopy


def parse_marks(marks_raw: str) -> tuple[str, list]:
    """
    Парсинг строки с оценками
    """
    raw_list = marks_raw.split("(")
    if len(raw_list) > 2:
        raise ValueError("Неверный формат строки с оценками")
    course = raw_list[0].strip()
    parsed_marks = map(lambda x: int(x.strip()), raw_list[1].split(","))
    return course, list(parsed_marks)


# "lesson11/students_grades.txt"
def parse_load_marks(in_file: str) -> dict:
    """
    Парсинг файла с оценками учеников
    :param in_file: str: путь к файлу
    :return: dict: словарь с оценками
    """
    with open(in_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    students = {}
    rec_num = 0

    # проходим по строкам
    for line in lines:
        # разбиваем строку на части
        parts = line.split("), ")
        # получаем ФИО
        semi_pos_1 = parts[0].find(", ")
        fio = parts[0][:semi_pos_1]
        # получаем класс
        semi_pos_2 = parts[0][semi_pos_1 + 2 :].find(", ")
        class_name = parts[0][semi_pos_1 + 2 : semi_pos_1 + 2 + semi_pos_2]
        students[rec_num] = {"fio": fio, "class": class_name, "objects": {}}
        # получаем оценки
        cource, marks = parse_marks(parts[0][semi_pos_1 + 2 + semi_pos_2 :].strip(", "))
        students[rec_num]["objects"] = {cource: marks}  # тут словарь по предметам

        # из parts[1:] получаем остальные оценки
        for part in parts[1:]:
            cource, marks = parse_marks(part.strip(")\n"))
            students[rec_num]["objects"][cource] = marks

        rec_num += 1

    return students


def export_best_marks(out_file: str, best_students: dict) -> None:
    """
    Экспорт лучших учеников в файл
    :param out_file: str: путь к файлу
    :param best_students: dict: словарь с лучшими учениками
    """
    with open(out_file, "w", encoding="utf-8") as file:
        for class_name, students in best_students.items():
            # вывод через pprint в файл
            file.write(f"{class_name}:\n")
            for student in students:
                # copy with deepcopy
                student_cpy = deepcopy(student)
                student_cpy.pop("avg_total")
                student_cpy.pop("class")
                pprint([student_cpy], stream=file)  # именно список, как в задании

                file.write("\n")
                break  # только 1 ученик


if __name__ == "__main__":

    # ------------ parse file ------------
    students = parse_load_marks("lesson11/students_grades.txt")
    pprint(students)

    # ------------ find best students ------------
    best_students = {}
    # для каждого ученика
    # - считаем средний бал по каждому предмету
    # - считаем средний бал по всем предметам, добавляем его в запись студента c ключем avg_total
    # - best_students для class_name подбираем ученика с наибольшим балом (список, потму что может быть несколько)
    # - - если записи для class_name нет - добавляем ученика в список лучших класса
    # - - если запись есть - сравниваем баллы с первым из списка лучших и если средний бал лучше, очищаем список и добавляем нового студента
    # - - - если баллы равны - добавляем ученика в список лучших класса
    for student in students.values():
        avg_marks = {}
        for cource, marks in student["objects"].items():
            avg_marks[cource] = sum(marks) / len(marks)
        avg_marks["total"] = sum(avg_marks.values()) / len(avg_marks)
        student["avg_total"] = avg_marks["total"]

        if student["class"] not in best_students:
            best_students[student["class"]] = []
            best_students[student["class"]].append(student)
        else:
            # запись есть
            if student["avg_total"] > best_students[student["class"]][0]["avg_total"]:
                # заменяем потому что лучше
                best_students[student["class"]] = []
                best_students[student["class"]].append(student)
            elif (
                student["avg_total"] == best_students[student["class"]][0]["avg_total"]
            ):
                # бал такойже добавляем
                best_students[student["class"]].append(student)

    pprint(best_students)
    export_best_marks("lesson11/excellent_students.txt", best_students)
