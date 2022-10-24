# Task2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
import random

N = random.randint(1, 100) 
print(N)
lst = []
for i in range(1, 1000000):  
    if N % i == 0:
        lst.append(i)
print(lst)
