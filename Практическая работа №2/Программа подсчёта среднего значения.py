i, summa, number = 0, 0, 1
print("Вводите числа для нахождения их среднего значения (0 - окончание ввода) - ")

while number != 0:
    i += 1
    number = int(input())
    summa += number

    if (i == 1) and (number == 0):
        print("Ошибка! Первым число не может быть ноль.")
        exit()

i -= 1
middle = summa / i
print("Среднее значение = ", middle)
