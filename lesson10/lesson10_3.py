"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

Реализация:
- устраняем все символы кроме скобок
- далее в цикле проверяем посимвольно
-- если ( - увеличиваем счетчтк
-- если ) - уменьшаем счетчик
-- если счетчик меньше 0 - возвращаем False
-- если после цикла счетчик равен 0 - возвращаем True    
"""


def check_brackets(s):
    s = "".join([i for i in s if i in "()"])
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


print(check_brackets("(()())"))  # True
print(check_brackets("(()()()"))  # False
print(check_brackets("(hello(2)ver()(33)python)"))  # True
print(check_brackets("(hello(2()ver(33)python))"))  # True
