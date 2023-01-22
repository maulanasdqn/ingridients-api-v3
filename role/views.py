from sqlalchemy.orm import Session

from . import schemas
from . import models

def get_role(db: Session,role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()

def get_role_by_name(db: Session, name: str):
    return db.query(models.Role).filter(models.Role.name == name).first()

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Role).offset(skip).limit(limit).all()

def create_role(db: Session, data: schemas.RoleCreate):
    db_role = models.Role(name=data.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role