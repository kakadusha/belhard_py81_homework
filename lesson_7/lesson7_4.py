"""
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******
"""

from random import Random
from rich.console import Console

random = Random()
console = Console()

while True:
    try:
        rows = int(input("Введите высоту елочки от 3 до 20: "))
    except ValueError:
        print("Введите число")
        continue

    if rows < 3 or rows > 20:
        print("Неверное значение")
    else:
        break

# Рисуем зелёную елочку через rich со случайными белыми снежинками
for i in range(0, rows):
    random.seed()
    for k in range(0, rows - i - 1):
        console.print((" " if random.randint(0, 5) else "."), style="white", end="")
    print(" ", end="")
    console.print("*" * (2 * i + 1), style="green", end="")
    print(" ", end="")
    for k in range(0, rows - i - 1):
        console.print((" " if random.randint(0, 5) else "."), style="white", end="")
    print()
