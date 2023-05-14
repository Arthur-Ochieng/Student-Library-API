# SQLAlchemy models
from database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship

class StudentModel(Base):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String,index=True)
    last_name = Column(String,index=True)
    dob = Column(Date,index=True)
    Email = Column(String, unique=True, index=True)
    books = relationship("StudentBookAssociation", back_populates="stud_id")

class BookModel(Base):
    __tablename__ = 'Book'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String,index=True)
    author = Column(String,index=True)
    publication_date = Column(Date,index=True)
    ISBN = Column(String, unique=True, index=True)
    students = relationship("StudentBookAssociation", back_populates="book_id")

class StudentBookAssociation(Base):
    __tablename__ = 'Studentbooks'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    stud_id = Column(Integer, ForeignKey('StudentsModel.Students.id'), index=True)
    book_id = Column(Integer, ForeignKey('BooksModel.Books.id'), index = True)
    date_read = Column(Date, index=True)

class Item(Base):
    __tablename__ = 'Items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True,nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    on_offer = Column(Boolean, default=False)     

    def __repr__(self):
        return f"<Item {self.name}> price: {self.price} on_offer: {self.on_offer} "