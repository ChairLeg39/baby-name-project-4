from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import random
import numpy as np
from collections import defaultdict

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client.babyNameDB
collection = db.babyNames

# Home page url
@app.route("/")
def default():
    return render_template('index.html')

# Route to dataset
@app.route("/sourcedata")
def sourcedata():
    data = list(collection.find({}, {'_id': False}))
    return jsonify(data)

# Selects a random name from the dataset that meets the dropdown criteria
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