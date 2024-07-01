from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user_success():
    response = client.post("/user/", json={
        "username": "john_doe",
        "age": 25,
        "email": "john@example.com",
        "password": "super_secret123",
        "phone": "1234567890"
    })
    assert response.status_code == 200
    assert response.json() == {
        "message": "Пользователь создан",
        "user": {
            "username": "john_doe",
            "age": 25,
            "email": "john@example.com",
            "password": "super_secret123",
            "phone": "1234567890"
        }
    }


def test_create_user_invalid_age():
    response = client.post("/user/", json={
        "username": "john_doe",
        "age": 17,
        "email": "john@example.com",
        "password": "super_secret123",
        "phone": "1234567890"
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": "Ошибка проверки данных",
        "errors": ["body -> age: Input should be greater than 18"]
    }


def test_create_user_invalid_email():
    response = client.post("/user/", json={
        "username": "john_doe",
        "age": 25,
        "email": "johnexample.com",  # Неверный email
        "password": "super_secret123",
        "phone": "1234567890"
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": "Ошибка проверки данных",
        "errors": ["body -> email: value is not a valid email address: An email address must have an @-sign."]
    }


def test_create_user_invalid_password_length():
    response = client.post("/user/", json={
        "username": "john_doe",
        "age": 25,
        "email": "john@example.com",
        "password": "short",  # Пароль слишком короткий
        "phone": "1234567890"
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": "Ошибка проверки данных",
        "errors": ["body -> password: String should have at least 8 characters"]
    }


def test_create_user_password_contains_username():
    response = client.post("/user/", json={
        "username": "john_doe",
        "age": 25,
        "email": "john@example.com",
        "password": "john_doe123",  # Пароль содержит имя пользователя
        "phone": "1234567890"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Пароль не должен содержать имя пользователя."}


def test_create_user_missing_username():
    response = client.post("/user/", json={
        "age": 25,
        "email": "john@example.com",
        "password": "super_secret123",
        "phone": "1234567890"
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": "Ошибка проверки данных",
        "errors": ["body -> username: Field required"]
    }


def test_create_user_invalid_phone():
    response = client.post("/user/", json={
        "username": "john_doe",
        "age": 25,
        "email": "john@example.com",
        "password": "super_secret123",
        "phone": "invalid_phone"  # Невалидный телефон
    })
    # Ожидаем, что пользователь будет создан, т.к. телефон не обязателен
    assert response.status_code == 200
    assert response.json() == {
        "message": "Пользователь создан",
        "user": {
            "username": "john_doe",
            "age": 25,
            "email": "john@example.com",
            "password": "super_secret123",
            "phone": "invalid_phone"
        }
    }


def test_create_user_missing_mandatory_fields():
    response = client.post("/user/", json={})
    assert response.status_code == 422
    assert response.json() == {
        "detail": "Ошибка проверки данных",
        "errors": [
            "body -> username: Field required",
            "body -> age: Field required",
            "body -> email: Field required",
            "body -> password: Field required"
        ]
    }
