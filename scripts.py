import sql_scripts as sc
import sqlite3
from class_dish import Dish
from class_user import User

connection = sqlite3.connect("first_version.db")
cursor = connection.cursor()


def getuser(id):
    cursor.execute(sc.users_sql_scripts_making_object, (id,))
    result0 = cursor.fetchall()
    result = result0[0]
    user = User(result[0], result[1], result[2], result[3], result[4])
    return user


def getdish(id):
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

def sql_update_user(user):
    cursor.execute(sc.users_sql_scripts_update_object,
                   (user.name, user.surname, user.age, user.love_dish_id, user.id))


def sql_update_dish(dish):
    cursor.execute(sc.dishes_sql_scripts_update_object,
                   (dish.name, dish.calories, dish.proteins, dish.fats, dish.carbos, dish.id))

def dishes_dict():
    cursor.execute(sc.dishes_sql_scripts_dishes_dict)
    result0 = cursor.fetchall()
    dishes_dict = dict()
    for i in range(len(result0)):
        dishes_dict[result0[i][0]] = i+1
    return dishes_dict