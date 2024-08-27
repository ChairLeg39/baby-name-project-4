from flask import Flask, jsonify, render_template, render_template_string, request
from pymongo import MongoClient
import random
import numpy as np
from collections import defaultdict
import json

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client.babyNameDB
collection = db.babyNames

# Markov chain model
class MarkovChain:
    def __init__(self, order=2):
        self.order = order
        self.chain = defaultdict(lambda: defaultdict(int))
        self.start_tokens = defaultdict(int)

    def load_from_dict(self, data):
        self.order = data['order']
        self.chain = defaultdict(lambda: defaultdict(int), {tuple(eval(k)): defaultdict(int, v) for k, v in data['chain'].items()})
        self.start_tokens = defaultdict(int, {tuple(eval(k)): v for k, v in data['start_tokens'].items()})

    def generate(self, min_length=3, max_length=12):
        state = self._weighted_choice(self.start_tokens)
        result = list(state)
        while '<START>' in result:
            result.remove('<START>')  # Remove all <START> tokens
        while True:
            next_char = self._weighted_choice(self.chain[state])
            if next_char == '<END>' or len(result) >= max_length:
                if len(result) >= min_length:
                    return ''.join(result)
                else:
                    return self.generate(min_length, max_length)
            result.append(next_char)
            state = state[1:] + (next_char,)

    def _weighted_choice(self, choices):
        total = sum(choices.values())
        r = random.random() * total
        for choice, weight in choices.items():
            r -= weight
            if r <= 0:
                return choice

# Global Markov chain models
gender_ethnicity_models = {}

# Function to load models
def load_models():
    global gender_ethnicity_models
    with open('../Output/markov_trained.json', 'r') as f:
        trained_models = json.load(f)

    for key, model_data in trained_models.items():
        gender, ethnicity = key.split('_')
        model = MarkovChain(order=model_data['order'])
        model.load_from_dict(model_data)
        gender_ethnicity_models[(gender, ethnicity)] = model

# Load models on startup
load_models()

# Home page url
@app.route("/")
def default():
    return render_template('index.html')

# Route to dataset
@app.route("/sourcedata")
def sourcedata():
    data = list(collection.find({}, {'_id': False}))
    return jsonify(data)

# Route to Power BI images
@app.route("/powerbi")
def powerbi():
    return render_template('powerbi.html')

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