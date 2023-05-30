# from fastapi import FastAPI, Status ,Path, Query, Body
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, List
from sql_app.database import SessionLocal
import sql_app.models as models

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: int
    on_offer: bool

    # Serialize pydantic  models into json
    class Config:
        orm_mode = True

db = SessionLocal()

# Returns all the items
@app.get('/items', response_model = List[Item], status_code=status.HTTP_200_OK)
def get_all_items():
    items = db.query(models.Item).all()
    return items

# Gets a particular item
@app.get('/items/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item

# Creating a new item
@app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    db_item = db.query(models.Item).filter(models.Item.name == item.name).first()
    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")
    
    new_item = models.Item(
        name = item.name,
        description = item.description,
        price = item.price,
        on_offer = item.on_offer
    )
    db.add(new_item)
    db.commit()

    return new_item

# Modify a specific item
@app.put('/items/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def update_item(item_id:int, item: Item):
    item_to_update = db.query(models.Item).filter(models.Item.id == item_id).first()
    item_to_update.name = item.name
    item_to_update.price = item.price
    item_to_update.description = item.description
    item_to_update.on_offer = item.on_offer
    db.commit()
    return item_to_update

# Deleting an existing item
@app.delete('/items/{item_id}')
def delete_item(item_id:int):
    item_to_delete = db.query(models.Item).filter(models.Item.id == item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=404, detail="Item not found") 
    db.delete(item_to_delete)
    db.commit()         
    return item_to_delete