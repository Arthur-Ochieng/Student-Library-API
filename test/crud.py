from sqlalchemy.orm import Session
import models, schemas

# Students
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(email=student.email, first_name=student.first_name, last_name=student.last_name, dob= student.dob)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):
    return db.query(models.Student).filter(models.Student.id == student_id).update(student.__dict__)

def delete_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).delete()


# Books
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author=book.author, isbn=book.isbn, published_date=book.published_date)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    return db.query(models.Book).filter(models.Book.id == book_id).update(book.__dict__)

def delete_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).delete()


# StudentBookAssociation
def get_book_student_association(db: Session, student_id: int, book_id: int):
    return db.query(models.StudentBookAssociation).filter(models.StudentBookAssociation.student_id == student_id, models.StudentBookAssociation.book_id == book_id).first()

# CRUD Operations to get a book read by a student
def book_read_by_student(db: Session, student_id: int):
    return db.query(models.StudentBookAssociation).filter(models.StudentBookAssociation.student_id == student_id).all()

# CRUD Operations to get students who have read a book
def students_who_read_book(db: Session, book_id: int):
    return db.query(models.StudentBookAssociation).filter(models.StudentBookAssociation.book_id == book_id).all()