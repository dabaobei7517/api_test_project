import allure
import requests
import openpyxl
import pytest

def read_test_data():
    wb = openpyxl.load_workbook("test_data/test_data.xlsx")
    ws = wb.active
    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] is not None:  # 过滤空行
            data.append(row)
    return data

@allure.feature("POST接口测试")
@pytest.mark.parametrize("username, password, expected_status", read_test_data())
def test_post_login(base_url, headers, username, password, expected_status):
    with allure.step("发送POST请求"):
        body = {"username": username, "password": password}
        response = requests.post(f"{base_url}/post", json=body, headers=headers)
        allure.attach(str(response.json()), name="返回数据", attachment_type=allure.attachment_type.TEXT)
    with allure.step("验证状态码"):
        assert response.status_code == expected_status
    with allure.step("验证用户名"):
        assert response.json()["json"]["username"] == username