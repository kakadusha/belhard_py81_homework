"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

from phone import Phone

phone1 = Phone("Samsung", "A55", 2019)
phone2 = Phone("Apple", "iPhone 11", 2020)
phone3 = Phone("Xiaomi", "Redmi 9", 2020)
# копия объекта phone3
phone4 = phone3.__copy__()
phone4.brand = "Huawei"
phone4.model = "P40"

phone1.receive_call("Маша Шишкина")
print(phone1.get_info())
print("-----------------")
print(phone1)

phone2.receive_call("Вася Пупкин")
phone3.receive_call("Вася Пупкин")
phone4.receive_call("Вася Пупкин")
