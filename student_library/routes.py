from fastapi import APIRouter, HTTPException, Depends
from .database import SessionLocal
from sqlalchemy.orm import Session
from .schemas import Response, RequestStudent, RequestBook

from . import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Students
@router.post("/")
async def create_student(request: RequestStudent,  db: Session = Depends(get_db)):
    crud.create_student(db, student=request.parameter)
    return Response(status="OK", code=200, message="Student created successfully").dict(exclude_none=True)

@router.get("/students")
async def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    student = crud.get_students(db, skip, limit)
    return Response(status="OK", code=200, message="Students retrieved successfully", result=student)

@router.get("/{student_id}")
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return Response(status="OK", code=200, message="Student retrieved successfully", result=student)

@router.put("/{student_id}")
async def update_student(student_id: int, request: RequestStudent, db: Session = Depends(get_db)):
    student = crud.update_student(db, student_id, student_id=request.parameter.id, first_name=request.parameter.first_name, 
            last_name=request.parameter.last_name, dob=request.parameter.dob, email=request.parameter.email)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return Response(status="OK", code=200, message="Student updated successfully", result=student)

@router.delete("/{student_id}")
async def delete_student(student_id: int, request: RequestStudent,  db: Session = Depends(get_db)):
    student = crud.delete_student(db, student_id=request.parameter.id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return Response(status="OK", code=200, message="Student deleted successfully", result=student)



# Books
@router.post("/")
async def create_book(request: RequestStudent,  db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(status="OK", code=200, message="Book created successfully").dict(exclude_none=True)

@router.get("/books")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    book = crud.get_books(db, skip, limit)
    return Response(status="OK", code=200, message="Books retrieved successfully", result=book)

@router.get("/{book_id}")
async def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status="OK", code=200, message="Book retrieved successfully", result=book)

@router.put("/{book_id}")
async def update_book(book_id: int, request: RequestBook, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, book_id=request.parameter.id, title=request.parameter.title, 
            author=request.parameter.author, published_date=request.parameter.published_date, ISBN=request.parameter.ISBN)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status="OK", code=200, message="Book updated successfully", result=book)

@router.delete("/{book_id}")
async def delete_book(book_id: int, request: RequestBook,  db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id=request.parameter.id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status="OK", code=200, message="Book deleted successfully", result=book)
