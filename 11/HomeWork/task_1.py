class Matrix:
    def __init__(self, my_matrix):
        """Класс матрица для сложения, сравнения и вывода на печать!  """
        self.my_matrix = my_matrix

    def __str__(self):
        result = f'{"-" * 25}\n'
        size = f'{"-" * 25}\n Матрица размером: {len(self.my_matrix)} * {len(self.my_matrix[1])}'
        for i in self.my_matrix:
            result += '    ' + ',  '.join(map(str, i))
            result += '\n'
        return f'{size} \n{result}{"-" * 25}'

    def __add__(self, other):
        result = list([] for _ in range(len(self.my_matrix)))

        for i in range(len(self.my_matrix)):
            for j in range(len(self.my_matrix[1])):
                temp = self.my_matrix[i][j] + other.my_matrix[i][j]
                result[i].append(temp)
        return Matrix(result)

    def __sum_matrix(self, other):
        """Метод возвращает картеж чисел, состоящий из сумм 2-х матриц
        (нужен для реализации методов класса, что бы не нарушать принцип DRY)"""
        sum_1_matrix = 0
        sum_2_matrix = 0
        for i in range(len(self.my_matrix)):
            for j in range(len(self.my_matrix[1])):
                sum_1_matrix += self.my_matrix[i][j]
                sum_2_matrix += other.my_matrix[i][j]
        result = (sum_1_matrix, sum_2_matrix)
        return result

    def __eq__(self, other):
        sum_1_matrix, sum_2_matrix = self.__sum_matrix(other)
        return sum_1_matrix == sum_2_matrix

    def __lt__(self, other):
        sum_1_matrix, sum_2_matrix = self.__sum_matrix(other)
        return sum_1_matrix < sum_2_matrix

    def __le__(self, other):
        _bool = self.__eq__(other) or self.__lt__(other)
        return _bool


my_matrix_1 = [[1, 2, 4, 71],
               [3, 4, 6, 1]]


my_matrix_2 = [[1, 2, 4, 29],
               [3, 4, 6, 1]]

print('Сложение матриц:')
my_matrix_1 = Matrix(my_matrix_1)
my_matrix_2 = Matrix(my_matrix_2)
my_matrix_3 = my_matrix_1 + my_matrix_2
print(my_matrix_3)


print('Проверка на равенство: ')
my_matrix_3 = [[1, 2, 4, 29],
               [3, 4, 6, 1]]
my_matrix_3 = Matrix(my_matrix_3)
print('первая матрица больше остальных !')
print(my_matrix_3 == my_matrix_2)
print(my_matrix_1 == my_matrix_2)

print('Проверка больше меньше: ')
print(my_matrix_3 > my_matrix_2)
print(my_matrix_1 > my_matrix_2)

print('Проверка больше или равно, меньше или равно: ')
print(my_matrix_3 >= my_matrix_2)
print(my_matrix_1 >= my_matrix_2)