import pytest
import requests
import yaml
from ddt import ddt, data, unpack

@ddt
def test_other_user_posts(auth_header):
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    url = config["site"] + "api/posts"
    params = {"owner": "notMe"}
    response = requests.get(url, params=params, headers=auth_header)
    response.raise_for_status()
    posts = response.json()
    # проверяем наличие поста с определенным заголовком в списке постов
    assert any(post["title"] == "Test post" for post in posts)

def test_create_and_check_post(auth_header):
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    url = config["site"] + "api/posts"
    data = {"title": "New post", "description": "Description of new post", "content": "Content of new post"}
    response = requests.post(url, json=data, headers=auth_header)
    response.raise_for_status()

    url = config["site"] + "api/posts"
    params = {"owner": config["username"]}
    response = requests.get(url, params=params, headers=auth_header)
    response.raise_for_status()
    posts = response.json()
    # проверяем наличие поста с определенным описанием
    assert any(post["description"] == "Description of new post" for post in posts)
