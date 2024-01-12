'''
    and - логическое и
    or - логическое или
    not - логическое отрицание (инверсия)
    > - больше
    < - меньше
    >= - больше или равно
    <= - меньше или равно
    != - неравно
    == - равно


a = int(input('Введите первое целое число - '))
b = int(input('Введите второе целое число - '))

print(f'{a} > {b} :', a > b )
print(f'{a} < {b} :', a < b )
print(f'{a} >= {b} :', a >= b )
print(f'{a} <= {b} :', a <= b )
print(f'{a} == {b} :', a == b )
print(f'{a} != {b} :', a != b )


a = a + b
a += b

a = a - b
a -= b

a = a * b
a *= b

a = a / b
a /= b

a = a // b
a //= b

a = a % b
a %= b


print(True)
print(not(True))
print('ff' not in 'Hello world')

a = 10
b = 20
print(a is not b)
print(a is b)

a = int(input('Введите целое число - '))
if a == 5 or a == 7 or a == 4:
    a += 5

    if a == 12:
        print('Целое число a = 12')
    elif a == 13:
        print('Целое число a = 13')
    else:
        print('Целое число a != 12 и 13')

    print('Мы попали в блок if')
    print('Целое число a = 5')
elif a == 10:
    print('Мы попали в блок elif')
    print('Целое число a = 10')
else:
    print('Мы попали в блок else')
    print('Целое число a != 5 или 10')

print('Данный текст выведется вне зависимости от условия if')


admin_login = 'admin'
admin_password = '00000'

login = input('Введите логин - ')
password = input('Введите пароль - ')
role = input('Введите вашу роль - ')

if admin_login == login and admin_password == password:
    print('Поздравляем! Вы успешно аутентифицировались.')
# Аутентификация — процедура проверки подлинности
    if role == 'admin':
        print('Поздравляем! Вы успешно авторизовались как администратор.')
    elif role == 'user':
        print('Поздравляем! Вы успешно авторизовались как пользователь.')
# Авторизация — предоставление определенному лицу или группе лиц прав на выполнение определенных действий.
    elif role == 'guest':
        print('Поздравляем! Вы успешно авторизовались как гость.')
else:
    print('Вы ввели неверные данные!')


a = int(input('Введите целое число от 1 до 5 - '))

match a:
    case 1:
        print('Ваше число = 1')
    case 2:
        print('Ваше число = 2')
    case 3:
        print('Ваше число = 3')
    case 4:
        print('Ваше число = 4')
    case 5:
        print('Ваше число = 5')
    case _:
        print('Вы ввели неверное число')

age = int(input('Введите ваш возраст - '))   # age = int(input())
print('Ваш возраст - ', age)

if age > 18:
    print('Вы совершеннолетний')
elif age == 18:
    print('Вам только-только исполнилось 18')

'''

print(10 % 2)
