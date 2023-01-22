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

class UserLogin(UserBase):
    email: str
    password: str


class User(UserBase):
    id: int
    fullname: str
    email: str
    roles: object
    is_active: bool

    class Config:
        orm_mode = True