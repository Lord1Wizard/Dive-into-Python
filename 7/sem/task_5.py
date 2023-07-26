# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

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
        names.add(f"{PATH_TO_FILES}{''.join(choices(ASCII, k=randint(smallest, largest)))}.{extention}")
    for name in names:
        with open(f"{name}", 'wb') as file:
            file.write(randbytes_py38(min_bytes, max_bytes))

def create_files(**extention_files):
    # extention_files = {}
    # while sum(extention_files.values()) < count:
    #     key = ''.join(choices(args))
    #     extention_files[key] = extention_files.setdefault(key,0) + 1
    # print(extention_files)
    for key, value in extention_files.items():
        create_file(key, count=value)


# create_file('mp3', min_bytes=6, max_bytes=8, count=24)
create_files(mp3=1,txt=2,doc=1,xls=4)