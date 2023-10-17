'''
    Модуль 3
    Реализуйте все функции, затем запустите test.py для тестирования
'''


# Дано число. Если простое - вернуть 'PRIME', если составное - 'COMPOSITE', если 1 - '1', иначе - 'ERROR'
def task_1(n: int, number=None) -> str:
    num1 = n
    num2 = random number
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
        return num1 or num2
    else:
        'ERROR'

# Найти НОК и НОД 2 чисел (используя, что НОД(x,y) = НОД(x-y,y) если x > y, и НОД(х,х) = х). Предполагаем, что оба числа > 1
def task_2(x: int, y: int) -> int:
    return 0


# Решить квадратное уравнение по данным a, b, c.
def task_3(a: int, b: int, c: int) -> list[float]:
    import math
    x1 = a
    x2 = b
    discr = b ** 2 - 4 * a * c
    return "Дискриминант D = %.2f" % discr
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return ("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    if discr == 0:
        x = -b / (2 * a)
        return ("x = %.2f" % x)
    else:
        return[x1, x2]

# Даны 2 многочлена набором коэффициентов ([1, 0, -3, 10] = 10x^3 - 3x^2 + 1). Старший коэффииент не 0
# Перемножить их и результат представить так же
def task_4(p: list[int], q: list[int]) -> list[int]:
    return []
