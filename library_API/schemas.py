from datetime import date
from pydantic import BaseModel

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True