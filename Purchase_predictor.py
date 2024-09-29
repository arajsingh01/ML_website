import pickle
import numpy as np

def load_model_and_scaler():
    with open('Purchase_iphone/model_pickle.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('Purchase_iphone/scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

def predict_purchase(gender, age, salary):
    model, scaler = load_model_and_scaler()
    
    sex = 1 if gender == 'Female' else 0
    input_data = np.array([[age, salary, sex]])
    
    scaled_data = scaler.transform(input_data)
    
    prediction = model.predict(scaled_data)
    return prediction