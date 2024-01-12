import csv
from functools import reduce
from tabulate import tabulate


def main():
    """
    Функция позволяет пользователю выбрать действие:
    1 - Добавить информацию о товарах на склад (наименование, кол-во, стоимость): вызов функции dataWrite()
    2 - Заказать товар: вызов функции Input
    """
    print("Выберите операцию:\n 1- Добавить информацию о товарах на склад (наименование, кол-во, стоимость)\n 2 - Заказать товар")

    choice = 0

    try:
        choice = int(input())
    except:
        print("Введён неверный номер операции")
        main()

    if choice == 1:
        dataWrite()

    elif choice == 2:
        Input()

    else:
        print("Введено неверное значение операции!")
        main()


def dataWrite():
    """
    Функция позволяет записывать информацию о преступлениях в csv файл:
    1 - Название продукта
    2 - Кол-во этого продукта на складе
    3 - Цена за единицу товара
    """
    with open("products.csv", 'a') as file:
        product_name = str(input("Введите название товара: "))

        try:
            product_quantity = int(input("Введите кол-во товара на складе: "))
        except:
            print("Кол-во товара должно быть в формате int")
            dataWrite()

        if product_quantity < 0:
            print("Кол-во товара не может быть отрицательным")
            dataWrite()

        try:
            product_cost = int(input("Введите цену за единицу товара: "))
        except:
            print("Цена товара должна быть в формате float")
            dataWrite()

        if product_cost < 0:
            print("Цена товара не может быть отрицательной")
            dataWrite()

        file.write(f"\n{product_name},{product_quantity},{product_cost}")
        file.close()
        main()



def Input():
    """
    Функция позволяет считывать информацию из csv файла,
    выводить список товаров, который состоит из порядкового номера, названия, кол-ва на складе, цены за единицу товара
    """
    products = []

    with open("products.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        for row in csv_reader:
            products.append(row)

    csv_file.close()

    products = sorted(products, key=lambda x: x[0])
    headers = ["№", "Название продукта", "Кол-во на складе", "Цена за единицу"]
    print(tabulate(products, headers, tablefmt="grid", showindex=True), )
    Order(products)

    
def Order(products: []):
    """
    Функция высчитывает стоимость заказа пользователя и редактирует csv файл, уменьшая кол-во выбранного пользователем товара на кол-во, заказанное пользователем,
    выводит стоимость заказа
    :param products: список продуктов, прочитанный из csv файла функцией Input
    """
    product_choice = int(input("Введите номер товара для заказа: "))
    if product_choice < 0 or product_choice > len(products) - 1:
        print("Введено неверное значение номера товара!")
        main()

    quantity_choice = int(input("Введите кол-во товара для заказа: "))
    order_cost = int(products[product_choice][2]) * quantity_choice
    if quantity_choice > int(products[product_choice][1]):
        print("На складе нет такого кол-ва продуктов!")
        main()

    products[product_choice][1] = int(products[product_choice][1]) - quantity_choice

    for i in range(len(products)):
        products[i] = reduce(lambda x, y: str(x) + ',' + str(y), products[i])

    products = "\n" + reduce(lambda x, y: x + "\n" + y, products)

    with open("products.csv", 'w') as csv_file:
        csv_file.write(products)

    print("Стоимость вашего заказа: ", order_cost)
    main()


if __name__ == "__main__":
    main()
