from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT

from . import schemas
from . import models as role_models, views as crud
from config.database import SessionLocal, engine
from sqlalchemy.orm import Session

role_models.Base.metadata.create_all(bind=engine)

app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/roles/", response_model=schemas.Role)
def create_role(data: schemas.RoleCreate, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.fresh_jwt_required()
    current_user = Authorize.get_raw_jwt()
    db_role = crud.get_role_by_name(db, name=data.name)

    if current_user['role'] != 1:
        raise HTTPException(status_code=403, detail="You dont have acces to create role")

    if db_role:
        raise HTTPException(status_code=400, detail="Role already exist")


    return crud.create_role(db=db, data=data)

@app.get("/roles/", response_model=list[schemas.Role])
def read_roles(Authorize: AuthJWT = Depends(), skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Authorize.fresh_jwt_required()
    roles = crud.get_roles(db, skip=skip, limit=limit)
    return roles

@app.get("/roles/{role_id}/", response_model=schemas.Role)
def read_detail_role(role_id: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends(),):
    Authorize.fresh_jwt_required()
    db_role = crud.get_role(db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role