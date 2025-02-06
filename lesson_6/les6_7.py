"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

# pip install pyowm

from pyowm import OWM
from pprint import pprint
from rich.console import Console

owm = OWM("3b7520cfa14d8220f49bed37a19a7b4d")
mgr = owm.weather_manager()

# obs = mgr.weather_at_place("Minsk")
# w = obs.to_dict()
# pprint(w)

city = input("Введите название города, проверим какая там погода: ")

# Получаем данные о погоде для указанного города
obs = mgr.weather_at_place(city)
weather = obs.weather

# Извлекаем
weather_data = {
    "Температура": weather.temperature("celsius")["temp"],
    "Давление": weather.pressure["press"],
    "Осадки": weather.rain if weather.rain else "Нет осадков",
    "Скорость ветра": weather.wind()["speed"],
}

# pprint
pprint(weather_data)

print("\n")
# с использованием rich, люблю цвета
console = Console()
for key, value in weather_data.items():
    console.print(f"[green]{key}[/green]: {value}")
