# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json

FILENAME = 'res.txt'

def file_transform_to_json(filename):
    with open(filename, "r", encoding='utf-8') as file_r, \
        open(f'{filename}.json',"w", encoding='utf-8') as file_w:
        data = file_r.readlines()
        # print(data)
        dict_to_save = {}
        for line in data:
            key, value = line.strip().split(" ")
            if key.title() in dict_to_save.keys():
                dict_to_save[key.title()].append(value)
            else:
                dict_to_save[key.title()]= [value]
        json.dump(dict_to_save, file_w, ensure_ascii=False)




file_transform_to_json(FILENAME)