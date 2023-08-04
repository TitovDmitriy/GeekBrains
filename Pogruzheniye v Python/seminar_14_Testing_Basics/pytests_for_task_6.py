import pytest
from task_6 import Project


@pytest.fixture
def project():
    return Project()


def test_load_data(project):
    project.load_data('data.json')
    assert len(project.users) > 0


def test_login_valid_user(project):
    project.users = {('John', 1, 1), ('Alice', 2, 2)}
    assert project.login('John', 1) == 1


def test_login_invalid_user(project):
    project.users = {('John', 1, 1), ('Alice', 2, 2)}
    with pytest.raises(Exception):
        project.login('Bob', 3)


def test_add_user_higher_level(project):
    project.users = {('John', 1, 1)}
    with pytest.raises(Exception):
        project.add_user('Alice', 2, 2)


def test_add_user_lower_level(project):
    project.users = {('John', 1, 1)}
    project.add_user('Alice', 2, 0)
    assert ('Alice', 2, 0) in project.users


def test_get_user_level(project):
    project.users = {('John', 1, 1), ('Alice', 2, 2)}
    assert project.get_user_level(('John', 1)) == 1
    assert project.get_user_level(('Alice', 2)) == 2


if __name__ == '__main__':
    pytest.main()
