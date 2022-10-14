# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.
import random
N = int(input('Введите число N: '))
lst = []
for i in range(N):
    lst.append(random.randint(-N, N))
print(f'Список из N элементов - {lst}')

f = open('C:\GitHub_projects\GB\Python\Seminar2\positions.txt', 'r')
result = f.readlines()
result = list(map(int, result))
print(f'Позиции - {result}')
f.close()

composition = 1
for i in result:
    composition *= lst[i] 
print(f'Произведение элементов на указанных позициях равно - {composition}')