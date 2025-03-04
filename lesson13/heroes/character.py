"""
Модуль персонажа

Содержит:
- родительский класс Character
- дочерние классы Hero и Enemy
- методы attack, equip, drop
"""

# ------------ imports ------------
from weapon import dukes as fists
from health_bar import HealthBar


# ------------ parent class setup ------------
class Character:
    """Базовый класс персонажа"""

    def __init__(
        self, name: str, health: int, color="green", status_len: int = 40
    ) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists
        self.health_bar = HealthBar(self, color=color, status_len=status_len)

    def attack(self, target):
        """Атакует цель"""
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(
            f"{self.name} dealt {self.weapon.damage} damage to "
            f"{target.name} with {self.weapon.name}"
        )


# ------------ subclass setup ------------
class Hero(Character):
    """Класс героя"""

    def __init__(
        self,
        name: str,
        health: int,
        status_len: int = 40,
        color="green",
    ) -> None:
        super().__init__(name=name, health=health, status_len=status_len, color=color)

        self.default_weapon = self.weapon

    def equip(self, weapon) -> None:
        """Экипировать, получает оружие"""
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        """Сбросить оружие"""
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon


# ------------ subclass setup ------------
class Enemy(Character):
    """Класс врага"""

    def __init__(
        self,
        name: str,
        health: int,
        weapon,
        status_len: int = 40,
        color="red",
    ) -> None:
        super().__init__(name=name, health=health, status_len=status_len, color=color)
        self.weapon = weapon
