from sql_app.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Text


class Student(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String,index=True)
    last_name = Column(String,index=True)
    dob = Column(Date,index=True)
    email = Column(String, unique=True, index=True)
    # books = relationship("StudentBookAssociation", back_populates="stud_id")

class Book(Base):
    __tablename__ = 'Book'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String,index=True)
    author = Column(String,index=True)
    publication_date = Column(Date,index=True)
    ISBN = Column(String, unique=True, index=True)
    # students = relationship("StudentBookAssociation", back_populates="book_id")

class StudentBookAssociation(Base):
    __tablename__ = 'Studentbooks'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    stud_id = Column(Integer, ForeignKey('StudentsModel.Students.id', ondelete="CASCADE"), index=True, )
    book_id = Column(Integer, ForeignKey('BooksModel.Books.id', ondelete="CASCADE"), index = True)
    date_read = Column(Date, index=True)