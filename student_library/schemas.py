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
    dob:  date
    email: str
    class Config:
        orm_mode = True

class RequestStudent(BaseModel):
    parameter: StudentSchema = Field(...)
    # The field function sets the attribute as required



# Books
class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    published_date: date 
    ISBN: str
    class Config:
        orm_mode = True 

class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)



# Association
class AssociationSchema(BaseModel):
    id: int
    stud_id: int
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
