from fastapi import APIRouter, HTTPException, Depends 
from user import models as user_models, views as crud
from config.database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate
from user import schemas
from helper.main import Hasher
from sqlalchemy import inspect
from helper.main import JWTBearer

user_models.Base.metadata.create_all(bind=engine)

app = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/auth/register/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post('/auth/login/', summary="Create access and refresh tokens for user")
async def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_email = crud.get_user_by_email(db, email=user.email)
    if not db_email:
        raise HTTPException(status_code=404,detail="User not found")

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}

    query_db = db.query(user_models.User).filter(user_models.User.email==user.email).one()
    password = object_as_dict(query_db).get("hashed_password")

    if not Hasher.verify_password(user.password, password):
        raise HTTPException(status_code=401,detail="Wrong password")

    return {
        "token": {
          "access_token": schemas.create_access_token(user.email),
          "refresh_token": schemas.create_refresh_token(user.email),
        },
        "user": db_email
    }


@app.get("/users/", response_model=Page[schemas.User], dependencies=[Depends(JWTBearer())])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return paginate(users)


@app.get("/users/{user_id}", response_model=schemas.User, dependencies=[Depends(JWTBearer())])
def read_user(user_id: int, db: Session = Depends(get_db)):
    print(JWTBearer)
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/me", response_model=schemas.User, dependencies=[Depends(JWTBearer())])
def read_user_me(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

