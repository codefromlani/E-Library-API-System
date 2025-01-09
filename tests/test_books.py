import pytest
from fastapi.testclient import TestClient
from main import app  
import schemas
import data

client = TestClient(app)


@pytest.fixture
def reset_db():
   
    data.users_db.clear()
    data.books_db.clear()  
    data.borrow_records_db.clear()

   
    data.users_db[1] = {"id": 1, "name": "Test User", "email": "test@example.com", "is_active": True}
    data.books_db[1] = {"id": 1, "title": "1984", "author": "George Orwell", "is_available": True}
    
    return data




def test_create_book_duplicate_title():
    
    book_data_1 = {
        "title": "1984",
        "author": "George Orwell"
    }
    client.post("/books/", json=book_data_1)  
    
   
    book_data_2 = {
        "title": "1984",  
        "author": "George Orwell"
    }
    response = client.post("/books/", json=book_data_2)
    
    
    assert response.status_code == 409
    assert response.json()["detail"] == "Book already exists"
