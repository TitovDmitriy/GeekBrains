class Rectangle:
    """
    Класс Rectangle представляет прямоугольник.

    Атрибуты:
        length (float): Длина прямоугольника.
        width (float): Ширина прямоугольника.

    Методы:
        perimeter(): Возвращает периметр прямоугольника.
        area(): Возвращает площадь прямоугольника.
        __add__(other): Возвращает новый экземпляр прямоугольника, являющийся результатом сложения с другим прямоугольником.
        __sub__(other): Возвращает новый экземпляр прямоугольника, являющийся результатом вычитания из текущего прямоугольника другого прямоугольника.
        __str__(): Возвращает строковое представление прямоугольника.
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __add__(self, other):
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_length = self.length - other.length
        new_width = self.width - other.width
        if new_length < 0:
            new_length = 0
        if new_width < 0:
            new_width = 0
        return Rectangle(new_length, new_width)

    def __str__(self):
        return f"Прямоугольник: Длина - {self.length}, Ширина - {self.width}"

    @staticmethod
    def print_docstring():
        """Вывод документации класса на печать."""
        print(Rectangle.__doc__)


if __name__ == '__main__':
    Rectangle.print_docstring()
    rectangle1 = Rectangle(5, 10)
    rectangle2 = Rectangle(3, 7)
    print(rectangle1.perimeter())
    print(rectangle2.area())
    rectangle3 = rectangle1 + rectangle2
    print(rectangle3)
    rectangle4 = rectangle1 - rectangle2
    print(rectangle4)
