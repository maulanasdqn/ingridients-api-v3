from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    name: str
   
class Role(RoleBase):
    id: Optional[int]
    name: Optional[str]
    permission: object
    users: object
    updated_at: Optional[date]
    created_at: Optional[date]

    class Config:
        orm_mode = True