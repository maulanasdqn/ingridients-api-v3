from config.database import engine
from user import models as user_models
from role import models as role_models
from category import models as category_models
from ingridient import models as ingridient_models

user_models.Base.metadata.create_all(bind=engine)
role_models.Base.metadata.create_all(bind=engine)
category_models.Base.metadata.create_all(bind=engine)
ingridient_models.Base.metadata.create_all(bind=engine)