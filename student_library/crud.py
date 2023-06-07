
from datetime import date
from sqlalchemy.orm import Session
from models import Student, Book,  StudentBookAssociation
from schemas import StudentSchema, BookSchema, AssociationSchema
from fastapi import Path, Query

# Students
# Retrieve one student 
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

# Retrieve all students
def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

# Create a student
def create_student(db: Session, student: StudentSchema):
    _student = Student(email=student.email, first_name=student.first_name, last_name=student.last_name, date_of_birth= student.date_of_birth)
    db.add(_student)
    db.commit()
    db.refresh(_student)
    return _student

# Update student's details
def update_student(db: Session, student_id: int, first_name: str, last_name: str, date_of_birth: date , email: str):
    _student = get_student(db = db, student_id = student_id)
    _student.first_name = first_name
    _student.last_name = last_name    
    _student.date_of_birth = date_of_birth
    _student.email = email

    db.commit()
    db.refresh(_student)
    return _student

# def update_student(db:Session, student_id: int, student: UpdateStudent):
#     _student = get_student(db = db, student_id = student_id)
    
#     if student_id not in Student.query.all():
#         return {"Error" : "Student not found"}
#     if student.first_name != None:
#         Student.query.filter_by(id=student_id).update({"first_name": student.first_name})
#     if student.last_name != None:
#         Student.query.filter_by(id=student_id).update({"last_name": student.last_name})
#     if student.date_of_birth != None:
#         Student.query.filter_by(id=student_id).update({"date_of_birth": student.date_of_birth})
#     if student.email != None:
#         Student.query.filter_by(id=student_id).update({"email": student.email})

#     db.commit()
#     db.refresh(Student.query.filter_by(id=student_id).first())
#     return Student.query.filter_by(id=student_id).first()

# Delete a student
def delete_student(db: Session, student_id: int):
    _student = get_student(db = db, student_id = student_id)
    db.delete(_student)
    db.commit()

# def delete_student(db: Session, student_id: int):
#     _student = get_student(db = db, student_id = student_id)
#     if student_id not in Student.query.all():
#         return {"Error" : "Student not found"}
#     Student.query.filter_by(id=student_id).delete()
#     db.commit()

# Books
# Retrieve a book
def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

# Retrieve all books
def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

# Create a book
def create_book(db: Session, book: BookSchema):
    _book = Book(title=book.title, author=book.author, published_date=book.published_date, ISBN=book.ISBN)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book

# Update the book's details
def update_book(db: Session, book_id: int, title: str, author: str, published_date: date, ISBN: str):
    _book = get_book(db = db, book_id = book_id)

    _book.title = title
    _book.author = author
    _book.published_date = published_date
    _book.ISBN = ISBN

    db.commit()
    db.refresh(_book)
    return _book

# Delete a book
def delete_book(db: Session, book_id: int):
    _book = get_book(db = db, book_id = book_id)
    db.delete(_book)
    db.commit()

# Association
def create_association(db: Session, association: AssociationSchema):
    _association = StudentBookAssociation(student_id=association.student_id, book_id=association.book_id, date_read=association.date_read)
    db.add(_association)
    db.commit()
    db.refresh(_association)
    return _association

def get_association(db: Session, student_id: int, book_id: int):
    return db.query(StudentBookAssociation).filter(StudentBookAssociation.student_id == student_id, StudentBookAssociation.book_id == book_id).first()

def get_books_by_student(db: Session, student_id: int):
    books = []
    student_books = db.query(StudentBookAssociation).filter(StudentBookAssociation.student_id == student_id).all()
    for student_book in student_books:
        book = get_book(db=db, book_id=student_book.book_id)
        books.append(book)
    return books

def get_students_by_book(db: Session, book_id: int):
    students = []
    book_students = db.query(StudentBookAssociation).filter(StudentBookAssociation.book_id == book_id).all()
    for book_student in book_students:
        student = get_student(db=db, student_id=book_student.student_id)
        students.append(student)
    return students
