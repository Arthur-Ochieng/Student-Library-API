from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:78@localhost:5432/Student_Library_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()