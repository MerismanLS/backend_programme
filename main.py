import sqlite3


connection = sqlite3.connect("first_version.db")
cursor = connection.cursor()

if __name__ == "__main__":
    pass

connection.commit()
connection.close()
