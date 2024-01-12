import codecs
import csv
from tabulate import tabulate


def main():
    """
    Функция позволяет пользователю выбрать действие:
    1 - Авторизоваться
    2 - Зарегистрироваться
    """
    print("Выберите операцию:\n 1 - Авторизоваться.\n 2 - Зарегистрироваться.")

    try:
        choice = int(input())
    except ValueError:
        print("Введено неверное значение!")
        main()

    if choice == 1 or choice == 2:
        login = input("Введите логин: ")
        if len(login) < 3:
            print("Длина логина должна быть больше 2 символов!")
            main()
        password = input("Введите пароль: ")
        if len(password) < 8:
            print("Длина пароля должна быть больше 7 символов!")
            main()
        file_reading(choice=choice, login=login, password=password)

    else:
        print("Введено неверное значение операции!")
        main()


def file_reading(choice: int, login: str, password: str):
    """
    Функция считывает файл с данными зарегистрированных пользователей (логин, пароль, роль) и в зависимости от выбора в
    главном меню (функции main) перенаправляет в функцию аутентификации или проверки на занятость логина
    :param choice: выбор в функции main
    :param login: введённый пользователем логин
    :param password: введённый пользователем пароль
    """
    with open("users.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        users = []
        for row in csv_reader:
            users.append(row)

    csv_file.close()

    if choice == 1:
        authentication(users=users, login=login, password=password)
    elif choice == 2:
        checking_for_existing(users=users, login=login, password=password)


def authentication(users: [], login: str, password: str):
    """
    Функция проверяет введённые пользователем логин и пароль со значениями в базе данных и при совпадении вызывает
    функцию Admin или Common (в зависимости от роли в базе данных) класса User, в обратном случае - выводит ошибку
    :param users: база данных зарегистрированных пользователей (логин, пароль, роль)
    :param login: введённый пользователем логин
    :param password: введённый пользователем пароль
    """
    if any(login == user[0] and password == user[1] for user in users):
        for user in users:
            if login == user[0] and password == user[1]:
                role = user[2]

                if role == "admin":
                    print(f"Добро пожаловать, администратор {login}!")
                    Admin(login=login, password=password)

                elif role == "common":
                    print(f"Добро пожаловать, пользователь {login}!")
                    Common(login=login, password=password, registration=False)  # Флаг регистрации
    else:
        print("Введён неправильный логин или пароль!")
        main()


def checking_for_existing(users: [], login: str, password: str):
    """
    Функция проверяет базу данных на наличие введённого пользователем логина для регистрации и соответствие двух
    введённых паролей и, в зависимости от результата, вызывает функцию Common класса User или выводит ошибку
    :param users: база данных зарегистрированных пользователей (логин, пароль, роль)
    :param login: введённый пользователем логин
    :param password: введённый пользователем пароль
    """
    if not any(login == user[0] for user in users):
        password_check = input("Введите пароль повторно: ")

        if password_check == password:
            Common(login=login, password=password, registration=True)  # Флаг регистрации
        else:
            print("Введённые пароли не совпадают!")
            main()

    else:
        print("Пользователь с таким именем уже зарегистрирован.")
        authentication(users=users, login=login, password=password)


class User:
    def __init__(self, login: str, password: str):
        """
        Конструктор класса User, атрибуты класса - логин и пароль для регистрации пользователя и дальнейшем сохранении
        для аутентификации
        :param login: введённый пользователем логин
        :param password: введённый пользователем пароль
        """
        self.__login = login
        self.__password = password

    def registration(self):
        """
        Функция регистрации пользователя - сохраняет логин, пароль и роль нового пользователя в базе данных, вызывается
        только из конструкторов подклассов Admin и Common класса User
        """
        new_user = [self.login, self.password, self.role]

        with open("users.csv", 'a', newline='') as csv_file:
            csv_write = csv.writer(csv_file)
            csv_write.writerow(new_user)

        csv_file.close()
        print("Вы успешно зарегистрировались!")

    @staticmethod
    def visualization():
        """
        Функция прочитывает базу данных товаров и выводит её в форме сортированной по названию таблицы с помощью
        библиотеки tabulate (заголовки, индексы, центрирование)
        """
        products = []

        with codecs.open("products.csv", 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                products.append(row)

        csv_file.close()

        products = sorted(products, key=lambda x: x[0])
        headers = ["Название", "Описание", "Поставщик", "Цена (₽)", "Доступно"]
        print(tabulate(products, headers=headers, tablefmt="grid", showindex=True, stralign='center'))

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


class Common(User):
    def __init__(self, login: str, password: str, registration: bool):
        """
        Конструктор подкласса Common класса User - представляет собой функционал обычного пользователя: регистрация,
        показ таблицы товаров
        :param login: введённый пользователем логин
        :param password: введённый пользователем пароль
        :param registration: флаг регистрации зависит от выбора в главном меню (функции main)
        """
        super().__init__(login, password)
        self.__role = "common"
        if registration:
            self.registration()
        print("Личный кабинет пользователя.")
        self.visualization()

    @property
    def role(self):
        return self.__role


class Admin(User):
    def __init__(self, login: str, password: str):
        """
        Конструктор подкласса Admin класса User - представляет собой функционал супер-пользователя: регистрация,
        показ и редактирование значений таблицы товаров, добавление, и удаление товаров
        :param login: введённый пользователем логин
        :param password: введённый пользователем пароль
        """
        super().__init__(login, password)
        self.__role = "admin"
        print("Личный кабинет администратора.")
        self.visualization()
        self.change_lobby()

    def change_lobby(self):
        """
        Функция считывает базу данных товаров и позволяет супер-пользователю сделать выбор:
        1 - Редактирование товара
        2 - Добавление товара
        3 - Удаление товара
        4 - Выход в главное меню
        """
        products = []

        with codecs.open("products.csv", 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                products.append(row)

        products = sorted(products, key=lambda x: x[0])

        csv_file.close()

        print("Выберите действие: \n 1 - Редактирование товара.\n 2 - Добавление товара.\n 3 - Удаление товара.\n 4 - "
              "Выход в главное меню.")

        choice = int(input())

        if choice == 1:
            self.product_edit(products=products)
        elif choice == 2:
            self.product_add()
        elif choice == 3:
            self.product_delete(products=products)
        elif choice == 4:
            main()

    def product_edit(self, products: []):
        """
        Функция позволяет выбрать ячейку отображённой таблицы для изменения её значения и изменить значение выбранной
        ячейки
        :param products: база данных товаров (название, описание, поставщик, цена, доступно)
        """
        print("Выберите столбец для изменения: \n 1 - Название\n 2 - Описание\n 3 - Поставщик\n 4 - "
              "Цена\n 5 - Доступно")
        try:
            column = int(input())
        except ValueError:
            print("Введено неверное значение для столбца!")
            self.product_edit(products=products)
        try:
            row = int(input("Выберите строку для изменения: "))
        except ValueError:
            print("Введено неверное значение для строки!")
            self.product_edit(products=products)

        print(f"Изменяемое значение: {products[row][column - 1]}")
        products[row][column - 1] = input("Введите новое значение: ")

        if products[row][column - 1] == "":
            products[row][column - 1] = "null"

        self.product_save(products=products)

    def product_add(self):
        """
        Функция позволяет записать в конец базы данных товаров новый товар с введёнными пользователем атрибутами
        """
        name = input("Введите имя нового продукта: ")

        description = input("Введите описание нового продукта: ")
        provide = input("Введите поставщика нового продукта: ")
        try:
            price = int(input("Введите цену (₽) нового продукта: "))
        except ValueError:
            print("Введено неверное значение цены товара!")
            self.product_add()

        try:
            available = int(input("Введите доступное кол-во нового продукта: "))
        except ValueError:
            print("Введено неверное значение доступного кол-ва товара!")
            self.product_add()

        new_product = [name, description, provide, price, available]

        for i in range(len(new_product)):
            if new_product[i] == "":
                new_product[i] = "null"

        with codecs.open("products.csv", 'a', encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(new_product)
        csv_file.close()

        self.visualization()
        self.change_lobby()

    def product_delete(self, products: []):
        """
        Функция позволяет удалить строчку из базы данных товара по её индексу, по умолчанию удаляет последнюю строчку
        :param products: база данных товаров (название, описание, поставщик, цена, доступно)
        """
        choice = input("Выберите номер строки для удаления (по умолчанию - последняя): ")

        if choice != "":
            try:
                choice = int(choice)
            except ValueError:
                print("Введено неверное значение для номера строки!")
                self.product_delete(products=products)
        else:
            choice = -1

        products.pop(choice)
        self.product_save(products=products)

    def product_save(self, products: []):
        """
        Функция сохраняет значения базы данных товаров после изменения значения ячейки выведенной таблицы или удаления
        строки из базы данных
        :param products: база данных товаров (название, описание, поставщик, цена, доступно)
        """
        with codecs.open("products.csv", 'w', encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(products)
        csv_file.close()

        self.visualization()
        self.change_lobby()


if __name__ == "__main__":
    main()
