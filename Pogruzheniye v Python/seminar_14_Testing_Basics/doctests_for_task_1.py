from task_1 import Rectangle


def test_perimeter():
    """
    >>> r = Rectangle(5, 10)
    >>> r.perimeter()
    30
    """


def test_area():
    """
    >>> r = Rectangle(5, 10)
    >>> r.area()
    50
    """


def test_add():
    """
    >>> r1 = Rectangle(5, 10)
    >>> r2 = Rectangle(3, 7)
    >>> r3 = r1 + r2
    >>> r3.length
    8
    >>> r3.width
    17
    """


def test_subtract():
    """
    >>> r1 = Rectangle(5, 10)
    >>> r2 = Rectangle(3, 7)
    >>> r4 = r1 - r2
    >>> r4.length
    2
    >>> r4.width
    3
    """


def test_str():
    """
    >>> r = Rectangle(5, 10)
    >>> str(r)
    'Прямоугольник: Длина - 5, Ширина - 10'
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
