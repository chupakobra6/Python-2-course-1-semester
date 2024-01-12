import csv
from tabulate import tabulate


def main():
    """
    Функция позволяет пользователю выбрать действие:
    1 - Добавить город и совершённые преступления: вызов функции dataWrite()
    2 - Просмотр статистики преступлений: вызов функции ReadnWrite(path)
    """
    print("Выберите операцию:\n 1 - Добавить город и совершённые преступления\n 2 - Просмотр статистики преступлений")

    choice = 0
    
    try:
        choice = int(input())
    except:
        print("Введён неверный номер операции")
        main()

    if choice == 1:
        dataWrite()

    elif choice == 2:
        ReadnWrite()

    else:
        print("Введено неверное значение операции")
        main()


def dataWrite():
    """
    Функция позволяет записывать информацию о преступлениях в csv файл:
    1 - Название города
    2 - Кол-во совершённых преступлений в городе за этот год
    3 - Кол-во совершённых преступлений в городе за прошлый год
    4 - Число раз, в которое увеличилось кол-во совершённых преступлений
    """
    with open("crimes.csv", 'a') as file:
        try:
            city_name = str(input("Введите название города: "))

            try:
                now_year_crimes = int(input("Введите кол-во совершённых преступлений в городе за этот год: "))
            except:
                print("Кол-во преступлений должно быть в формате int")
                dataWrite()

            if now_year_crimes < 0:
                print("Кол-во преступлений не может быть отрицательным")
                dataWrite()

            try:
                last_year_crimes = int(input("Введите кол-во совершённых преступлений в городе за прошлый год: "))
            except:
                print("Кол-во преступлений должно быть в формате int")
                dataWrite()

            if last_year_crimes < 0:
                print("Кол-во преступлений не может быть отрицательным")
                dataWrite()

            time = float(now_year_crimes) / float(last_year_crimes)

            file.write(f"\n{city_name},{last_year_crimes},{now_year_crimes},{time:.2f}")
            file.close()
            main()

        except:
            print("Ошибка ввода")


def ReadnWrite():
    """
    Функция позволяет считывать информацию из csv файла,
    заносить в список город, в котором кол-во преступлений увеличилось в максимальное число раз (и какое).
    Список состоит из порядкового номера город, названия города, статистики совершённых преступлений.
    """
    max_time = 0
    cities = []

    with open("crimes.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        for row in csv_reader:
            if max_time < float(row[3]):
                max_time = float(row[3])

        csv_file.close()

    with open("crimes.csv") as csv_file1:
        csv_reader = csv.reader(csv_file1, delimiter=',')
        next(csv_reader)

        for row in csv_reader:
            if float(row[3]) == max_time:
                cities.append(row)

        csv_file.close()
        dataInput(cities)


def dataInput(cities: []):
    """
    Функция выводит сортированный список с городами, в которых в максимальное число раз увеличилось кол-во преступлений с прошлого года
    """
    cities = sorted(cities, key=lambda x: x[0])
    headers = ["№", "Название города", "За прошлый год", "За этот год", "Увеличение в (раз)"]
    print(tabulate(cities, headers, tablefmt="grid", showindex=True), )
    main()


if __name__ == "__main__":
    main()
