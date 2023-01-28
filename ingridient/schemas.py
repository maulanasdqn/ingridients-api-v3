from datetime import date
from pydantic import BaseModel
from category.schemas import Category

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
    category_id: int

class Ingridient(IngridientBase):
    id: int
    name: str
    qty: int
    weight: int
    price: int
    categories: Category
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True