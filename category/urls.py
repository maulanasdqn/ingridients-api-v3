from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT

from . import schemas
from . import models as category_models, views as crud
from config.database import SessionLocal, engine
from sqlalchemy.orm import Session

category_models.Base.metadata.create_all(bind=engine)

app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/categories/", response_model=schemas.Category)
def create_category(data: schemas.CategoryCreate, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.fresh_jwt_required()
    current_user = Authorize.get_raw_jwt()
    db_category = crud.get_category_by_name(db, name=data.name)

    if current_user['role'] != 1:
        raise HTTPException(status_code=403, detail="You dont have acces to create category")

    if db_category:
        raise HTTPException(status_code=400, detail="Category already exist")


    return crud.create_category(db=db, data=data)

@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(Authorize: AuthJWT = Depends(), skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Authorize.fresh_jwt_required()
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories

@app.get("/categories/{category_id}/", response_model=schemas.Category)
def read_detail_category(category_id: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends(),):
    Authorize.fresh_jwt_required()
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category