#  Пользователь вводит строку текста. Подсчитайте сколько раз встречается каждая буква в строке
#  без использования метода count и с ним. Результат сохраните в словаре, где ключ — символ,
#  а значение — частота встречи символа в строке.
#  Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

user_string = "Словари в Python - неупорядоченные коллекции произвольных объектов с доступом по ключу"
user_string = user_string.replace(" ", "")
user_string = user_string.replace("-", "")
user_string = user_string.lower()
print(user_string)
str_to_dct = {}
for c in user_string:
    str_to_dct[c] = str_to_dct.get(c, 0) + 1
print(str_to_dct)

dct_2 = {}
for c in user_string:
    dct_2[c] = dct_2.get(c, user_string.count(c))
print(dct_2)
