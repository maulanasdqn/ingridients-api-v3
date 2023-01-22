from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, ColumnDefault
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base

class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    role_id = Column(ForeignKey('roles.id'), default=None)
    roles = relationship("Role", back_populates="permission")
    is_update = Column(Boolean, default=False)
    is_create = Column(Boolean, default=False)
    is_delete = Column(Boolean, default=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())