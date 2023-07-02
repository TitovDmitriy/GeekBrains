# Метод copy создал поверхностную копию, копию верхнего уровня. Изменения же
# вложенных объектов отразится и на оригинале. Для создания полной копии любой глубины вложенности
# используют функцию deepcopy из модуля copy.
import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')
# Функция рекурсивно обходит все вложенные объекты создавая их копии.
# Изменения одной коллекции теперь не затрагивают её копию.