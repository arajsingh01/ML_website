import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

# Load the trained model and scaler
model = joblib.load("NBAFiles/model_saved.pkl")
scaler = joblib.load("NBAFiles/scaler_saved.pkl")

# Function to get player statistics from the dataset
def get_player_stats(player_name, data):
    player_stats = data[data['PLAYER_NAME'] == player_name].select_dtypes(include=[np.number]).mean()
    return player_stats

# Function to predict the trade outcome
def predict_trade(player1_name, player2_name, data):
    player1_stats = get_player_stats(player1_name, data)
    player2_stats = get_player_stats(player2_name, data)

    if player1_stats.empty or player2_stats.empty:
        return None, "One or both players not found in the dataset."

    # Calculate feature differences
    test_trade = pd.DataFrame({
        'PTS_diff': [player2_stats['PTS'] - player1_stats['PTS']],
        'AST_diff': [player2_stats['AST'] - player1_stats['AST']],
        'REB_diff': [player2_stats['REB'] - player1_stats['REB']],
        'Efficiency_diff': [player2_stats['Efficiency'] - player1_stats['Efficiency']],
        'FG_PCT_diff': [player2_stats['FG_PCT'] - player1_stats['FG_PCT']],
        'FG3_PCT_diff': [player2_stats['FG3_PCT'] - player1_stats['FG3_PCT']],
        'FT_PCT_diff': [player2_stats['FT_PCT'] - player1_stats['FT_PCT']],
        'TOV_diff': [player2_stats['TOV'] - player1_stats['TOV']],
        'STL_diff': [player2_stats['STL_x'] - player1_stats['STL_x']],
        'BLK_diff': [player2_stats['BLK_x'] - player1_stats['BLK_x']],
        'MIN_diff': [player2_stats['MIN_x'] - player1_stats['MIN_x']]
    })

    # Standardize the test trade data
    test_trade_scaled = scaler.transform(test_trade)

    # Make prediction
    trade_prediction = model.predict(test_trade_scaled)

    return trade_prediction, None