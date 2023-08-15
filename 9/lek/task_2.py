from random import choice, randint
import csv
import json


def generate_abc(count: int = 100):
    all_data = []
    for _ in range(count):
        all_data.append((choice([*range(-100, 0), *range(1, 100)]), randint(-100, 100), randint(-100, 100)))
    with open('my_file.csv', 'w', newline='', encoding='utf-8') as f_csv:
        csv_write = csv.writer(f_csv, dialect='excel', delimiter=';')
        csv_write.writerows(all_data)


generate_abc(10)
