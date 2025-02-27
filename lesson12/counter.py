"""
класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое    
    - метод __iter__
    - метод __next__
    
    * - stat, возвращает среднее количество изменений счетчика в секунду

"""

import pendulum


class Counter:
    """
    класс Counter, реализующий целочисленный счетчик.
    """

    def __init__(self, value: int = 0, min_value: int = 0, max_value: int = 100):
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        self.init_time = pendulum.now()

    def increase(self, num: int = 1):
        """
        увеличивает счетчик на заданную величину или 1 по умолчанию
        """
        self.value += num
        if self.value > self.max_value:
            raise ValueError("Value is out of range, max value is", self.max_value)

    def decrease(self, num: int = 1):
        """
        уменьшает счетчик на заданную величину или 1 по умолчанию
        """
        self.value -= num
        if self.value < self.min_value:
            raise ValueError("Value is out of range, min value is", self.min_value)

    def reset(self):
        """
        сбрасывает значение счетчика на стартовое
        """
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.value += 1
        if self.value > self.max_value:
            raise StopIteration
        return self.value

    def stat(self, time: pendulum.DateTime = None):
        """
        возвращает среднее количество изменений счетчика в секунду к моменту time
        """
        time = time or pendulum.now()
        return (
            self.value / (time - self.init_time).seconds
            if (time - self.init_time).seconds != 0
            else 0
        )

    def __str__(self):
        return (
            f"Counter value: {self.value}, "
            f"min value: {self.min_value}, max value: {self.max_value}, "
            f"time: {self.init_time}, stat: {self.stat()}"
        )
