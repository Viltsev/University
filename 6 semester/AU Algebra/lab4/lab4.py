"""
Копредставления полугрупп

1. Рассмотреть понятия порождающего множества и определяющих соотношений
полугруппы. Разработать алгоритм построения полугруппы по порождающему
множеству и определяющим соотношениям [4],[5],[9].
Вход: конечное множество символов A и конечное множество R определяющих соотношений.
Выход: полугруппа 〈A|R〉. Для тестирования можно взять пример из лекции.

2. Разработать алгоритм построения графов Кэли полугруппы с порождающим
множеством [9].
Вход: конечное множество символов A и конечное множество R определяющих соотношений.
Выход: граф Кэли полугруппы 〈A|R〉. Для тестирования можно взять пример из
лекции.

3. Разработать алгоритм вычисления расстояния между полугруппами [9].
Вход: две полугруппы S1, S2 с общим порождающим множеством X.
Выход: расстояние d(S1, S2) между полугруппами S1, S2
"""
from tabulate import tabulate
import math

"""
FUNCTIONS
"""

# Функция для 1 задания

# Функция преобразования строки
# Вход: строка, словарь соответствий
# Выход: упрощенная строка, в которой любая подстрока, которая соответствует
# ключу в словаре, заменена на значение этого ключа
def updateString(string, dictionary: dict):
    lengthOfString = len(string) # длина строки
    for i in range(lengthOfString): # перебор всех возможных подстрок
        for j in range(i + 1, lengthOfString + 1):
            subString = string[i:j]
            dictionaryItems = dictionary.items() # здесь хранятся все ключи и значения к ним словаря
            for key, value in dictionaryItems: # перебор всех ключей и значений словаря
                if string == key: # если строка совпадает с ключом -> возвращаем
                    return string
                if subString in value: # если подстрока есть в значении -> заменяем ее на ключ
                    return updateString(string[:i] + key + string[j:], dictionary)
    return string # если замен не обнаружено -> возвращаем исходную строку

# Функция получения нового уникального слова из словаря
# Вход: словарь
# Выход: уникальное слово
def getWord(dictionary: dict):
    dictionaryKeys = dictionary.keys() # ключи словаря
    for i in dictionaryKeys:
        for j in dictionaryKeys:
            value = updateString(j + i, dictionary) # получим новое значение из словаря
                                                    # упростив строку функцией updateString
            # Если новое значение не содержится в словаре, то возвращаем его
            if value not in dictionaryKeys: # если полученного значения нет в словаре
                return value # возвращаем его
    return None # иначе ничего не возвращаем


# Функция формирования полугруппы и таблицы Кэли
# Вход: конечное множество R определяющих соотношений
# (сформировано раннее по конечному множеству символов A)
# Выход: полугруппа <A|R>, таблица Кэли, названия столбцов
def makePolugroupAndCaleyTable(arrayR):
    # пока есть новые значения - добавляем их в R
    newValue = getWord(arrayR)
    while (newValue != None):
        arrayR[newValue] = set()
        newValue = getWord(arrayR)

    colNames = ['']
    polugroup = []
    caleyTable = []

    [polugroup.append(str(i)) for i in arrayR.keys()]
    [colNames.append(str(i)) for i in arrayR.keys()]

    for i in arrayR.keys():
        row = [str(i)]
        for j in arrayR.keys():
            row.append(updateString(j + i, arrayR))
        caleyTable.append(row)

    return polugroup, caleyTable, colNames

# Функция для 2 задания

# Функция получения графа Кэли
# Вход: конечное множество R определяющих соотношений
# # (сформировано раннее по конечному множеству символов A)
# Выход: граф Кэли полугруппы <A|R>

def getCaleyGraph(arrayR):
    rightCaley = dict()
    leftCaley = dict()
    # пройдемся по всем ключам, перемножив их
    for i in arrayR.keys():
        for j in arrayR.keys():
            leftWord = updateString(i + j, arrayR)
            rightWord = updateString(j + i, arrayR)

            if len(j) == 1:
                leftCaley[(i, leftWord)] = leftCaley.get((i, leftWord), []) + [j]
            if len(j) == 1:
                rightCaley[(i, rightWord)] = rightCaley.get((i, rightWord), []) + [j]
    return rightCaley, leftCaley

# Функция печати графов Кэли
# Вход: левый граф Кэли, правый граф Кэли
# Выход: печать левого и правого графов Кэли

def printCaleyGraph(leftCaley, rightCaley):
    print("Полученные графы Кэли: ")
    print("\n Левый граф: ")
    for i, elem in leftCaley.items():
        print(f"""({elem[0]}) --> """, end="( ")
        for j in i:
            print(j, end=" ")
        print(")")
        print()

    print("\n Правый граф: ")
    for i, elem in rightCaley.items():
        print(f"""({elem[0]}) --> """, end="( ")
        for j in i:
            print(j, end=" ")
        print(")")
        print()


# Функции для 3 задания
# Функция для подсчета биномиального коэффициэнта
def getBinCoef(n, k):
    if n < k: return 0
    result = 1.0
    for i in range(k):
        result *= (n - i)
        result /= (i + 1)
    return result

# Функция для подсчета суммы биномиальных коэффициэнтов
def getBinCoefSum(m, n):
    s = 0
    for i in range(1, m + 1):
        s += getBinCoef(n / m, 2)
    return s

# Функция для вычисления расстояния между полугруппами
# Вход: полугруппа S1, S2
# Выход: расстояние между полугруппами S1 и S2
def getDistant(S1, S2):
    gcd = math.gcd(S1, S2)
    if gcd == S2:
        return 1.0 / getBinCoef(S1, 2) * getBinCoefSum(S2, S1)
    elif gcd == S1:
        return 1.0 / getBinCoef(S2, 2) * getBinCoefSum(S1, S2)
    else:
        return (getDistant(S1, gcd) + getDistant(gcd, S2)) / 2

"""
MAIN PROGRAM
"""
print("Лабораторная работа №4. Вильцев Д.Д., 311")

# ввод конечного множества символов a
print("Введите элементы полугруппы:")
arrA = input().split()

# ввод конечного множества R определяющих соотношений
arrR = dict()
for i in arrA:
    arrR[i] = set()

print("Введите количество определяющих соотношений:")
amountR = int(input())

print("Введите определяющие соотношения")
for i in range(amountR):
    x, y = input().split()
    if x in arrR.keys():
        arrR[x].add(y)
    elif y in arrR.keys():
        arrR[y].add(x)
    elif len(x) < len(y):
        arrR[x] = {y}
    else:
        arrR[y] = {x}

# ввод полугрупп S1, S2
distFirst = int(input("Введите полугруппу S1 для вычисления расстояния: "))
distSecond = int(input("Введите полугруппу S2 для вычисления расстояния: "))


# получение результатов
resultPolugroup, resultCaleyTable, columnTitles = makePolugroupAndCaleyTable(arrR)

print("Задание 1.")
print("Полученная полугруппа: ", resultPolugroup)
print("Таблица Кэли: ")
print(tabulate(resultCaleyTable, headers=columnTitles))

print()
print("Задание 2. Графы Кэли")
rightCaleyGraph, leftCaleyGraph = getCaleyGraph(arrR)
printCaleyGraph(leftCaleyGraph, rightCaleyGraph)

print()
print("Задание 3. Расстояние между полугруппами")
print(f"Расстояние между Z_{distFirst} и Z_{distSecond} = " +
      f"{getDistant(distFirst, distSecond)}")




