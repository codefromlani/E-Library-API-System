from fastapi import APIRouter
from services import borrow_operations_service
from datetime import date


router = APIRouter(
    tags=["Borrow Operation"]
)

@router.post("/books/borrow/{book_id}/{user_id}")
def borrow_book(book_id: int, user_id: int):
    return borrow_operations_service.borrow_book(book_id=book_id, user_id=user_id)

@router.post("/books/return/{book_id}")
def return_book(book_id: int):
    return borrow_operations_service.return_book(book_id=book_id)