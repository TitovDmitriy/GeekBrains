# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
lst = []
for i in range(random.randint(3, 10)):
    lst.append(random.randint(1, 20))
print(f'Список из нескольких чисел - {lst}')

resultlst = []
count = len(lst)
#resultlst = len(lst) / 2 + len(lst) % 2
for i in range(len(lst)):
    if i < (len(lst) / 2) and count > (len(lst) / 2):
        count -= 1
        resultlst.append(lst[i] * lst[count])
        
print(f'Произведение пар чисел списка - {resultlst}')
