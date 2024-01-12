def checkingForSimplicity(a: int) -> bool:
    """
    Возвращает True, если число является и простым, и False, если число сложное

    :param a: проверяемое число
    :return bool:
    """
    divisors = []

    for i in range(1, a + 1):
        if a % i == 0:
            divisors.append(i)

    if len(divisors) == 2:
        return True
    else:
        return False


if __name__ == "__main__":
    number = int(input("Введите число - "))

    if number <= 1:
        print("Ошибка! Введённое число должно быть больше или равно 1")
        exit()

    if checkingForSimplicity(a=number):
        print("Ваше число является простым")

    elif not checkingForSimplicity(a=number):
        print("Ваше число не является простым")
