import numpy as np

# копирование матрицы
def copy(matrix):
    return [row[:] for row in matrix]

# Функции для задания №1
# проверка на рефлексивность
def reflex(matrix, n):
    reflexCheck = True
    for i in range(n):
        # если на главной диагонали есть хотя бы один 0 -> нерефлексивное
        if (matrix[i][i] != 1):
            reflexCheck = False
            break
    return reflexCheck

# проверка на симметричность
def symmetry(matrix, n):
    symmetryCheck = True
    for i in range(n):
        for j in range(n):
            # если i,j элемент не равен с j,i -> несимметричное
            if (i != j and matrix[i][j] != matrix[j][i]):
                symmetryCheck = False
                break
    return symmetryCheck

# проверка на транзитивность
def transitivity(matrix, n):
    transitivityCheck = True
    for i in range(n):
        for j in range(n):
            # если i,j элемент = 1
            if (matrix[i][j] == 1):
                for k in range(n):
                    # а также j,k = 1, но при этом i,k != 1 -> нетранзитивное
                    if (matrix[j][k] == 1 and matrix[i][k] == 0):
                        transitivityCheck = False
                        break
    return transitivityCheck


# проверка на антисимметричность
def antisymmetry(matrix, n):
    antisymmetryCheck = True
    for i in range(n):
        for j in range(n):
            # если элемент не на главной диагонали i,j != 0
            # и при этом i,j == j,i -> не антисимметричное
            if (i != j and matrix[i][j] != 0 and matrix[i][j] == matrix[j][i]):
                antisymmetryCheck = False
                break
    return antisymmetryCheck

# проверка на антирефлексивность
def antireflex(matrix, n):
    antireflexCheck = True
    # если на главной диагонали есть хотя бы одна единица - не антирефлексивно
    for i in range(n):
        if (matrix[i][i] == 1):
            antireflexCheck = False
            break
    return antireflexCheck


# Функции для задания №2
# рефлексивное замыкание
def reflexClosure(matrix, n):
    result = copy(matrix)
    for i in range(n):
        # если на главной диагонали есть элемент != 1 -> присваиваем ему единицу
        if (result[i][i] != 1):
            result[i][i] = 1
    return result

# симметричное замыкание
def symmetryClosure(matrix, n):
    result = copy(matrix)
    for i in range(n):
        for j in range(n):
            # если элемент не на главной диагонали i,j или j,i равны 1
            # тогда делаем их оба равными единице
            if (i != j and (result[i][j] == 1 or result[j][i] == 1)):
                result[i][j] = result[j][i] = 1
    return result

# транзитивное замыкание
# def transitiveClosure(matrix, n):
#     result = copy(matrix)
#     for i in range(n):
#         for j in range(n):
#             # если элемент с индексом i,j = 1
#             if result[i][j] == 1:
#                 for k in range(n):
#                     # а также элемент с индексом j,k = 1
#                     if result[j][k] == 1:
#                         # тогда i,k элемент будет равен 1
#                         result[i][k] = 1
#     return result


# возведение матрицы в квадрат
def matrixSquare(matrix, n):
    result = copy(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mul = 0
                if result[i][k] and result[k][j]:
                    mul = 1
                if mul == 0 and result [i][j] == 0:
                    pass
                else:
                    result[i][j] = 1
    return result

# сумма матриц
def matrixSum(matrix1, matrix2, n):
    mat1 = copy(matrix1)
    mat2 = copy(matrix2)
    result = np.empty((n, n), dtype="int")
    for i in range(n):
        for j in range(n):
            if mat1[i][j] == 0 and mat2[i][j] == 0:
                result[i][j] = 0
            else:
                result[i][j] = 1
    return result

def transitiveClosure(matrix, mulOfMatrix, n):
    mat1 = copy(matrix) # копия матрицы
    mat2 = copy(mulOfMatrix) # копия квадратной матрицы
    res = matrixSum(mat1, mat2, n)
    if mat1 == mat2: # если матрицы равны, тогда выводим результат
        for i in range(n):
            for j in range(n):
                print(res[i][j], end=" ")
            print()
    else:
        # рекурсивно вызываем функцию транзитивного замыкания
        transitiveClosure(matrixSquare(mat1, n), matrixSquare(mat2, n), n)

# Функции для задания №3
def equivalentClosure(matrix, n):
    result = copy(matrix)
    # рефлексивное замыкание
    for i in range(n):
        for j in range(n):
            if (i == j and result[i][j] != 1):
                result[i][j] = 1
    # симметричное замыкание
    for i in range(n):
        for j in range(n):
            if (i != j and (result[i][j] == 1 or result[j][i] == 1)):
                result[i][j] = result[j][i] = 1
    # транзитивное замыкание
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if result[i][j] == 1 and result[j][k] == 1:
                    result[i][k] = 1
    return result

def factorSet(matrix, n):
    m = np.array(matrix) # копируем исходную матрицу
    ind = [] # массив индексов
    res = [] # результирующий массив
    checkArr = [] # массив для проверки посещения столбца
    for i in range(n):
        checkArr.append(0) # изначально все столбцы непосещены
    for i in range(n):
        if checkArr[i] == 0: # если i-ый столбец не посещен
            a = m[:, i] # берем i-ый столбец
            for j in range(i + 1, n): # сравнение с остальные столбцами на равенство
                b = m[:, j] # берем j-ый столбец
                if np.array_equal(a, b): # если два столбца одинаковы
                    ind.append(j) # записываем в массив индексов j-ый столбец
                    checkArr[j] = 1 # отмечаем его посещенным
            ind.append(i) # записываем в массив индексов i-ый столбец
            res.append(set(ind)) # записываем массив индексов равных столбцов в результирующий массив
            ind = [] # обнуляем массив индексов
            checkArr[i] = 1 # отмечаем i-ый столбец за посещенный
    return res


def representSystem(matrix):
    matrixCopy = matrix
    res = []
    for i in range(len(matrixCopy)):
        # берем первые элементы из фактор-множеств
        res.append(matrixCopy[i].pop())
    return res

# -----------------main programm-----------------------
print("Лабораторная работа №1")
n = int(input("Введите размер матрицы:"))
matrix = []

print("Введите матрицу:")

# Ввод матрицы
for i in range(n):
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

# Вывод матрицы
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

# 1. Проверка на основные виды бинарных отношений
print("1. Классификация бинарных отношений")
reflexCheck = reflex(matrix, n)
if reflexCheck:
    print("Рефлексивность - да")
else:
    print("Рефлексивность - нет")

symmetryCheck = symmetry(matrix, n)
if symmetryCheck:
    print("Симметричность - да")
else:
    print("Симметричность - нет")

transitivityCheck = transitivity(matrix, n)
if transitivityCheck:
    print("Транзитивность - да")
else:
    print("Транзитивность - нет")

antisymmetryCheck = antisymmetry(matrix, n)
if antisymmetryCheck:
    print("Антисимметричность - да")
else:
    print("Антисимметричность - нет")

antireflexCheck = antireflex(matrix,n)
if antireflexCheck:
    print("Антирефлексивность - да")
else:
    print("Антирефлексивность - нет")

# 2. Построение основных замыканий
print("2. Построение основных замыканий бинарных отношений")

# рефлексивное замыкание
# reflexMatrixClosure = matrix.copy()
reflexClosure = reflexClosure(matrix, n)

print("Матрица рефлексивного замыкания: ")
for i in range(n):
    for j in range(n):
        print(reflexClosure[i][j], end=" ")
    print()

# симметричное замыкание
# symMatrixClosure = matrix.copy()
symmetryClosure = symmetryClosure(matrix, n)
print("Матрица симметричного замыкания: ")
for i in range(n):
    for j in range(n):
        print(symmetryClosure[i][j], end=" ")
    print()

# транзитивное замыкание
# transMatrixClosure = matrix.copy()
transitivityClosure = transitiveClosure(matrix, n)
print("Матрица транзитивного замыкания: ")
for i in range(n):
    for j in range(n):
        print(transitivityClosure[i][j], end=" ")
    print()


# 3. Построение эквивалентного замыкания бинарного отношения
print("3. Построение эквивалентного замыкания бинарного отношения")
eqClosure = equivalentClosure(matrix, n)
print("Матрица эквивалентного замыкания: ")
for i in range(n):
    for j in range(n):
        print(eqClosure[i][j], end=" ")
    print()

print("Фактор множество:")
a = factorSet(eqClosure, n)
for i in range(len(a)):
    print(a[i], end=" ")
print()

print("Полная система представителей:")
b = representSystem(a)
for i in range(len(b)):
    print(b[i], end=" ")
print()
