"""
класс Dog
"""

from animal import Animal


class Dog(Animal):
    """
    класс Dog
    """

    def says(self):
        return f"{self.name} - собака. Говорит ГАВ!"
