from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

from app.database.config import DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# print("Databse engine created successfully")
# print(engine)

def get_db():  
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
