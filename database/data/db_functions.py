import sql_scripts as sc
import sqlite3
from models.class_dish import Dish
from models.class_user import User


def get_all_user(connection):
    cursor = connection.cursor()
    cursor.execute(sc.users_sql_scripts_getting_everything)
    list_of_users = cursor.fetchall()
    return list_of_users


def getuser(connection: sqlite3.Connection, id: id):
    cursor = connection.cursor()
    cursor.execute(sc.users_sql_scripts_making_object, (id,))
    result0 = cursor.fetchall()
    result = result0[0]
    user = User.making_car_object(result)
    return user


def getdish(connection: sqlite3.Connection, id: id):
    cursor = connection.cursor()
    cursor.execute(sc.dishes_sql_scripts_making_object, (id,))
    result0 = cursor.fetchall()
    result = result0[0]
    dish = Dish(result[0], result[1], result[2], result[3], result[4], result[5])
    return dish


# юзер выбирает блюдо, которое желает изменить,
# затем перед ним открывается новое окно,
# а на бэкэнд передаётся id и создаётся объект этого блюда,
# с которым идёт дальнейшая работа
# пользователь что-то изменяет, а затем нажимает на кнопку подтверждения,
# которая будет изменять значения уже в бд

def sql_update_user(connection: sqlite3.Connection, user: User):
    try:
        cursor = connection.cursor()
        cursor.execute(sc.users_sql_scripts_update_object,
                       (User.getting_data(user)))
        return True
    except Exception:
        return False


def sql_update_dish(connection: sqlite3.Connection, dish: Dish):
    try:
        cursor = connection.cursor()
        cursor.execute(sc.dishes_sql_scripts_update_object,
                       (Dish.getting_data(dish)))
        return True
    except Exception:
        return False


def dishes_dict(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute(sc.dishes_sql_scripts_dishes_dict)
    result0 = cursor.fetchall()
    dishes_dict = dict()
    for i in range(len(result0)):
        dishes_dict[result0[i][0]] = i + 1
    return dishes_dict
