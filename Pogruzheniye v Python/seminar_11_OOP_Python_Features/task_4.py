# Добавьте методы представления экземпляра для программиста
# и для пользователя

class Archive:
    """
    Класс Archive хранит пару свойств (число и строку)
    и архивирует их в пару списков при создании каждого нового экземпляра

    Атрибуты:
        number (int): Числовое значение для хранения.
        string (str): Стоковое значение для хранения.
        data_archive (list): Список, содержащий архивы предыдущих чисел и строк.

    Методы:
        __init__(self, number, string): Конструктор класса.
        add_to_archive(self): Добавляет текущие значения числа и строки в архив.
        print_archive(self): Выводит все данные из архива на печать.
        get_number(self): Возвращает текущее числовое значение.
        get_string(self): Возвращает текущее строковое значение.
        show_to_programmer(self): Выводит данные архива в формате, удобном для программиста.
        show_to_user(self): Выводит данные архива в формате, удобном для пользователя.
    """

    def __init__(self, number, string):
        self.number = number
        self.string = string
        self.data_archive = []

    def add_to_archive(self):
        self.data_archive.append((self.number, self.string))

    def print_archive(self):
        print("Архив данных:")
        for data in self.data_archive:
            print(f"Число: {data[0]}, Строка: {data[1]}")

    def get_number(self):
        return self.number

    def get_string(self):
        return self.string

    def show_to_programmer(self):
        print("Архив данных (для программиста):")
        for data in self.data_archive:
            print(f"Number: {data[0]}, String: {data[1]}")

    def show_to_user(self):
        print("Архив данных (для пользователя):")
        for data in self.data_archive:
            print(f"Число: {data[0]}, Строка: {data[1]}")

    @staticmethod
    def print_docstring():
        print(Archive.__doc__)


if __name__ == '__main__':
    Archive.print_docstring()
