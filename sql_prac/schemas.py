from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

# Model to be passed when creating a new user
class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
        # orm-mode will tell the pydantic model to read the data even if it is not a dict, but an ORM model.
        # this means that it can read data as id = data["id"] or id = data.id


# Pydantic models are used primarily for request and response bodies. That is 
# for data validation and serialization/deserialization. They do not have to mirror the
# database model exactly.