# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


# if example.tell() > example_size
#     example.seek(0)


# names_size = len(list(1 for _ in open('names.txt')))
# nums_size = len(list(1 for _ in open('example.txt')))
# count = max(nums_size, names_size)
# with open('res.txt', 'w') as res, \
#         open('names.txt', 'r') as names, \
#         open('example.txt', 'r') as example:
#     names_str = itertools.cycle(names.readlines())
#     example_str = itertools.cycle(example.readlines())
#
#     for i in range(count):
#         example_str1, example_str2 = next(example_str).split('|')
#         prod = float(example_str1) * float(example_str2)
#         if prod < 0:
#             res.write(f'{next(names_str).strip().lower()} {abs(prod)}\n')
#         else:
#             res.write(f'{next(names_str).strip().upper()} {round(prod)}\n')


def union_file(name_file, example_file, res_file):
    with open(res_file, 'w', encoding='utf-8') as res, \
            open(name_file, 'r', encoding='utf-8') as name, \
            open(example_file, 'r', encoding='utf-8') as example:
        name_flag = True
        example_flag = True
        while True:
            name_str = name.readline()[:-1]
            example_str = example.readline()
            if not name_str:
                if not example_flag:
                    break
                name_flag = False
                name.seek(0)
                name_str = name.readline()[:-1]
            if not example_str:
                if not name_flag:
                    break
                example_flag = False
                example.seek(0)
                example_str = example.readline()
            print(example_str, name_str)
            ex1, ex2 = example_str.split('|')
            mult = float(ex1) * float(ex2)
            if mult < 0:
                res.write(f'{name_str.lower()} {abs(mult)}\n')
            else:
                res.write(f'{name_str.upper()} {round(mult)}\n')


union_file('name.txt', 'example.txt', 'res.txt')
