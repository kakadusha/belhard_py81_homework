"""
класс Cow
"""

from animals.animal import Animal


class Cow(Animal):
    """
    класс Cow
    """

    def says(self):
        return f"{self.name} - корова. Говорит МУ!"
