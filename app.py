from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
def load_model():
    try:
        with open("rainfall_prediction_model.pkl", "rb") as file:
            model_data = pickle.load(file)
        return model_data
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model_data = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        
        # Extract features
        pressure = float(data['pressure'])
        dewpoint = float(data['dewpoint'])
        humidity = float(data['humidity'])
        cloud = float(data['cloud'])
        sunshine = float(data['sunshine'])
        winddirection = float(data['winddirection'])
        windspeed = float(data['windspeed'])
        
        # Create input dataframe
        input_data = (pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed)
        input_df = pd.DataFrame([input_data], columns=model_data["feature_names"])
        
        # Make prediction
        prediction = model_data["model"].predict(input_df)[0]
        prediction_proba = model_data["model"].predict_proba(input_df)[0]
        
        # Get confidence score
        confidence = max(prediction_proba) * 100
        
        # Return result
        result = {
            'prediction': int(prediction),
            'confidence': round(confidence, 2),
            'message': 'Rainfall Expected' if prediction == 1 else 'No Rainfall Expected'
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)