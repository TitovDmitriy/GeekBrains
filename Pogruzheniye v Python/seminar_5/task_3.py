# Создайте функцию генератор чисел Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


f = fibonacci()
print(next(f))
print(next(f))
print(next(f))
