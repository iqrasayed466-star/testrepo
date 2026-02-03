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
    # Fix: Use parameterized query to prevent SQLi
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    return jsonify(user)

# PROBLEM 2: Path Traversal
@app.route('/read')
def read_file():
    filename = request.args.get('file')
    # Fix: Validate and sanitize the filename to prevent path traversal
    if '.' in filename:
        return jsonify({'error': 'File extension is not allowed'}), 400
    if '..' in filename:
        return jsonify({'error': 'Path traversal is not allowed'}), 400
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

# PROBLEM 3: Hardcoded Secret (In-code)
def verify_admin():
    # Fix: Store the secret securely in an environment variable
    admin_token = os.environ.get('ADMIN_TOKEN')
    if request.headers.get('X-Admin') == admin_token:
        return True
    return False

if __name__ == "__main__":
    app.run(debug=True)