# Each student should have a book id and each book should have its own student id
from sqlalchemy import Column, String, Date, ForeignKey, Integer
from database import Base
from uuid import UUID
from sqlalchemy.orm import relationship
import uuid

class Student(Base):
    __tablename__ = 'Student'

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    books = relationship("StudentBookAssociation", back_populates="students")

class Book(Base):   
    __tablename__ = 'Book'

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publication_date = Column(Date,index=True, nullable=False)
    ISBN = Column(String, unique=True, index=True)

    student = relationship("StudentBookAssociation", back_populates="books")

class StudentBookAssociation(Base):
    __tablename__ = 'StudentBookAssociation'

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('Student.id', ondelete="CASCADE"), index=True, nullable=False)
    book_id = Column(Integer, ForeignKey('Book.id', ondelete="CASCADE"), index = True, nullable=False)
    students = relationship("Student", back_populates="books")
    books = relationship("Book", back_populates="student")
    date_read = Column(Date)


# Creating models using UUID
# class MyModel(Base):
#     __tablename__ = "my_models"

#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     name = Column(String, nullable=False)
