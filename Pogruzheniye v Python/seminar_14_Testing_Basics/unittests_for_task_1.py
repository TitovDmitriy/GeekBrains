import unittest
from task_1 import Rectangle
from task_1 import NegativeSideError


class TestRectangle(unittest.TestCase):
    def test_create_rectangle(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.length, 5)
        self.assertEqual(rectangle.width, 10)

    def test_create_rectangle_negative_length(self):
        with self.assertRaises(NegativeSideError) as context:
            rectangle = Rectangle(-5, 10)
        self.assertEqual(str(context.exception), "Длина -5 недопустима")

    def test_create_rectangle_negative_width(self):
        with self.assertRaises(NegativeSideError) as context:
            rectangle = Rectangle(5, -10)
        self.assertEqual(str(context.exception), "Ширина -10 недопустима")

    def test_calculate_perimeter(self):
        rectangle = Rectangle(5, 10)
        perimeter = rectangle.perimeter()
        self.assertEqual(perimeter, 30)

    def test_calculate_area(self):
        rectangle = Rectangle(5, 10)
        area = rectangle.area()
        self.assertEqual(area, 50)


if __name__ == '__main__':
    unittest.main()
