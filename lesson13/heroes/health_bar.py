"""
Модуль содержит класс HealthBar
готовит для отрисовки две строки 
статус здоровья персонажа и графический health bar

|        Hero's HEALTH:  48/100                 Enemy's HEALTH:  35/100            |
|███████████████████_____________________||██████████████__________________________|

"""


class HealthBar:
    """
    Класс HealthBar
    готовит для отрисовки две строки
    статус здоровья персонажа и графический health bar
    Цвета: red, purple, blue, blue2, blue3, green, green2, brown, yellow, grey, default
    """

    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {
        "red": "\033[91m",
        "purple": "\33[95m",
        "blue": "\33[34m",
        "blue2": "\33[36m",
        "blue3": "\33[96m",
        "green": "\033[92m",
        "green2": "\033[32m",
        "brown": "\33[33m",
        "yellow": "\33[93m",
        "grey": "\33[37m",
        "default": "\033[0m",
    }

    def __init__(
        self, entity, status_len: int = 30, is_colored: bool = True, color: str = ""
    ) -> None:
        self.entity = entity
        self.status_len = status_len
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:
        """Обновляет health bar"""
        self.current_value = self.entity.health

    def status_1(self) -> str:
        """Формирует первую строку health bar"""
        line = f"HEALTH: {str(self.entity.health).rjust(3)}/{self.entity.health_max}"
        # spaces = self.status_len - len(line)
        # return " " * (spaces // 2) + line + " " * (spaces - spaces // 2)  # centred
        return line

    def status_2(self) -> str:
        """Формирует вторую строку health bar"""
        remaining_bars = int(self.current_value / self.max_value * self.status_len) - 1
        lost_bars = self.status_len - remaining_bars - 1
        return (
            f"{self.barrier}"
            f"{self.color if self.is_colored else ''}"
            f"{remaining_bars * self.symbol_remaining}"
            f"{lost_bars * self.symbol_lost}"
            f"{self.colors['default'] if self.is_colored else ''}"
            f"{self.barrier}"
        )

    def get_status(self) -> list[str]:
        """
        Возвращает список строк состоящий из строк имя, health, helfth bar
        """
        return [self.entity.name, self.status_1(), self.status_2()]
