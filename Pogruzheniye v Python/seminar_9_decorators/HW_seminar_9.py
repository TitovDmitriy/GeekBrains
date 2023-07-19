"""
Напишите следующие функции:
* Нахождение корней квадратного уравнения
* Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
* Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
* Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
"""
import math
import csv
import json
import random
import shutil
import os


# Функция для нахождения корней квадратного уравнения:
def solve_quad_eq(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return None


# Функция для генерации CSV файла с тремя случайными числами в каждой строке:
def generate_csv_file(filename, num_rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)


# Декоратор для выполнения функции нахождения корней квадратного
# уравнения с каждой тройкой чисел из CSV файла:
def solve_quad_eq_with_csv(func):
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"For coefficients {a}, {b}, {c}: {result}")

    return wrapper


# Декоратор для сохранения переданных параметров и результатов работы
# функции в JSON файл:
def save_params_and_results(func):
    def wrapper(*args, **kwargs):
        params = {'args': args, 'kwargs': kwargs}
        result = func(*args, **kwargs)
        data = {'params': params, 'result': result}
        with open('params_and_results.json', 'w') as file:
            json.dump(data, file)
        return result

    return wrapper


# Создание временной папки для хранения игр
os.makedirs("games")

# Копирование файлов игр в временную папку
shutil.copy("game_queens.py", "games/game_queens.py")
shutil.copy("task_6.py", "games/game_guess.py")

# Архивирование игр в пакет
shutil.make_archive("games_package", "zip", "games")

# Удаление временной папки
shutil.rmtree("games")
