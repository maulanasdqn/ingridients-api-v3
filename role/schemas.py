from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    fullname: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
class PermissionBase(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class PermissionRole(BaseModel):
    id: Optional[int]
    permission : Optional[PermissionBase]
    is_active: Optional[bool]
    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    id: int
    name: str
    permissions: List[PermissionRole]
    users: List[UserBase]
    updated_at: Optional[date]
    created_at: Optional[date]

    #def dict(self, **kwargs):
    #    data = super(RoleBase, self).dict(**kwargs)
    #
    #    for a in data['permissions']:
    #        a['id'] = a['permission']['id']
    #        a['name'] = a['permission']['name']
    #        del a['permission']
    #
    #    return data

class RoleUser(BaseModel):
    id: int
    name: str
    permissions: object

class RoleCreate(RoleBase):
    name: str
   
class Role(RoleBase):
    id: Optional[int]
    name: Optional[str]
    updated_at: Optional[date]
    created_at: Optional[date]

    class Config:
        orm_mode = True
