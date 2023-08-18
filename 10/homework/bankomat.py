# Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# Дополнительно сохраняйте все операции поступления и снятия средств в список

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
class Bank:
    __PRIZE = 0.03
    __FREE_LIMIT = 5_000_000
    __MIN_COMMISSION = 30
    __MAX_COMMISSION = 600
    __COMMISSION = 1.5
    __DIVISION_CHECK = 50
    def __init__(self, total=0.0, count=0):
        self.__total = total
        self.__count = count
        self.__log = [self.__total]

    def wealth_tax(self):

        if self.__total > self.__FREE_LIMIT:
            self.__total *= 0.01

    def check_sum(self, deposit):
        if abs(deposit) % self.__DIVISION_CHECK != 0:
            print('Сумма должна быть кратна 50 операция отменена')
            return False
        if deposit < 0:
            if deposit * self.__COMMISSION / 100 < -self.__MAX_COMMISSION:
                deposit -= self.__MAX_COMMISSION
            elif deposit * self.__COMMISSION / 100 > -self.__MIN_COMMISSION:
                deposit -= self.__MIN_COMMISSION
            else:
                deposit += deposit * self.__COMMISSION / 100
            if self.__total < abs(deposit):
                print('Вы пытаетесь снять больше чем у вас есть! операция отменена')
                return False
        return deposit

    def work(self):
        while True:
            print('\nУ вас на счету :', self.__total)
            action = int(input(' 1. Пополнить\n 2. Снять\n 3. Выйти\n 4. История операций \nВыберете действие: '))
            self.__count += 1
            if action == 3:
                break
            elif action == 2:
                deposit_amount = -float(input('Введите сумму: '))
            elif action == 1:
                deposit_amount = float(input('Введите сумму: '))
            else:
                print(self.__log)
                continue
            deposit_amount = self.check_sum(deposit_amount)
            if not deposit_amount:
                continue
            if self.__count > 2:
                deposit_amount += abs(deposit_amount) * self.__PRIZE
                self.__count = 0
            self.__total += deposit_amount
            self.wealth_tax()
            if self.__log[-1] != self.__total:
                self.__log.append(self.__total)


if __name__ == "__main__":
    bank1 = Bank()
    bank1.work()
