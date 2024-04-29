import sql_scripts
import sqlite3
from database.data.models.User import User


def get_all(connection: sqlite3.Connection) -> list[User]:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.users_sql_script_select_all)
        value: list[tuple] = cursor.fetchall()
        users: list[User] = []

        for data in value:
            user = User.of(data)
            users.append(user)

        return users
    except Exception as e:
        print(e)
        return []


def insert(connection: sqlite3.Connection, user: User) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.users_sql_script_insert, user.to_data())
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_all(connection: sqlite3.Connection) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.users_sql_script_delete_all)
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def delete_by_id(connection: sqlite3.Connection, user_id: int) -> bool:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_scripts.users_sql_script_delete_by_id, (user_id,))
        connection.commit()
        return True
    except Exception as e:
        print(e)
        return False


def getting_all_logins(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute(sql_scripts.users_sql_script_select_login)
    value: list[tuple] = cursor.fetchall()
    logins = []

    for data in value:
        logins.append(data)

    return logins


def checking_login(connection: sqlite3.Connection, login: str) -> bool:
    cursor = connection.cursor()
    cursor.execute(sql_scripts.users_sql_script_select_login)
    value: list[tuple] = cursor.fetchall()
    logins = []

    for data in value:
        logins.append(data)

    if login in logins:
        return True
    else:
        return False


def checking_password(connection: sqlite3.Connection, login: str, password: str) -> bool:
    cursor = connection.cursor()
    cursor.execute(sql_scripts.users_sql_script_find_password, login)
    value = cursor.fetchall()
    if value[0] == password:
        return True
    else:
        return False
