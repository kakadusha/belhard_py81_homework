"""
запросить у пользователя логин пароль и возраст
вывести доступ разрешен:
    логин:admin   пароль:123456    возраст: любой    
    логин:vasya   пароль: vas123   возраст: менее 60
    логин:guest   пароль: любой    возраст:более 18
    
в остальных случаях - "доступ запрещен".
"""

# будем вычислять возраст через eval,
# в condition можно использовать любые простые операции сравнения
# например, "<60", ">18", "==25", "!=30"
# * - любое значение
access_dict = {
    "admin": {"password": "123456", "condition": "*"},
    "vasya": {"password": "vas123", "condition": "<60"},
    "guest": {"password": "*", "condition": ">18"},
}

login = input("Введите логин: ")
password = input("Введите пароль: ")
age = int(input("Введите возраст: "))
if login in access_dict:
    if (
        access_dict[login]["password"] == password
        or access_dict[login]["password"] == "*"
    ):
        # ok, проверяем возраст
        if access_dict[login]["condition"] == "*" or eval(
            str(age) + access_dict[login]["condition"]
        ):
            print("Доступ разрешен")
        else:
            print("Доступ запрещен, не подходит возраст")
    else:
        print("Доступ запрещен, не подходит логин/пароль")
