from sqlalchemy import Boolean, Column, Integer, String, DateTime, ColumnDefault
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base
from ingridient import models

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    ingridients = relationship("Ingridient", back_populates="categories")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())