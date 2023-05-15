from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import sql_app.crud as crud, sql_app.models as models, sql_app.schemas as schemas

# from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/{user_id}/objects/", response_model=schemas.Object)   
def create_objects_for_user(
    user_id: int, object: schemas.ObjectCreate, db: Session = Depends(get_db)):
    return crud.create_user_object(db=db, object=object, user_id=user_id)

@app.get("/objects/", response_model=list[schemas.Object])  
def read_(objects: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    objects = crud.get_objects(db, skip=objects, limit=limit)
    return objects