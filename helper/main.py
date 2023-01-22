from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

class PermissionChecker():
    def check_role(role_id: int):
        pass

    def check_permission():
        pass

    def is_allowed(permission_id: bool):
        if permission_id:
            return True
        else:
            return False

    def attach_permission():
        pass

    def detach_permission():
        pass