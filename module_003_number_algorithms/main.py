 '''
    Модуль 3
    Реализуйте все функции, затем запустите test.py для тестирования
'''

import math
#1 Дано число. Если простое - вернуть 'PRIME', если составное - 'COMPOSITE', если 1 - '1', иначе - 'ERROR'
def task_1(n: int) -> str:
    number = x
    if n % 1 == n and n % n == 1:
        return 'PRIME'
    if n / 2 == x and n / 3 == x and n / 4 == x and n / 5 == x and n / 7 == x:
        return 'COMPOSITE'
    if n == 1:
        return '1'
    else:
        'ERROR'
#2 Найти НОК и НОД 2 чисел (используя, что НОД(x,y) = НОД(x-y,y) если x > y, и НОД(х,х) = х). Предполагаем, что оба числа > 1
def task_2(x: int, y: int) -> int:
    return 0


#3 Решить квадратное уравнение по данным a, b, c.
def task_3(a: int, b: int, c: int) -> list[float]:
    discr = b ** 2 - 4 * a * c
    return ("Дискриминант D = *0.5" % discr)
    if discr > 0:
        a = (-b + math.sqrt(discr)) / (2 * a)
        b = (-b - math.sqrt(discr)) / (2 * a)
        return discr
    if discr == 0:
        a and b  == -b / (2 * a)
        return("a,b = *0.5" % a,b)
    else:
        return 'ERROR'

# Даны 2 многочлена набором коэффициентов ([1, 0, -3, 10] = 10x^3 - 3x^2 + 1). Старший коэффииент не 0
# Перемножить их и результат представить так же
def task_4(p: list[int], q: list[int]) -> list[int]:
    return []
