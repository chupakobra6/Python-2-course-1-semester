print("Вводите цифры для сортировки (0 - окончание ввода) - ")
n = 1
numbers = []

while n != 0:
    n = int(input())
    numbers.append(n)

numbers.pop(-1)
numbers.sort()

for i in range(len(numbers)):
    print(numbers[i])
