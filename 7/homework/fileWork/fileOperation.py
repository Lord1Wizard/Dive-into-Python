import os
from random import randint, choice, choices

ASCII = 'abcdefghijklmnopqrstuvwxyz'
PATH_TO_FILES = 'test'
EXTENTION_PATH = {'txt': 'document', 'doc': 'document', 'xls': 'document', 'mp3': 'music', 'vaw': 'music',
                  'jpg': 'pictures', 'png': 'pictures'}


def randbytes_py38(min_bytes, max_bytes):
    '''Функция для генерации случайной последовательности байт
    min_bytes - минимальное количество байт
    max_bytes - максимальное количество байт'''
    ONE_BYTE = 128
    count = randint(min_bytes, max_bytes)
    res = bytes('', encoding="utf_8")
    for i in range(count):
        bt = randint(0, ONE_BYTE)
        res += bytes(chr(bt), encoding="utf_8")
    return res


def create_file(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):
    """Функция создаёт файлы с указанным расширением .
    Функция принимает следующие параметры:
    ✔ расширение - extention
    ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6 - smallest
    ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30 - largest
    ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256 - min_bytes
    ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096 - max_bytes
    ✔ количество файлов, по умолчанию 42 - count"""
    names = set()
    while len(names) < count:
        names.add(f"{''.join(choices(ASCII, k=randint(smallest, largest)))}.{extention}")
    for name in names:
        with open(f"{name}", 'wb') as file:
            file.write(randbytes_py38(min_bytes, max_bytes))


def create_files(**extention_files):
    """Функция создает файлы
     пример вызова: mp3=2 создаст два файла с раширением mp3"""
    for key, value in extention_files.items():
        create_file(key, count=value)


def make_path(path, **extention):
    """Функция создает файлы по указанному пути
     пример вызова:('test', mp3=2) создаст два файла с раширением mp3 в дериктории test"""
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    create_files(**extention)
    os.chdir('..')

def move_files(path):
    """Функция перемещает файлы в зависимости от расширения по указанному пути"""
    if os.path.exists(path):
        os.chdir(path)
        for file in os.listdir():
            extention = file.split('.')[-1]
            if EXTENTION_PATH.get(extention):
                make_path(EXTENTION_PATH.get(extention))
                os.replace(file, f'{EXTENTION_PATH.get(extention)}\\{file}')
        os.chdir('..')


def rename_files(desired_file_name, length_sequence_number, source_extention, destination_extention, span):
    """Функция группового переименования файлов.
        desired_file_name : параметр желаемое конечное имя файлов.
        length_sequence_number : параметр количество цифр в порядковом номере.
        source_extention : параметр расширение исходного файла.
        destination_extention : параметр расширение конечного файла.
        span : диапазон сохраняемого оригинального имени.
        Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
    желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение."""
    count = 1
    os.chdir(PATH_TO_FILES)
    for cur_name in os.listdir():
        if cur_name.endswith(f'.{source_extention}'):
            new_name = f'{cur_name[span[0]:span[1]]}{desired_file_name}{"0" * (length_sequence_number - len(str(count)))}{count}.{destination_extention}'
            os.rename(cur_name, new_name)
            count += 1


if __name__ == '__main__':
    make_path('trash', mp3=2)
