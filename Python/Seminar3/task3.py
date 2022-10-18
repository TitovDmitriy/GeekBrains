# №3.  Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random
lst = []
for i in range(random.randint(5, 15)):
    lst.append(round(random.uniform(1, 20), 2))
print(f'Список из нескольких чисел - {lst}')
min = 0.99
max = 0.01
for i in range(len(lst)):
    if lst[i] % 1 < min:
        min = lst[i] % 1
for y in range(len(lst)):
    if lst[y] % 1 > max:
        max = lst[y] % 1
        
print(round(max, 2), round(min, 2))
print(f'разницa между max и min значением дробной части элементов = {round(max - min, 2)}')
