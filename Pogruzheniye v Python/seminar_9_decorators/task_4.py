# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.
import json


def save_to_json(repeats):
    def decorator(func):
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

        for _ in range(repeats):
            wrapper = decorator(wrapper)

        return wrapper

    return decorator


@save_to_json(repeats=3)
def add_numbers(a, b):
    return a + b


add_numbers(2, 3)
