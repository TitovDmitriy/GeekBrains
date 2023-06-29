"""
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""
friends_items = {
    'Александр': ('палатка', 'спальник', 'рюкзак'),
    'Илья': ('спальник', 'фонарик', 'карта', 'перцовка'),
    'Екатерина': ('рюкзак', 'еда', 'фляжка', 'палатка')
}
# Какие вещи взяли все три друга
for key, values in friends_items.items():
    string_values = [str(i) for i in values]
    joined = ", ".join(string_values)
    print(f"{key} взял: {joined}")

all_items = set.intersection(*map(set, friends_items.values()))
print(f"Друзья взяли с собой: {', '.join(all_items)}")

# Какие вещи уникальны, есть только у одного друга
unique_items = set.union(*map(set, friends_items.values())) - all_items
for friend, items in friends_items.items():
    if set(items) & unique_items:
        print(f"У {friend} уникальные вещи: {', '.join(set(items) & unique_items)}")

# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
common_items = set()
for friend in friends_items:
    for item in friends_items[friend]:
        count = sum(item in friends_items[other_friend] for other_friend in friends_items if other_friend != friend)
        if count == len(friends_items) - 2:
            common_items.add(item)
            for friend in friends_items:
                if not set(friends_items[friend]).intersection(common_items):
                    print(f"У {friend} нет общих вещей: {', '.join(common_items)}")

