from config.database import engine
from user import models as user_models
from role import models as role_models
from permission import models as permission_models
from category import models as category_models
from ingridient import models as ingridient_models

print("Migrating User Models....")
user_models.Base.metadata.create_all(bind=engine)
print("Migrating Roles Models....")
role_models.Base.metadata.create_all(bind=engine)
print("Migrating Permission Models....")
permission_models.Base.metadata.create_all(bind=engine)
print("Migrating Category  Models....")
category_models.Base.metadata.create_all(bind=engine)
print("Migrating Ingridient Models....")
ingridient_models.Base.metadata.create_all(bind=engine)
print("Success Migrating All Models!")