# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
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
def wealth_tax(tax):

    if tax > 5000000:
        return tax * 0.01
    else:
        return 0


def check_sum(deposit):
    if abs(deposit) % 50 != 0:
        print('Сумма должна быть кратна 50 операция отменена')
        return False
    if deposit < 0:
        if deposit * 0.015 < -600:
            deposit -= 600
        elif deposit * 0.015 > -30:
            deposit -= 30
        else:
            deposit += deposit * 0.015
        if total < abs(deposit):
            print('Вы пытаетесь снять больше чем у вас есть! операция отменена')
            return False
    return deposit


PRIZE = 0.03
total = 0.0
count = 0
log = [total]
while True:
    print('\nУ вас на счету :', total)
    action = int(input(' 1. Пополнить\n 2. Снять\n 3. Выйти\n 4. История операций \nВыберете действие: '))
    count += 1
    if action == 3:
        break
    elif action == 2:
        deposit_amount = -float(input('Введите сумму: '))
    elif action == 1:
        deposit_amount = float(input('Введите сумму: '))
    else:
        print(log)
        continue
    deposit_amount = check_sum(deposit_amount)
    if not deposit_amount:
        continue
    if count > 2:
        deposit_amount += abs(deposit_amount) * PRIZE
        count = 0
    total += deposit_amount
    total -= wealth_tax(total)
    if log[-1] != total:
        log.append(total)
