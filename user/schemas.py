from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from role.schemas import PermissionRole
from typing import List, Union, Any
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 1
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY')

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt

class RoleBase(BaseModel):
    id: int
    name: str
    permissions: List[PermissionRole]

    
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    id: Optional[int]
    email: str
    fullname: Optional[str]
    roles: Optional[RoleBase]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class TokenPayload(BaseModel):
    exp: int
    sub: str

class UserCreate(UserBase):
    email: str
    password: str
    fullname: str

class UserLogin(UserBase):
    email: str
    password: str

class User(UserBase):
    id: int
    fullname: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True
