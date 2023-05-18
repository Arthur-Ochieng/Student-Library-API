from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .database import Base

class Student(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    dob = Column(Date,index=True)
    email = Column(String, unique=True, index=True)

class Book(Base):
    __tablename__ = 'Book'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String)
    author = Column(String)
    published_date = Column(Date,index=True)
    ISBN = Column(String, unique=True, index=True)

class StudentBookAssociation(Base):
    __tablename__ = 'StudentBookAssociation'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    stud_id = Column(Integer, ForeignKey('StudentsModel.Students.id', ondelete="CASCADE"), index=True, )
    book_id = Column(Integer, ForeignKey('BooksModel.Books.id', ondelete="CASCADE"), index = True)
    date_read = Column(Date)


    # UUID