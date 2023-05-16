from datetime import date
from sqlalchemy.orm import Session
from .models import Student
from .schemas import StudentSchema

# Students
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: StudentSchema):
    db_student = student(email=student.email, first_name=student.first_name, last_name=student.last_name, dob= student.dob)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, first_name: str, last_name: str, dob: date , email: str):
    db_student = get_student(db = db, student_id = student_id)

    db_student.first_name = first_name
    db_student.last_name = last_name    
    db_student.dob = dob
    db_student.email = email

    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db = db, student_id = student_id)
    db.delete(db_student)
    db.commit()
