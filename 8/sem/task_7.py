# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle

with open('my_file_picle.csv', 'r', newline='', encoding='utf-8') as f_csv:
    csv_read = csv.reader(f_csv, delimiter=';')
    my_dict = {}
    for i, line in enumerate(csv_read):
        if i == 0:
            pass
        else:
            if line[0] not in my_dict.keys():
                my_dict[line[0]] = {}
            my_dict[line[0]][line[1]] = line[2]
print(pickle.dumps(my_dict))
