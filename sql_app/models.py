# SQLAlchemy models
from sql_app.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = 'Items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True,nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    on_offer = Column(Boolean, default=False)     

    # For visualization purposes
    def __repr__(self):
        return f"<Item {self.name}> price: {self.price} on_offer: {self.on_offer}"
    
class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True,nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False) 

    objects = relationship('Object', back_populates='owner')

    
class Object(Base):
    __tablename__ = 'Objects'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey('Users.id'), index=True)
    
    owner = relationship('User', back_populates='objects')
