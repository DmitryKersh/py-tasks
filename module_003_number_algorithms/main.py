'''
    Модуль 3
    Реализуйте все функции, затем запустите test.py для тестирования
'''


# Дано число. Если простое - вернуть 'PRIME', если составное - 'COMPOSITE', если 1 - '1', иначе - 'ERROR'
def task_1(n: int) -> str:

    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return 'PRIME'
        else:
            return 'COMPOSITE'
    if n == 1:
        return'1'
    else:
        'ERROR'

# Найти НОК и НОД 2 чисел (используя, что НОД(x,y) = НОД(x-y,y) если x > y, и НОД(х,х) = х). Предполагаем, что оба числа > 1
def task_2(x: int, y: int) -> int:
    return 0


# Решить квадратное уравнение по данным a, b, c.
def task_3(a: int, b: int, c: int) -> list[float]:
    import math

        dis = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(dis))
        if dis > 0:
            return("real and different roots")
            return((-b + sqrt_val) / (2 * a))
            return((-b - sqrt_val) / (2 * a))

        elif dis == 0:
            return("real and same roots")
            return(-b / (2 * a))

        else:
            return("Complex Roots")
            return(- b / (2 * a), + i, sqrt_val)
            return(- b / (2 * a), - i, sqrt_val)


# Даны 2 многочлена набором коэффициентов ([1, 0, -3, 10] = 10x^3 - 3x^2 + 1). Старший коэффииент не 0
# Перемножить их и результат представить так же
def task_4(p: list[int], q: list[int]) -> list[int]:
    return []
