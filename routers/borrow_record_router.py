from fastapi import APIRouter
from services import borrow_record_service
import schemas


router = APIRouter(
    tags=["Borrow Record"]
)

@router.get("/borrow_records/{user_id}", response_model=list[schemas.BorrowRecordResponse])
def view_borrowing_records(user_id: int):
    return borrow_record_service.view_borrowing_records(user_id=user_id)

@router.get("/borrow/records/", response_model=list[schemas.BorrowRecordResponse])
def view_all_borrowing_records():
    return borrow_record_service.view_all_borrowing_records()
