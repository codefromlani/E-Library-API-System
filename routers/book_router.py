from fastapi import APIRouter, status
from services import book_service
import schemas


router = APIRouter(
    tags=["Book"]
)

@router.post("/books/", status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate):
    return book_service.create_book(book=book)

@router.get("/books/")
def get_books(skip: int = 0, limit: int = 5):
    return book_service.get_books(skip=skip, limit=limit)

@router.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    return book_service.get_book_by_id(book_id=book_id)

@router.patch("/books/{book_id}")
def update_book(book_id: int, book_data: schemas.BookUpdate):
    return book_service.update_book(book_id=book_id, book_data=book_data)

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    return book_service.delete_book(book_id=book_id)

@router.patch("/books/{book_id}/unavailable")
def mark_book_unavailable(book_id: int):
    return book_service.mark_book_unavailable(book_id=book_id)