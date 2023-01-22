from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta
from role.schemas import PermissionRole
from typing import List

class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    access_expires: int = timedelta(minutes=5)
    refresh_expires: int = timedelta(hours=1)

class RoleBase(BaseModel):
    id: int
    name: str
    permissions: List[PermissionRole]

    def dict(self, **kwargs):
        data = super(RoleBase, self).dict(**kwargs)

        for a in data['permissions']:
            a['id'] = a['permission']['id']
            a['name'] = a['permission']['name']
            del a['permission']

        return data
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