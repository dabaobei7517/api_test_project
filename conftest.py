import pytest

@pytest.fixture
def base_url():
    return "https://httpbin.org"

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }