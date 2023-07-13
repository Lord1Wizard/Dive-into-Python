input_str = input('Ведите текст')
if input_str.isdecimal():
    input_str = int(input_str)
    print('Число {0} в двоичной системе {1} в восьмеричной системе {2} в шестнадцатиричной системе {3}'.format(str(input_str), bin(input_str), oct(input_str), hex(input_str)))
elif input_str.isascii():
    print('Это ASCII')
else:
    print('Это не ASCII')
