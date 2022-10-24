# Task5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# Берём данные из первого файла
file = open('C:\GitHub_projects\GB\Python\Seminar4\polyfile1.txt', 'r') 
temp = file.read()
file.close()
temp = temp[:-4] # удаляем лишнее
temp = temp[:2] + temp[7:]
temp = temp[:4] + temp[9:]
temp = temp[:6] + temp[12:]
first_poly = temp.split(' ')
poly_one = list(map(int, first_poly)) # преобразовываем в список чисел
print(poly_one)

# Берём данные из второго файла
file = open('C:\GitHub_projects\GB\Python\Seminar4\polyfile2.txt', 'r')
temp = file.read()
file.close()
temp = temp[:-4] # повторяем манипуляции и преобразования, но уже со вторым
temp = temp[:2] + temp[7:]
temp = temp[:4] + temp[9:]
temp = temp[:6] + temp[12:]
second_poly = temp.split(' ')
poly_two = list(map(int, second_poly))
print(poly_two)

sum_poly = '' # здесь будет храниться сумма многочленов
# высчитываем сумму многочленов
for i in range(len(poly_one) - 1):
    if poly_one[i] != 0:
        if (len(poly_one)-i) == 0:
            sum_poly += str(poly_one[i] + poly_two[i]) + "x + "
        else:
            sum_poly += str(poly_one[i] + poly_two[i]) + "x^" + str(len(poly_one)-i) + " + "

sum_poly += str(poly_one[-1] + poly_two[-1])

print(f'Cуммa многочленов = {sum_poly}')

f = open('C:\GitHub_projects\GB\Python\Seminar4\sum_poly.txt', 'w')
f.write(sum_poly) 
f.close()

