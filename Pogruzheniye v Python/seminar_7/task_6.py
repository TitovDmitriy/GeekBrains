import os
import random
import string

"""
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""


def generate_files(directory, num_files):
    # Проверяем, существует ли указанная директория
    if not os.path.exists(directory):
        # Если директория отсутствует, то создаём её
        os.makedirs(directory)

    # Получаем список файлов в указанной директории
    existing_files = os.listdir(directory)

    for i in range(num_files):
        file_name = generate_unique_filename(existing_files)
        file_path = os.path.join(directory, file_name)

        # Генерируем случайное содержимое файла
        file_content = generate_random_content()

        # Записываем содержимое в новый файл
        with open(file_path, 'w') as f:
            f.write(file_content)

        # Добавляем новое имя файла в список существующих файлов
        existing_files.append(file_name)


def generate_unique_filename(existing_files):
    while True:
        file_name = ''.join(random.choices(string.ascii_lowercase, k=10)) + '.txt'
        if file_name not in existing_files:
            return file_name


def generate_random_content():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=100))


# Создаём папку "my_directory" и заполняем её 10-тью файлами
generate_files("my_directory", 10)
