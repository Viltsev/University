"""
Идеалы полугрупп
"""
import numpy as np
from tabulate import tabulate

"""
FUNCTIONS
"""

# Функции для 1 задания

# Функция получения идеалов
# Вход: таблица Кэли, полугруппа S
# Выход: печать идеалов полугруппы S

def getIdeals(caleyTable, semigroup, isPrinted = False):
    ideals = {} # идеалы полугруппы
    for i in range(len(semigroup)): # проходимся по полученной полугруппе
        setFirst = set(caleyTable[i]) # получаем i-ый эл-т из таблицы Кэли
        setSecond = set(caleyTable.T[i])
        rIdeal, lIdeal, dIdeal = setFirst, setSecond, setFirst.union(setSecond)
        ideals[semigroup[i]] = rIdeal, lIdeal, dIdeal
        if isPrinted: # печать идеалов полугруппы
            print(f"Подполугруппа <{semigroup[i]}>. Правый идеал = ", rIdeal,
                  f"\nПодполугруппа <{semigroup[i]}>. Левый идеал = ", lIdeal,
                  f"\nПодполугруппа <{semigroup[i]}>. Двусторонний идеал = ", dIdeal)
    return cayley_table, semigroup, ideals

# Функция получения полугруппы S и таблицы Кэли
# Вход: множество символов A, конечное множество R определяющих соотношений
# Выход: таблица Кэли, полугруппа S
def makePolugroupAndCaleyTable(arrA, arrR):
    # получение полугруппы
    semigroup = arrA.copy() # копируем в полугруппу элементы из введенного множества
    flag = True
    while flag:
        newElems = [] # новые элементы, которые будут добавляться в полугруппу
        for firstElem in semigroup: # проходимся по элементам полугруппы
            for secondElem in semigroup:
                newElemOne = firstElem + secondElem # получаем новый элемент
                while flag:
                    copyOfNewElement = str(newElemOne) # копия нового элемента
                    for first, second in arrR.items(): # проходимся по элементам определяющих соотношений
                        if first in newElemOne:
                            newElemOne = newElemOne.replace(first, second)
                    if copyOfNewElement == newElemOne:
                        break
                newElems.append(newElemOne)
        newestSemigroup = set(semigroup.copy()) # формирование новой полугруппы
        for i in newElems:
            if i not in semigroup:
                semigroup.append(i)
        if newestSemigroup == set(semigroup):
            break
    semigroup = list(semigroup)

    # получение таблицы Кэли
    matrixCaley = []
    for firstElem in semigroup: # проходимся по элементам полугруппы
        matrixStr = [] # строка таблицы Кэли
        for secondElem in semigroup:
            newElement = firstElem + secondElem # получаем новый элемент для таблицы Кэли
            while flag:
                copyOfNewElement = str(newElement) # копия нового элемента
                for first, second in arrR.items():
                    if first in newElement:
                        newElement = newElement.replace(first, second)
                if copyOfNewElement == newElement:
                    break
            matrixStr.append(newElement)
        matrixCaley.append(matrixStr) # получаем таблицу Кэли

    semigroupLen = len(semigroup)
    resultCaley = np.array(matrixCaley).reshape(semigroupLen, semigroupLen)

    return resultCaley, semigroup, matrixCaley


# Функции для 2-3 заданий
def getGrinRelation():
    breakPoint = True
    while breakPoint:
        print("Вычислить отношение Грина по: ")
        print("1 - таблице Кэли")
        print("2 - порождающему множеству и определяющим соотношениям")
        print("3 - выйти")
        choose = input()
        if choose == "1":
            print("Введите элементы таблицы Кэли: ")
            newArrA = input().replace(",", "").split()
            n = len(newArrA)

            matrix = []
            for i in range(n):
                row = input(f"Введите элементы {i + 1}-й строки через пробел: ").split()
                matrix.append(row)

            r = getR(matrix, newArrA)
            l = getL(matrix, newArrA)
            j = r
            d = r + [x for x in l if x not in r]
            h = [x for x in r if x in l]
            print("Отношение Грина: ")
            print("R: ", r)
            print("L: ", l)
            print("J: ", j)
            print("D: ", d)
            print("H: ", h)

            rClass = getClass(r)
            lClass = getClass(l)
            jClass = getClass(j)
            dClass = getClass(list(d))
            hClass = getClass(list(h))

            print("Класс экв-ти R", rClass)
            print("Класс экв-ти L", lClass)
            print("Класс экв-ти J", jClass)
            print("Класс экв-ти D", dClass)
            print("Класс экв-ти H", hClass)

            print("Egg-box-картина:")
            getEggBox(rClass)
        if choose == "2":
            print('Введите элементы множества:')
            arrA = input().split()

            print("Введите количество определяющих соотношений:")
            amountR = int(input())

            arrR = {}

            print("Введите определяющие соотношения")
            for i in range(amountR):
                x, y = input().split()
                arrR[x] = y

            _, semigroup, caleyTable  = makePolugroupAndCaleyTable(arrA, arrR)
            print("Полученная полугруппа: ", semigroup)
            print("Таблица Кэли: ")
            print(tabulate(caleyTable))
            r = getR(caleyTable, semigroup)
            l = getL(caleyTable, semigroup)
            j = r
            d = r + [x for x in l if x not in r]
            h = [x for x in r if x in l]

            rClass = getClass(r)
            lClass = getClass(l)
            jClass = getClass(j)
            dClass = getClass(d)
            hClass = getClass(h)

            print("Класс экв-ти R", rClass)
            print("Класс экв-ти L", lClass)
            print("Класс экв-ти J", jClass)
            print("Класс экв-ти D", dClass)
            print("Класс экв-ти H", hClass)

            print("Egg-box-картина:")
            getEggBox(rClass)
        if choose == "3":
            breakPoint = False

def getR(matrix, arrA):
    comparisons = []

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            if set(matrix[i]) == set(matrix[j]):
                pair = (arrA[i], arrA[j])
                comparisons.append(pair)
                if i != j:
                    pair = (arrA[j], arrA[i])
                    comparisons.append(pair)
    return comparisons

def getL(matrix, arrA):
    transposed = list(zip(*matrix))

    comparisons = []

    n = len(transposed)

    for i in range(n):
        for j in range(i, n):
            if set(transposed[i]) == set(transposed[j]):
                pair = (arrA[i], arrA[j])
                comparisons.append(pair)
                if i != j:
                    pair = (arrA[j], arrA[i])
                    comparisons.append(pair)
    return comparisons

def getClass(array):
    result = []
    subresult = []

    for pair in array:
        for otherPair in array:
            if pair[0] == otherPair[0]:
                subresult.append(pair[1])
                subresult.append(otherPair[1])

        if set(subresult) not in result:
            result.append(set(subresult))
        subresult = []
    return result


def getEggBox(array):
    for mySet in array:
        print("----")
        res = '|' + '|'.join(mySet) + '|'
        print(res)
        print("----")

"""
MAIN PROGRAM
"""
print("Лабораторная работа №5. Вильцев Д.Д., 311")


breakPoint = True
while breakPoint:
    print("Выбор задания: ")
    print("1 - Построить идеалы полугруппы по таблице Кэли")
    print("2 - Вычислить отношения Грина и построить <<egg-box>>-картину конечной полугруппы")
    print("3 - Выйти")
    chooseTask = input()
    if chooseTask:
        if chooseTask == "1":
            print('Введите элементы множества:')
            arrA = input().split()

            print("Введите количество определяющих соотношений:")
            amountR = int(input())

            arrR = {}

            print("Введите определяющие соотношения")
            for i in range(amountR):
                x, y = input().split()
                arrR[x] = y

            cayley_table, semigroup, _ = makePolugroupAndCaleyTable(arrA, arrR)

            print("Задание 1.")
            print("Полученная полугруппа: ", semigroup)
            print("Таблица Кэли: ")
            print(tabulate(cayley_table))

            print("Полученные идеалы полугруппы S, порожденные множеством X: ")
            getIdeals(cayley_table, semigroup, True)

        if chooseTask == "2":
            print("Задание 2.")
            print("Отношения Грина и egg-box картина полугруппы S: ")
            getGrinRelation()
        if chooseTask == "3":
            breakPoint = False

