from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, ColumnDefault
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base

class PermissionRoles(Base):
    __tablename__ = 'permission_roles'
    role_id = Column(ForeignKey('roles.id'), primary_key=True)
    permission_id = Column(ForeignKey('permissions.id'), primary_key=True)
    role = relationship("Role", back_populates="permissions")
    permission = relationship("Permission", back_populates="roles")
    is_active = Column(Boolean, default=True)

class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    roles = relationship("PermissionRoles", back_populates="permission")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())