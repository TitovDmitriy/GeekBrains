import pytest
import requests
import yaml

@pytest.fixture(scope="session")
def auth_token():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    url = config["site"] + "gateway/login"
    params = {"username": config["username"], "password": config["password"]}
    response = requests.post(url, json=params)
    response.raise_for_status()
    token = response.json()["token"]
    yield token

@pytest.fixture
def auth_header(auth_token):
    return {"X-Auth-Token": auth_token}
