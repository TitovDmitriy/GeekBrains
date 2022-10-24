# Task3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности. 
import random
lst = []
for i in range(random.randint(15, 25)):
    lst.append(random.randint(1, 20))
print(f'Некая последовательность чисел - {lst}')
arr = []
for i in lst:
    if i not in arr:
        arr.append(i)
print(f'Cписок неповторяющихся элементов - {arr}')