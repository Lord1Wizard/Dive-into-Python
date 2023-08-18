# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
from random import randint

from task_3 import Person


class Worker(Person):

    def __init__(self, worker_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.worker_id = worker_id if len(worker_id) == 6 else '000000'
        self.level_id = int(self.worker_id) % 7

    def __str__(self):
        return f'Сотрудник: {self.full_name()} идентификационный номер: {self.worker_id} уровень доступа: {self.level_id}'


w1 = Worker('01010','Иван', 'Петров', 10, 'male')
print(w1)
