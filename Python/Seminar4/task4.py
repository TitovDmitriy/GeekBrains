# Task4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random 

polynomial = [] # список коэффициентов многочлена
k = random.randint(2, 5) # генерируем кол-во коэффициентов многочлена
print(k)
for i in range(k):
    polynomial.append(random.randint(0, 100)) # заполняем список

print(polynomial)
s = ''
for i in range(len(polynomial) - 1):
    if polynomial[i] != 0:
        if (k-i) == 0:
            s += str(polynomial[i]) + "x + "
        else:
            s += str(polynomial[i]) + "x^" + str(k-i) + " + "
output_string = s + str(polynomial[-1]) + " = 0"
print(output_string)

f = open('C:\GitHub_projects\GB\Python\Seminar4\polynomials.txt', 'a')
f.write(output_string) 
f.write('\n')
f.close()


