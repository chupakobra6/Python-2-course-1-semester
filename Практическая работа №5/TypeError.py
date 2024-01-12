try:
    a = 5
    b = "abc"
    c = a + b

except TypeError:
    print("Операция применена к объекту несоответствующего типа.")
finally:
    print("Программа завершена")
