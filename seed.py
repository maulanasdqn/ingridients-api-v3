from config.database import engine
from sqlalchemy.orm import Session
from role.models import Role
from permission.models import Permission
from user.models import User
from helper.main import Hasher
import getopt, sys

argumentList = sys.argv[1:]
options = "rpu:"
long_options = ["role", "permission", "user"]

def seed_role():
    with Session(bind=engine) as session:
        admin = Role(name="Admin")
        staff = Role(name="Staff")
        employee = Role(name="Employee")

        session.add_all([admin, staff, employee])
        session.commit()

def seed_permission():
    with Session(bind=engine) as session:
        ingridient = Permission(name="Ingridient")
        category = Permission(name="Category")
        user = Permission(name="User")

        session.add_all([ingridient, category, user])
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
             
except getopt.error as err:
    print (str(err))