"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""

import time

user_year = int(input("Введите год рождения: "))
current_year = time.localtime().tm_year
age = current_year - user_year
# Охарактеризовать пользователя
if age <= 10:
    print("Ребенок")
elif age <= 15:
    print("Подросток")
elif age <= 20:
    print("Юноша")
elif age <= 60:
    print("В расцвете сил")
elif age <= 60:
    print("Пожилой")
else:
    print("Senior")
