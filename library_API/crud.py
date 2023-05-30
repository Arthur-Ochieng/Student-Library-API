from datetime import date
from sqlalchemy.orm import Session
import models, schemas
from fastapi import Path, Query

# Students
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    fake_hashed_password = student.hashed_password + "notreallyhashed"
    db_student = models.Student(email=student.email, first_name=student.first_name, last_name=student.last_name, date_of_birth= student.date_of_birth, hashed_password = fake_hashed_password)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(student_id: int, student: schemas.StudentUpdate, db: Session):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        if student.email:
            db_student.email = student.email
        if student.first_name:
            db_student.first_name = student.first_name
        if student.last_name:
            db_student.last_name = student.last_name
        if student.date_of_birth:
            db_student.date_of_birth = student.date_of_birth
        if student.hashed_password:
            db_student.hashed_password = student.hashed_password

        db.commit()
        db.refresh(db_student)
        return db_student

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student is None:
        raise Exception("Student not found")
    db.delete(db_student)
    db.commit()


# Books
def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author=book.author, publication_date=book.publication_date, ISBN=book.ISBN)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(book_id:int, book: schemas.BookUpdate, db: Session):
    db_book = get_book(db, book_id)
    if db_book: 
        if book.title:
            db_book.title = book.title
        if book.author:
            db_book.author = book.author
        if book.publication_date:
            db_book.publication_date = book.publication_date
        if book.ISBN:
            db_book.ISBN = book.ISBN
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book is None:
        raise Exception("Book not found")
    db.delete(db_book)
    db.commit()


# Association
def create_association(db: Session, association: schemas.AssociationCreate):
    db_association = models.StudentBookAssociation(student_id=association.student_id, book_id=association.book_id, date_read=association.date_read)
    db.add(db_association)
    db.commit()
    db.refresh(db_association)
    return db_association

def get_association(db: Session, student_id: int, book_id: int):
    return db.query(models.StudentBookAssociation).filter(models.StudentBookAssociation.student_id == student_id, models.StudentBookAssociation.book_id == book_id).first()

def get_books_by_student(db: Session, student_id: int):
    books = []
    student_books = db.query(models.StudentBookAssociation).filter(models.StudentBookAssociation.student_id == student_id).all()
    for student_book in student_books:
        book = get_book(db, student_book.book_id)
        books.append(book)
    return books

def get_students_by_book(db: Session, book_id: int):
    students = []
    book_students = db.query(models.StudentBookAssociation).filter(models.StudentBookAssociation.book_id == book_id).all()
    for book_student in book_students:
        student = get_student(db, book_student.student_id)
        students.append(student)
    return students



