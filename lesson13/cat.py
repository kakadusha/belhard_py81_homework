"""
класс Cat
"""

from animal import Animal


class Cat(Animal):
    """
    класс Cat
    """

    def says(self):
        return f"{self.name} - кошка. Говорит МЯУ!"
