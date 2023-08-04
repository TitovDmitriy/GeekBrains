import unittest
from task_6 import Project


class TestProject(unittest.TestCase):
    def test_load_data(self):
        project = Project()
        project.load_data('data.json')
        self.assertGreater(len(project.users), 0)

    def test_login_valid_user(self):
        project = Project()
        project.users = {('John', 123, 1), ('Alice', 456, 2)}
        user_level = project.login('John', 123)
        self.assertEqual(user_level, 1)

    def test_add_user_higher_level(self):
        project = Project()
        project.users = {('John', 123, 1)}
        project.add_user('Alice', 456, 2)
        self.assertIn(('Alice', 456, 2), project.users)

    def test_add_user_lower_level(self):
        project = Project()
        project.users = {('John', 123, 1)}
        with self.assertRaises(Exception) as context:
            project.add_user('Alice', 456, 0)
        self.assertEqual(str(context.exception), "Уровень доступа недостаточен")


if __name__ == '__main__':
    unittest.main()
