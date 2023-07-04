# Напишите функцию, которая принимает на вход строку — абсолютный путь
# до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла,
# расширение файла.

def split_filepath(filepath: str) -> tuple:
    # разбиваем путь на компоненты
    path_parts = filepath.split('/')
    # получаем имя файла
    filename = path_parts[-1]
    # получаем расширение файла
    extension = filename.split('.')[-1]
    # получаем имя файла без расширения
    name = '.'.join(filename.split('.')[:-1])
    # получаем путь без имени файла
    path = '/'.join(path_parts[:-1])
    return (path, name, extension)


filepath = "/home/user/documents/file.txt"
path, name, extension = split_filepath(filepath)
print(f"Path: {path}, Name: {name}, Extension: {extension}")
