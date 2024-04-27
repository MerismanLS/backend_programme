import database.data.db_functions as db

class CarDataLogic:
    @staticmethod
    def get_all(connection):
        return db.get_all(connection)

    @staticmethod
    def get_by_id(connection):
        pass