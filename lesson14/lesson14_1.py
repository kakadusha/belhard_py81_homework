"""
Создать класс User с атрибутами:

Свойства:
        - name - имя - содержит только буквы русского алфавита
        - login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
        - password - пароль - может содержать  только латинские буквы цифры. Обязательные условия:
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
        - is_blocked - заблокирован
        - subscription_date - дата до какой действует подписка
        - subscription_mode - вид подписки (free, paid)

Методы:
        - bloc - принимает логическое значение и помечает пользователя заблокированным
        - check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату.
                                                Если дата не передана значит на дату проверки.
                                                Возвращает  действует ли подписка, ее вид и сколько осталось дней.
        - change_pass - смена пароля и присваивание его в качестве действующего.
                                                Пароль должен пройти валидацию.
                                                Если пароль не был передан сгенерировать по правилам и вывести в консоль.
        - get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.

Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль
должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""

import secrets
import string

import hashlib


class User:
    """
    Класс пользователя
    """

    def __init__(self, name, login, password=None):
        self.name = name
        self.login = login

        self.is_blocked = False
        self.subscription_date = 30
        self.subscription_mode = "free"

        if password is None:
            password = self._generate_password()
            print(f"Сгенерированный пароль, запишите его обязательно: {password}")
            self._password_hash = self._hash_password(password)
        else:
            self._password_hash = self._hash_password(password)

    def _generate_password(self, length=6):
        """
        Генерация пароля вида U9lxxx по заданным правилам
        U - заглавная буква
        l - строчная буква
        9 - цифра
        x - любой символ из латинских букв и цифр
                :param length: длина пароля
        :return: пароль
        """
        any_characters = string.ascii_letters + string.digits
        upper = secrets.choice(string.ascii_uppercase)
        lower = secrets.choice(string.ascii_lowercase)
        digit = secrets.choice(string.digits)
        password = (
            upper
            + digit
            + lower
            + "".join(secrets.choice(any_characters) for _ in range(length - 3))
        )
        return password

    def _hash_password(self, password):
        # Используем SHA-256 для хэширования пароля
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    @property
    def password(self):
        """
        Возвращает ошибку "доступ к паролю запрещен"
        """
        raise AttributeError("Доступ к паролю запрещен")

    @password.setter
    def password(self, new_password):
        """
        Установка нового пароля
        """
        self._password_hash = self._hash_password(new_password)

    def verify_password(self, password):
        """ "
        Поверка пароля на соответствие
        """
        return self._password_hash == self._hash_password(password)


##############
# внимание тут я еще не доделал задание :)
##############

# Пример использования:
user = User("учфьзду_гыук", "example_user", "secure_password")
print(user.verify_password("secure_password"))  # True

user2 = User("учфьзду_гыук2", "example_user")
print(user2.verify_password("secure_password"))  # False

user2.password = "secure_password"  # установка нового пароля разрешена через setter
print(user2.verify_password("secure_password"))  # True
