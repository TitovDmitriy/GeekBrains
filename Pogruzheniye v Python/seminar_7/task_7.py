"""
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
import shutil


def sort_files(source_directory, destination_directory):
    # Проверяем, существует ли исходная директория
    if not os.path.exists(source_directory):
        print("Исходная директория не существует.")
        return

    # Проверяем, существует ли папка назначения
    if not os.path.exists(destination_directory):
        # Если папка назначения отсутствует, создаем ее
        os.makedirs(destination_directory)

    # Список групп файлов и соответствующих расширений
    file_groups = {
        "видео": [".mp4", ".avi", ".mkv"],
        "изображения": [".jpg", ".jpeg", ".png", ".gif"],
        "текст": [".txt", ".docx", ".pdf"]
    }

    # Получаем список файлов в исходной директории
    files = os.listdir(source_directory)

    for file in files:
        file_extension = os.path.splitext(file)[1]

        # Проверяем расширение файла и определяем группу
        for group_name, extensions in file_groups.items():
            if file_extension.lower() in extensions:
                # Папка назначения для данной группы
                group_directory = os.path.join(destination_directory, group_name)

                # Проверяем, существует ли папка назначения для данной группы
                if not os.path.exists(group_directory):
                    os.makedirs(group_directory)

                # Копируем файл в папку назначения
                source_path = os.path.join(source_directory, file)
                destination_path = os.path.join(group_directory, file)
                shutil.copy(source_path, destination_path)

                # Удаляем файл из исходной директории
                os.remove(source_path)
                break

    print("Сортировка файлов завершена.")


# Пример использования функции
sort_files("my_directory", "sorted_directory")
