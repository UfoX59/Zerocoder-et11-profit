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


cost = 77
price = 100

profit = profit_calculation(cost, price)
print(f"Прибыль составляет {profit}")

if is_profit(cost, price):
    print ("Удачная сделка, есть прибыль")
else:
    print("Не повезло, сделка убыточна")
