import pytest
import requests
from utils import get_config
from logger import logger

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

@pytest.fixture(scope="session")
def token():
    logger.info("开始登录...")
    response = requests.post(f"{MALL_URL}/api/login", json={
        "username": "admin",
        "password": "123456"
    })
    data = response.json()
    logger.info(f"登录结果：{data}")
    return data["token"]

@pytest.fixture
def clean_data(token):
    # 测试前先清理
    requests.delete(f"{MALL_URL}/api/orders/clear", params={"token": token})
    logger.info("测试前数据已清理")
    yield
    # 测试后再清理
    requests.delete(f"{MALL_URL}/api/orders/clear", params={"token": token})
    logger.info("测试后数据已清理")