from task_6 import Project


def test_load_data():
    project = Project()
    project.load_data('data.json')
    assert len(project.users) > 0


def test_login_valid_user():
    project = Project()
    project.users = {('John', 123, 1), ('Alice', 456, 2)}
    user_level = project.login('John', 123)
    assert user_level == 1


def test_login_invalid_user():
    project = Project()
    project.users = {('John', 123, 1), ('Alice', 456, 2)}
    try:
        project.login('Bob', 789)
        assert False
    except Exception as e:
        assert str(e) == "Доступ запрещен"


def test_add_user_higher_level():
    project = Project()
    project.users = {('John', 123, 1)}
    project.add_user('Alice', 456, 2)
    assert ('Alice', 456, 2) in project.users


def test_add_user_lower_level():
    project = Project()
    project.users = {('John', 123, 1)}
    try:
        project.add_user('Alice', 456, 0)
        assert False
    except Exception as e:
        assert str(e) == "Уровень доступа недостаточен"


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
