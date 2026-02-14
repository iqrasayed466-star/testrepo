import os
import sqlite3
import MySQLdb

# Hardcoded Secret - AWS Key
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMIK7MDENG/bPxRfiCYEXAMPLEKEY"

def get_user_data(username):
    # SQL Injection Vulnerability
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    return cursor.fetchall()

def execute_command(hostname):
    # Command Injection Vulnerability
    os.system("ping " + hostname)

def read_file(filename):
    # Path Traversal Vulnerability
    with open("/var/www/uploads/" + filename, "r") as f:
        return f.read()

def insecure_mysql_query(user_id):
    # Another SQL Injection
    db = MySQLdb.connect("localhost", "root", "password", "testdb")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE id = {user_id}")
    return cursor.fetchone()
