# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов

lst = [1, 2, 3, 4, 4, 2, 8, 1, 3, 9, 10]

unique_elements = set()
duplicates = set()
for item in lst:
    if item in unique_elements:
        duplicates.add(item)
    else:
        unique_elements.add(item)
result = list(duplicates)
print(result)