price = 0
amount = int(input("Введите количество человек в вашей группе - "))

for i in range(amount):

    age = int(input("Поочереди введите возраст всех людей в вашей группе - "))

    if age <= 2:
        price += 0
    elif (age >= 3) and (age <= 12):
        price += 14
    elif age >= 65:
        price += 18
    else:
        price += 23

print("Общая цена билета для всей группы = {:.2f}$".format(price))
