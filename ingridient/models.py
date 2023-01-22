from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base

class Ingridient(Base):
    __tablename__ = "ingridients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    qty = Column(Integer, unique=False, index=True)
    weight = Column(Integer)
    price = Column(Integer, unique=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    categories = relationship("Category", back_populates="ingridients")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())