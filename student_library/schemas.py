from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from datetime import date

T = TypeVar('T')

# Student
class StudentSchema(BaseModel):
    id: int
    first_name: Optional [str] = None
    last_name: Optional [str] = None
    dob: Optional [date] = None 
    email: Optional [str] = None
    class Config:
        orm_mode = True
class RequestStudent(BaseModel):
    parameter: StudentSchema = Field(...)

# Books
class BookSchema(BaseModel):
    id: int
    title: Optional [str] = None
    author: Optional [str] = None
    published_date: Optional [date] = None 
    ISBN: Optional [str] = None
    class Config:
        orm_mode = True 

class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)

# Association

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
