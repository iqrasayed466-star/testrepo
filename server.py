from flask import Flask, request, jsonify
import sqlite3
import os
from sqlite3 import Error

app = Flask(__name__)

# PROBLEM 1: SQL Injection
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    if not user_id:  # Check if user_id is provided
        return jsonify({"error": "User ID is required"}), 400
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        # Use parameterized query to prevent SQLi
        query = "SELECT * FROM users WHERE id = ?"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        return jsonify(user)
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()

# PROBLEM 2: Path Traversal
@app.route('/read')
def read_file():
    filename = request.args.get('file')
    if not filename:  # Check if filename is provided
        return jsonify({"error": "File name is required"}), 400
    
    # Validate filename to prevent path traversal
    if '..' in filename or '/' in filename:
        return jsonify({"error": "Invalid file name"}), 400
    
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PROBLEM 3: Hardcoded Secret (In-code)
def verify_admin():
    admin_token = os.environ.get('ADMIN_TOKEN')  # Get token from environment variable
    if request.headers.get('X-Admin') == admin_token:
        return True
    return False

if __name__ == "__main__":
    app.run(debug=True)