from sklearn.tree import DecisionTreeClassifier
import pickle
import pandas as pd
import joblib

def load_model():
    model = joblib.load('DarksideOfSocialMedia/social_media_impact_model2.joblib')
    return model

def predict_impact(input_data):
    model = load_model()

    if not isinstance(input_data, pd.DataFrame):
        raise ValueError("Input data should be a Pandas DataFrame.")

    prediction = model.predict(input_data)

    return prediction