# Task_1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15)
import random
from decimal import *

d = random.randint(1, 100) 
print(d)
getcontext().prec = d # задаём точность
denominator = 1 # знаменатель
sum = 0
for i in range(1000000):  # чем выше значение в цикле, тем точнее pi
    if i % 2 == 0:
        sum += 4 / denominator
    else:
        sum -= 4 / denominator
    denominator += 2
print(sum)
print(Decimal(sum) / Decimal(1))
