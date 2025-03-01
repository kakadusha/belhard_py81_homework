"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""

from cat import Cat
from dog import Dog
from cow import Cow

from animal import Animal, WildAnimal


# из за Мета-класса MetaAnimal, который проверяет наличие метода says в классе наследнике
# класс WildDog не проходит проверку и вызывает ошибку ValueError во время инициализации
# class WildDog(WildAnimal):
#     """
#     класс WildDog
#     """
#
#     def barks(self):
#         """
#         метод barks
#         """
#         return f"{self.name} - дикая собака. Гавкает!"


class BadDog(Animal):
    """
    класс BadDog
    """

    def barks(self):
        """
        метод barks
        """
        return f"{self.name} - дикая собака. Гавкает!"


if __name__ == "__main__":
    cat = Cat("Мурка")
    dog = Dog("Шарик")
    cow = Cow("Бурёнка")

    print(cat.says())
    print(dog.says())
    print(cow.says())

    try:
        bad_dog = BadDog("Тузик")
        print(bad_dog.barks())
        print(bad_dog.says())
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
