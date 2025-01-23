"""
Запросить логин и пароль.
Вывести - True/False  соответственно
если ввели логин - 'admin', пароль - '12345'.
Формат вывода: "Логин:True / Пароль:True"
"""

login = input("login : ")
password = input("password : ")
print(f"Логин:{login == 'admin'} / Пароль:{password == '12345'}")
