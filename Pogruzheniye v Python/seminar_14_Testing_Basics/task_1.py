class InvalidRectangleError(Exception):
    """Исключение для недопустимых прямоугольников."""

    def __init__(self, message="Недопустимый прямоугольник."):
        self.message = message
        super().__init__(self.message)


class NegativeSideError(Exception):
    """Исключение для отрицательных сторон прямоугольника."""

    def __init__(self, side_name, side_value):
        self.side_name = side_name
        self.side_value = side_value
        self.message = f"Прямоугольник не может иметь отрицательную сторону: {self.side_name} = {self.side_value}"
        super().__init__(self.message)


class Rectangle:
    """
        Класс InvalidRectangleError будет использоваться для исключения ошибок,
        связанных с созданием недопустимых прямоугольников (например, если длина или ширина равна 0).

        Класс NegativeSideError будет использоваться, чтобы исключать создание прямоугольников с отрицательными сторонами.

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
        if length <= 0 or width <= 0:
            raise InvalidRectangleError("Прямоугольник не может иметь нулевую /n"
                                        "или отрицательную длину или ширину.")
        if length < 0:
            raise NegativeSideError("Длина", length)
        if width < 0:
            raise NegativeSideError("Ширина", width)
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

    try:
        rectangle1 = Rectangle(5, 10)
        rectangle2 = Rectangle(3, 7)
    except (InvalidRectangleError, NegativeSideError) as e:
        print("Ошибка при создании прямоугольника:", e)
    else:
        print(rectangle1.perimeter())
        print(rectangle2.area())

        try:
            rectangle3 = rectangle1 + rectangle2
            print(rectangle3)
            rectangle4 = rectangle1 - rectangle2
            print(rectangle4)
        except (InvalidRectangleError, NegativeSideError) as e:
            print("Ошибка при выполнении операции с прямоугольниками:", e)
