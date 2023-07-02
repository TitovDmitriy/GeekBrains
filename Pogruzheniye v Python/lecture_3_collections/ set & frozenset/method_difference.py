# Метод difference удаляет из левого множества элементы правого.
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
# На выходе получаем множество элементов встречающихся только в левом множестве.
# Более короткая запись возможно при помощи знака минус. Вычитаем из левого элементы правого.
new_set_2 = my_set - other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')
