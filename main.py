# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only use for development.

from fastapi import FastAPI, Path, Query, Body
from enum import Enum
from typing import Optional, Annotated
from pydantic import BaseModel, Field


app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     # Declaring the type of variable would help with error checks and completions
#     return{"item_id": item_id}


# Path operations are evaluated in order
# In this case, /users/me should be declared before /users/{user_id}
# Path for user id might match thinking that it received "me" as an argument
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# You also cannot redefine a path operation once declared, the first match will always run
# Enums are used when you want to predefine your parameters in your operation
class ModelName(str, Enum):
    # This means that you create a class that inherits from str and enum
    arthur = "arthur"
    john = "john"
    ochieng = "ochieng"

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.arthur:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "john":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# You can pass a path as a parameter of another path operation
@app.get("/files/{files_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Query parameters - Function parameters that are not part of the path parameters
# Query id the set of key-value that go after the ? inthe url. separated by & characters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# You can create query params which are of type bool and are still optional
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Request body - The data sent in the body of the request by the client to your API
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item.update({"price_with_tax": price_with_tax})
    return item_dict

# Request body, path and query parameters at the same time
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# Annotated is used to add metadata to your parameters
# The main purpose for annotations is for validation when the api is retrieving data
# You can also add metadata to your path parameters
# You can perform number validations for type int or float for both path and query parameters
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title = "The ID of the item to get", ge = 1)],
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
    size: Annotated[float | None, Query(gt = 0, lt = 10)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Declarig body parameters to be optional
# Annotations for body params too
@app.put("items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title = "The ID of the item to get", ge = 1)],
    user: User,
    item: Item,
    importance: Annotated[int, Body(gt =0)],
    q: Optional[str] = None,
):
    results = {"item_id": item_id}
    if q: 
        results.update({"q": q})
    if item:    
        results.update({"item": item})
    return results




# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal