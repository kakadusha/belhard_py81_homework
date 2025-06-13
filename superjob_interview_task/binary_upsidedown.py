"""
Дано бинарное дерево, в котором узлы пронумерованы от `1`, начиная с дочерних узлов.
Например, дерево глубины `3` выглядит так:
     7
  ┌──┴──┐
  3     6
┌─┴─┐ ┌─┴─┐
1   2 4   5

Нужно по глубине дерева и номеру узла найти номер родительского узла.
Если узла с таким номером нет или номер соответствует корневому узлу, то нужно вернуть `-1`.

>>> find_parent_node(node=1, depth=2)
3

>>> find_parent_node(node=7, depth=3)
-1

>>> find_parent_node(node=10, depth=4)
14

>>> find_parent_node(node=19, depth=5)
21

>>> find_parent_node(depth=3, node=3)
7
>>> find_parent_node(depth=2, node=3)
-1
>>> find_parent_node(depth=1, node=1)
-1
>>> find_parent_node(depth=2, node=2)
3
>>> find_parent_node(depth=3, node=2)
3

"""


def bintree_node_count(depth) -> int:
    """Вычисляет количество узлов полного бинарного дерева
    :depth: Глубина дерева
    """
    return 2**depth - 1


def upsidedown_bin_tree(depth: int, find_node: int, start_num: int = 1) -> int:
    """Реккурсивно ищем ребенка с нужным номером и возвращаем свой номер,
    если нет такого ребенка, идем в одно из поддеревьев рекурсивно
    :depth: Глубина дерева
    :find_node: Номер разыскиваемого узла
    :start_num: Нумерация узлов дерева начиная с
    """

    children_noeds_count = bintree_node_count(depth - 1)
    left_child_num = start_num - 1 + children_noeds_count
    right_child_num = left_child_num + children_noeds_count
    my_num = right_child_num + 1

    if (
        left_child_num == find_node or right_child_num == find_node
    ):  # ребенок этого узла
        return my_num
    elif find_node < left_child_num:  # в глубине левого дерева
        return upsidedown_bin_tree(depth - 1, find_node, start_num)
    elif find_node < right_child_num:  # в глебине правого дерева
        return upsidedown_bin_tree(depth - 1, find_node, left_child_num + 1)
    else:  # вызов с номером узла больше допустимого
        raise ValueError(
            f"Binary tree depth={depth} cannot contain node find_node={find_node}"
        )


def find_parent_node(depth, node) -> int:
    """Проверяем корректность запроса и вызываем рекурсивную функцию"""
    if node >= bintree_node_count(depth):
        return -1
    else:
        return upsidedown_bin_tree(depth, node)


if __name__ == "__main__":
    import doctest

    # Все тесты из докстинга
    doctest.testmod()

    # Выбрасывает ValueError
    print(upsidedown_bin_tree(3, 100))
