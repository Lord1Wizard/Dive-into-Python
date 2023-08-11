from pprint import pprint

dlina_zagotovki = 6000
list_otrezkov = [1000, 2000, 3000]
# list_otrezkov = [1000, 1000, 3000, 4000, 2000, 7000, 3650, 800, 1000]
list_variantov = []


# class otrezok():
#     dlina : int
#     count : int
def poisk(my_list=list_otrezkov,my_list_clear=[]):
    print('----------')
    print(len(my_list))
    print(f'--{my_list = }')
    print(f'--{my_list_clear = }')
    global list_variantov
    if len(my_list) > 1:
        for j in range(len(my_list)-1):
            my_list_temp = my_list.copy()
            # print(j, len(my_list))
            # my_list_clear = []
            print(f'--{my_list = } --{j =} ++{len(my_list)-1 = } {my_list_clear = }')
            my_list_clear.append(my_list_temp.pop(j))
            print(f'--{my_list_temp = } --{my_list_clear = }')
            my_list_clear = poisk(my_list_temp, my_list_clear)
            # print(f'++{my_list = }')
            # print(f'++{my_list_clear = }')
            # print(j, len(my_list))
    else:
        list_variantov.append(my_list_clear)
        my_list_clear = []
        print(f'00000000000000000000000000000{my_list_clear = }')
        return my_list_clear

poisk()
print(list_variantov)
# my_list_clear = []
# my_list_clear.append(list_otrezkov[1])
# my_list_clear.extend([list_otrezkov[0]])
# print(my_list_clear)