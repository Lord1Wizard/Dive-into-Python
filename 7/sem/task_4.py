# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

from random import randint, choices


ASCII = 'abcdefghijklmnopqrstuvwxyz'
PATH_TO_FILES = 'trash//'
def randbytes_py38(min_bytes, max_bytes):
    ONE_BYTE = 128
    count = randint(min_bytes,max_bytes)
    res = bytes('', encoding="utf_8")
    for i in range(count):
        bt = randint(0,ONE_BYTE)
        res += bytes(chr(bt), encoding="utf_8")
    return res

def create_file(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):
    names = set()
    while len(names) < count:
        names.add(f"{PATH_TO_FILES}{''.join(choices(ASCII,k=randint(smallest, largest)))}.{extention}")
    for name in names:
        with open(f"{name}", 'wb') as file:
            file.write(randbytes_py38(min_bytes, max_bytes))

create_file('mp3', min_bytes=6, max_bytes=8, count=2)