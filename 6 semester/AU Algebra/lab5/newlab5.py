def build_right_ideal(cayley_table, element):
    n = len(cayley_table)
    right_ideal = set([element])  # Инициализируем правый идеал текущим элементом
    new_elements_added = True

    while new_elements_added:
        new_elements_added = False
        for i in range(n):
            if all(cayley_table[j][i] in right_ideal for j in range(n)):
                # Если все результаты умножения элементов правого идеала на элемент i справа принадлежат правому идеалу,
                # добавляем элемент i к правому идеалу
                right_ideal.add(i)
                new_elements_added = True

    return right_ideal

def build_right_ideals(cayley_table):
    n = len(cayley_table)
    right_ideals = []

    for i in range(n):
        right_ideal = build_right_ideal(cayley_table, i)

        # Проверяем, есть ли эквивалентный правый идеал уже в списке правых идеалов
        is_duplicate = False
        for existing_ideal in right_ideals:
            if right_ideal == existing_ideal:
                is_duplicate = True
                break

        # Добавляем правый идеал в список правых идеалов, если он не является дубликатом
        if not is_duplicate:
            right_ideals.append(right_ideal)

    return right_ideals




cayley_table = [
    [0, 0, 0],
    [1, 2, 0],
    [2, 2, 1]
]

right_ideals = build_right_ideals(cayley_table)
print("Right ideals:")
for right_ideal in right_ideals:
    print(right_ideal)
