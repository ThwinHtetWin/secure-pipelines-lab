"""
API Security Lab - Vulnerable Flask Application
This app intentionally contains security vulnerabilities for training purposes.
"""

from flask import Flask, request, jsonify
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# Initialize database
def init_db():
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT,
            role TEXT
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'admin@company.com', 'admin')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'user1', 'user1@company.com', 'user')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (3, 'user2', 'user2@company.com', 'user')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return jsonify({
        'message': 'API Security Lab',
        'endpoints': [
            '/api/users',
            '/api/user/<id>',
            '/api/admin'
        ]
    })

@app.route('/api/users')
def get_users():
    """
    VULNERABILITY: SQL Injection
    This endpoint is vulnerable to SQL injection
    """
    username = request.args.get('username', '')

    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()

    # VULNERABLE CODE - DO NOT USE IN PRODUCTION
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    users = cursor.fetchall()
    conn.close()

    return jsonify({'users': users})

@app.route('/api/user/<int:user_id>')
def get_user(user_id):
    """
    VULNERABILITY: IDOR (Insecure Direct Object Reference)
    Missing authorization checks
    """
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            'id': user[0],
            'username': user[1],
            'email': user[2],
            'role': user[3]
        })
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/admin')
def admin_panel():
    """
    VULNERABILITY: Weak Authentication
    Simple token that can be easily guessed
    """
    auth_token = request.headers.get('Authorization', '')

    # WEAK AUTHENTICATION - DO NOT USE
    if auth_token == 'Bearer admin123':
        return jsonify({'message': 'Welcome to admin panel', 'secret': 'FLAG{you_found_the_admin_panel}'})

    return jsonify({'error': 'Unauthorized'}), 401

if __name__ == '__main__':
    init_db()
    print("Starting API Security Lab...")
    print("Visit http://localhost:5000 to begin")
    app.run(debug=True, port=5000)
