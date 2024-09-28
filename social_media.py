from sklearn.tree import DecisionTreeClassifier
import pickle
import pandas as pd
import joblib

# Function to load the saved model
def load_model():
    # Ensure you replace 'social_media_impact_model.pkl' with the actual model file path
    model = joblib.load('DarkSideOfSocialMedia/social_media_impact_model2.joblib')
    return model

# Function to make predictions
def predict_impact(input_data):
    # Load the model
    model = load_model()

    # Ensure input_data is in the correct format (Pandas DataFrame)
    if not isinstance(input_data, pd.DataFrame):
        raise ValueError("Input data should be a Pandas DataFrame.")

    # Make predictions using the model
    prediction = model.predict(input_data)

    return prediction