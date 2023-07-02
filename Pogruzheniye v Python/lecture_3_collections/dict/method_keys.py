# Метод keys возвращает объект-итератор dict_keys.
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())
for key in my_dict.keys():
    print(key)
# Обычно объект не используют напрямую. Метод keys применяется в связке с циклом for для перебора ключей словаря.
