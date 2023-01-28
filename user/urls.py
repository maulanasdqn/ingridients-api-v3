from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from helper.main import Hasher
from user import models as user_models, views as crud
from config.database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy import inspect

from user import schemas

user_models.Base.metadata.create_all(bind=engine)

app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/auth/login')
def login(user: schemas.UserLogin, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    db_email = crud.get_user_by_email(db, email=user.email)

    if not db_email:
        raise HTTPException(status_code=401,detail="User not found")

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

    get_email = db.query(user_models.User).filter(user_models.User.email==user.email).one()
    password = object_as_dict(get_email).get("hashed_password")

    if not Hasher.verify_password(user.password, password):
        raise HTTPException(status_code=401,detail="Wrong password")

    data_claims = {"role": object_as_dict(get_email).get("role_id")}

    access_token = Authorize.create_access_token(subject=user.email,  user_claims=data_claims, fresh=True)
    refresh_token = Authorize.create_refresh_token(subject=user.email, user_claims=data_claims)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
        }

@app.post('/auth/refresh/')
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_raw_jwt()
    data_claims = {"role": current_user["role"]}
    new_access_token = Authorize.create_access_token(subject=current_user["sub"], user_claims=data_claims,fresh=True)
    new_refresh_token = Authorize.create_refresh_token(subject=current_user["sub"], user_claims=data_claims)
    return {"access_token": new_access_token, "refresh_token": new_refresh_token}

@app.get('/users/me/', response_model=schemas.User)
def user(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.fresh_jwt_required()
    current_user = Authorize.get_raw_jwt()
    return crud.get_user_by_email(db=db, email=current_user["sub"])

@app.post("/auth/register/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(Authorize: AuthJWT = Depends(), skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Authorize.fresh_jwt_required()
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db), Authorize: AuthJWT = Depends(),):
    Authorize.fresh_jwt_required()
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user