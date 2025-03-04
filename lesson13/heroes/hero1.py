"""
Модуль героев

        - Создать метод атаки special_attack которая возможна только если количество 
                спец.очков более 0.
        - Добавить метод attack который при атаке с вероятностью 25% будет использовать 
                спец.способность героя если у него остались спец.очки. 
                При спец атаке вычитать из очков 1. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
                о типе и результате атаки.

"""

import os
from time import sleep

from random import randint
from heroes.weapon import (
    dukes,
    iron_sword,
    short_bow,
)
from heroes.health_bar import HealthBar


class Hero:
    """
    Класс для создания героя

    Attributes
    ----------
    name : str
        Имя героя
    health : int
        здоровье героя
    age : int
        age of the person

    Methods
    -------
    print_info():
        Печатает в консоль информацию о герое

    kick():
        производит один удар - высчитывает и уменьшает броню и здоровье

    """

    #  свойства класса - каждый созданный объект будет их иметь по умолчанию
    option1 = True
    points = 0
    level = 1

    # конструктор - тут мы создаем свойства которые должны быть у каждого нового объекта
    # и присылаем сюда первоначальные их значения
    def __init__(
        self, name, health, armor, strong, color="grey", status_len=40
    ) -> None:
        # свойства объектов
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong

        self.health_max = health
        self.weapon = dukes
        self.health_bar = HealthBar(self, color=color, status_len=status_len)

    # методы - это действия/команды которые могут выполнять объекты
    def _refresh_points(self):
        """Здесь спецкачество будем конвертировать в очки"""
        return self.points

    def _get_info(self):
        """Возвращает строку с информацией о герое"""
        self._refresh_points()
        return (
            ""
            + self.health_bar.status_2()
            + "\n"
            + self.health_bar.status_1()
            + "\n"
            + f"Armor: {self.armor}"
        )

    def print_info(self):
        """
        Печатает в консоль информацию о герое
        """
        print(self._get_info() + "\n")

    def kick(self, target):
        """Производит один удар используя strong (не оружие) - высчитывает и уменьшает
        броню и здоровье
        """
        target.armor -= self.strong
        if target.armor < 0:
            target.health += target.armor
            target.armor = 0

    def attack(self, target) -> str:
        """Атакует цель оружием, уменьшает сначало броню, потом здоровье цели
        и возвращает строку с описание атаки"""

        self._refresh_points()
        # 25% шанс использовать спец атаку
        if self.points > 0:
            if self.points > 0 and randint(0, 3) == 0:
                self.points -= 1
                return self.special_attack(target)
        # обычная атака
        target.armor -= self.weapon.damage
        if target.armor < 0:
            target.health += target.armor
            target.armor = 0

        target.health = max(target.health, 0)  # чтобы не было отрицательного здоровья
        target.health_bar.update()
        return (
            f"{self.name} dealt {self.weapon.damage} damage to "
            f"{target.name} with {self.weapon.name}"
        )

    def special_attack(self, target) -> str:
        """Атакует цель спец.способностью"""

        target.armor -= self.strong
        if target.armor < 0:
            target.health += target.armor
            target.armor = 0

        target.health = max(target.health, 0)
        target.health_bar.update()

        return (
            f"{self.name} dealt {self.strong} damage to "
            f"{target.name} with special attack!!!"
        )

    def equip(self, weapon) -> None:
        """Экипировать, получает оружие"""
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        """Сбросить оружие"""
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = dukes


class Mag(Hero):
    """
    Маг сын героя, умеет атаковать магией
    спец очки - мана
    """

    def __init__(
        self, name, health, armor, strong, mana, color="blue", status_len=40
    ) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        super().__init__(name, health, armor, strong, color, status_len)
        self.mana = mana

    def add_mana(self, value=1):
        """Добавляет ману с вероятностью 1/3"""
        if randint(0, 2) == 0:
            self.mana += value
            self._refresh_points()

    def _refresh_points(self):
        """Здесь спецкачество будем конвертировать в очки"""
        self.points = self.mana
        return self.points

    def print_info(self, ident: str = ""):
        info = (
            ["<:-{) " + self.name]
            + super()._get_info().split("\n")
            + [f"Mana: {self.mana}"]
        )
        for s in info:
            print(ident + s)

    def special_attack(self, target) -> str:
        """Атакует цель магией"""

        target.armor -= self.points
        if target.armor < 0:
            target.health += target.armor
            target.armor = 0

        target.health = max(target.health, 0)
        target.health_bar.update()

        return (
            f"{self.name} dealt {self.mana} damage to {target.name} with ✨MAGIC✨!!!"
        )


class Orc(Hero):
    """
    Орк сын героя, умеет атаковать кулаками
    спец очки - ярость
    """

    def __init__(
        self, name, health, armor, strong, anger, color="green2", status_len=40
    ) -> None:
        super().__init__(name, health, armor, strong, color, status_len)
        self.anger = anger

    def add_anger(self, value=1):
        """Добавляет злось с вероятностью 1/2"""
        if randint(0, 1) == 0:
            self.anger += value
            self._refresh_points()

    def _refresh_points(self):
        """Здесь спецкачество будем конвертировать в очки"""
        self.points = self.anger
        return self.points

    def print_info(self, ident: str = ""):
        info = (
            [f"@-[.] {self.name}"]
            + super()._get_info().split("\n")
            + [f"Anger: {self.anger}"]
        )
        for s in info:
            print(ident + s)

    def special_attack(self, target) -> str:
        """Атакует цель злобно"""

        target.armor -= self.points
        if target.armor < 0:
            target.health += target.armor
            target.armor = 0

        target.health = max(target.health, 0)
        target.health_bar.update()
        return (
            f"{self.name} dealt {self.anger} damage to {target.name} with 😡 ANGER!!!"
        )


class Elf(Mag):
    """
    Эльф сын мага, умеет атаковать луком
    """

    def __init__(
        self, name, health, armor=10, strong=10, mana=10, color="yellow", status_len=40
    ) -> None:

        super().__init__(name, health, armor, strong, color, status_len)
        self.mana = mana

    def print_info(self, ident: str = ""):
        info = (
            [");-J " + self.name]
            + super()._get_info().split("\n")
            + [f"Mana: {self.mana}"]
        )
        for s in info:
            print(ident + s)


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
        color="blue2",
    )
    hero3 = Orc(
        "Grom",
        health=80,
        armor=25,
        strong=20,
        anger=0,
        color="green",
    )
    hero4 = Elf(
        "Legolas",
        health=31,
        armor=25,
        strong=10,
    )
    hero1.equip(iron_sword)
    hero2.equip(short_bow)
    hero4.equip(short_bow)

    h_list = [hero1, hero2, hero3, hero4]

    # print("---< Kicks >---")
    # hero1.kick(hero2)
    # hero2.kick(hero1)
    # hero1.print_info()
    # hero2.print_info()

    # ------------ game loop ------------
    round_cnt = 0
    while True:
        round_cnt += 1
        print(f"---< Round {round_cnt} >---")

        for h in h_list:
            if isinstance(h, Orc):
                h.add_anger()
            elif isinstance(h, Mag):
                h.add_mana(5)
            h.print_info()

        if any(h.health <= 0 for h in h_list):
            print("Game Over!")
            print(f"{hero1.name} won!" if hero2.health <= 0 else f"{hero2.name} won!")
            break

        print(hero1.attack(hero2))
        print(hero2.attack(hero3))
        print(hero3.attack(hero4))
        print(hero4.attack(hero1))

        sleep(0.1)
        print()
