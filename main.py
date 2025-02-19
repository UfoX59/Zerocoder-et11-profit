# 11. Доходность
# Напишите функцию, которая высчитывает размер прибыли по
# заданной себестоимости и цены, по которой продают товар.

def profit_calculation (c, p):
    prof = p - c
    return prof

cost = 77
price = 100

profit = profit_calculation(cost, price)
print(f"Прибыль составляет {profit}")

