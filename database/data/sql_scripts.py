users_sql_scripts_creating = """
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER NOT NULL,
    love_dish_id INTEGER,
    comments TEXT, 
    login TEXT NOT NULL,
    password TEXT NOT NULL
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
    carbos INTEGER 
    comments TEXT
    )
"""

dishes_sql_script_insert = """
    INSERT INTO Dishes (name, calories, proteins, fats, carbos, comments) VALUES (?, ?, ?, ?, ?, ?)
"""

dishes_sql_script_select_all = """
    SELECT * FROM Dishes
"""

dishes_sql_script_delete_all = """
    DELETE FROM Dishes
"""

dishes_sql_script_delete_by_id = """
    DELETE FROM Dishes WHERE id = ? 
"""

users_sql_script_insert = """
    INSERT INTO Users (name, surname, age, love_dish_id, comments, login, password) VALUES (?, ?, ?, ?, ?, ?, ?)
"""

users_sql_script_select_all = """
    SELECT * FROM Users
"""

users_sql_script_select_login = """
    SELECT login FROM Users
"""

users_sql_script_find_password = """
    SELECT password FROM Users WHERE login = ?
"""

users_sql_script_delete_all = """
    DELETE FROM Users
"""

users_sql_script_delete_by_id = """
    DELETE FROM Users WHERE id = ? 
"""