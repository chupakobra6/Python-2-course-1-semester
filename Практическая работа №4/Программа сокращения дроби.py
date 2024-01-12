def fractionReduction(numerator: float, denominator: float) -> str | int:
    """
    Возвращает числитель дроби, если знаменатель равен 1, возвращает сокращённую дробь в формате (n/n), в противном случае

    :param numerator: числитель дроби
    :param denominator: знаменатель дроби
    :return str | int:
    """
    a = numerator
    b = denominator

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    numerator /= a
    denominator /= a

    result_string = str(int(numerator)) + "/" + str(int(denominator))

    if denominator == 1:
        return int(numerator)
    else:
        return result_string


fractionInput = input("Введите дробь для сокращения (n/n) - ").split("/")
numerator = float(fractionInput[0])
denominator = float(fractionInput[1])

print(fractionReduction(numerator=numerator, denominator=denominator))
