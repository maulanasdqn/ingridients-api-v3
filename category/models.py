from sqlalchemy import Boolean, Column, Integer, String, DateTime, ColumnDefault
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import Base

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    ingridients = relationship("Ingridient")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())