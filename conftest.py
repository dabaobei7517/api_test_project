import pytest
import requests
from utils import get_config

config = get_config()

@pytest.fixture
def base_url():
    return config["base_url"]

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

MALL_URL = "http://127.0.0.1:8000"

@pytest.fixture
def token():
    response = requests.post(f"{MALL_URL}/api/login", json={
        "username": "admin",
        "password": "123456"
    })
    return response.json()["token"]