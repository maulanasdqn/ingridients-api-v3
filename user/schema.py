from typing import Optional
from pydantic import BaseModel
from datetime import timedelta

class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    access_expires: int = timedelta(minutes=5)
    refresh_expires: int = timedelta(hours=1)

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    email: str
    password: str
    fullname: str
    role: Optional[int] = 1

class UserLogin(UserBase):
    email: str
    password: str
    role: Optional[int]


class User(UserBase):
    id: int
    fullname: str
    email: str
    role: int
    is_active: bool

    class Config:
        orm_mode = True