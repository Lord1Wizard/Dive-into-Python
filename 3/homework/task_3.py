# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

things = {'спальный мешок': 2, 'еда': 1, 'вода': 2, 'одежда': 2, 'котелок': 1, 'палатка': 7, 'байдарка': 15,
          'шатер': 12, 'мангал': 2, 'спорт инвертарь': 6}


def choosing_things(max_weight, cur_weight=None, backpack=None, cur_things_old=None):
    if cur_weight is None:
        cur_things = things.copy()
        backpack = ''
        cur_weight = max_weight
    else:
        cur_things = cur_things_old.copy()
    while len(cur_things) > 0:
        key, value = cur_things.popitem()
        if key not in backpack.split(','):
            if cur_weight - value > 0:
                choosing_things(max_weight, cur_weight - value,f'{key}' if backpack == '' else f'{backpack},{key}', cur_things)
    print(f'{backpack = } вес рюкзака {max_weight-cur_weight}')


max_weight = int(input('Введите грузоподьемность: '))
choosing_things(max_weight)
