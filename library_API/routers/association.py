from fastapi import APIRouter, HTTPException, Depends
import schemas, crud
from sqlalchemy.orm import Session
from dependencies import get_db

router = APIRouter(
    prefix="/association",
    tags=["association"],
    responses={404: {"description": "Not found"}},
)  

@router.post("/student/{student_id}/book/{book_id}", response_model=schemas.Association)
def create_associations(student_id: int, book_id: int, association: schemas.AssociationCreate, db: Session = Depends(get_db)):
    _student = crud.get_student(db, student_id)
    _book = crud.get_book(db, book_id)
    if _student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    if _book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if crud.get_association(db, student_id=student_id, book_id=book_id) is not None:
        raise HTTPException(status_code=400, detail="Association already exists")
    return crud.create_association(db, association=association)

@router.get("/student/{student_id}/books", response_model=list[schemas.Book])
def get_books_by_student(student_id: int, db: Session = Depends(get_db)):
    _student = crud.get_student(db, student_id)
    if _student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    association = crud.get_books_by_student(db, student_id=student_id)
    return association

@router.get("/book/{book_id}/students", response_model=list[schemas.Student])
def get_students_by_book(book_id: int, db: Session = Depends(get_db)):
    _book = crud.get_book(db, book_id)
    if _book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    association = crud.get_students_by_book(db, book_id=book_id)
    return association