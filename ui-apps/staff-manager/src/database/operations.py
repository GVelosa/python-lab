import sqlite3

from database.db import get_connection

conection = get_connection()
cursor = conection.cursor()

def create_user(username, user_email, user_pass):
    cursor.execute("""INSERT INTO users
                   (username, user_email, user_password) VALUES
                   (?,?,?)""", (username, user_email, user_pass))

    conection.commit()

def consute_user():
    cursor.execute("""SELECT * FROM users""")
    users_account = cursor.fetchall()
    return users_account

def create_department(title, manager_id=None):
    cursor.execute("""INSERT INTO departments
                   (title, manager_id) VALUES
                   (?,?)""", (title, manager_id))
    
def consult_manager():
    cursor.execute("""SELECT name, manager_id FROM employees
                   WHERE is_manager == 1""")
    managers_ids = cursor.fetchall()
    return managers_ids

def create_jobs_title(title):
    cursor.execute("""INSERT INTO job_titles
                   (title)
                   (?)""", (title))
    
