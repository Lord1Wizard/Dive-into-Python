# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import os
import pickle

for cur_name in os.listdir():
    if cur_name.endswith(f'.json'):
        with open(cur_name, 'r', encoding='utf-8') as f_json:
            data = json.load(f_json)
        with open(f'{cur_name.split(".")[0]}.pickle', 'wb') as f_pickle:
            pickle.dump(data, f_pickle)
