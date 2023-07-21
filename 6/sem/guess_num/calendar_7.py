# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


def test():
    pass

def check_date(year: str):
    res = year.split('.')
    if 0>int(res[1]) or int(res[1])>12:
        return False
    if 0>int(res[2]) or int(res[2])>9999:
        return False

    day_chek = {i+j:30+(i+j)%2  for i in range(1,7) for j in range(0,7)}
    if int(res[2]) < 1582 or (int(res[2]) % 4 != 0 or int(res[2]) % 100 == 0 and int(res[2]) % 400 != 0):
        day_chek[2]=28
    else:
        day_chek[2]=29
    if 0>int(res[0]) or int(res[0])>day_chek[int(res[1])]:
        return False
    return True


if __name__ == '__main__':
    print(check_date('29.02.2020'))