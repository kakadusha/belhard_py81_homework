"""
Дан список:
['hello', 'python', 'интерпретатор', 'pep8', "123"]
Вернуть список где вместо элементов данного списка прописаны количество символов каждого элемента.
"""

LI_LI = ["hello", "python", "интерпретатор", "pep8", "123"]
LI_COUNT = list(map(len, LI_LI))
print(LI_COUNT)
