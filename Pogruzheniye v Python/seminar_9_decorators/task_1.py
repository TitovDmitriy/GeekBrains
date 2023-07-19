# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# - от 1 до 100 для загадывания,
# - от 1 до 10 для количества попыток
# 2. Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

def guess_number():
    # Функция-замыкание, которая просит пользователя угадать число

    number = None
    attempts = None

    def set_values():
        nonlocal number, attempts
        number = int(input("Загадайте число от 1 до 100: "))
        attempts = int(input("Введите количество попыток (от 1 до 10): "))

    def play_game():
        nonlocal number, attempts
        if number is None or attempts is None:
            set_values()

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

    return play_game


game = guess_number()
game()
