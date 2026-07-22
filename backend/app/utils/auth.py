from  jose import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
# from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError
from fastapi import Depends, HTTPException, status  
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.user import User

SECRET_KEY = "your_super_secret_key_here"  # Replace with your
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time in minutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
       
    return jwt.encode(
        to_encode, 
        SECRET_KEY, 
        algorithm=ALGORITHM
        )
def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db)
    ):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, 
            SECRET_KEY, 
            algorithms=[ALGORITHM]
            )
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    current_user = db.query(User).filter(User.email == email).first()
    if current_user is None:
        raise credentials_exception
    return current_user