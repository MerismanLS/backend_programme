import sql_scripts
import sqlite3
from database.data.models.Dish import Dish
from database.data.models.User import User


def get_all(connection: sqlite3.Connection) -> list[Dish]:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.dishes_sql_script_select_all)
        value: list[tuple] = cursor.fetchall()
        dishes: list[Dish] = []

        for data in value:
            dish = Dish.of(data)
            dishes.append(dish)

        return dishes
    except Exception as e:
        print(e)
        return []


def insert(connection: sqlite3.Connection, dish: Dish) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.dishes_sql_script_insert, dish.to_data())
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_all(connection: sqlite3.Connection) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.dishes_sql_script_delete_all)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_by_id(connection: sqlite3.Connection, dish_id: int) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.dishes_sql_script_delete_by_id, (dish_id,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
