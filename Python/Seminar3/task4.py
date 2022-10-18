# №4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
import random
num = random.randint(0, 100)
bin = ''
print(num) 
while num > 0:
    bin = str(num % 2) + bin
    num = num // 2
 
print(bin)
