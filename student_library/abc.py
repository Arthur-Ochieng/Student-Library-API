from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router_book, router_stud, router_association

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_stud, prefix="/students", tags=["students"])
app.include_router(router_book, prefix="/books", tags=["books"])
app.include_router(router_association, prefix="/association", tags=["association"])