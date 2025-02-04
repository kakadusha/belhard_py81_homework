"""
Запросить число от 1 до 12. 
Если ввели другое число сообщить об ошибке. 
Если ввели не число сообщить об ошибке. 
Когда введут допустимое число - вывести на экран соответствующее 
название месяца, пору года и сколько дней в данном месяце.
"""

MONTHS_DICT = {
    "1": {"month_name": "Январь", "month_code": 1, "days": 31, "season": "Зима"},
    "2": {"month_name": "Февраль", "month_code": 2, "days": 28, "season": "Зима"},
    "3": {"month_name": "Март", "month_code": 3, "days": 31, "season": "Весна"},
    "4": {"month_name": "Апрель", "month_code": 4, "days": 30, "season": "Весна"},
    "5": {"month_name": "Май", "month_code": 5, "days": 31, "season": "Весна"},
    "6": {"month_name": "Июнь", "month_code": 6, "days": 30, "season": "Лето"},
    "7": {"month_name": "Июль", "month_code": 7, "days": 31, "season": "Лето"},
    "8": {"month_name": "Август", "month_code": 8, "days": 31, "season": "Лето"},
    "9": {"month_name": "Сентябрь", "month_code": 9, "days": 30, "season": "Осень"},
    "10": {"month_name": "Октябрь", "month_code": 10, "days": 31, "season": "Осень"},
    "11": {"month_name": "Ноябрь", "month_code": 11, "days": 30, "season": "Осень"},
    "12": {"month_name": "Декабрь", "month_code": 12, "days": 31, "season": "Зима"},
}

month_str = input("Введите число (месяц) от 1 до 12: ")
if not month_str.isdigit():
    print("Ошибка! Введено не число!")
elif month_str not in MONTHS_DICT:
    print("Ошибка! Введено число вне диапазона от 1 до 12!")
else:
    month = MONTHS_DICT[month_str]
    print(
        f"Вы ввели {month['month_name']}, это {month['season']}, в нем {month['days']} дней."
    )
