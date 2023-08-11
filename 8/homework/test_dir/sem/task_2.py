# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json

while True:
    try:
        with open('my_file.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    print(data)
    try:
        name, pers_id, level = input('Введите данные(Имя id уровень) через пробел: ').split()
    except ValueError:
        break
    flag = True
    if not 0 < int(level) < 8:
        print('Уровень от 1 до 7.Давай сначала')
        continue
    for lev in data.values():
        for key in lev.keys():
            if key == pers_id:
                flag = False
    if flag:
        with open('my_file.json', 'w', encoding='utf-8') as f:
            if level not in data.keys():
                data[level] = {}
            data[level][pers_id] = name
            json.dump(data, f, indent=2, ensure_ascii=False)
    else:
        print('Такой id уже есть. Давай сначала')
