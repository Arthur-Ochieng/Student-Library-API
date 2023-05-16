from fastapi import APIRouter, HTTPException, Path, Depends
from .database import SessionLocal
from sqlalchemy.orm import Session
from .schemas import StudentSchema, Request, Response, RequestStudent

from . import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create_student(request: RequestStudent,  db: Session = Depends(get_db)):
    crud.create_student(db, student=request.parameter)
    return Response(status="OK", code=200, message="Student created successfully").dict(exclude_none=True)

@router.get("/")
async def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return Response(status="OK", code=200, message="Students retrieved successfully", data=students)

@router.get("/{student_id}")
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return Response(status="OK", code=200, message="Student retrieved successfully", data=student)

@router.put("/update/{student_id}")
async def update_student(student_id: int, request: RequestStudent, db: Session = Depends(get_db)):
    student = crud.update_student(db, student_id, request.parameter)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return Response(status="OK", code=200, message="Student updated successfully", data=student)

@router.delete("/delete/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.delete_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return Response(status="OK", code=200, message="Student deleted successfully", data=student).dict(exclude_none=True)