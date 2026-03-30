import allure
import requests

@allure.feature("GET接口测试")
@allure.story("基本GET请求")
def test_get_status(base_url, headers):
    with allure.step("发送GET请求"):
        response = requests.get(f"{base_url}/get", headers=headers)
        allure.attach(str(response.url), name="请求URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.json()), name="返回数据", attachment_type=allure.attachment_type.TEXT)
    with allure.step("验证状态码"):
        assert response.status_code == 200

@allure.feature("GET接口测试")
@allure.story("带参数GET请求")
def test_get_with_params(base_url, headers):
    with allure.step("发送带参数GET请求"):
        params = {"name": "张三", "age": 20}
        response = requests.get(f"{base_url}/get", params=params, headers=headers)
        allure.attach(str(response.url), name="请求URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.json()), name="返回数据", attachment_type=allure.attachment_type.TEXT)
    with allure.step("验证状态码"):
        assert response.status_code == 200
    with allure.step("验证参数"):
        data = response.json()
        assert data["args"]["name"] == "张三"
        assert data["args"]["age"] == "20"


def test_get_post():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["userId"] == 1
