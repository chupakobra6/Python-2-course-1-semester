def reverseLookup(somedict, keyvalue):
    keys = []
    for key in somedict:
        if somedict[key] == keyvalue:
            keys.append(key)
    return keys


somedict = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

keyvalue = input("Введите необходимое значение - ")

print(reverseLookup(somedict, keyvalue))
