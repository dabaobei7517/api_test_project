import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"




def test_login_wrong_password():
    response = requests.post(f"{BASE_URL}/api/login", json={
        "username": "admin",
        "password": "wrongpass"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "用户名或密码错误"
def test_login_success(token):
    assert token != ""

def test_get_products(token):
    response = requests.get(f"{BASE_URL}/api/products", params={"token": token})
    data = response.json()
    assert response.status_code == 200
    assert data["code"] == 200
    assert len(data["data"]) > 0

def test_getby_id_product(token):
    # 获取第一个商品的ID
    response = requests.get(f"{BASE_URL}/api/products", params={"token": token})
    data = response.json()
    product_id = data["data"][0]["id"]

    # 根据ID获取商品详情
    response = requests.get(f"{BASE_URL}/api/products/{product_id}", params={"token": token})
    data = response.json()
    assert response.status_code == 200
    
    assert data["code"] == 200
    assert data["data"]["name"] == "苹果"
def test_get_product_not_found(token):
    response = requests.get(f"{BASE_URL}/api/products/999", params={"token": token})
    assert response.status_code == 404
    assert response.json()["detail"] == "商品不存在"

def test_add_to_cart(token):
    response = requests.post(f"{BASE_URL}/api/cart", 
        params={"token": token},
        json={"product_id": 1, "quantity": 2}
    )
    data = response.json()
    assert response.status_code == 200
    assert data["message"] == "加入购物车成功"

def test_get_cart(token):
    response = requests.get(f"{BASE_URL}/api/cart", params={"token": token})
    data = response.json()
    assert response.status_code == 200
    assert len(data["data"]) > 0
def test_full_shopping_flow(token):
    # 第一步：查看商品列表
    response = requests.get(f"{BASE_URL}/api/products", params={"token": token})
    products = response.json()["data"]
    assert len(products) > 0

    # 第二步：选第一个商品加入购物车
    product_id = products[0]["id"]
    response = requests.post(f"{BASE_URL}/api/cart",
        params={"token": token},
        json={"product_id": product_id, "quantity": 1}
    )
    assert response.json()["message"] == "加入购物车成功"

    # 第三步：验证购物车有这个商品
    response = requests.get(f"{BASE_URL}/api/cart", params={"token": token})
    cart = response.json()["data"]
    assert any(item["product_id"] == product_id for item in cart)

def test_create_order(token):
    # 先加入购物车
    requests.post(f"{BASE_URL}/api/cart",
        params={"token": token},
        json={"product_id": 1, "quantity": 1}
    )
    # 下单
    response = requests.post(f"{BASE_URL}/api/orders", params={"token": token})
    data = response.json()
    assert response.status_code == 200
    assert data["message"] == "下单成功"
    assert data["order_id"] > 0

def test_get_orders(token):
    response = requests.get(f"{BASE_URL}/api/orders", params={"token": token})
    data = response.json()
    assert response.status_code == 200
    assert len(data["data"]) > 0

def test_complete_order_flow(token):
    # 第一步：查商品
    response = requests.get(f"{BASE_URL}/api/products", params={"token": token})
    product_id = response.json()["data"][0]["id"]

    # 第二步：加购物车
    response = requests.post(f"{BASE_URL}/api/cart",
        params={"token": token},
        json={"product_id": product_id, "quantity": 2}
    )
    assert response.json()["message"] == "加入购物车成功"

    # 第三步：下单
    response = requests.post(f"{BASE_URL}/api/orders", params={"token": token})
    data = response.json()
    assert data["message"] == "下单成功"
    order_id = data["order_id"]

    # 第四步：查订单
    response = requests.get(f"{BASE_URL}/api/orders", params={"token": token})
    orders = response.json()["data"]
    assert any(o["order_id"] == order_id for o in orders)