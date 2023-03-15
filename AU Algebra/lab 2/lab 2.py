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
    level = 1
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

def getSetsFromMatrix(matrix, n):
    arrayOfSets = []
    array = []
    transposeMatrix = np.transpose(matrix)
    for i in range(n):
        for j in range(n):
            if transposeMatrix[i][j] == 1:
                array.append(j + 1)
        arrayOfSets.append(set(array))
        array = []
    return arrayOfSets

def closureSystem(arrayOfSets, G, n):
    resultClosure = []
    resultClosure.append(G)
    resultArrayOfSets = []
    for i in range(n):
        for j in range(len(resultClosure)):
            if not((arrayOfSets[i] & resultClosure[j]) in resultClosure):
                resultArrayOfSets.append(arrayOfSets[i] & resultClosure[j])
        for k in resultArrayOfSets:
            if not(k in resultClosure):
                resultClosure.append(k)
        resultArrayOfSets = []
    return resultClosure

# функция получения матрицы, состоящей из 0 и 1, из системы замыканий
def getMatrixClosure(closureSys, n):
    resultMatrix = []
    for i in range(0, n):
        a = []
        for j in range(0, n):
            if closureSys[j] <= closureSys[i]:
                a.append(1)
            else:
                a.append(0)
        resultMatrix.append(a)
    return resultMatrix

# вспомогательная функция для подсчета единиц в строке матрице
def onesNumber(line):
    res = 0
    for i in line:
        if i == 1:
            res += 1
    return res

# функция получения диаграммы Хассе по матрице системы замыканий
def hasseDiagramMatrix(closureSys, matrix):
    level = 1
    currentIndex = []

    arrayOfLevels = []
    currentLevel = []

    while len(matrix) > 0:
        minNumber = onesNumber(matrix[0])
        for i in range(len(matrix)):
            currentNumber = onesNumber(matrix[i])
            if currentNumber < minNumber:
                minNumber = currentNumber
                currentIndex = []
                currentIndex.append(i)
            elif currentNumber == minNumber:
                currentIndex.append(i)
        print("Уровень", level, ": ", end= ' ')
        for k in currentIndex:
            if closureSys[k] == set():
                print('Empty Set', end= ' ')
            else:
                print(closureSys[k], end= ' ')
            currentLevel.append(closureSys[k])
        arrayOfLevels.append(currentLevel)
        for k in currentIndex:
            if k > (len(matrix) - 1):
                k = (len(matrix) - 1)
            matrix.pop(k)
            closureSys.pop(k)
        print()
        currentIndex = []
        level += 1
        currentLevel = []

    print("Связи: ")
    array = []
    for curLevelInd in range(0, len(arrayOfLevels) - 1):
        for curLevel in arrayOfLevels[curLevelInd]:
            for nextLevel in arrayOfLevels[curLevelInd + 1]:
                if curLevel <= nextLevel:
                    array.append(nextLevel)
            print(curLevel, ":", *array, sep=' ')
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
n = int(input("Введите размер матрицы контекста:"))
matrix = []

print("Введите матрицу контекста:")

for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

arrayForMainSet = []
for i in range(n):
    arrayForMainSet.append(i + 1)

mainSet = set(arrayForMainSet)
# print(mainSet)

arrayOfElements = getSetsFromMatrix(matrix, n)
# print(arrayOfElements)

closureSys = closureSystem(arrayOfElements, mainSet, n)
print("Система замыканий Zfg: ")
print(closureSys)

matrixFromClosureSystem = getMatrixClosure(closureSys, len(closureSys))
print(matrixFromClosureSystem)
# for i in range(len(closureSys)):
#     for j in range(len(closureSys)):
#         print(matrixFromClosureSystem[i][j], end=" ")
#     print()

hasseDiagramMatrix(closureSys, matrixFromClosureSystem)
