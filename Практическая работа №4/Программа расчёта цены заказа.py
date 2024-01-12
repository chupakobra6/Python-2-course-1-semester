def orderPrice(amount:float) -> float:
    """
    Возвращает значение float - стоимость заказа из расчёта $10,95 за первый товар в заказе и $2,95 – за все последующие

    :param amount: количество товаров в заказе
    :return float:
    """
    price = 10.95 + ((amount - 1) * 2.95)
    return price


ordersAmount = float(input("Введите количество позиций в заказе ($10,95 за первый товар в заказе и $2,95 – за все последующие) - "))

if ordersAmount < 1:
    print("Введено неверное значение")
    exit()

print(f"Цена вашего заказа: {orderPrice(amount = ordersAmount):.2f}$")