from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory store (replace with DB if needed)
messages = []

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/api/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400
    messages.append(data['text'])
    return jsonify({"message": "Added"}), 201

# Optional health route
@app.route('/health', methods=['GET'])
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
