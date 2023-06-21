import random

a = random.randint(5, 10)
b = random.randint(5, 9)
c = random.randint(5, 8)
if a > b + c or b > c + a or c > a + b:
    print("Треугольника с такими сторонами не существует!")
elif a == b and b == c and c == a:
    print("Треугольник равносторонний!")
elif a != b and b != c and c != a:
    print("Треугольник разносторонний!")
else:
    print("Треугольник равнобедренный!")
print(f'a = {a}\nb = {b}\nc = {c}')