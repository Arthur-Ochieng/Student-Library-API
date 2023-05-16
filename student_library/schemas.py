from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from datetime import date

T = TypeVar('T')

class StudentSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: date
    email: str
    class Config:
        orm_mode = True

class RequestStudent(BaseModel):
    parameter: StudentSchema = Field(...)

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]