from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    fullname = Column(String, unique=False, index=True)
    hashed_password = Column(String)
    role = Column(Integer, unique=False)
    is_active = Column(Boolean, default=True)