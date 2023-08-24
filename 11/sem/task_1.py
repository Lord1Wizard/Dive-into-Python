# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time
from getpass import getuser
class MyString(str):

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.name = getuser()
        instance.time_creat = time.time()
        return instance
    def __init__(self, str_val):
        self.str_val = str_val

a = MyString('Hello world')

print(a, a.name, a.time_creat)
print(a.split())