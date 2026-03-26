import sqlite3

from database.db import get_connection

conection = get_connection()
cursor = conection.cursor()

def create_user(username, user_email, user_pass):
    cursor.execute("""INSERT INTO users
                   (username, user_email, user_password) VALUES
                   (?,?,?)""", (username, user_email, user_pass))

    conection.commit()


