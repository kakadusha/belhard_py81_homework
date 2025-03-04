"""
в файле hero1 добавить следующий функционал
        - добавить несколько классов других героев унаследовав их от Hero.
        - Каждому герою добавить уникальное свойство-спец.очки (мана, ярость, и т.п. ) и 
                и свойство cо значением урона от спец.атаки.
        - Создать метод атаки special_attack которая возможна только если количество 
                спец.очков более 0.
        - Добавить метод attack который при атаке с вероятностью 25% будет использовать 
                спец.способность героя если у него остались спец.очки. 
                При спец атаке вычитать из очков 1. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
                о типе и результате атаки.

добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"
        - метод choose_warrior, который не принимает аргументов и возвращает случайного
                воина из warriors
        - метод battle, который не принимает аргументов и симулирует битву. Сперва 
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
                Вернуть данного воина из метода battle.
                   
Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
Выжить должен только один.
"""

import os
from time import sleep

from random import randint
from heroes.hero1 import Mag, Orc, Elf
from heroes.weapon import (
    iron_sword,
    short_bow,
)

IDEND_WIDTH = 20


class Arena:
    """
    Арена для битвы героев
    """

    warriors = []

    def __init__(self, warriors=None):
        if warriors:
            self.warriors = warriors
        else:
            self.warriors = []

    def add_warrior(self, warrior):
        """
        Добавить воина на арену
        """
        if warrior in self.warriors:
            raise ValueError("Воин уже на арене!")
        self.warriors.append(warrior)
        print(f"Теперь {warrior.name} участвует в битве!")

    def choose_warrior(self, exclude=None):
        """
        Выбрать случайного воина из списка воинов, исключая exclude
        """
        if exclude:
            ret_warriors = [w for w in self.warriors if w != exclude]
        else:
            ret_warriors = self.warriors

        return ret_warriors[randint(0, len(ret_warriors) - 1)]

    def battle(self, sleep_time=0.1, keybord_control=False):
        """
        Симуляция битвы
        """
        if len(self.warriors) < 2:
            raise ValueError("Количество воинов на арене должно быть больше 1!")

        round_cnt = 0
        while len(self.warriors) > 1:
            round_cnt += 1
            print(
                f"\n  *********************** Round {round_cnt} ***********************\n"
            )
            attacker = self.choose_warrior()
            defender = self.choose_warrior(attacker)

            for h in (attacker, defender):
                if isinstance(h, Orc):
                    h.add_anger(3)
                elif isinstance(h, Mag):
                    h.add_mana(5)

            print(f"{attacker.name} атакует {defender.name}!")
            print(attacker.attack(defender))
            print(defender.attack(attacker))
            print()
            defender.print_info("  ")
            attacker.print_info(" " * IDEND_WIDTH)

            if defender.health <= 0:
                self.warriors.remove(defender)
                print(f"\n{defender.name} пал в битве!\n RIP!\n")

            sleep(sleep_time)
            if keybord_control:
                input("\n> Press Enter to continue...")
            print()

        winner = self.warriors[0]
        print(f"Победил воин: {winner.name}!\n")
        return winner


if __name__ == "__main__":
    # ------------ clear screen ------------
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

    hero1 = Mag(
        "Gendalf",
        health=30,
        armor=25,
        strong=10,
        mana=30,
        color="blue",
    )
    hero2 = Mag(
        "Sauron",
        health=60,
        armor=55,
        strong=60,
        mana=30,
        color="red",
    )
    hero3 = Orc(
        "Grom",
        health=80,
        armor=25,
        strong=20,
        anger=0,
        color="green",
    )
    hero4 = Elf("Legolas", health=31, armor=25, strong=10, color="green")
    # снаряжение
    hero1.equip(iron_sword)
    hero2.equip(short_bow)
    hero4.equip(short_bow)

    arena = Arena()
    arena.add_warrior(hero1)
    arena.add_warrior(hero2)
    arena.add_warrior(hero3)
    arena.add_warrior(hero4)
    arena.battle(sleep_time=0.2, keybord_control=True)

    ### тестовый прогон ###
    # h_list = [hero1, hero2, hero3, hero4]

    # # print("---< Kicks >---")
    # # hero1.kick(hero2)
    # # hero2.kick(hero1)
    # # hero1.print_info()
    # # hero2.print_info()

    # # ------------ game loop ------------
    # round_cnt = 0
    # while True:
    #     round_cnt += 1
    #     print(f"---< Round {round_cnt} >---")

    #     for h in h_list:
    #         if isinstance(h, Orc):
    #             h.add_anger()
    #         elif isinstance(h, Mag):
    #             h.add_mana(5)
    #         h.print_info()

    #     if any(h.health <= 0 for h in h_list):
    #         print("Game Over!")
    #         print(f"{hero1.name} won!" if hero2.health <= 0 else f"{hero2.name} won!")
    #         break

    #     print(hero1.attack(hero2))
    #     print(hero2.attack(hero3))
    #     print(hero3.attack(hero4))
    #     print(hero4.attack(hero1))

    #     sleep(0.1)
    #     print()
