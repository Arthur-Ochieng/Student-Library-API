from fastapi import APIRouter, HTTPException, Depends
import schemas, crud
from sqlalchemy.orm import Session
from dependencies import get_db

router = APIRouter(
    prefix="/student",
    tags=["student"],
    responses={404: {"description": "Not found"}},
)    

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate,  db: Session = Depends(get_db)):
    return crud.create_student(db = db, student=student)

@router.get("/students", response_model=list[schemas.Student])
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _student = crud.get_students(db, skip=skip, limit=limit)
    return _student

@router.get("/{student_id}", response_model=schemas.Student)
def get_student(student_id: int, db: Session = Depends(get_db)):
    _student = crud.get_student(db, student_id=student_id)
    if _student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return _student

@router.put("/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    _student = crud.update_student(db, student_id, student)
    if _student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return _student

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    crud.delete_student(db=db, student_id=student_id)
    return {"message": "Student deleted successfully"}