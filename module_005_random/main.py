'''
    Модуль 5
    Реализуйте все функции, затем запустите test.py для тестирования
'''
import random
# C помощью функции random реализуйте функцию, возвращающую случайное вещественное число от a до b
def task_1(a:float, b:float) -> float:
    return a+(b-a)*random.random()