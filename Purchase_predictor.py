# iphone_predictor.py
import pickle
import numpy as np

# Function to load the model and scaler
def load_model_and_scaler():
    with open('Purchase_iphone/model_pickle.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('Purchase_iphone/scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

# Function to make predictions
def predict_purchase(gender, age, salary):
    model, scaler = load_model_and_scaler()
    
    # Prepare input data
    sex = 1 if gender == 'Female' else 0
    input_data = np.array([[age, salary, sex]])
    
    # Scale the input data
    scaled_data = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(scaled_data)
    return prediction