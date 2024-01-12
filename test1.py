print('Данная программа реализует калькулятор')

a = int(input('Введите первое число - '))
b = int(input('Введите второе число - '))
c = input('Введите действие - ')

if c == '+':
    a = a + b
if c == '-':
    a = a - b
if c == '*':
    a = a * b
if c == '/':
    a = a / b
if c == '//':
    a = a // b
if c == '%':
    a = a % b
if c == '**':
    a = a ** b

print(a)

