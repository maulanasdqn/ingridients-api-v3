from fastapi import APIRouter, HTTPException, Depends

from . import schemas
from . import models as ingridient_models, views as crud
from config.database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate

ingridient_models.Base.metadata.create_all(bind=engine)

app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/ingridients/", response_model=schemas.Ingridient)
def create_ingridient(data: schemas.IngridientCreate, db: Session = Depends(get_db)):
    db_ingridient = crud.get_ingridient_by_name(db, name=data.name)
    if db_ingridient:
        raise HTTPException(status_code=400, detail="Ingridient already exist")
    return crud.create_ingridient(db=db, data=data)


@app.get("/ingridients/", response_model=Page[schemas.Ingridient])
def read_ingridients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ingridients = crud.get_ingridients(db, skip=skip, limit=limit)
    return paginate(ingridients)


@app.get("/ingridients/{ingridient_id}/", response_model=schemas.Ingridient)
def read_detail_ingridient(ingridient_id: int, db: Session = Depends(get_db) ):
    db_ingridient = crud.get_ingridient(db, ingridient_id=ingridient_id)
    if db_ingridient is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_ingridient
