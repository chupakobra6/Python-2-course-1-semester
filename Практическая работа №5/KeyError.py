try:
    num = {"key1": 1, "key2": 2}

    print(num["key3"])

except KeyError:
    print("Несуществующий ключ")
finally:
    print("Программа завершена")
