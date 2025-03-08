import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.post('/bot')
def get_bot_data():
    try:
        body = request.json
        query = body.get('query')
        data = {"token":"6141630044:e9FqKv8V", "request":query, "limit": 1000, "lang":"en"}
        url = 'https://leakosintapi.com/' 
        response = requests.post(url, json=data) 
        print(response.json()) # Please note that the request data is sent in json format. If you send it as request parameters, you will get a 501 error.
        return jsonify({'msg':response.json()}), 200
    except Exception as e:
        return jsonify({'msg':e}), 500
    

if __name__ == '__main__':
    app.run(port=5001)