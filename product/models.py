from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, ColumnDefault
from datetime import datetime

from config.database import Base
from ingridient import models

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(String)
    category = Column(ForeignKey("categories.id"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())