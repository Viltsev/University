"""
Отношение порядка и упорядоченные множества

1. Разобрать определения отношения порядка и диаграммы Хассе. Разработать
алгоритмы вычисления минимальных (максимальных) и наименьших
(наибольших) элементов
Вход: отношение порядка.
Выход: найденные минимальные (максимальные) и наименьшие (наибольшие) элементы данного отношения порядка.

2. Разработать алгоритм построения диаграммы Хассе
Вход: отношение порядка.
Выход: диаграмма Хассе данного отношения порядка.

3. Разобрать определения контекста и концепта. Разработать алгоритм вычисления
решетки концептов.
Вход: матрица контекста.
Выход: решетка концептов данного контекста и ее диаграмма Хассе.
"""

"""
FUNCTIONS
"""
import math
import numpy as np
import sys
# функция нахождения делителей числа (отношения порядка)
def find_divisors(n):
    divisors = []
    for i in range(2, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def smallest_divisors(arr):
    def find_minimal_divisor(n):
        for i in arr:
            if n % i == 0:
                return i
        return n
    res = []
    for n in arr:
        res.append(find_minimal_divisor(n))
    result = list(set(res))
    return result


def count_divisors(n, arr):
    """возвращает количество делителей числа n"""
    count = 0
    for i in arr:
        if n % i == 0:
            count += 1
    return count

def min_divisors(arr):
    min_num_divisors = sys.maxsize
    min_num_divisors_elem = []
    for elem in arr:
        num_divisors = count_divisors(elem, arr)
        if num_divisors <= min_num_divisors:
            min_num_divisors = num_divisors
            min_num_divisors_elem.append(elem)
    return min_num_divisors_elem

def max_divisors(arr):
    """возвращает число с наибольшим количеством делителей"""
    max_num_divisors = 0
    max_num_divisors_elem = []
    for elem in arr:
        num_divisors = count_divisors(elem, arr)
        if num_divisors > max_num_divisors:
            max_num_divisors = num_divisors
            if len(max_num_divisors_elem) > 0:
                max_num_divisors_elem.remove(max_num_divisors_elem[0])
            max_num_divisors_elem.append(elem)
        # elif num_divisors == max_num_divisors:
        #     max_num_divisors_elem.append(elem)
    return max_num_divisors_elem

def hasseDiagram(orderRatio):
    level = 0
    arrayOfLevels = []

    while len(orderRatio) > 0:
        minLevel = min_divisors(orderRatio)
        print("Уровень", level, ": ", *minLevel, sep= ' ')
        print()

        for valueToRemove in minLevel:
            orderRatio.remove(valueToRemove)

        arrayOfLevels.append(minLevel)
        level += 1

    print("Связи: ")
    array = []
    for curLevel in range(0, len(arrayOfLevels) - 1):
        for i in arrayOfLevels[curLevel]:
            for j in arrayOfLevels[curLevel + 1]:
                if j % i == 0:
                    array.append(j)
            print(i, ":", *array, sep=' ')
            print()
            array = []



"""
MAIN PROGRAM
"""

print("Лабораторная работа №2")
myNumber = int(input("Введите число:"))

# 1.Алгоритмы вычисления минимальных (максимальных) и наименьших (наибольших) элементов
print("1. Алгоритмы вычисления минимальных (максимальных) и наименьших (наибольших) элементов")

orderRatio = find_divisors(myNumber)
print("Отношение порядка числа ", myNumber)
print("{", *orderRatio, "}")
print()

minElementsOR = min_divisors(orderRatio)
if len(minElementsOR) == 1:
    print("Наименьший (минимальный) элемент отношения порядка: ")
    print(minElementsOR[0])
else:
    print("Минимальные элементы отношения порядка: ")
    print("{", *minElementsOR, "}")

maxElementsOR = max_divisors(orderRatio)
if len(maxElementsOR) == 1:
    print("Наибольший (максимальный) элемент отношения порядка: ")
    print(maxElementsOR[0])
else:
    print("Максимальные элементы отношения порядка: ")
    print("{", *maxElementsOR, "}")
print()

# 2. Алгоритм построения диаграммы Хассе
print("2. Алгоритм построения диаграммы Хассе")
hasseDiagram(orderRatio)

# 3. Алгоритм вычисления решетки концептов
print("3. Алгоритм вычисления решетки концептов")


