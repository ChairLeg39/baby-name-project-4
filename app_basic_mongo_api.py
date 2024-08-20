from bson import json_util
from flask import Flask, jsonify
import pymongo
import json

app = Flask(__name__)

serverUrl = "mongodb://localhost:27017"
client = pymongo.MongoClient(serverUrl)

# connect to mongo db and collection
db = client.babyNameDB
baby_collection = db.babyNames

@app.route("/")
def default():
    dict_list = [{'id':1,'source':'python'}]
    return jsonify(dict_list)

@app.route("/api")
def api():
    data = baby_collection.find()
    return json_util.dumps(data)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
