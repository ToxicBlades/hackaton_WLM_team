import numpy as np
import seaborn as sns
import pandas as pd

import sklearn
import joblib

from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app


@app.route('/api/data', methods=['GET'])
def get_data():
    # Здесь можно вернуть данные, которые клиент запросил
    data = {'message': 'Idi nahui'}
    return jsonify(data)


@app.route('/api/request', methods=['POST'])
def handle_request():
    try:
        model = joblib.load('children_violance_predictor.joblib')
        # Retrieve the JSON data sent from the form
        data = request.json

        gender_value = data.get('dropdown1', None)
        gender = 0 if gender_value == 'Female' else 1 if gender_value == 'Male' else None
        # Extract the specific fields from the data
        age = data.get('additionalField', None)
        mother = 1 if data.get('checkbox1', False) else 0
        father = 1 if data.get('checkbox2', False) else 0
        smoke = 1 if data.get('checkbox3', False) else 0
        drinks = 1 if data.get('checkbox4', False) else 0
        drugs = 1 if data.get('checkbox5', False) else 0


        welfare = data.get('dropdown2', None)
        welfare_L = 1 if welfare == 'low' else 0
        welfare_M = 1 if welfare == 'medium' else 0


        model_input = [age, mother, father, smoke, drugs, drinks, gender, welfare_L, welfare_M]

        # Make the prediction
        prediction = model.predict([model_input])

        # Convert NumPy data types to Python data types for JSON serialization
        prediction = prediction[0].item() if len(prediction) > 0 else None

        # Return the prediction in the response
        result = {
            'prediction': prediction
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})



@app.route('/api/csvdata', methods=['GET'])
def get_csv_data():
    try:
        # Read the CSV file
        df = pd.read_csv('./data_set.csv')
        # Convert DataFrame to a list of dictionaries
        data = df.to_dict(orient='records')
        # Use jsonify to return the data
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)