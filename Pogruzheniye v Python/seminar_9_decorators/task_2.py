# Дорабатываем предыдущую задачу.
# 1. Превратите внешнюю функцию в декоратор.
# 2. Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны
# [1, 100] и [1, 10].
# 3. Если не входят, вызывать функцию со случайными числами из диапазонов.


import random


def number_range_check(func):
    def wrapper():
        number = int(input("Загадайте число от 1 до 100: "))
        attempts = int(input("Введите количество попыток (от 1 до 10): "))

        if number < 1 or number > 100 or attempts < 1 or attempts > 10:
            number = random.randint(1, 100)
            attempts = random.randint(1, 10)
            print("Введены некорректные значения. Будут использованы случайные числа:")

        func(number, attempts)

    return wrapper


@number_range_check
def guess_number(number, attempts):
    while attempts > 0:
        guess = int(input("Угадайте число: "))
        if guess < number:
            print("Загаданное число больше.")
        elif guess > number:
            print("Загаданное число меньше.")
        else:
            print("Поздравляю, вы угадали!")
            return

        attempts -= 1
        if attempts == 0:
            print("Количество попыток исчерпано.")
            return

        print(f"Осталось {attempts} попыток.")


guess_number()
