"""
Описать класс Counter, реализующий целочисленный счетчик.
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

from random import randint
from time import sleep

from counter import Counter

c = Counter(0, 0, 100)
# В цикле увеличиваем значение счетчика на случайный шаг
# и выводим текущее значение счетчика
for i in range(10):
    add = randint(1, 10)
    sleep_time = randint(1, 2) / 2
    # заснем
    sleep(sleep_time)
    print("Add:", add)
    try:
        c.increase(add)
    except ValueError as e:
        print(e)
    print(f"Value: {c.value}, Stat: {c.stat()}")

# В цикле увеличиваем значение счетчика на i
# и выводим текущее значение счетчика
for i in range(10):
    print("Subtract:", i)
    sleep_time = randint(1, 2) / 2
    # заснем
    sleep(sleep_time)
    try:
        c.decrease(i)
    except ValueError as e:
        print(e)
    print(f"Value: {c.value}, Stat: {c.stat()}")

# Сбрасываем значение счетчика
print("Reset here...")
c.reset()
print(f"Value: {c.value}, Stat: {c.stat()}")

# В цикле итерируем счетчик
for i in c:
    print("Next... ", i, c.stat())
    sleep(1)
    if i > 10:
        break
