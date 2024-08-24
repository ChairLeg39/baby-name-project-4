from bson import json_util
from flask import Flask, jsonify, render_template
import pymongo
import os
import json

app = Flask(__name__)

# setup mongo connection
serverUrl = os.environ.get('MONGO', "mongodb://localhost:27017")
client = pymongo.MongoClient(serverUrl)

# connect to mongo db and collection
db = client.babyNameDB
baby_collection = db.babyNames

@app.route("/")
def default():
    return render_template('index.html')

@app.route("/home")
def home():
    dict_list = [{'id':1,'source':'python'}]
    heading_text = "this text came from a varaible python"
    return render_template('home.html', data=dict_list, heading=heading_text)

@app.route("/api")
def api():
    data = baby_collection.find()
    return json_util.dumps(data)




if __name__ == '__main__':
    app.run(debug=True, port=5010)

