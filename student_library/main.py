from fastapi import FastAPI
from . import models
from .database import engine
from .models import Student, Book
from .routes import router_book, router_stud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_stud, prefix="/students", tags=["students"])
app.include_router(router_book, prefix="/books", tags=["books"])