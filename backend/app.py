from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_HOST = os.getenv('MONGO_HOST', 'database')
MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))

client = MongoClient(host = MONGO_HOST, port = MONGO_PORT)
db = client['mydatabase']

@app.route("/")
def index():
    return "Backend is running!"

@app.route("/data", methods=["GET"])
def get_data():
    collection = db['mycollection']
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)