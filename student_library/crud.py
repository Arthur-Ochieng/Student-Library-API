from datetime import date
from sqlalchemy.orm import Session
from .models import Student, Book, StudentBookAssociation
from .schemas import StudentSchema, BookSchema

# Students
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

# How to create student without inputing the id(Autoincrement)
def create_student(db: Session, student: StudentSchema):
    _student = Student(email=student.email, first_name=student.first_name, last_name=student.last_name, dob= student.dob)
    db.add(_student)
    db.commit()
    db.refresh(_student)
    return _student

def update_student(db: Session, student_id: int, first_name: str, last_name: str, dob: date , email: str):
    _student = get_student(db = db, student_id = student_id)

    _student.first_name = first_name
    _student.last_name = last_name    
    _student.dob = dob
    _student.email = email

    db.commit()
    db.refresh(_student)
    return _student

def delete_student(db: Session, student_id: int):
    _student = get_student(db = db, student_id = student_id)
    db.delete(_student)
    db.commit()

# Books
def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: BookSchema):
    _book = Book(title=book.title, author=book.author, published_date=book.published_date, ISBN=book.ISBN)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book

def update_book(db: Session, book_id: int, title: str, author: str, published_date: date, ISBN: str):
    _book = get_book(db = db, book_id = book_id)

    _book.title = title
    _book.author = author
    _book.published_date = published_date
    _book.ISBN = ISBN

    db.commit()
    db.refresh(_book)
    return _book

def delete_book(db: Session, book_id: int):
    _book = get_book(db = db, book_id = book_id)
    db.delete(_book)
    db.commit()

# Association

# Associate a student with a book
# Endpoint: POST /students/{student_id}/books/{book_id}
# Parameters: Student ID, Book ID
# Response: JSON object with confirmation message
def create_association(db: Session, student_id: int, book_id: int):
    _student = get_student(db = db, student_id = student_id)
    _book = get_book(db = db, book_id = book_id)

    _student.append(_book)
    db.commit()
    db.refresh(_student)
    return _student


# Get books read by a student
# Endpoint: GET /students/{id}/books
# Parameters: Student ID
# Response: JSON array with book details
def get_books_by_student(db: Session, student_id: int):
    books = []
    student_books = db.query(StudentBookAssociation).filter(StudentBookAssociation.stud_id == student_id).all()
    for student_book in student_books:
        book = get_book(db=db, book_id=student_book.book_id)
        books.append(book)
    return books

    _student = get_student(db = db, student_id = student_id)
    # Establish the relationship between one student and all the books related to that id
    return _student.books


# Get students who have read a book
# Endpoint: GET /books/{id}/students
# Parameters: Book ID
# Response: JSON array with student details
def get_students_by_book(db: Session, book_id: int):
    _book = get_book(db = db, book_id = book_id)
    return _book.students