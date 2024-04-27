users_sql_scripts_creating = """
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER NOT NULL,
    love_dish_id INTEGER,
    FOREIGN KEY (love_dish_id) REFERENCES Dishes (id)
    )
"""

dishes_sql_scripts_creating = """
    CREATE TABLE IF NOT EXISTS Dishes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    calories INTEGER,
    proteins INTEGER,
    fats INTEGER,
    carbohydrates INTEGER 
    )
"""
# последние четыре поля могут быть пустыми,
# их пользователь по желанию заполнит

users_sql_scripts_insert = """
    INSERT INTO Users (name, surname, age) VALUES (?,?,?)
"""

dishes_sql_scripts_insert = """
    INSERT INTO Dishes (name) VALUES (?)
"""

users_sql_scripts_making_object = """
    SELECT * FROM Users WHERE id = ?
"""

dishes_sql_scripts_making_object = """
    SELECT * FROM Dishes WHERE id = ?
"""

users_sql_scripts_update_object = """
    UPDATE Users SET name = ?, surname = ?, age = ?, love_dish_id = ? WHERE id = ?
"""

dishes_sql_scripts_update_object = """
    UPDATE Dishes SET name = ?, calories = ?, proteins = ?,
           fats = ?, carbos = ? WHERE id = ?
"""

dishes_sql_scripts_dishes_dict = """
    SELECT (name) FROM Dishes
"""

users_sql_scripts_getting_everything = """
    SELECT * FROM Users
"""