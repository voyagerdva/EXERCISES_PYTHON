matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

result = sorted(matrix1, key=lambda matrix_row: sum(matrix_row))

print(result)