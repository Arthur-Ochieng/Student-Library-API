from sqlalchemy.orm import Session
import sql_app.models as models, sql_app.schemas as schemas

# Users
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first() 

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Objects
def get_objects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Object).offset(skip).limit(limit).all()

def create_user_object(db: Session, object: schemas.ObjectCreate, user_id: int):
    db_object = models.Object(**object.dict(), owner_id=user_id)
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

def get_object(db: Session, object_id: int):
    return db.query(models.Object).filter(models.Object.id == object_id).first()