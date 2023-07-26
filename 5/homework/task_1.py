# ✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

# первый способ
def patch_name_extension(patch_str:str):
    """Функция  на вход принимает строку на выходе ext - расширение
    patch_str - путь file - имя файла """
    ext = patch_str.split('.')[-1]
    patch_str = patch_str.split('.')[0]
    file = patch_str.split('\\')[-1]
    patch_str = patch_str.replace(file,'')
    return (patch_str, file, ext)

# второй способ
def patch_name_extension1(patch_str:str):
    """ Функция  на вход принимает строку на выходе кортеж путь, имя, расширение"""
    return '\\'.join(patch_str.split('\\')[0:-1]),*patch_str.split('\\')[-1].split('.')

my_list=(patch_name_extension1('C:\\Users\\Wizard\\AppData\\Local\\Programs\\Python\\Python38\\lib\\ntpath.py'))
print(my_list)
print(type(my_list))
print(patch_name_extension('C:\\Users\\Wizard\\AppData\\Local\\Programs\\Python\\Python38\\lib\\ntpath.py'))