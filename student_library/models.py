from sqlalchemy import Column, String, Date, ForeignKey, Integer
from .database import Base
from uuid import UUID

class Student(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    # book_id = Column(Integer, ForeignKey('Book.id', ondelete="CASCADE"), index = True)

class Book(Base):   
    __tablename__ = 'Book'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_date = Column(Date,index=True, nullable=False)
    ISBN = Column(String, unique=True, index=True)
    # student_id = Column(Integer, ForeignKey('Student.id', ondelete="CASCADE"), index = True)

# class StudentBookAssociation(Base):
#     __tablename__ = 'StudentBookAssociation'

#     id = Column(Integer, primary_key=True, autoincrement=True, index=True)
#     student_id = Column(Integer, ForeignKey('StudentsModel.Students.id', ondelete="CASCADE"), index=True, )
#     book_id = Column(Integer, ForeignKey('BooksModel.Books.id', ondelete="CASCADE"), index = True)
#     date_read = Column(Date)


    # UUID