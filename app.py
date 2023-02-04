from fastapi import FastAPI
from user import urls as user_urls
from ingridient import urls as ingridient_urls
from category import urls as category_urls
from role import urls as role_urls
from fastapi_pagination import add_pagination

app = FastAPI()

app.include_router(user_urls.app,tags=['users'])
app.include_router(role_urls.app,tags=['roles'])
app.include_router(ingridient_urls.app,tags=['ingridients'])
app.include_router(category_urls.app,tags=['categories'])

add_pagination(app)



