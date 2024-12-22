E-Library API System

Overview

The E-Library API System is a RESTful API built to manage a library's book borrowing system. It allows users to perform CRUD operations on users and books, as well as manage book borrowing and returning. This system also allows users to view their borrowing records and track the availability of books.

Features

User Management:

- Create, update, delete, and view user details.
- Deactivate users.

Book Management:

- Add, update, delete, and view books.
- Mark a book as unavailable (e.g., lost or under maintenance).

Borrowing and Returning Books:

- Borrow a book: An active user can borrow an available book.
- Return a book: Marks a book as returned and updates its availability.

Borrow Record Management:

- View borrowing records for a specific user.
- View all borrowing records for all users.

API Endpoints
1. User Endpoints
- Create a User: POST /users/

- Get a User: GET /users/{user_id}

- Update a User: PUT /users/{user_id}

- Delete a User: DELETE /users/{user_id}

- Deactivate a User: PATCH /users/{user_id}/deactivate

2. Book Endpoints
- Create a Book: POST /books/

- Get a Book: GET /books/{book_id}

- Update a Book: PUT /books/{book_id}

- Delete a Book: DELETE /books/{book_id}

- Mark a Book as Unavailable: PATCH /books/{book_id}/unavailable

3. Borrow Operations
- Borrow a Book: POST /borrow/

- Return a Book: POST /return/

4. Borrow Record Management
- View Borrowing Records for a Specific User: GET /borrow/records/{user_id}

- View All Borrowing Records: GET /borrow/records/

Getting Started

Prerequisites:

- Python 3.7+
- FastAPI
- Uvicorn (for running the server)

Installation

To get started with this project, follow these steps:

- Clone the repository: git clone https://github.com/codefromlani/E-Library-API-System.git

- Navigate into the project directory: cd E-Library-API-System

- Create and activate a virtual environment: On Windows: python -m venv venv venv\Scripts\activate On macOS/Linux: python3 -m venv venv source venv/bin/activate

- Install dependencies: pip install -r requirements.txt

- To start the application, use: uvicorn main:app --reload This will start the FastAPI server locally at http://127.0.0.1:8000.