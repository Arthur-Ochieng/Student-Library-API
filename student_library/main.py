from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.post("/product", status_code=201)
async def create_product(product_data: Product):
    return {
        "name": product_data.name,
        "price": product_data.price
    }