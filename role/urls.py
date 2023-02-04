from fastapi import APIRouter, HTTPException, Depends
from . import schemas
from . import models as role_models, views as crud
from config.database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate

role_models.Base.metadata.create_all(bind=engine)

app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/roles/", response_model=schemas.Role)
def create_role(data: schemas.RoleCreate, db: Session = Depends(get_db)):
    db_role = crud.get_role_by_name(db, name=data.name)

    if db_role:
        raise HTTPException(status_code=400, detail="Role already exist")


    return crud.create_role(db=db, data=data)

@app.get("/roles/", response_model=Page[schemas.Role])
def read_roles( skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.get_roles(db, skip=skip, limit=limit)
    return paginate(roles)

@app.get("/roles/{role_id}/", response_model=schemas.Role)
def read_detail_role(role_id: int, db: Session = Depends(get_db)):
    db_role = crud.get_role(db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role
