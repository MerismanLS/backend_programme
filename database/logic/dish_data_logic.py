import database.data.db_functions as db
from database.data.models.Dish import Dish

class DishDataLogic:
    @staticmethod
    def get_all(connection) -> list[Dish]:
        return db.get_all(connection)

    @staticmethod
    def get_by_id(connection, dish_id: int) -> Dish:
        dishes = DishDataLogic.get_all(connection)
        for dish in dishes:
            if dish.id == dish_id:
                return dish

        return None

    @staticmethod
    def insert(connection, dish: Dish) -> bool:
        if dish.calories < 0:
            return False

        if dish is None:
            return False
        return db.insert(connection, dish)

    @staticmethod
    def delete_all(connection) -> bool:
        return db.delete_all(connection)

    @staticmethod
    def delete_by_id(connection, dish_id: int):
        if dish_id < 0:
            return False
        return db.delete_by_id(connection, dish_id)
