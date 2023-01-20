from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from category.models import Category
from config.database import Base

class Ingridient(Base):
    __tablename__ = "ingridient"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    qty = Column(Integer, unique=False, index=True)
    weight = Column(Integer)
    price = Column(Integer, unique=False)
    categories = Column(Integer, ForeignKey(Category.id))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())