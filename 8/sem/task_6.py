# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import csv
import pickle

with open('my_file_csv.pickle', 'rb') as f:
    new_dict = pickle.load(f)
print(new_dict)
with open('my_file_picle.csv', 'w', newline='', encoding='utf-8') as f_csv:
    csv_write = csv.writer(f_csv, delimiter=';')
    line = ['level', 'id', 'name']
    csv_write.writerow(line)
    all_data = []
    for values in new_dict.values():
        for lev, value in values.items():
            all_data.append([lev, value[0], value[1]])
    csv_write.writerows(all_data)
