from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine  

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  


# Students
# Create Student
@app.post("/students/", response_model=schemas.Student)
def create_student(
    student_id:int, student: schemas.StudentCreate, db: Session = Depends(get_db)
):
    return crud.create_student(db=db, student_id=student_id, student=student)

# Get Student's details
@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# Get Students details
@app.get("/students", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

# Update a student's details // Not sure
@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(
    student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)
):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.update_student(db=db, student_id=student_id, student=student)

# Delete a student
@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.delete_student(db=db, student_id=student_id)



# Books
# Create a book
@app.post("/books/", response_model=schemas.Book)
def create_book(
    book_id:int, book: schemas.BookCreate, db: Session = Depends(get_db)
):
    return crud.create_book(db=db, book_id=book_id, book=book)

# Get a book's details
@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# Get books details
@app.get("/books", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

# Update a book's detail
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(
    book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)
):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db=db, book_id=book_id, book=book)

# Delete a book
@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.delete_book(db=db, book_id=book_id)


# StudentsBookAssociation
# Associate a student with a book

# Get books read by a student

# Get students who have read a book
# @app.get("/students/{student_id}/books", response_model=list[schemas.StudentBookAssociation])
# def read_student_books(student_id: int, db: Session = Depends(get_db)):
#     db