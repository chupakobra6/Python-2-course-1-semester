try:
    a = 4 / 0

except ZeroDivisionError:
    print("Ошибка деления на ноль")
finally:
    print("Программа завершена")
