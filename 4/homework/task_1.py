matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
matrix_T = [list(i) for i in zip(*matrix)]
print(matrix_T)

def tr_matrix(matrix):
    for item in matrix:
        led = list(item)
        print(led)
    print(*matrix)
    print(led)


tr_matrix(matrix)