print('Исходная цена | Сумма скидки | Новая цена')

for price in [4.95, 9.95, 14.95, 19.95, 24.95]:
    for discount in range(1):
        discount = price / 100 * 60
        for price2 in range(1):
            price2 = price - discount
            print("{0:.2f}\t\t\t {1:.2f}\t\t\t {2:.2f}".format(price, discount, price2))
