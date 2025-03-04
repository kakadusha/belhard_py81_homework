"""
Модуль для теста классов Hero и Enemy и health_bar
"""

import os
from time import sleep

from character import Hero, Enemy
from weapon import short_bow, iron_sword


CHARACTER_WIDTH = 16  # 16 is minimal width for health bar


if __name__ == "__main__":
    # ------------ clear screen ------------
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    # ------------ setup ------------
    hero = Hero(name="Hero", health=100, status_len=CHARACTER_WIDTH)
    hero.equip(iron_sword)
    enemy = Enemy(
        name="Enemy", health=100, weapon=short_bow, status_len=CHARACTER_WIDTH
    )

    # ------------ game loop ------------
    while True:

        print(hero.health_bar.status_1().rjust(CHARACTER_WIDTH), end="")
        print(enemy.health_bar.status_1().rjust(CHARACTER_WIDTH))

        print(hero.health_bar.status_2(), end="")
        print(enemy.health_bar.status_2())
        if hero.health <= 0 or enemy.health <= 0:
            print("Game Over!")
            print("Hero won!" if enemy.health <= 0 else "Enemy won!")
            break

        hero.attack(enemy)
        enemy.attack(hero)

        # print(hero.health_bar.draw1())
        # print(enemy.health_bar.draw1())
        # print(hero.health_bar.draw2())
        # print(enemy.health_bar.draw2())

        # input()
        sleep(0.1)
        print()
