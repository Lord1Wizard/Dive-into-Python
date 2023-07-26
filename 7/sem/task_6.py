# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import os
from random import randint, choice, choices

ASCII = 'abcdefghijklmnopqrstuvwxyz'
PATH_TO_FILES = 'trash//'


def randbytes_py38(min_bytes, max_bytes):
    ONE_BYTE = 128
    count = randint(min_bytes, max_bytes)
    res = bytes('', encoding="utf_8")
    for i in range(count):
        bt = randint(0, ONE_BYTE)
        res += bytes(chr(bt), encoding="utf_8")
    return res


def create_file(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):
    names = set()
    while len(names) < count:
        names.add(f"{''.join(choices(ASCII, k=randint(smallest, largest)))}.{extention}")
    for name in names:
        with open(f"{name}", 'wb') as file:
            file.write(randbytes_py38(min_bytes, max_bytes))

def create_files(**extention_files):
    for key, value in extention_files.items():
        create_file(key, count=value)

def make_path(path, extention):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    create_file(extention)

# create_file('mp3', min_bytes=6, max_bytes=8, count=24)
# create_files(mp3=1,txt=2,doc=1,xls=4)
make_path('test','txt')