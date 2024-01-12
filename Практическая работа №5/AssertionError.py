try:
    a = 4
    b = 5
    assert a == b

except AssertionError:
    print("Выражение в функции assert ложно.")
finally:
    print("Программа завершена")
