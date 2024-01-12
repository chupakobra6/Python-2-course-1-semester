try:
    a = "adfas123123"
    a = int(a)

except ValueError:
    print("Функция получает аргумент правильного типа, но некорректного значения.")
finally:
    print("Программа завершена")
