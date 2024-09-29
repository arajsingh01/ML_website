import numpy as np

import joblib

def load_model_and_scaler():
    # Load the model using joblib
    model = joblib.load('Purchase_iphone/model_joblib.joblib')
    
    # Load the scaler using joblib
    scaler = joblib.load('Purchase_iphone/scaler_joblib.joblib')
    
    return model, scaler

def predict_purchase(gender, age, salary):
    model, scaler = load_model_and_scaler()
    
    sex = 1 if gender == 'Female' else 0
    input_data = np.array([[age, salary, sex]])
    
    scaled_data = scaler.transform(input_data)
    
    prediction = model.predict(scaled_data)
    return prediction