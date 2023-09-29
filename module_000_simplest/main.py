'''
    Модуль 0
    Реализуйте все функции, затем запустите test.py для тестирования
    Встроенные функции min/max использоавть нельзя (но можно написать свои)
'''

import math
# 1  Даны 2 целых числа. Если одно из них делится на другое, вернуть их сумму, иначе - произведение
# Ноль делится на любое число кроме нуля
def task_1(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return a + b
    if a % b == 0 or b % a == 0:
        return a + b
    else:
        return a * b


# 2  Дано целое число. Если оно делится на 3, вернуть 'fizz', если на 5 - 'buzz', если и на 3 и на 5 - 'fizzbuzz' иначе - пустую строку
def task_2(a: int) -> str:
    if a % 3 == 0 and a % 5 != 0:
        return 'fizz'
    if a % 5 == 0 and a % 3 != 0:
        return 'buzz'
    if a % 3 == 0 and a % 5 == 0:
        return 'fizzbuzz'
    else:
        return ''


# 3 Даны длины двух катетов треугольника. Посчитать гипотенузу. Если хоть одно из чисел <= 0, вернуть -1
def task_3(a: float, b: float) -> float:
    if a <= 0 or b <= 0:
        return -1
    c = math.sqrt(a*a + b*b)
    return c


# 4 Посчитать факториал числа. Если число < 0, вернуть -1
def task_4(a: int) -> int:
    result = 1
    if a < 0:
        return -1
    if a == 0:
        return 1
    i = 1
    while i <= a:
        result = result * i
        i = i + 1
    return result

# 5 Посчитать сумму целых чисел между a и b включительно
def task_5(a: int, b: int) -> int:
    number1 = a
    number2 = b
    return sum(range(number1 + 1, number2))


# 6 Посчитать площадь поверхности параллелепипеда со сторонами a, b, c. Если хоть одно число <= 0, вернуть 0
def task_6(a: int, b: int, c: int) -> int:
    s = 2*(a*b+b*c+c*a)
    if a <= 0 or b <= 0 or c <= 0:
        return 0

# 7 Проверить существование треугольника со сторонами a, b, c (неравенство треугольника)
def task_7(a: int, b: int, c: int) -> bool:
    if a + b > c:
        return "False"
    if a + b <= c:
        return "true"