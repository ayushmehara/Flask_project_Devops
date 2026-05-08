from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"

# Create file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# API route to get data
@app.route('/api', methods=['GET'])
def get_data():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

# API route to submit form data
@app.route('/submit', methods=['POST'])
def submit_data():
    new_data = request.json

    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    data.append(new_data)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    return jsonify({
        "message": "Data saved successfully",
        "data": new_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)