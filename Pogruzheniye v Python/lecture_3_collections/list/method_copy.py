# Метод copy создаёт поверхностную копию списка.
my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')
