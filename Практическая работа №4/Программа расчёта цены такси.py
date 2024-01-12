def taxiPrice(distance:float) -> float:
    """
    Возвращает значение float - стоимость поездки из расчёта $4,00 + $0,25 за каждые 140 м поездки
    :param distance: дистанция / километраж поездки (км)
    :return float:
    """
    price = 4 + ((distance * 1000 // 140) * 0.25)
    return price


distance = float(input("Введите километраж поездки ($4,00 плюс $0,25 за каждые 140 м поездки) - "))

if distance < 0:
    print("Введено неверное значение")
    exit()

print(f"Цена вашей поездки: {taxiPrice(distance=distance):.2f}$")