import requests

def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response.json())
    assert response.status_code == 200

def test_get_single_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert data["id"] == 1

def test_user_address():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()
    assert data["address"]["city"] == "Gwenborough"
    assert data["address"]["geo"]["lat"] == "-37.3159"

def test_create_post():
    body = {
        "title": "测试文章",
        "body": "文章内容",
        "userId": 1
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=body
    )
    data = response.json()
    print(data)
    assert response.status_code == 201
    assert data["title"] == "测试文章"
    assert data["userId"] == 1

def test_update_post():
    body = {"title": "修改后的标题"}
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=body
    )
    assert response.status_code == 200
    assert response.json()["title"] == "修改后的标题"

def test_delete_post():
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    assert response.status_code == 200