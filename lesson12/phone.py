"""
Класс Phone определяет телефон и его свойства
"""


class Phone:
    """Класс Phone определяет телефон и его свойства"""

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        """Принимает имя звонящего и выводит на экран"""
        print(f"<{self.brand}-{self.model}> - Звонит {name}")

    def get_info(self):
        """Возвращает кортеж (brand, model, issue_year)"""
        return self.brand, self.model, self.issue_year

    def __str__(self):
        return (
            f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"
        )

    def __copy__(self):
        # Создание нового объекта, констркутор копирования, оч надо!
        new_obj = type(self)(self.brand, self.model, self.issue_year)
        return new_obj
