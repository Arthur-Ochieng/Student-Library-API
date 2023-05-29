from fastapi import FastAPI
import models
from database import engine
from routers import students, books

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(students.router)
app.include_router(books.router)
