# Rainfall Prediction App

This is a website that predicts if it will rain based on weather information.

## What It Does
- Tells you if it will rain or not
- Uses 7 different weather measurements
- Works on phones and computers
- Shows how confident the prediction is
- Gives fast results

## How It Works
- Backend: Python with Flask
- Frontend: Regular website (HTML/CSS/JavaScript)
- Uses smart computer learning (Random Forest)
- Stores code on GitHub

## Weather Information Needed:
1. Air Pressure
2. Dew Point (temperature when water forms)
3. Humidity (how much moisture in air)
4. Cloud Cover (how cloudy it is)
5. Sunshine (hours of sun)
6. Wind Direction
7. Wind Speed

## How to Set It Up

### What You Need First:
- Python installed
- Git installed

### Step by Step:
```bash
# 1. Download the project
git clone https://github.com/YOUR_USERNAME/rainfall-prediction-app.git

# 2. Go to the project folder
cd rainfall-prediction-app

# 3. Install required software
pip install flask pandas scikit-learn numpy

# 4. Start the website
python app.py

# 5. Open your web browser and go to:
# http://127.0.0.1:5000


rainfall-prediction-app/
├── app.py                         (main program)
├── rainfall_prediction_model.pkl  (smart brain)
├── templates/
│   └── index.html                 (website design)
└── README.md                      (this file)
