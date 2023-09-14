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
"""
Входные данные: таблица Кэли бинарной операции на множестве X
Выходные данные: операция ассоциативна или неассоциативна.
Описание алгоритма: 
1. n = размер таблицы Кэли, i = 0
2. пока i меньше n-1, то j = 0 и шаг 3, иначе щаг 7
3. пока j меньше n-1, то k = 0 и шаг 4, иначе i++ и шаг 2
4. пока k меньше n-1, то шаг 5, иначе j++ и шаг 3
5. если cayleyTable[cayleyTable[i][j]][k] неравно cayleyTable[i][cayleyTable[j][k]], тогда шаг 6,
иначе k++ и шаг 4
6. вывод: операция неассоциативна, далее выход из функции
7. вывод: операция ассоциативна, далее выход из функции
Временная сложность алгоритма:
O(n^3), так как он содержит три вложенных цикла, каждый из которых работает от 0 до n-1 раз.
"""
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

"""
Входные данные: полугруппа S с таблицей Кэли и подмножество X ⊂ S.
Выходные данные: подполугруппа 〈X〉 ⊂ S.
Описание алгоритма:
1. result = [] (результирующая подполугруппа)
2. проходимся по всем элементам подмножества X и добавляем их в result
3. проходимся по всем элементам result (i), если прошли по всем, тогда шаг 9
4. находим индекс i-го элемента (index1) в полугруппе S (semigroup)
5. проходимся по всем элементам result (j)
6. находим индекс j-го элемента (index2) в полугруппе S (semigroup)
7. проверяем, входит ли элемент в таблице Кэли (cayleTable[index1][index2]) в result, если да, шаг 8, иначе шаг 5
8. добавляем этот элемент в result
9. делаем из result множество (result = set(result))
10. на выходе: result, конец алгоритма.


Временная сложность алгоритма:
есть временная сложность самой медленной части алгоритма, а именно два вложенных цикла «for». 
Таким образом, временная сложность = O(n^2)
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

# функция получения полугруппы бинарных отношений по заданному порождающему множеству X

"""
Входные данные: конечное множество X бинарных отношений (булевых матриц)
Выходные данные: полугруппа <X>
Описание алгоритма:
1. копируем полученное на входе конечное множество X булевых матриц в результирующую полугруппу (semigroup), i = 0
2. пока i меньше (размер полугруппы + 1), тогда j = 0 и шаг 3, иначе шаг 7
3. пока j меньше (размер полугруппы), тогда шаг 4, иначе i++ и шаг 2
4. matrix = с помощью вспомогательной функции matrixComposition получаем композицию матриц semigroup[i] и semigroup[j]
5. если matrix нет в semigroup, тогда шаг 6, иначе j++ и шаг 3
6. добавляем matrix в semigroup, j++ и шаг 3
7. на выходе: полугруппа <X> (semigroup)

Временная сложность алгоритма: O(n^3), так как в функции getSemigroup присутствует вызов функции matrixComposition, 
в которой присутствует три вложенных цикла "for". 
"""
def getSemigroup(X):
    semigroup = X.copy()  # начальное состояние полугруппы - порождающее множество
    # добавляем новые матрицы, полученные композицией уже имеющихся
    for i in range(len(semigroup)+1):
        for j in range(len(semigroup)):
            matrix = matrixComposition(semigroup[i], semigroup[j])
            if matrix not in semigroup:
                semigroup.append(matrix)
    return semigroup

# композиция двух матриц
def matrixComposition(matrix1, matrix2):
    n = len(matrix1)
    m = len(matrix2[0])
    result = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(matrix2)):
                if matrix1[i][k] and matrix2[k][j]:
                    result[i][j] = 1
                    break
    return result


# ------------------------------------------------------------------------------------------------------------------- #
"""
Входные данные: конечное множество X бинарных отношений (булевых матриц)
Выходные данные: полугруппа <X>
Описание алгоритма:
1. копируем полученное на входе конечное множество X булевых матриц в результирующую полугруппу (semigroup)
2. проходимся по всем преобразованиями текущей полугруппы (i)
3. проходимся по всем преобразованиями текущей полугруппы (j)
4. с помощью вспомогательной функции getNewMatrix получаем новое преобразование на основе преобразований i и j
5. если нового преобразования нет в полугруппе, тогда добавляем его, иначе берем следующее преобразование j
7. на выходе: полугруппа <X> (semigroup)

Временная сложность алгоритма: O(n^3), так как в функции присутствует два вложенных цикла <<for>>, а так же во втором
вложенным цикле происходит вызов функции getNewMatrix, которая обладает сложностью O(n^2), посколько во втором цикле 
<<for>> данной функции происходит вызов еще одной функции getElement, которая обладает сложностью O(n). 
"""

def makeSemigroup(X):
    semigroup = X.copy()  # начальное состояние полугруппы - порождающее множество
    for i in semigroup:
        for j in semigroup:
            matrix = getNewMatrix(i, j)
            if matrix not in semigroup:
                semigroup.append(matrix)
    return semigroup

def getNewMatrix(matrix1, matrix2):
    newMatrix = [] # результирующее преобразование
    layerMatrix = [] # строка преобразования
    for i in range(len(matrix1)+1): # проходимся по элементам строки
        layerMatrix.append(matrix1[0][i]) # добавляем элементы первый строки в layerMatrix
    newMatrix.append(layerMatrix) # добавляем полученную layerMatrix в результирующее преобразование
                                  # в кач-ве первой строки
    layerMatrix = [] # обновляем layerMatrix
    for i in range(len(matrix1)+1): # проходимся по всем элементам следующей строки первого преобразования
        layerMatrix.append(getElement(matrix1[1][i], matrix2)) # добавляем в layerMatrix
                                                               # соответствующий элемент из второго преобразования
    newMatrix.append(layerMatrix) # добавляем полученную layerMatrix в результирующее преобразование
                                  # в кач-ве второй строки
    return newMatrix

def getElement(a, matrix2):
    for i in range(len(matrix2)+1): # проходимся по элементам второго преобразования
        if (matrix2[0][i]) == a: # если элемент из первой строки второго преобразования равен
                                 # элементу из второй строки первого преобразования
            res = matrix2[1][i] # добавляем соответствующий
            return res




"""
MAIN PROGRAM
"""
print("Лабораторная работа №3")
choosePoint = int(input("Выберите номер задания: "))
if choosePoint == 1:
    """
    1. Алгоритм теста Лайта проверки ассоциативности бинарной операции
    """
    print("1. Алгоритм теста Лайта проверки ассоциативности бинарной операции")
    n = int(input("Введите размер таблицы Кэли"))
    cayleyTable = []

    print("Введите таблицу Кэли: ")
    cayleyTable = [list(map(int, input(f"Enter row {i + 1}: ").split())) for i in range(n)]

    # вывод таблицы Кэли
    print("Таблица Кэли: ")
    for i in range(n):
        for j in range(n):
            print(cayleyTable[i][j], end=" ")
        print()

    # проверка на ассоциативность
    assocoativityCheck = check_assocoativity(cayleyTable)
    print(assocoativityCheck)
elif choosePoint == 2:
    """
    2. Алгоритм построения подполугрупп по таблице Кэли.
    """
    print("2. Алгоритм построения подполугрупп по таблице Кэли.")
    # число элементов в полугруппе
    countS = int(input("Введите число элементов в полугруппе S: "))

    # элементы полугруппы
    semigroupElements = [0, 1, 2, 3, 4, 5, 6, 7]
    print("Введите элементы полугруппы: ")
    for i in range(countS):
        semigroupElements.append(int(input()))

    # таблица Кэли
    cayleyTable2 = []
    print("Введите таблицу Кэли: ")
    cayleyTable2 = [list(map(int, input(f"Enter row {i + 1}: ").split())) for i in range(countS)]
    # cayleyTable2 = [[0, 1, 2, 3, 4, 5, 6, 7],
    #                  [1, 2, 3, 4, 5, 6, 7, 0],
    #                  [2, 3, 4, 5, 6, 7, 0, 1],
    #                  [3, 4, 5, 6, 7, 0, 1, 2],
    #                  [4, 5, 6, 7, 0, 1, 2, 3],
    #                  [5, 6, 7, 0, 1, 2, 3, 4],
    #                  [6, 7, 0, 1, 2, 3, 4, 5],
    #                  [7, 0, 1, 2, 3, 4, 5, 6]]
    # число элементов в подмножестве
    countX = int(input("Введите число элементов в подмножестве X: "))
    # элементы подмножества
    subset = []
    print("Введите элементы подмножества: ")
    for i in range(countX):
        subset.append(int(input()))

    result = findSubsemigroup(cayleyTable2, subset, semigroupElements)
    print("Таблица Кэли: ")
    for i in cayleyTable2:
        print(i)
    print("Подполугруппа: ", result)
elif choosePoint == 3:
    """
    3. Алгоритм построения полугруппы бинарных отношений по заданному порождающему множеству.
    """
    print("3. Алгоритм построения полугруппы бинарных отношений по заданному порождающему множеству.")
    matrixCount = int(input("Количество матриц = "))
    matrixSizeN = int(input("Размерность матрицы (строки) = "))
    matrixSizeM = int(input("Размерность матрицы (столбцы) = "))
    matrix3 = []

    for i in range(0, matrixCount):
        print("Матрица #", i + 1)
        matrix = []
        for i in range(matrixSizeN):
            a = []
            for j in range(matrixSizeM):
                a.append(int(input()))
            matrix.append(a)
        matrix3.append(matrix)

    y = 1
    for mat in matrix3:
        print("Матрица ", y)
        for i in mat:
            print(i, sep=' ')
        print()
        y += 1

    result = getSemigroup(matrix3)
    k = 1
    for i in result:
        print("Полугруппа ", k)
        for j in i:
            print(j, sep=' ')
        k += 1
else:
    """
    второй вариант алгоритма для нахождения полугруппы
    """
    print("3. Алгоритм построения полугруппы бинарных отношений по заданному порождающему множеству.")
    matrixCount = int(input("Количество преобразований = "))
    matrixSizeN = 2
    matrixSizeM = 3
    matrix3 = []

    for i in range(0, matrixCount):
        print("Преобразование #", i + 1)
        matrix = []
        for i in range(matrixSizeN):
            a = []
            for j in range(matrixSizeM):
                a.append(int(input()))
            matrix.append(a)
        matrix3.append(matrix)

    y = 1
    for mat in matrix3:
        print("Преобразование ", y)
        for i in mat:
            print(i, sep=' ')
        print()
        y += 1

    res = makeSemigroup(matrix3)
    k = 1
    print("Найденная полугруппа преобразований множества X")
    for i in res:
        print()
        for j in i:
            print(j, sep=' ')








"""
matrixSet = [[[1, 0, 1],[0, 1, 0], [0, 0, 1]], [[1, 1, 0], [0, 0, 1], [1, 0, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
1 0 1
0 1 0
0 0 1

1 1 0
0 0 1
1 0 1

0 0 0
0 0 0
0 0 0

1
0
1
0
1
0
0
0
1

1
1
0
0
0
1
1
0
1

0
0
0
0
0
0
0
0
0





0 1 0 1
0 1 0 1
0 1 2 3
0 1 2 3

0 1 2 3 4 5 6 7
1 2 3 4 5 6 7 0 
2 3 4 5 6 7 0 1 
3 4 5 6 7 0 1 2
4 5 6 7 0 1 2 3
5 6 7 0 1 2 3 4
6 7 0 1 2 3 4 5 
7 0 1 2 3 4 5 6


"""