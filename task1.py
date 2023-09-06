import random

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    return matrix

def fill_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = random.randint(1, 10)

def print_matrix(matrix):
    for row in matrix:
        print(row)

def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        print("Неможливо перемножити матриці. Кількість стовпців першої матриці повинна бути рівною кількості рядків другої матриці.")
        return None

    result_matrix = create_matrix(rows1, cols2)

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

rows1 = int(input("Введіть кількість рядків першої матриці: "))
cols1 = int(input("Введіть кількість стовпців першої матриці: "))
rows2 = int(input("Введіть кількість рядків другої матриці: "))
cols2 = int(input("Введіть кількість стовпців другої матриці: "))

matrix1 = create_matrix(rows1, cols1)
matrix2 = create_matrix(rows2, cols2)
fill_matrix(matrix1)
fill_matrix(matrix2)

print("Перша матриця:")
print_matrix(matrix1)
print("Друга матриця:")
print_matrix(matrix2)

result = multiply_matrices(matrix1, matrix2)
if result is not None:
    print("Результат множення матриць:")
    print_matrix(result)
