from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class UserResponse(UserCreate):
    id: int
    is_active: bool = True


class BookCreate(BaseModel):
    title: str
    author: str
    is_available: bool = True


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    is_available: Optional[bool] = None


class BookResponse(BookCreate):
    id: int


class BorrowRecordCreate(BaseModel):
    user_id: int
    book_id: int
    borrow_date: date
    return_date: Optional[date] = None


class BorrowRecordResponse(BorrowRecordCreate):
    id: int