# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
from random import randint, choice, choices

ASCII = 'abcdefghijklmnopqrstuvwxyz'
PATH_TO_FILES = 'trash//'
EXTENTION_PATH = {'txt': 'document', 'doc': 'document', 'xls': 'document', 'mp3': 'music', 'vaw': 'music',
                  'jpg': 'pictures', 'png': 'pictures'}


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


def make_path(path):
    if not os.path.exists(path):
        os.mkdir(path)
    # os.chdir(path)
    # create_file(extention)


def move_files():
    for file in os.listdir():
        extention = file.split('.')[-1]
        if EXTENTION_PATH.get(extention):
            make_path(EXTENTION_PATH.get(extention))
            os.replace(file, f'{EXTENTION_PATH.get(extention)}\\{file}')


# create_file('mp3', min_bytes=6, max_bytes=8, count=24)
# create_files(mp3=1, txt=2, doc=1, xls=4, vaw=5, jpg=1, png=2)
# make_path('test')
move_files()
