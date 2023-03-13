# reflex closure
def reflexClosure(matrix, n, m):
    reflexCheck = True
    for i in range(n):
        for j in range(m):
            if (i == j and matrix[i][j] != 1):
                reflexCheck = False
                break
    if reflexCheck:
        print("the matrix is already reflex!")
    else:
        # reflex closure
        for i in range(n):
            for j in range(m):
                if (i == j and matrix[i][j] != 1):
                    matrix[i][j] = 1
    # print new matrix
    print("reflex closure")
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()


# symmetry closure
def symmetryClosure(matrix, n):
    for i in range(n):
        for j in range(n):
            if (i != j and matrix[i][j] != matrix[j][i]):
                matrix[j][i] = matrix[i][j]
    print("symmetry closure")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

# transitive closure
def transitiveClosure(matrix, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[j][j] and matrix[i][k]:
                    matrix[j][k] = 1
    print("transitive closure")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end= " ")
        print()

n = int(input("Enter the size of matrix:"))
m = n

# Initialize matrix
matrix = []
print("Enter the matrix:")

# For user input
for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()

reflexClosure(matrix, n, m)
symmetryClosure(matrix, n)
transitiveClosure(matrix, n)