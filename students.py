from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()

# class Students(BaseModel):
#     id: int 
#     first_name: str
#     last_name: str
#     dob: date
#     email: str

# class Books(BaseModel):
#     id: int 
#     title: str
#     author: str
#     publication_date: date
#     ISBN: str

# class StudentBook(BaseModel):
#     id: int
#     student_id: int (BaseModel)
#     book_id: int (BaseModel)
#     dateread: date