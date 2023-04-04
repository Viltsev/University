"""
Комбинаторная теория полугрупп

1. Рассмотреть понятия полугруппы разработать алгоритм теста Лайта проверки ассоциативности бинарной операции [4],[5].
Вход: таблица Кэли бинарной операции на множестве 􏰀.
Выход: операция ассоциативна или неассоциативна.

2. Рассмотреть понятия подполугруппы и порождающего множества [4],[5].
Разработать алгоритм построения подполугрупп по по таблице Кэли. Вход: полугруппа S с таблицей Кэли и подмножество X ⊂ S.
Выход: подполугруппа 〈X〉 ⊂ S.

3. Разработать алгоритм построения полугруппы бинарных отношений по заданному порождающему множеству [4],[5],[9] .
Вход: конечное множество X бинарных отношений (булевых матриц).
Выход: полугруппа 〈X〉.
"""

"""
FUNCTIONS
"""
import math
import numpy as np
import sys

# функция проверки операции на ассоциативность
def check_assocoativity(cayleyTable):
    n = len(cayleyTable)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if cayleyTable[cayleyTable[i][j]][k] != cayleyTable[i][cayleyTable[j][k]]:
                    return "Операция неассоциативна"
    return "Операция ассоциативна"

# функция получения подполугруппы
"""
подмножество: {2}
таблица:
0, 1, 2, 3, 4, 5, 6, 7
1, 2, 3, 4, 5, 6, 7, 0
2, 3, 4, 5, 6, 7, 0, 1
3, 4, 5, 6, 7, 0, 1, 2
4, 5, 6, 7, 0, 1, 2, 3
5, 6, 7, 0, 1, 2, 3, 4
6, 7, 0, 1, 2, 3, 4, 5
7, 0, 1, 2, 3, 4, 5, 6

полугруппа: 0, 1, 2, 3, 4, 5, 6, 7

1. берем элемент из текущего подмножества и кладем его в подполугруппу
2. далее находим индекс данного элемента в полугруппе
3. проделываем шаг 2 для остальных элементов в подполугруппе
4. i-ую позицию умножаем на j-ую и полученный элемент кладем в подполугруппу

"""
def findSubsemigroup(cayleTable, X, semigroup):
    result = []
    for i in X:
        result.append(i)
    for i in result:
        index1 = semigroup.index(i)
        for j in result:
            index2 = semigroup.index(j)
            elementToAppend = cayleTable[index1][index2]
            if not(elementToAppend in result):
                result.append(elementToAppend)
    result = set(result)
    return result
    




"""
MAIN PROGRAM
"""
print("Лабораторная работа №3")

"""
1. Алгоритм теста Лайта проверки ассоциативности бинарной операции
"""

# print("1. Алгоритм теста Лайта проверки ассоциативности бинарной операции")
# n = int(input("Введите размер таблицы Кэли"))
# cayleyTable = []
#
# print("Введите таблицу Кэли: ")
# cayleyTable = [list(map(int, input(f"Enter row {i+1}: ").split())) for i in range(n)]
#
# # вывод таблицы Кэли
# print("Таблица Кэли: ")
# for i in range(n):
#     for j in range(n):
#         print(cayleyTable[i][j], end=" ")
#     print()
#
# # проверка на ассоциативность
# assocoativityCheck = check_assocoativity(cayleyTable)
# print(assocoativityCheck)

"""
2. Алгоритм построения подполугрупп по таблице Кэли.
"""
print("2. Алгоритм построения подполугрупп по таблице Кэли.")
# число элементов в полугруппе
# countS = int(input("Введите число элементов в полугруппе S: "))

# элементы полугруппы
semigroupElements = [0, 1, 2, 3, 4, 5, 6, 7]
# print("Введите элементы полугруппы: ")
# for i in range(countS):
#     semigroupElements.append(int(input()))

# таблица Кэли
# cayleyTable2 = []
# print("Введите таблицу Кэли: ")
# cayleyTable2 = [list(map(int, input(f"Enter row {i+1}: ").split())) for i in range(countS)]
cayleyTable2 = [[0, 1, 2, 3, 4, 5, 6, 7],
                 [1, 2, 3, 4, 5, 6, 7, 0],
                 [2, 3, 4, 5, 6, 7, 0, 1],
                 [3, 4, 5, 6, 7, 0, 1, 2],
                 [4, 5, 6, 7, 0, 1, 2, 3],
                 [5, 6, 7, 0, 1, 2, 3, 4],
                 [6, 7, 0, 1, 2, 3, 4, 5],
                 [7, 0, 1, 2, 3, 4, 5, 6]]
# число элементов в подмножестве
# countX = int(input("Введите число элементов в подмножестве X: "))
countX = 1
# элементы подмножества
subset = [2]
# print("Введите элементы подмножества: ")
# for i in range(countX):
#     subset.append(int(input()))

result = findSubsemigroup(cayleyTable2, subset, semigroupElements)
print("Таблица Кэли: ")
for i in cayleyTable2:
    print(i)
print("Подполугруппа: ", result)
