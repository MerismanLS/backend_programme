import database.data.db_functions_user as dbu
from database.data.models.User import User

class UserDataLogic:
    @staticmethod
    def get_all(connection) -> list[User]:
        return dbu.get_all(connection)

    @staticmethod
    def get_by_id(connection, user_id: int) -> User:
        users = UserDataLogic.get_all(connection)
        for user in users:
            if user.id == user_id:
                return user

        return None

    @staticmethod
    def insert(connection, user: User) -> bool:
        if user.age < 0:
            return False

        if user is None:
            return False
        return dbu.insert(connection, user)

    @staticmethod
    def delete_all(connection) -> bool:
        return dbu.delete_all(connection)

    @staticmethod
    def delete_by_id(connection, user_id: int):
        if user_id < 0:
            return False
        return dbu.delete_by_id(connection, user_id)
