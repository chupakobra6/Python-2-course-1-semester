print("Вводите цифры для сортировки (\" \" - окончание ввода) - ")
n = 1
plusnum, minusnum, nullnum = [], [], []

while n != "":
    n = input()

    if n != "":
        a = int(n)

        if a < 0:
            minusnum.append(a)
        elif a == 0:
            nullnum.append(a)
        else:
            plusnum.append(a)

numbers = minusnum + nullnum + plusnum

for i in range(len(numbers)):
    print(numbers[i])
