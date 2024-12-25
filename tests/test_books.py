import pytest
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app
import schemas
import data

client = TestClient(app)

# Define the fixture to reset the database
@pytest.fixture
def reset_db():
    # Clear the in-memory database before each test
    data.users_db.clear()
    data.books_db.clear()  # Clear books to ensure no conflicts
    data.borrow_records_db.clear()

    # Optionally, you can add initial data for testing if needed
    # Initial setup can include some users and books
    data.users_db[1] = {"id": 1, "name": "Test User", "email": "test@example.com", "is_active": True}
    data.books_db[1] = {"id": 1, "title": "1984", "author": "George Orwell", "is_available": True}
    
    return data




def test_create_book_duplicate_title():
    # Arrange: Create the first book
    book_data_1 = {
        "title": "1984",
        "author": "George Orwell"
    }
    client.post("/books/", json=book_data_1)  # Create first book
    
    # Act: Try to create a book with the same title
    book_data_2 = {
        "title": "1984",  # Same title as the first book
        "author": "George Orwell"
    }
    response = client.post("/books/", json=book_data_2)
    
    # Assert: Ensure a conflict status is returned (409)
    assert response.status_code == 409
    assert response.json()["detail"] == "Book already exists"
