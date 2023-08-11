# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import json
import csv

with open('my_file.json', 'r', encoding='utf-8') as f_json, \
        open('my_file.csv', 'w', newline='', encoding='utf-8') as f_csv:
    data = json.load(f_json)
    csv_write = csv.writer(f_csv, delimiter=';')
    line = ['level', 'id', 'name']
    csv_write.writerow(line)
    all_data = []
    for lev, values in data.items():
        for key, value in values.items():
            all_data.append([lev, key, value])
    csv_write.writerows(all_data)
print(data)
