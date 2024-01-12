try:
    num = [1, 2]

    for i in range(3):
        print(num[i])

except IndexError:
    print("Индекс не входит в диапазон элементов.")
finally:
    print("Программа завершена")
