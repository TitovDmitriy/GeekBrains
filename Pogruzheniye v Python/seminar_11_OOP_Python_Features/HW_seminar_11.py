# Создайте класс Матрица. Добавьте методы для:
# 1. Строк документации и вывода на печать,
# 2. сравнения,
# 3. сложения,
# 4. *умножения матриц

class Matrix:
    """
    Класс Matrix представляет собой матрицу.

    Атрибуты:
        matrix (list): Список списков, представляющих матрицу.

    Методы:
        __init__(self, matrix: list): Конструктор класса. Инициализирует матрицу.
        print_matrix(self): Выводит матрицу на печать.
        __eq__(self, other: 'Matrix') -> bool: Проверяет матрицу на равенство с другой матрицей.
        __add__(self, other: 'Matrix') -> 'Matrix': Складывает текущую матрицу с другой матрицей.
        __mul__(self, other: 'Matrix') -> 'Matrix': Умножает текущую матрицу на другую матрицу.
    """

    def __init__(self, matrix: list):
        self.matrix = matrix

    def print_matrix(self):
        """Выводит матрицу на печать."""
        for row in self.matrix:
            print(" ".join(str(element) for element in row))

    def __eq__(self, other: 'Matrix') -> bool:
        """Проверяет матрицу на равенство с другой матрицей."""
        return self.matrix == other.matrix

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Складывает текущую матрицу с другой матрицей."""
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")
        result_matrix = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result_matrix)

    def __mul__(self, other: 'Matrix') -> 'Matrix':
        """Умножает текущую матрицу на другую матрицу."""
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
        result_matrix = [
            [sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix)))
             for j in range(len(other.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result_matrix)

    @staticmethod
    def print_docstring():
        """Вывод документации класса на печать."""
        print(Matrix.__doc__)


if __name__ == '__main__':
    Matrix.print_docstring()

    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])

    print("Матрица 1:")
    matrix1.print_matrix()

    print("Матрица 2:")
    matrix2.print_matrix()

    if matrix1 == matrix2:
        print("Матрицы равны.")
    else:
        print("Матрицы не равны.")

    result_sum = matrix1 + matrix2
    print("Сумма матриц:")
    result_sum.print_matrix()

    result_mul = matrix1 * matrix2
    print("Произведение матриц:")
    result_mul.print_matrix()
