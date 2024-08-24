import streamlit as st
from PIL import Image
import base64
import pickle
import pandas as pd
import io
from PIL import Image
from NBA_Predictor import predict_trade
from Recruitment_predictor import prepare_input_data, predict_hiring_decision
from Purchase_predictor import predict_purchase

# Load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
load_css("style.css")

# Sidebar with logo and name side by side
logo = Image.open("images/logo.jpeg")

# Convert logo to base64
buffered = io.BytesIO()
logo.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Display the logo and name side by side
st.sidebar.markdown(
    f"""
    <div class="logo-container">
        <img src="data:image/png;base64,{img_str}" alt="Logo" style="width:50px; margin-right:10px;">
        <h1 style="display:inline; vertical-align: middle;">Devcomm</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Create a dropdown for selecting a model
model_choice = st.sidebar.selectbox(
    "Choose a Machine Learning Model",
    ("NBA Player Trade Examiner", "Recruitment Predictor", "Purchase Predictor")
)

# Function to load the model
# def load_model(model_name):
#     with open(f'Models/{model_name}.pkl', 'rb') as file:
#         model = pickle.load(file)
#     return model

# Display form and handle prediction based on selected model
if model_choice == "NBA Player Trade Examiner":
    # Load your dataset
    data = pd.read_csv("NBAFiles/final_data.csv")  # Replace with your actual dataset

    st.title("NBA Player Trade Examiner")
    # Get user input for player names
    player1_name = st.text_input("Enter the name of Player 1:")
    player2_name = st.text_input("Enter the name of Player 2:")

    # Predict button
    if st.button("Predict"):
        if player1_name and player2_name:
            trade_prediction, error_message = predict_trade(player1_name, player2_name, data)
        
            if error_message:
                st.write(error_message)
            else:
                if trade_prediction > 0.5:
                    st.write(f"It's a good trade to take {player2_name} over {player1_name}.")
                else:
                    st.write(f"It's a bad trade to take {player2_name} over {player1_name}.")
        else:
            st.write("Please enter both player names.")
            
elif model_choice == "Recruitment Predictor":
    st.title("Recruitment Predictor")
    # Collect input data from the user using sliders
    age = st.slider("Age", min_value=20, max_value=50, step=1)
    gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
    education_level = st.selectbox("Education Level", options=[1, 2, 3, 4], format_func=lambda x: {1: "Bachelor's (Type 1)", 2: "Bachelor's (Type 2)", 3: "Master's", 4: "PhD"}[x])
    experience_years = st.slider("Experience Years", min_value=0, max_value=15, step=1)
    previous_companies = st.slider("Previous Companies Worked", min_value=1, max_value=5, step=1)
    distance_from_company = st.slider("Distance From Company (km)", min_value=1.0, max_value=50.0, step=0.1)
    interview_score = st.slider("Interview Score", min_value=0, max_value=100, step=1)
    skill_score = st.slider("Skill Score", min_value=0, max_value=100, step=1)
    personality_score = st.slider("Personality Score", min_value=0, max_value=100, step=1)
    recruitment_strategy = st.selectbox("Recruitment Strategy", options=[1, 2, 3], format_func=lambda x: {1: "Aggressive", 2: "Moderate", 3: "Conservative"}[x])
    
    if st.button("Predict Hiring Decision"):
        input_data = prepare_input_data(age, gender, education_level, experience_years, previous_companies, distance_from_company, interview_score, skill_score, personality_score, recruitment_strategy)
        prediction = predict_hiring_decision(input_data)
        image1 = Image.open("images/hired.webp")
        image2 = Image.open("images/rejected.png")
    
        if prediction[0] == 1:
            st.image(image1, use_column_width=True)
            st.success("The candidate is likely to be hired.")
        else:
            st.image(image2, use_column_width=True)
            st.warning("The candidate is not likely to be hired.")

elif model_choice == "Purchase Predictor":
    st.title("iPhone Purchase Prediction")

    # Collect input data
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", min_value=19, max_value=60, step=1)
    salary = st.slider("Salary", min_value=10000, max_value=100000, step=1000)

    # Predict button
    if st.button("Predict"):
        prediction = predict_purchase(gender, age, salary)
        if prediction == 1:
            st.success("The person is likely to purchase an iPhone.")
        else:
            st.warning("The person is not likely to purchase an iPhone.")