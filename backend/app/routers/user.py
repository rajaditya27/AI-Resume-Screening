from fastapi import Depends, APIRouter,HTTPException,status
from app.schemas.user_schema import UserCreate,Userlogin
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user_schema import UserCreate
from app.models.user import User   
from app.utils.security import hash_password, verify_password 
from app.utils.auth import create_access_token


router = APIRouter()
# @router.post("/register")
# def register(user: UserCreate):
#     return{
#         "message": "User registration API Working",
#         "name": user.name,
#         "email": user.email
#     }
@router.post("/register",status_code=status.HTTP_201_CREATED)
def register(user: UserCreate,db: Session = Depends(get_db)):
    # Step1: Check duplicate email
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="Email already Exists")     
    hashed_password = hash_password(user.password)
    # Step 2: Create user object
    new_user=User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    # Step 3: Save to Database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return{
        "message": "User registration API Working",
        "id" : new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }

@router.post("/login")
def login(user: Userlogin, db: Session = Depends(get_db)):
    # Step 1: Check if user exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    # Step 2: Verify password
    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")
    
    access_token=create_access_token(
        data={"sub": existing_user.email}
        )
    
    #login successful
    return {
        "message": "Login successful",
        "name": existing_user.name,
        "email": existing_user.email,
        "access_token": access_token,
        "token_type": "bearer"
    }