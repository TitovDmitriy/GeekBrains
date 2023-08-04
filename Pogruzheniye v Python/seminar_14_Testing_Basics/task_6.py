"""
На семинаре 13 был создан проект, который имел следующие методы:
1. загрузка данных (напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей)
2. вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
3. добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.) по работе с
пользователями (имя, id, уровень).
4. Напишите 3-7 тестов pytest для данного проекта.
5. Используйте фикстуры.

"""

import json


class Project:
    def __init__(self):
        self.users = set()

    def load_data(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            self.users = set(data['users'])

    def login(self, name, user_id):
        user = (name, user_id)
        if user not in self.users:
            raise Exception("Доступ запрещен")
        else:
            user_level = self.get_user_level(user)
            return user_level

    def add_user(self, name, user_id, user_level):
        current_user_level = self.get_user_level((name, user_id))
        if current_user_level < user_level:
            raise Exception("Уровень доступа недостаточен")
        else:
            self.users.add((name, user_id, user_level))

    def get_user_level(self, user):
        for u in self.users:
            if u[:2] == user:
                return u[2]
