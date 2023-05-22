from datetime import date
from pydantic import BaseModel

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    date_of_birth: date
    
class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    
    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    author: str
    ISBN: str
    
class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    
    class Config:
        orm_mode = True


class StudentBookBase(BaseModel):
    date_read: date

class StudentBookCreate(StudentBookBase):
    pass

class StudentBook(StudentBookBase):
    id: int
    stud_id:  int
    book_id: int

    class Config:
        orm_mode = True