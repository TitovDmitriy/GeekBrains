# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
vars = "Hello"
str_worlds = "World"
num = 10
word = "Python"
s = "learning"


def replace_s_var():
    global vars, str_worlds, num, word, s
    s_vars = []  # получаем список переменных, оканчивающихся на s
    for var_name in list(globals().keys()):
        if var_name.endswith('s') and var_name != 's':
            s_vars.append(var_name)

    # переносим значения из переменных на новые переменные без s на конце
    for s_var_name in s_vars:
        var_value = globals()[s_var_name]
        new_var_name = s_var_name[:-1]
    globals()[new_var_name] = var_value

    # заменяем значения переменных, оканчивающихся на s, на None
    for var_name in s_vars:
        globals()[var_name] = None

    print(vars, str_worlds, num, word, s, s_vars, sep='\n')


replace_s_var()
