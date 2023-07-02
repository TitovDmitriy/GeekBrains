"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
 используйте его строковое представление.
"""


def key_value_func(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        result_dict[str(value)] = key
    return print(result_dict)


key_value_func(a=1, b="hello", c=[1, 2, 3])
