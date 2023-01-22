from sqlalchemy.orm import Session

from . import schemas
from . import models

def get_ingridient(db: Session, ingridient_id: int):
    return db.query(models.Ingridient).filter(models.Ingridient.id == ingridient_id).first()


def get_ingridient_by_name(db: Session, name: str):
    return db.query(models.Ingridient).filter(models.Ingridient.name == name).first()


def get_ingridients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ingridient).offset(skip).limit(limit).all()


def create_ingridient(db: Session, data: schemas.IngridientCreate):
    db_ingridient = models.Ingridient(
        name=data.name,
        weight=data.weight,
        qty=data.qty,
        price=data.price,
        category_id=data.category_id
        )
    db.add(db_ingridient)
    db.commit()
    db.refresh(db_ingridient)
    return db_ingridient