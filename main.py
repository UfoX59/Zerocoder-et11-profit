# 11. Доходность
# Напишите функцию, которая высчитывает размер прибыли по
# заданной себестоимости и цены, по которой продают товар.

def profit_calculation (c, p):
    prof = p - c
    return prof

def is_profit (c, p):
    prof = p -c
    if prof > 0 :
        return True
    else:
        return False

def extra_profit (c, p):
    prof = p - c
    if prof >= c * 2:
        return True
    else:
        return False


cost = 120
price = 100

profit = profit_calculation (cost, price)
print(f"Прибыль составляет {profit}")

if is_profit (cost, price):
    print ("Хорошая сделка, есть прибыль")
else:
    print("Не повезло, сделка убыточна")

if is_profit(cost, price):
    if extra_profit (cost, price):
        print ("Супер удачная сделка, маржа зашкаливает")
    else:
        print("Обычная сделка, нормальная маржа")