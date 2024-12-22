from fastapi import HTTPException, status
from datetime import date
from typing import List
import schemas
import data


def create_book(book: schemas.BookCreate):
    for existing_book in data.books_db.values():
        if existing_book["title"] == book.title:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Book already exists"
            )
    
    new_book = {
        "id": len(data.books_db) + 1,
        "title": book.title,
        "author": book.author,
        "is_available": True
    }

    data.books_db[new_book["id"]] = new_book
    return schemas.BookResponse(**new_book)

def get_books(skip: int = 0, limit: int = 5) -> List[schemas.BookResponse]:
    books = list(data.books_db.values())
    return [schemas.BookResponse(**book) for book in books[skip:skip+limit]]


def get_book_by_id(book_id: int):
    book = data.books_db.get(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    return schemas.BookResponse(**book)

def update_book(book_id: int, book_data: schemas.BookUpdate):
    existing_book = data.books_db.get(book_id)
    if not existing_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    
    if book_data.title is not None:
        existing_book["title"] = book_data.title
    if book_data.author is not None:
        existing_book["author"] = book_data.author
    if book_data.is_available is not None:
        existing_book["is_available"] = book_data.is_available 

    return schemas.BookResponse(**existing_book)

def delete_book(book_id: int):
    existing_book = data.books_db.get(book_id)
    if not existing_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    data.books_db.pop(book_id)

    return {"detail": "Book successfully deleted"}

def mark_book_unavailable(book_id: int):
    existing_book = data.books_db.get(book_id)
    if not existing_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    
    existing_book["is_available"] = False  
    return schemas.BookResponse(**existing_book)