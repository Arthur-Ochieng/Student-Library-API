from fastapi import FastAPI, Path, HTTPException, status
from pydantic import BaseModel

# Necessary when using optional parameters
# Pydantic is responsible for the data validation
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
    # Optional means that this parameter is not mandatory

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}

# This is type of a mandatory parameter
# It is a path parameter
@app.get("/inventory/{item_id}")
def get_item(item_id: int = Path(description = "The ID of the item to get", gt = 0)):
    return inventory[item_id]

# Query Parameters
# This is an optional parameter, but test is a mandatory parameter
@app.get("/get-by-name")
def get_item(*, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id].name== name:
            return inventory[item_id]
    # return {"Data": "Not Found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

# When looking for sumn that is neither a path nor a query parameter, you need to set it equal to a class that inherits from the base model
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        # return {"Error": "Item ID already exists"}
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item ID already exists")
    inventory[item_id] = item
    return inventory[item_id]

# Updating an item
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        # return {"Error": "Item ID does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist")
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

# Deleting an item
@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        # return {"Error": "Item ID does not exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID does not exist")
    del inventory[item_id]
    return {"Success": "Item deleted"}