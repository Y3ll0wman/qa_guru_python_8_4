import math
from random import randint


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)

    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    perimeter = 2 * (a+b)

    assert perimeter == 60
    area = a * b
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    PI = math.pi
    area = PI * r**2
    print(area)

    assert area == 1661.9025137490005

    length = (PI * 2) * r
    print(length)

    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    l = [f"{randint(a=1, b=100)}",
         f"{randint(a=1, b=100)}",
         f"{randint(a=1, b=100)}",
         f"{randint(a=1, b=100)}",
         f"{randint(a=1, b=100)}",
         f"{randint(a=1, b=100)}",
         f"{randint(a=1, b=100)}",
         f"{randint(a=1, b=100)}",
         f"{randint(a=1, b=100)}",
         f"{randint(a=1, b=100)}"]

    l.sort()

    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    l = set(l)
    l = list(l)

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    zipped_values = zip(first, second)
    d = dict(zipped_values)

    print(d.values())
    assert isinstance(d, dict)
    assert len(d) == 5
