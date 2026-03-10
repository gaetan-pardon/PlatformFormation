

# create_access_token, get_current_user, verify_access_token
from fastapi import Cookie, HTTPException
from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import dotenv_values
import os


config = dotenv_values(".env")
SECRET_KEY = os.getenv('DOCKER_APP_SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = config["SECRET_KEY"]
ALGORITHM = os.getenv('DOCKER_APP_ALGORITHM')
if not ALGORITHM:
    ALGORITHM = config["ALGORITHM"]
TOKEN_EXPIRE_MINUTES = os.getenv('DOCKER_APP_TK_EX_MIN')
if not TOKEN_EXPIRE_MINUTES:
    TOKEN_EXPIRE_MINUTES = config["TOKEN_EXPIRE_MINUTES"]

def create_access_token(email: str):
    expire = datetime.now() + timedelta(minutes=int(TOKEN_EXPIRE_MINUTES))
    to_encode = {"sub": email, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise JWTError("Invalid token")
        return email
    except JWTError as e:
        raise JWTError(f"Token verification failed: {str(e)}")
    
def get_current_user(access_token: str=Cookie(None)):
    if access_token is None:
        raise HTTPException(status_code=401, detail="Access token missing")
    try:
        email = verify_access_token(access_token)
        return email
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Invalid access token: {str(e)}")