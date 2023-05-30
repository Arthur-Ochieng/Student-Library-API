from fastapi import APIRouter, HTTPException, Depends
from database import SessionLocal
from sqlalchemy.orm import Session
from schemas import Response, RequestStudent, RequestBook, RequestAssociation, StudentSchema, BookSchema
import crud

router_stud = APIRouter()
router_book = APIRouter()
router_association = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Know how you can partially update a model
# This must be done using put as indicated in the documentation
# Refer to body updates on the fast api documentation
# The same applies for deleting a record in model and being able to successfully see the status code and the return message

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
@router_association.post("/student/{student_id}/book/{book_id}")
async def create_associations(student_id: int, book_id: int, request:RequestAssociation, db:Session = Depends(get_db)):
    _student = crud.get_student(db, student_id)
    _book = crud.get_book(db, book_id)
    if _student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    if _book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    # if _student.id == _book.id:
    #     raise HTTPException(status_code=400, detail="Student and Book cannot be associated with the same id")
    if crud.get_association(db, student_id=request.parameter.student_id, book_id=request.parameter.book_id) is not None:
        raise HTTPException(status_code=400, detail="Association already exists")
    crud.create_association(db, association=request.parameter)
    return Response(status="OK", code=200, message="Association created successfully").dict(exclude_none=True)

@router_association.get("/student/{student_id}/books")
async def get_books_by_student(student_id: int, db: Session = Depends(get_db)):
    _books = crud.get_books_by_student(db, student_id)
    return Response(status="OK", code=200, message="Books retrieved successfully", result=_books)

@router_association.get("book/{book_id}/students")
async def get_students_by_book(book_id: int, db: Session = Depends(get_db)):
    _students = crud.get_students_by_book(db, book_id)
    return Response(status="OK", code=200, message="Students retrieved successfully", result=_students)