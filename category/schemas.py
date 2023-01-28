from datetime import date
from typing import Optional, Union
from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    name: str
   
class Category(CategoryBase):
    id: Optional[int]
    name: Optional[str]
    ingridients: object
    updated_at: Optional[date]
    created_at: Optional[date]
   

    class Config:
        orm_mode = True