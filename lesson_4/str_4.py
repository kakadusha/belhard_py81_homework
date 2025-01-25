"""
Даны данные пользователя в строке:
    s = "имя: Дмитрий, фамилия: Иванов, возраст: 18"
    Программа должна достать из этой строки, имя, фамилию и возраст пользователя 
    присвоить их отдельным переменным и вывести на экран  через один print(), 
    но каждый элемент должен быть выведен в новой строке. 
    Программа должна работать с любой аналогичной строкой с данными др. человека.
        пример вывода:        
            - Дмитрий
            - Иванов
            - 18
"""

S = "имя: Дмитрий, фамилия: Иванов, возраст: 18"

# вариант 1 - четкая последовательность и разделители
records = S.split(",")
pairs = list(map(str.split, records, [":"] * len(records)))
name = pairs[0][1].strip()
surname = pairs[1][1].strip()
age = pairs[2][1].strip()
print(f"Вариант 1\n- {name}\n- {surname}\n- {age}")

# вариант 2 - поиск по ключам, нарезаем салями
KEY_NAME = "имя: "
KEY_SURNAME = "фамилия: "
KEY_AGE = "возраст: "
name = S[S.find(KEY_NAME) + len(KEY_NAME) : S.find(",")]
surname = S[S.find(KEY_SURNAME) + len(KEY_SURNAME) : S.find(",", S.find(KEY_SURNAME))]
age = S[S.find(KEY_AGE) + len(KEY_AGE) :]
print(f"Вариант 2\n- {name}\n- {surname}\n- {age}")
