import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')  # 👈 This handles the root route
def home():
    return jsonify({"message": "API is running!"})

@app.post('/bot')
def get_bot_data():
    try:
        body = request.json
        query = body.get('query')
        data = {"token":"6141630044:e9FqKv8V", "request":query, "limit": 1000, "lang":"en"}
        url = 'https://leakosintapi.com/' 
        response = requests.post(url, json=data) 
        print(response.json())  
        return jsonify({'msg': response.json()}), 200
    except Exception as e:
        return jsonify({'msg': str(e)}), 500  # Convert error to string to avoid issues

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # 👈 Ensure it runs on 0.0.0.0 for public access
