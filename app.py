from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from user import urls as user_urls
from ingridient import urls as ingridient_urls
from category import urls as category_urls
from user.schema import Settings
from fastapi_jwt_auth.exceptions import AuthJWTException

app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

app.include_router(user_urls.app,tags=['users'])
app.include_router(ingridient_urls.app,tags=['ingridients'])
app.include_router(category_urls.app,tags=['categories'])


