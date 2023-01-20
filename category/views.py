from sqlalchemy.orm import Session
from . import models, schema as schemas

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_category_by_name(db: Session, name: str):
    return db.query(models.Category).filter(models.Category.name == name).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db: Session, data: schemas.CategoryCreate):
    db_category = models.Category(name=data.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category