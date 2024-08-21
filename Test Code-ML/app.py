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

# Markov chain model
class MarkovChain:
    def __init__(self):
        self.chain = defaultdict(lambda: defaultdict(int))

    def train(self, names):
        for name in names:
            name = '^' + name + '$'
            for i in range(len(name) - 1):
                self.chain[name[i]][name[i+1]] += 1

    def generate(self, min_length=3, max_length=12):
        current = '^'
        result = ''
        while current != '$' and len(result) < max_length:
            choices = list(self.chain[current].keys())
            weights = list(self.chain[current].values())
            total = sum(weights)
            weights = [w/total for w in weights]
            next_char = np.random.choice(choices, p=weights)
            if next_char != '$':
                result += next_char
            current = next_char
        return result if len(result) >= min_length else self.generate(min_length, max_length)

# Global Markov chain models
gender_ethnicity_models = {}

# Function to train models
def train_models():
    global gender_ethnicity_models
    for gender in ['MALE', 'FEMALE']:
        for ethnicity in ['WHITE NON HISPANIC', 'BLACK NON HISPANIC', 'ASIAN AND PACIFIC ISLANDER', 'HISPANIC']:
            names = [doc['First Name'] for doc in collection.find({'Gender': gender, 'Ethnicity': ethnicity})]
            model = MarkovChain()
            model.train(names)
            gender_ethnicity_models[(gender, ethnicity)] = model

# Train models on startup
train_models()

# Home page url
@app.route("/")
def default():
    return render_template('index.html')

# Route to dataset
@app.route("/sourcedata")
def sourcedata():
    data = list(collection.find({}, {'_id': False}))
    return jsonify(data)

# Used trained models to generate names
@app.route("/generate_name", methods=['POST'])
def generate_name():
    data = request.json
    gender = data['gender']
    ethnicity = data['ethnicity']
    
    if (gender, ethnicity) in gender_ethnicity_models:
        generated_name = gender_ethnicity_models[(gender, ethnicity)].generate()
        return jsonify({'name': generated_name})
    else:
        return jsonify({'error': 'No model available for the selected criteria'})

if __name__ == '__main__':
    app.run(debug=True, port=5010)