string1 = input("Введите строку - ")
string2 = ""

for i in range(len(string1)):

    if i % 2 == 0:
        char = string1[i].upper()
    else:
        char = string1[i].lower()

    string2 += char

print("Изменённая строка: ", string2)
