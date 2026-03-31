import pytest
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
