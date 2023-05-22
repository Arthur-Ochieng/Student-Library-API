from fastapi import APIRouter, HTTPException, Depends
from .database import SessionLocal
from sqlalchemy.orm import Session
from .schemas import Response, RequestStudent, RequestBook, RequestAssociation, StudentSchema, BookSchema

from . import crud

router_stud = APIRouter()
router_book = APIRouter()
router_association = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Students
@router_stud.post("")
async def create_student(request: RequestStudent,  db: Session = Depends(get_db)):
    crud.create_student(db, student=request.parameter)
    return Response(status="OK", code=200, message="Student created successfully").dict(exclude_none=True)

@router_stud.get("/students")
async def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _student = crud.get_students(db, skip, limit)
    return Response(status="OK", code=200, message="Students retrieved successfully", result=_student)

@router_stud.get("/{student_id}")
async def get_student(student_id: int, db: Session = Depends(get_db)):
    _student = crud.get_student(db, student_id)
    if _student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return Response(status="OK", code=200, message="Student retrieved successfully", result=_student)

@router_stud.put("/{student_id}")
async def update_student(student_id: int, request: RequestStudent, db: Session = Depends(get_db)):
    _student = crud.update_student(db, student_id=request.parameter.id, first_name=request.parameter.first_name, 
            last_name=request.parameter.last_name, date_of_birth=request.parameter.date_of_birth, email=request.parameter.email)
    if _student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return Response(status="OK", code=200, message="Student updated successfully", result=_student)

@router_stud.delete("/{student_id}")
async def delete_student(student_id: int, request: RequestStudent,  db: Session = Depends(get_db)):
    _student = crud.delete_student(db, student_id=request.parameter.id)
    if _student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    # _student = crud.delete_student(db, student_id=request.parameter.id)
    return Response(status="OK", code=200, message="Student deleted successfully", result=_student).dict(exclude_none=True)



# Books
@router_book.post("")
async def create_book(request: RequestBook,  db: Session = Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(status="OK", code=200, message="Book created successfully").dict(exclude_none=True)

@router_book.get("/books")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    book = crud.get_books(db, skip, limit)
    return Response(status="OK", code=200, message="Books retrieved successfully", result=book)

@router_book.get("/{book_id}")
async def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status="OK", code=200, message="Book retrieved successfully", result=book)

@router_book.put("/{book_id}")
async def update_book(book_id: int, request: RequestBook, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id=request.parameter.id, title=request.parameter.title, 
            author=request.parameter.author, published_date=request.parameter.published_date, ISBN=request.parameter.ISBN)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status="OK", code=200, message="Book updated successfully", result=book)

@router_book.delete("/{book_id}")
async def delete_book(book_id: int, request: RequestBook,  db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id=request.parameter.id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Response(status="OK", code=200, message="Book deleted successfully", result=book)


# Association
# @router.post("/student/{student_id}/book/{book_id}")
# async def create_association(request:RequestAssociation, db:Session = Depends(get_db)):

# @router.get_books_by_student("/student/{student_id}/books")

# @router.get_students_by_book("book/{book_id}/students")