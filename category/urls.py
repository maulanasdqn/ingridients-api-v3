from fastapi import APIRouter, HTTPException, Depends

from . import schemas
from . import models as category_models, views as crud
from config.database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate

category_models.Base.metadata.create_all(bind=engine)

app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/categories/", response_model=schemas.Category)
def create_category(data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_name(db, name=data.name)

    if db_category:
        raise HTTPException(status_code=400, detail="Category already exist")

    return crud.create_category(db=db, data=data)

@app.get("/categories/", response_model=Page[schemas.Category])
def read_categories( skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return paginate(categories)

@app.get("/categories/{category_id}/", response_model=schemas.Category)
def read_detail_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
