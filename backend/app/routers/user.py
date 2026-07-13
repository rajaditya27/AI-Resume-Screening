from fastapi import Depends, APIRouter
from app.schemas.user_schema import UserCreate
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user_schema import UserCreate
from app.models.user import User        


router = APIRouter()
@router.post("/register")
# def register(user: UserCreate):
#     return{
#         "message": "User registration API Working",
#         "name": user.name,
#         "email": user.email
#     }
@router.post("/register")
def register(user: UserCreate,db: Session = Depends(get_db)):
    new_user=User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return{
        "message": "User registration API Working",
        "id" : new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }