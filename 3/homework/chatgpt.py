def find_missing_items(friends):
    # Формирование словаря с вещами друзей
    items_dict = {}
    for friend, items in friends.items():
        items_dict[friend] = set(items)

    # Нахождение вещей, которые есть у всех, кроме одного друга
    common_items = set.intersection(*items_dict.values())
    common_items = {'спальный мешок', 'газовая горелка'}
    print(items_dict)
    print(friends)
    print(items_dict.values())
    # Поиск друга, у которого отсутствуют эти вещи
    missing_items_friend = None
    for friend, items in friends.items():
        for common_item in common_items:
            if not(common_item in set(items)):
                print('------------')
                print(common_item, set(items),friend)
                missing_items_friend = friend

    return common_items, missing_items_friend


# Пример входных данных
friends = {
    'Друг1': ('рюкзак', 'спальный мешок', 'палатка'),
    'Друг2': ('рюкзак', 'палатка', 'газовая горелка'),
    'Друг3': ('рюкзак', 'спальный мешок', 'газовая горелка')
}

common_items, missing_items_friend = find_missing_items(friends)

print("Вещи, которые есть у всех друзей, кроме одного:")
print(common_items)
print("Имя друга, у которого отсутствуют эти вещи:")
print(missing_items_friend)