# 📌Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○Для дочерних объектов указывайте родительскую директорию.
# ○Для каждого объекта укажите файл это или директория.
# ○Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
import os
from pprint import pprint

my_dict={}
def directory_overviewer(path: str):
    size = 0
    global my_dict
    # print('-----')
    # if os.path.exists(path) :
    if os.path.isdir(path):
        for i in os.listdir(path):
            # print(path+i)
            size += directory_overviewer(path+'\\'+i)
        my_dict[path] = size
        return size
    else:
        size = os.path.getsize(path)
        # print(path, size)
        my_dict[path] = size
        return size


print(directory_overviewer(os.getcwd()))
pprint(my_dict)
print(os.getcwd())