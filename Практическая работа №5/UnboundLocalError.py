try:
    outer = 1

    def update_outer():
        if outer == 1:
            outer = 2

    update_outer()

except UnboundLocalError:
    print("Сделана ссылка на локальную переменную в функции, но переменная не определена ранее.")
finally:
    print("Программа завершена")
