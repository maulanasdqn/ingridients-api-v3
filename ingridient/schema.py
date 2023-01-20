from datetime import date
from typing import List
from pydantic import BaseModel
from category.schema import Category

class IngridientBase(BaseModel):
    name: str
    qty: int
    weight: int
    price: int

class IngridientCreate(IngridientBase):
    name: str
    qty: int
    weight: int
    price: int
    categories: int

class Ingridient(IngridientBase):
    id: int
    name: str
    qty: int
    weight: int
    price: int
    categories: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True