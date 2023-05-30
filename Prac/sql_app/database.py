from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a database  
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:78@localhost:5432/Student_Library_db"   
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Connect session to our database
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
