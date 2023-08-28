# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц



class LenError(ValueError):
    def __str__(self):
        return f'Ошибка размеров марицы'

class TypeError(ValueError):
    def __init__(self, other, Matrix):
        self.other = other
        self.Matrix = Matrix
        print(other)

    def __str__(self):
        return f'Ошибка. Ожидается тип  {self.Matrix} а получен тип {type(self.other)} '


class Matrix:

    def __init__(self, matr):
        """Создание экземпляра матрицы если все строки матрицы одинаковой длинны, иначе ошибка"""
        flag = True
        lenght = len(matr[0])
        for i in range(len(matr)):
            if lenght != len(matr[i]):
                flag = False
        if flag:
            self.matr = matr
        else:
            raise LenError

    def get_name(self):
        print(self.__name__)
        for i, j in globals().items():
            if j is self:
                return i
    def __str__(self):
        """Перевод матрицы в str для печати"""
        rez = ''
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                rez +=f'{self.matr[i][j]}\t'
            rez += f'\n'
        return rez

    def __eq__(self, other):
        """Сравнение матриц. Если матрицы одинакового размера то они равны"""
        if isinstance(other, Matrix):
            return len(self.matr) == len(other.matr) and len(self.matr[0]) == len(other.matr[0])
        else:
            raise TypeError(other, Matrix)

    def __add__(self, other):
        """Сложение матриц"""
        if isinstance(other, Matrix):
            if self == other:
                rez = list()
                for i in range(len(self.matr)):
                    temp = list()
                    for j in range(len(self.matr[0])):
                        temp.append(self.matr[i][j] + other.matr[i][j])
                    rez.append(temp)
                return Matrix(rez)
            else:
                raise LenError
        else:
            print(other)
            raise TypeError(other, Matrix)

    def __mul__(self, other):
        """Умножение матриц"""
        if isinstance(other, Matrix):
            if len(self.matr[0]) == len(other.matr):
                rez = list()
                for i in range(len(self.matr)):
                    temp = list()
                    for j in range(len(other.matr[0])):
                        temp.append(0)
                        for k in range(len(other.matr)):
                            # resulted matrix
                            temp[j] += self.matr[i][k] * other.matr[k][j]
                    rez.append(temp)
                return Matrix(rez)
            else:
                raise LenError
        else:
            raise ValueError




my_matrix_1 = [[1, 2, 4, 71],
               [3, 4, 6, 1, 5]] #LenError: Ошибка размеров марицы

my_matrix_2 = [[1, 2, 4, 29, 3],
               [3, 4, 6, 1, 3]] #LenError: Ошибка размеров марицы

# my_matrix_1 = [[1, 2, 4, 71], # раскоментировать для работы без ошибок
#                [3, 4, 6, 1]]
#
# my_matrix_2 = [[1, 2, 4, 29],
#                [3, 4, 6, 1]] # раскоментировать для работы без ошибок

my_matrix_3 = [[1, 2, 4, 29],
               [3, 4, 6, 1],
               [3, 4, 6, 1],
               [3, 4, 6, 1]]



m1 = Matrix(my_matrix_1)
m2 = Matrix(my_matrix_2)
m3 = Matrix(my_matrix_3)
print(f'm1\n{m1}')
print(f'm2\n{m2}')
print(f'm3\n{m3}')

print(f'Сравнение матриц m1 и m2\n{m1 == m2}')
m4 = m1 + m2
print(f'Результат сложения матриц m1 и m2\n{m4}')
m5 = m1 * m3
print(f'Результат умножения матриц m1 и m3\n{m5}')
m5 = m1 + '1' #Ошибка. Ожидается тип  <class '__main__.Matrix'> а получен тип <class 'str'>