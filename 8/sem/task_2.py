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
        name, pers_id, level = input('Введите данные: ').split()
    except ValueError:
        break
    if not 0 < int(level) < 8:
        print('Давай сначала')
        continue
    with open('my_file.json','r',encoding='utf-8') as f:
        try:
            data = json.load(f)
            print(data)
        except Exception:
            data = {}
    with open('my_file.json', 'w', encoding='utf-8') as f:

        if level not in data.keys():
            data[level]={}
            # dict_line = {pers_id: name}
        data[level][pers_id] = [name]
        # else:
            # dict_line = {pers_id: name}
            # data[level].append([dict_line])
            # data[level][pers_id].append(name)
        json.dump(data, f, ensure_ascii=False)

