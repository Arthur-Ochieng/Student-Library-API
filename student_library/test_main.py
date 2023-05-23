from fastapi.testclient import TestClient
from fastapi import status
from .main import app

Client = TestClient(app = app)

def test_index():
    response = Client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}

def test_create_products():
    response = Client.post("/products", json = {"name": "Ugali", "price": "100"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"name": "Ugali", "price": "100"}