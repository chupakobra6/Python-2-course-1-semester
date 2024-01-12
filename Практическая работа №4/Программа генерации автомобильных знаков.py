import random
import string


def generationOfCarSigns() -> str:
    """
    Возвращает строку sign - номерной знак, который в равной вероятности может быть в старом формате (NNNLLL) и в новом формате (LLLLNNN) (N - number, число. L - letter, буква)

    :return str:
    """
    choice = random.randint(0, 1)

    if choice == 0:
        sign = ""
        for j in range(3):
            sign += random.choice(string.ascii_uppercase)
        for k in range(3):
            sign += str(random.randint(0, 9))
        return sign

    elif choice == 1:
        sign = ""
        for j in range(4):
            sign += str(random.randint(0, 9))
        for k in range(3):
            sign += random.choice(string.ascii_uppercase)
        return sign


print("Ваш случайный номерной знак - ", generationOfCarSigns())
