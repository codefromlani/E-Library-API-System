from fastapi import FastAPI
from routers import user_router, book_router, borrow_operations_router, borrow_record_router


app = FastAPI(
    title="E-Library API System"
)

app.include_router(user_router.router)
app.include_router(book_router.router)
app.include_router(borrow_operations_router.router)
app.include_router(borrow_record_router.router)

@app.get("/")
def home():
    return {"message": "Welcome to my E-Library API System"}