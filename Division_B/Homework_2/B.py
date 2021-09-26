"""
Так как ограничения в задаче малы - можно решить перебором
"""


def walk_right(lst, house):
    """
    Двигаемся от текущего дома вправо

    :param lst: список с домами
    :param house: текущий индекс здания
    :return: расстояние от дома до магазина
    """
    num = house + 1
    while num < 10:
        if lst[num] == 2:
            return num - house
        num += 1
    return 11


def walk_left(lst, house):
    """
    Двигаемся от текущего дома влево

    :param lst: список с домами
    :param house: текущий индекс здания
    :return: расстояние от дома до магазина
    """
    num = house - 1
    while num >= 0:
        if lst[num] == 2:
            return house - num
        num -= 1
    return 11


if __name__ == '__main__':
    a = list(map(int, input().split()))  # считываем весь список домов

    max_path = 0  # максимальное расстояние

    for index, elem in enumerate(a):
        if elem == 1:
            # если элемент - дом, то ищем минимальное расстояние до магазина
            # и сравниваем с текущим максимумом
            max_path = max(min(walk_right(a, index),
                               walk_left(a, index)),
                           max_path)
    print(max_path)  # выодим ответ
