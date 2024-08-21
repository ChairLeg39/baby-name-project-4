from flask import Flask, request, jsonify
from pymongo import MongoClient
import random

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['babyNameDB']
collection = db['babyNames']

@app.route('/generate_name', methods=['POST'])
def generate_name():
    data = request.json
    gender = data.get('gender')
    ethnicity = data.get('ethnicity')
    
    if not gender or not ethnicity:
        return jsonify({"error": "Gender and ethnicity are required"}), 400
    
    # Retrieve data from MongoDB
    query = {"Gender": gender, "Ethnicity": ethnicity}
    names_data = list(collection.find(query))
    
    if not names_data:
        return jsonify({"error": "No data found for the given criteria"}), 404
    
    # Simple frequency-based name generation
    names_with_weights = [(name['First Name'], name['Count']) for name in names_data]
    total_count = sum(weight for _, weight in names_with_weights)
    
    generated_names = []
    for _ in range(5):  # Generate 5 names
        r = random.uniform(0, total_count)
        cumulative_weight = 0
        for name, weight in names_with_weights:
            cumulative_weight += weight
            if r <= cumulative_weight:
                generated_names.append(name)
                break
    
    return jsonify({
        "gender": gender,
        "ethnicity": ethnicity,
        "generated_names": generated_names
    })

if __name__ == '__main__':
    app.run(debug=True)