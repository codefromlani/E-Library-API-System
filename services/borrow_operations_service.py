from fastapi import HTTPException, status
from datetime import date
import schemas
import data


def borrow_book(book_id: int, user_id: int):

    user = data.users_db.get(user_id)
    if not user or not user["is_active"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found or not active"
        )

    for record in data.borrow_records_db:
        if record["book_id"] == book_id and record["user_id"] == user_id and not record["return_date"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You have already borrowed this book"
            )
            
    existing_book = data.books_db.get(book_id)
    if not existing_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    
    if not existing_book["is_available"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Book is not available"
        )
        
    borrow_record = {
        "id": len(data.borrow_records_db) + 1,  # Ensure id is included
        "user_id": user_id,
        "book_id": book_id,
        "borrow_date": date.today(),
        "return_date": None,  # Initially, no return date
    }

    data.borrow_records_db.append(borrow_record)
    
    existing_book["is_available"] = False

    return schemas.BookResponse(**existing_book)


def return_book(book_id: int):
    existing_book = data.books_db.get(book_id)
    if not existing_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    if existing_book["is_available"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This book is not currently borrowed"
        )
    
    for record in data.borrow_records_db:
        if record["book_id"] == book_id and not record["return_date"]:
            record["return_date"] = date.today()
            break

    existing_book["is_available"] = True

    return {"message": "Book returned successfully"}