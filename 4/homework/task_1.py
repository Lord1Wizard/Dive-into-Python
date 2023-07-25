matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
matrix_t1 = [list(i) for i in zip(*matrix)]
print(*matrix)
print(*zip(*matrix))
print(matrix_t1)
matrix_t2 = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print(matrix_t2)
def tr_matrix(matrix):
    pass


tr_matrix(matrix)
