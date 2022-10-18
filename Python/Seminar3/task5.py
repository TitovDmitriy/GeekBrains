# Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов. Негафибоначчи
#  Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# num > 0 = fif2onacci (num - 1) + fif2onacci (num - 2)
# num < 0 = fif2onacci (num + 2) - fif2onacci (num + 1)

import random
num = random.randint(5, 10)
print(num)
lst = []
f1, f2 = 1, 1
for i in range(num-1):
    lst.append(f1)
    f1, f2 = f2, f1 + f2

f1, f2 = 0, 1
for i in range(num):
    lst.insert(0, f1)
    f1, f2 = f2, f1 - f2

print(lst)

