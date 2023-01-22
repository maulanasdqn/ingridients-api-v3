from sqlalchemy import ARRAY, Boolean, Column, Integer, String, DateTime, ColumnDefault
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base
from user.models import User
from permission.models import Permission

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    permission = relationship(Permission, back_populates="roles")
    users = relationship(User, back_populates="roles")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())