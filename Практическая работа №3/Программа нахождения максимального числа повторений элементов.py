from random import randint


def tuplesgen(n):
    a = []
    for i in range(n):
        a.append(randint(1, n))
    return tuple(a)


tuples = []
max = 0
n = int(input("Введите количество кортежей в массиве - "))

for i in range(n):
    tuples.append(tuplesgen(n))

for i in range(n):
    sort = tuples[i]
    for j in range(n):
        amount = 0
        for k in range(n):
            if sort[j] == sort[k]:
                amount += 1
        if amount > max:
            max = amount

print(f"Список: {tuples}\nМаксимальное число повторений элементов в кортежах массива: {max}")

