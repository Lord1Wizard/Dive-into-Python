# 📌Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○Для дочерних объектов указывайте родительскую директорию.
# ○Для каждого объекта укажите файл это или директория.
# ○Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import csv
import json
import os
import pickle
from pprint import pprint

my_dict={}
def directory_overviewer(path: str):
    """Функция рекурсивно обходит все директории и файлы и заполняет словарь значениями"""
    size = 0
    global my_dict
    # print('-----')
    # if os.path.exists(path) :
    if os.path.isdir(path):
        for i in os.listdir(path):
            # print(path+i)
            size += directory_overviewer(path+'\\'+i)
        my_dict[path] = [path.split('\\')[-1],'isDir',size,path.split('\\')[-2]]
        return size
    else:
        size = os.path.getsize(path)
        # print(path, size)
        my_dict[path] = [path.split('\\')[-1],'isFile',size,path.split('\\')[-2]]
        return size

def save_csv(dict:{}):
    """апись словаря в csv"""
    with open('my_file.csv', 'w', newline='', encoding='utf-8') as f_csv:
        csv_write = csv.writer(f_csv, delimiter=';')
        line = ['path', 'name', 'type', 'size', 'parent']
        csv_write.writerow(line)
        all_data = []
        for key, values in dict.items():
            all_data.append([key, *values])
        csv_write.writerows(all_data)

def save_picle(dict:{}):
    """апись словаря в picle"""
    with open('my_file.pickle', 'wb') as f_pickle:
        pickle.dump(dict, f_pickle)

def save_json(dict:{}):
    """апись словаря в json"""
    with open('my_file.json', 'w', encoding='utf-8') as f_json:
        json.dump(dict, f_json, indent=2)

# directory_overviewer(os.getcwd())
directory_overviewer('c:\\temp')
save_csv(my_dict)
save_picle(my_dict)
save_json(my_dict)