import sqlite3
import sql_scripts as sc

connection = sqlite3.connect("first_version.db")
cursor = connection.cursor()

# USER
cursor.execute(sc.users_sql_scripts_creating)
# DISH
cursor.execute(sc.dishes_sql_scripts_creating)

connection.commit()
connection.close()
