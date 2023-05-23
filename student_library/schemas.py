from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from datetime import date

T = TypeVar('T')

# Student
class StudentSchema(BaseModel):
    id: int
    first_name: str 
    last_name: str 
    date_of_birth:  date
    email: str
    # book_id: int
    class Config:
        orm_mode = True

class RequestStudent(BaseModel):
    parameter: StudentSchema = Field(...)

# class UpdateStudent(BaseModel):
#     first_name: Optional[str]
#     last_name: Optional[str]
#     date_of_birth: Optional[date]
#     email: Optional[str]

# Books
class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    published_date: date 
    ISBN: str
    # student_id: int 
    class Config:
        orm_mode = True 

class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)

# class UpdateBook(BaseModel):
#     title: Optional[str]
#     author: Optional[str]
#     published_date: Optional[date]
#     ISBN: Optional[str]

# Association
class AssociationSchema(BaseModel):
    id: int
    student_id: int
    book_id: int
    date_read: date
    class Config:
        orm_mode = True

class RequestAssociation(BaseModel):
    parameter: AssociationSchema = Field(...)



class Request(GenericModel, Generic[T]):
    parameter: T = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
