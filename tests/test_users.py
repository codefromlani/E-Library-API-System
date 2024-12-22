import pytest
from fastapi.testclient import TestClient
from main import app
import data
import schemas


client = TestClient(app)

# Fixture to reset the in-memory user database before each test
@pytest.fixture
def reset_users_db():
    data.users_db.clear()  # Clear the in-memory database
    yield
    data.users_db.clear()  # Clear after the test if necessary


def test_create_user(reset_users_db):
    user_data = {"name": "John Doe", "email": "john.doe@example.com"}

    # Send a POST request to create the user
    response = client.post("/users/", json=user_data)

    # Assert the response status code is 201 Created
    assert response.status_code == 201

    # Check the response data
    response_data = response.json()
    assert response_data["name"] == user_data["name"]
    assert response_data["email"] == user_data["email"]
    assert response_data["is_active"] is True
    assert "id" in response_data  # id should be generated

    # Check if the user is added to the in-memory database
    assert len(data.users_db) == 1
    user_in_db = data.users_db[response_data["id"]]
    assert user_in_db["name"] == user_data["name"]

# Test creating a user with an existing email (should raise conflict)
def test_create_user_conflict(reset_users_db):
    user_data = {"name": "John Doe", "email": "john.doe@example.com"}

    # First, create a user with the same email
    client.post("/users/", json=user_data)

    # Attempt to create another user with the same email
    response = client.post("/users/", json=user_data)

    # Assert the response status code is 409 Conflict
    assert response.status_code == 409
    assert response.json()["detail"] == "User already exists"

    # Ensure no new user is added to the in-memory database
    assert len(data.users_db) == 1

# Test creating a user with missing required fields (e.g., missing email)
def test_create_user_missing_field(reset_users_db):
    user_data = {"name": "Jane Doe"}  # Missing email

    # Send the POST request with missing field
    response = client.post("/users/", json=user_data)

    # Assert that the status code is 422 Unprocessable Entity
    assert response.status_code == 422
    assert "detail" in response.json()
