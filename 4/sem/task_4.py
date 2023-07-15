# ✔Функция получает на вход список чисел.
# ✔Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
from random import randint

str_size = 10
def buble_sort(sorted_list):
    for i in range(str_size):
        for j in range(str_size-i -1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]


print(my_list := [randint(0,100) for i in range(str_size)])
buble_sort(my_list)
print(my_list)