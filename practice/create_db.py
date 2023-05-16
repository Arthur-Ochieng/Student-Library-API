from sql_app.database import Base, engine
from sql_app.models import Item

print("Creating database ....")

Base.metadata.create_all(engine)