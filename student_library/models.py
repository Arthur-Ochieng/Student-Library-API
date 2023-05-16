from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Student(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date,index=True)
    email = Column(String, unique=True, index=True)


# class Book(Base):
#     __tablename__ = 'Book'

#     id = Column(Integer, primary_key=True, autoincrement=True, index=True)
#     title = Column(String,index=True)
#     author = Column(String,index=True)
#     publication_date = Column(Date)
#     ISBN = Column(String, unique=True, index=True)