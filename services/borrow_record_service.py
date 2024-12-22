from fastapi import HTTPException, status
import data
import schemas


def view_borrowing_records(user_id: int):

    user_records = []
    
    for record in data.borrow_records_db:
        if record["user_id"] == user_id:

            try:
                user_records.append(schemas.BorrowRecordResponse(**record))

            except Exception as e:
                print(f"Error processing record {record}: {e}")

           
    if not user_records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No borrowing records found for this user"
        )
    
    return user_records

def view_all_borrowing_records():
    return [schemas.BorrowRecordResponse(**record) for record in data.borrow_records_db]
