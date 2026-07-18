from  jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_super_secret_key_here"  # Replace with your
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time in minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
       
    return jwt.encode(
        to_encode, 
        SECRET_KEY, 
        algorithm=ALGORITHM
        )