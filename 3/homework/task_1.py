# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
i = 0
while i < len(my_list):
    if my_list[i] in unique_list:
        i += 1
    else:
        unique_list.append(my_list.pop(i))


print(f'Дубли {my_list}')  # [1, 2, 3, 4, 5]
print(f'Список без дублей {unique_list}')  # [1, 2, 3, 4, 5]


