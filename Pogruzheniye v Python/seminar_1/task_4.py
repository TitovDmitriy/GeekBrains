import random
count = 0
n = random.randint(1, 100)
for i in range(2, n + 1):
    if n % i == 0:
        count += 1
print(f'n = {n}')
if count == 1:
    print("Число простое!")
else:
    print("Число не является простым!")