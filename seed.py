from config.database import engine
from sqlalchemy.orm import Session
from role.models import Role
from permission.models import Permission
from user.models import User
from helper.main import Hasher
from permission.models import PermissionRoles
import getopt, sys

argumentList = sys.argv[1:]
options = "rpus:"
long_options = ["role", "permission", "user", "permission-roles"]

def seed_permission_roles():
    with Session(bind=engine) as session:
        ReadIngridientPermission = PermissionRoles(role_id=1, permission_id=1)
        ReadCategoryPermission = PermissionRoles(role_id=1, permission_id=2)
        ReadUserPermission = PermissionRoles(role_id=1, permission_id=3)

        session.add_all([ReadCategoryPermission, ReadIngridientPermission, ReadUserPermission])
        session.commit()

def seed_role():
    with Session(bind=engine) as session:
        admin = Role(name="Admin")
        staff = Role(name="Staff")
        employee = Role(name="Employee")

        session.add_all([admin, staff, employee])
        session.commit()

def seed_permission():
    with Session(bind=engine) as session:
        ReadIngridient = Permission(name="Read Ingridient")
        ReadCategory = Permission(name="Read Category")
        ReadUser = Permission(name="Read User")

        session.add_all([ReadIngridient, ReadCategory, ReadUser])
        session.commit()

def seed_user():
    with Session(bind=engine) as session:
        admin = User(fullname="Admin", email="admin@admin.com", role_id=1, hashed_password=Hasher.get_password_hash("admin123"))
        staff = User(fullname="Staff", email="staff@staff.com", role_id=2, hashed_password=Hasher.get_password_hash("staff123"))
        employee = User(fullname="Employee", email="employee@employee.com", role_id=3, hashed_password=Hasher.get_password_hash("employee123"))

        session.add_all([admin, staff, employee])
        session.commit()

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-r", "--role"):
            print("Generate Role...")
            seed_role()
            print("Success Generate Role!")
             
        elif currentArgument in ("-p", "--permission"):
            print ("Generate Permission...")
            seed_permission()
            print("Success Generate Permission!")
             
        elif currentArgument in ("-u", "--user"):
            print ("Generate User...")
            seed_user()
            print("Success Generate User!")

        elif currentArgument in ("-s", "--permission-roles"):
            print ("Generate Permission Roles...")
            seed_permission_roles()
            print("Success Generate Permission Roles!")
             
except getopt.error as err:
    print (str(err))