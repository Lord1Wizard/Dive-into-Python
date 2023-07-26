# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.



def tabl_gen():
    for k in range(2):
        for i in range(2, 11):
            str = ''
            for j in range(2+4*k, 6+4*k):
                str += f'{j} * {i} = {i*j}\t\t'
                if j%5==0 or j%9==0:
                    str+='\n'
            yield str

for str in tabl_gen():
    print(f'{str}',end=' ')

# # вариант 2
# print(*(f'{j} X {i} = {i * j}\t\t' if j%5 !=0 else f'{j} X {i} = {i * j}\n'  for i in range(2, 11) for j in range(2, 6)))
#
# # вариант 3
# print('\n\n'.join(('\n'.join(['\t\t\t'.join([f'{x} x {y: >2} = {x*y:>3}' for x in range(2 + 4*k, 6+4*k)]) for y in range(2,11)]) for k in range(2))))