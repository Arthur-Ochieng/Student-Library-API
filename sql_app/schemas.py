# Pydantic models
from pydantic import BaseModel

class ObjectBase(BaseModel):
    title: str
    description: str | None = None

class ObjectCreate(ObjectBase):
    pass

class Object(ObjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_admin: bool
    objects: list[Object] = []

    class Config:
        orm_mode = True