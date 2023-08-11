# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import csv
import json

with open('my_file_csv.json', 'w', encoding='utf-8') as f_json, \
        open('my_file.csv', 'r', newline='', encoding='utf-8') as f_csv:
    csv_read = csv.reader(f_csv, delimiter=';')
    my_dict = {}
    for i, line in enumerate(csv_read):
        if i == 0:
            pass
        else:
            line[1] = f'{line[1]:0>10}'
            line[2] = line[2].title()
            hash_id = hash(line[2] + line[1])
            my_dict[hash_id] = {line[0]: [line[1], line[2]]}
    json.dump(my_dict, f_json, indent=2)
