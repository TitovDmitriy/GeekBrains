# f-строки похожи на более короткую и читаемую запись метода формат.
name = 'Alex'
age = 12
text = f'Меня зовут {name} и мне {age} лет'
print(text)
# Перед открывающей кавычкой пишут f — указатель на отформатированную строку.
# Текст внутри фигурных скобок воспринимается как переменная и на печать выводятся из значения.
# 🔥 Важно! Для печати фигурных скобок используется две фигурные скобки слитно.
print(f'{{Фигурные скобки}} и {{name}}')
# Помимо вывода содержимого переменной можно указать дополнительные символы, влияющие на представление.
