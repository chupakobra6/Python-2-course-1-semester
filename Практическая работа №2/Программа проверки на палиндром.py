string2 = ""

while True:
    string = input("Введите строку для проверки её на палиндром - ")

    for i in range(len(string) - 1, -1, -1):
        string2 += string[i]

    if string == string2:
        print("Поздравляем! Ваша строка - палиндром.")
    else:
        print("Ваша строка не палиндром.")

    string2 = ""
