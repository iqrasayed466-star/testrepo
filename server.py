from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# PROBLEM 1: SQL Injection
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Extremely vulnerable to SQLi
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    user = cursor.fetchone()
    return jsonify(user)

# PROBLEM 2: Path Traversal
@app.route('/read')
def read_file():
    filename = request.args.get('file')
    # No validation, allows reading any file on system
    with open(filename, 'r') as f:
        return f.read()

# PROBLEM 3: Hardcoded Secret (In-code)
def verify_admin():
    admin_token = "ABC12345DEF67890GHIJKL" # Hardcoded static secret
    if request.headers.get('X-Admin') == admin_token:
        return True
    return False

if __name__ == "__main__":
    app.run(debug=True)
