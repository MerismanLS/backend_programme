import sqlite3
import sql_scripts as sc
import scripts

connection = sqlite3.connect("first_version.db")
cursor = connection.cursor()

if __name__ == "__main__":
    # USER
    cursor.execute(sc.users_sql_scripts_creating)
    # DISH
    cursor.execute(sc.dishes_sql_scripts_creating)

    # cursor.execute(sc.users_sql_scripts_insert, ("Максим", "Осипов", 23, ))
    # cursor.execute(sc.dishes_sql_scripts_insert, ("Блины",))
    # cursor.execute(sc.dishes_sql_scripts_insert, ("Пельмени",))
    # cursor.execute(sc.dishes_sql_scripts_insert, ("Окрошка",))

    print(scripts.getuser(connection, 1).love_dish_id)

    print(scripts.dishes_dict(connection))

connection.commit()
connection.close()
