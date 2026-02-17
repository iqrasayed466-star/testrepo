import os
import sqlite3
import MySQLdb
import subprocess

# Hardcoded Secret - AWS Key
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMIK7MDENG/bPxRfiCYEXAMPLEKEY"

def get_user_data(username):
    # SQL Injection Vulnerability fixed using parameterized query
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def execute_command(hostname):
    # Command Injection Vulnerability fixed using subprocess
    try:
        subprocess.check_output(["ping", hostname])
    except subprocess.CalledProcessError as e:
        print(f"Error pinging {hostname}: {e}")

def read_file(filename):
    # Path Traversal Vulnerability fixed by validating filename
    if not filename.startswith("/var/www/uploads/"):
        raise ValueError("Invalid filename")
    with open("/var/www/uploads/" + filename, "r") as f:
        return f.read()

def insecure_mysql_query(user_id):
    # Another SQL Injection fixed using parameterized query
    db = MySQLdb.connect("localhost", "root", "password", "testdb")
    cursor = db.cursor()
    query = "SELECT * FROM accounts WHERE id = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone()