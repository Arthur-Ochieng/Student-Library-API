# main: the file main.py (the Python "module").
# app: the object created inside of main.py with the line app = FastAPI().
# --reload: make the server restart after code changes. Only use for development.

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # Declaring the type of variable would help with error checks and completions
    return{"item_id": item_id}

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

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):  
#     if model_name is ModelName.arthur:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
#     if model_name == "john":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}
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