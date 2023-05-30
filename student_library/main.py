# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.testclient import TestClient

# app = FastAPI()

# class Product(BaseModel):
#     name: str
#     price: float

# @app.get("/")
# async def index():
#     return {"message": "Hello World"}

# @app.post("/product", status_code=201)
# async def create_product(product_data: Product):
#     return {
#         "name": product_data.name,
#         "price": product_data.price
#     }

from fastapi import FastAPI
import models
from database import engine
from routes import router_book, router_stud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_stud, prefix="/students", tags=["students"])
app.include_router(router_book, prefix="/books", tags=["books"])