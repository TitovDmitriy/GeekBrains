# Task2(Seminar3, Task2).Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


def Couples_list(arrey):
    amount_couples = len(arrey)//2 + 1 if len(arrey) % 2 != 0 else len(arrey)//2
    arrey = [arrey[i]*arrey[len(arrey)-i-1] for i in range(amount_couples)]
    return arrey

lst = list(map(int, (randint(1, 20) for _ in range(randint(5, 15)))))
print(f'Список из нескольких чисел - {lst}')
print(f'Произведение пар чисел списка - {Couples_list(lst)} ')
