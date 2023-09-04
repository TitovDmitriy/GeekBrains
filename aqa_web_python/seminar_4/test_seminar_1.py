import requests
import yaml
import logging
from ddt import ddt, data, unpack


logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@ddt
def test_other_user_posts(auth_header):
    try:
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
        url = config["site"] + "api/posts"
        params = {"owner": "notMe"}

        response = requests.get(url, params=params, headers=auth_header)
        response.raise_for_status()
        posts = response.json()

        # Проверяем наличие поста с определенным заголовком в списке постов
        assert any(post["title"] == "Test post" for post in posts)

    except Exception as e:
        logging.error("Ошибка в test_other_user_posts: %s", str(e))
        raise

def test_create_and_check_post(auth_header):
    try:
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

        # Проверяем наличие поста с определенным описанием
        assert any(post["description"] == "Description of new post" for post in posts)

    except Exception as e:
        logging.error("Ошибка в test_create_and_check_post: %s", str(e))
        raise
