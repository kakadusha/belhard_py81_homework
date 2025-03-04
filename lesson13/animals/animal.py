"""
класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов
"""

from abc import ABC, ABCMeta, abstractmethod


class Animal(ABC):
    """
    абстрактный класс Animal
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def says(self):
        """
        Тут буем гавкать и мяукать, но потом
        """
        return "<заглушка Animal>"


# Создаем мета-класс, наследуемый от ABCMeta
class MetaAnimal(ABCMeta):
    """
    проверяем что есть реализация метода says
    """

    def __new__(mcs, name, bases, dct):
        new_class = super().__new__(mcs, name, bases, dct)
        if name != "Animal":
            if not "says" in dct:
                raise ValueError(f"Class {name} must have method says")
        return new_class


class WildAnimal(ABC, metaclass=MetaAnimal):
    """
    абстрактный класс WildAnimal c контролирующим метаклассом (падаем прямо на инициализации неправильного класса-наследника)
    """

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def says(self):
        """
        Тут буем гавкать и мяукать, но потом
        """
        return "<заглушка Animal>"
