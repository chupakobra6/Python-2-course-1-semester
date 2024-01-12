try:
    num = [1, 2, 3]

    num = iter(num)

    for i in num:
        print(next(num))

except StopIteration:
    print("В итераторе больше нет элементов")
finally:
    print("Программа завершена")
