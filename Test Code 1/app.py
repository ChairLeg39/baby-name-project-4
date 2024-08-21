from bson import json_util
from flask import Flask, jsonify, render_template, request
import random
import pymongo
import os

app = Flask(__name__)

# setup mongo connection
serverUrl = os.environ.get('MONGO', "mongodb://localhost:27017")
client = pymongo.MongoClient(serverUrl)

# connect to mongo db (babyNameDB) and collection (babyNames)
db = client.babyNameDB
collection = db.babyNames

@app.route("/")
def default():
    return render_template('index.html')

@app.route("/sourcedata")
def sourcedata():
    data = list(collection.find({}, {'_id': False}))
    return jsonify(data)

@app.route("/generate_name", methods=['POST'])
def generate_name():
    data = request.json
    gender = data['gender']
    ethnicity = data['ethnicity']
    
    # Query the database for names matching the criteria
    matching_names = list(collection.find({
        'Gender': gender,
        'Ethnicity': ethnicity
    }, {'First Name': 1, '_id': 0}))
    
    if matching_names:
        # Randomly select a name from the matching names
        selected_name = random.choice(matching_names)['First Name']
        return jsonify({'name': selected_name})
    else:
        return jsonify({'error': 'No matching names found'})


if __name__ == '__main__':
    app.run(debug=True, port=5010)