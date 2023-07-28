# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
import sys

from chek import *

if __name__ == '__main__':
    print(calendar.check_date(sys.argv[-1]))