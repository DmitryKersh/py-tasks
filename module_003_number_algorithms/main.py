'''
    Модуль 3
    Реализуйте все функции, затем запустите test.py для тестирования
'''

import math
#1 Дано число. Если простое - вернуть 'PRIME', если составное - 'COMPOSITE', если 1 - '1', иначе - 'ERROR'
def task_1(n: int) -> str:
    if n == 1:
        return '1'
    if n <= 0:
        return 'ERROR'
    num1 = 2
    while num1 < n:
        if n % num1 == 0:
            return 'COMPOSITE'
        num1 = num1 + 1
    return 'PRIME'

#2 Найти НОК и НОД 2 чисел (используя, что НОД(x,y) = НОД(x-y,y) если x > y, и НОД(х,х) = х). Предполагаем, что оба числа > 1
def task_2(x: int, y: int) -> int:
    return 0


#3 Решить квадратное уравнение по данным a, b, c.
def task_3(a: int, b: int, c: int) -> list[float]:
    if a == 0:
        return [-c / b]
    discr = b ** 2 - (4 * a * c)
    if discr > 0:
        x1 = (-b - math.sqrt(discr)) / (2 * a)
        x2 = (-b + math.sqrt(discr)) / (2 * a)
        return [x1, x2]
    if discr == 0:
        x = -b / (2 * a)
        return [x]
    return []

# Даны 2 многочлена набором коэффициентов ([1, 0, -3, 10] = 10x^3 - 3x^2 + 1). Старший коэффииент не 0
# Перемножить их и результат представить так же
def task_4(p: list[int], q: list[int]) -> list[int]:
    return []
