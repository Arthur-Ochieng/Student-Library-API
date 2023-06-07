from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import date
from uuid import UUID
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class AssociationBase(BaseModel):
    student_id: int
    book_id: int
    date_read: Optional[date]

class AssociationCreate(AssociationBase):
    pass

class AssociationUpdate(BaseModel):
    student_id: Optional[int]
    book_id: Optional[int]
    date_read: Optional[date]

class Association(AssociationBase):
    id: int

    class Config:
        orm_mode = True



class BookBase(BaseModel):
    title: str
    author: str
    publication_date: date
    ISBN: str

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    publication_date: Optional[date]
    ISBN: Optional[str]

class Book(BookBase):
    id: int
    # student: Optional[Student] = None

    class Config:
        orm_mode = True


        

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    email: str

class StudentCreate(StudentBase):
    hashed_password: str

class StudentUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[date]
    email: Optional[str]
    hashed_password: Optional[str]

class Student(StudentBase):
    id: int
    # books: list[Book] = []

    class Config:
        orm_mode = True

# class Request(GenericModel, Generic[T]):
#     parameter: T = Field(...)

# class Response(GenericModel, Generic[T]):
#     code: str
#     status: str
#     message: str
#     result: Optional[T]