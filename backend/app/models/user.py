from app.database.database import Base
from datetime import datetime,timezone
from sqlalchemy import Column, Integer, String,DateTime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    password = Column(String,nullable=False)
    created_at = Column(
        DateTime(timezone=True), 
        default=lambda:datetime.now(timezone.utc)
    )
    updated_at = Column(
    DateTime(timezone=True),
    default=lambda: datetime.now(timezone.utc),
    onupdate=lambda: datetime.now(timezone.utc)
    )