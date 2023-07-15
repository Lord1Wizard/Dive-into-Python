# ✔Создайте вручную список с повторяющимися целыми числами.
# ✔Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔Нумерация начинается с единицы.

my_list = [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9]
new_list=[]

for i in range(len(my_list)):
    if my_list[i] % 2 != 0:
        new_list.append(i+1)

print(*my_list)
print(*new_list)


# 2 вариант

print(my_list:= [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9])

print(*[i+1 for i in range(len(my_list)) if my_list[i] % 2])