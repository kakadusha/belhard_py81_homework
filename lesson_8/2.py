"""
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.
"""


def rectangle_calc(side_a: float, side_b: float, func: str) -> float:
    """
    Функция принимает 2 стороны прямоугольника и возвращает либо площадь либо периметр в зависимости
    от дополнительного параметра.
    func - параметр для выбора что считаем, допустимые значения: square, perimeter
    """
    if func == "square":
        return side_a * side_b
    elif func == "perimeter":
        return (side_a + side_b) * 2
    else:
        raise ValueError(
            "Неверный параметр func, допустимые значения: square, perimeter"
        )


if __name__ == "__main__":
    print("Тесты\n---")
    print(rectangle_calc(2.0, 3.0, "square"))
    print(rectangle_calc(2.1, 3.1, "perimeter"))
    try:
        print(rectangle_calc(2.2, 3.3, "test"))
    except ValueError as e:
        print(e)
    print("---\nPassed")
