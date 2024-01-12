string = input("Введите строку с некоторым кол-вом символов - ")
string = list(set(string.split(" ")))
string2 = ""

for i in range(len(string)):
    string2 += string[i] + " "

print("Слова из вашей строки без повторений: ", string2)
