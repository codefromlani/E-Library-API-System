from datetime import date


users_db = {
    1: {"id": 1, "name": "Alice Johnson", "email": "alice.johnson@example.com", "is_active": True},
    2: {"id": 2, "name": "Bob Smith", "email": "bob.smith@example.com", "is_active": True},
    3: {"id": 3, "name": "Carol Davis", "email": "carol.davis@example.com", "is_active": True},
}


books_db = {
    1: {"id": 1, "title": "1984", "author": "George Orwell", "is_available": True},
    2: {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "is_available": True},
    3: {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "is_available": True},
}

borrow_records_db = [
    {"id": 1, "book_id": 1, "user_id": 1, "borrow_date": date(2024, 12, 1), "return_date": date(2024, 12, 20)},
    {"id": 2, "book_id": 2, "user_id": 1, "borrow_date": date(2024, 12, 5), "return_date": date(2024, 12, 19)},
    {"id": 3, "book_id": 3, "user_id": 3, "borrow_date": date(2024, 12, 10), "return_date": date(2024, 12, 18)},
]
