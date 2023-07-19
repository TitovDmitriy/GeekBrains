# 1. Напишите декоратор, который сохраняет в json файл параметры
# декорируемой функции и результат, который она возвращает. При повторном вызове
# файл должен расширяться, а не перезаписываться.
# 2. Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 3. Для декорирования напишите функцию, которая может принимать как позиционные,
# так и ключевые аргументы.
# 4. Имя файла должно совпадать с именем декорируемой функции.

import json


def save_to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        filename = func.__name__ + ".json"
        data = {}

        # Если файл уже существует, загружаем данные из него
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            pass

        # Сохраняем параметры функции и результат
        key = len(data) + 1
        data[key] = {
            "args": args,
            "kwargs": kwargs,
            "result": result
        }

        # Записываем данные в файл
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        return result

    return wrapper


@save_to_json
def add_numbers(a, b):
    return a + b


add_numbers(2, 3)
add_numbers(4, 5)
