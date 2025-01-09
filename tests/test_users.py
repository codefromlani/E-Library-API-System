import pytest
from fastapi.testclient import TestClient
from main import app
import data
import schemas


client = TestClient(app)


@pytest.fixture
def reset_users_db():
    data.users_db.clear()  
    yield
    data.users_db.clear() 


def test_create_user(reset_users_db):
    user_data = {"name": "John Doe", "email": "john.doe@example.com"}

    
    response = client.post("/users/", json=user_data)

   
    assert response.status_code == 201

  
    response_data = response.json()
    assert response_data["name"] == user_data["name"]
    assert response_data["email"] == user_data["email"]
    assert response_data["is_active"] is True
    assert "id" in response_data  

    
    assert len(data.users_db) == 1
    user_in_db = data.users_db[response_data["id"]]
    assert user_in_db["name"] == user_data["name"]


def test_create_user_conflict(reset_users_db):
    user_data = {"name": "John Doe", "email": "john.doe@example.com"}

    
    client.post("/users/", json=user_data)

    
    response = client.post("/users/", json=user_data)

    
    assert response.status_code == 409
    assert response.json()["detail"] == "User already exists"

    
    assert len(data.users_db) == 1


def test_create_user_missing_field(reset_users_db):
    user_data = {"name": "Jane Doe"}  

    
    response = client.post("/users/", json=user_data)

    
    assert response.status_code == 422
    assert "detail" in response.json()
