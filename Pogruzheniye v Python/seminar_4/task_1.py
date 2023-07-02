# Напишите функцию Python для транспонирования матрицы

def transpose_matrix(matrix):
    transposed_matrix = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for j in range(len(matrix)):
            transposed_row.append(matrix[j][i])
        transposed_matrix.append(transposed_row)
    return transposed_matrix


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)
