"""
класс Cat
"""

from animals.animal import Animal


class Cat(Animal):
    """
    класс Cat
    """

    def says(self):
        return f"{self.name} - кошка. Говорит МЯУ!"
