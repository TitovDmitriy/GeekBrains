# Создайте функцию генератор чисел Фибоначчи
def fibonacci(n):
    fib = []
    a, b = 0, 1
    for i in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib


fib_numbers = fibonacci(10)
for num in fib_numbers:
    print(num)
