from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL connection details (use environment variables in production)
db_config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', 'your_password'),
    'database': os.environ.get('DB_NAME', 'labdb')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/api/messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, text FROM messages")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([{'id': row[0], 'text': row[1]} for row in rows])

@app.route('/api/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (text) VALUES (%s)", (data['text'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Added"}), 201

@app.route('/health', methods=['GET'])
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
