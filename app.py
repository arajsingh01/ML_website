import streamlit as st
from PIL import Image
import base64
import pandas as pd
import io
from NBA_Predictor import predict_trade
from Recruitment_predictor import prepare_input_data, predict_hiring_decision
from Purchase_predictor import predict_purchase
from social_media import predict_impact

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

logo = Image.open("images/logo.jpeg")

buffered = io.BytesIO()
logo.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

st.sidebar.markdown(
    f"""
    <div class="logo-container">
        <img src="data:image/png;base64,{img_str}" alt="Logo" style="width:50px; margin-right:10px;">
        <h1 style="display:inline; vertical-align: middle;">Devcomm</h1>
    </div>
    """,
    unsafe_allow_html=True
)

category = st.sidebar.selectbox(
    "Select a Category",
    ("Home", "ML Model", "Data Analysis")
)

if category == "Home":
    st.title("Welcome to the Devcomm Platform")
    st.write("Meet the team behind this platform:")
    
    col1, col2 = st.columns(2)

    with col1:
        image1 = Image.open("profileimg/nikunj.jpeg")
        st.image(image1, caption="John Doe - Data Scientist", use_column_width=True)
        st.write("John is an expert in machine learning and AI with a focus on predictive modeling.")

    with col2:
        image2 = Image.open("profileimg/Dhruv_Bhardwaj.jpg")
        st.image(image2, caption="Jane Smith - Full Stack Developer", use_column_width=True)
        st.write("Jane specializes in web development and backend integration for AI systems.")

    st.write("Explore our various models and data analysis tools using the sidebar.")

elif category == "ML Model":
    model_choice = st.sidebar.selectbox(
        "Choose a Machine Learning Model",
        ("NBA Player Trade Examiner", "Recruitment Predictor", "Iphone Purchase Predictor", "Social Media Impact Predictor")
    )

    if model_choice == "NBA Player Trade Examiner":
        data = pd.read_csv("NBAFiles/final_data.csv")
        st.title("NBA Player Trade Examiner")
        player1_name = st.text_input("Enter the name of Player 1:")
        player2_name = st.text_input("Enter the name of Player 2:")

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

    elif model_choice == "Iphone Purchase Predictor":
        st.title("Iphone Purchase Prediction")
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.slider("Age", min_value=19, max_value=60, step=1)
        salary = st.slider("Salary", min_value=10000, max_value=100000, step=1000)

        if st.button("Predict"):
            prediction = predict_purchase(gender, age, salary)
            if prediction == 1:
                st.success("The person is likely to purchase an iPhone.")
            else:
                st.warning("The person is not likely to purchase an iPhone.")

    elif model_choice == "Social Media Impact Predictor":
        st.title("Social Media Impact Prediction")
        
        total_time_spent = st.slider("Total Time Spent (hours)", min_value=0, max_value=24, step=1)
        num_sessions = st.slider("Number of Sessions", min_value=1, max_value=100, step=1)
        engagement = st.slider("Engagement Level", min_value=0, max_value=100, step=1)
        scroll_rate = st.slider("Scroll Rate", min_value=0, max_value=100, step=1)
        productivity_loss = st.slider("Productivity Loss", min_value=0, max_value=100, step=1)
        satisfaction = st.slider("Satisfaction Level", min_value=0, max_value=100, step=1)
        self_control = st.slider("Self Control", min_value=0, max_value=100, step=1)
        addiction_level = st.slider("Addiction Level", min_value=0, max_value=100, step=1)

        if st.button("Predict Impact"):
            input_data = pd.DataFrame({
                'Total Time Spent': [total_time_spent],
                'Number of Sessions': [num_sessions],
                'Engagement': [engagement],
                'Scroll Rate': [scroll_rate],
                'ProductivityLoss': [productivity_loss],
                'Satisfaction': [satisfaction],
                'Self Control': [self_control],
                'Addiction Level': [addiction_level]
            })

            prediction = predict_impact(input_data)
            
            bad_impact_image = Image.open("DarksideOfSocialMedia/addicted to socialmedia.jpg")
            no_impact_image = Image.open("DarksideOfSocialMedia/healthy mindset.jpg")

            if prediction[0] == 1:
                st.image(bad_impact_image, use_column_width=True)
                st.warning("You are badly impacted by social media.")
            else:
                st.image(no_impact_image, use_column_width=True)
                st.success("You are not badly impacted by social media.")

elif category == "Data Analysis":

    dataset_choice = st.sidebar.selectbox(
        "Choose a dataset",
        ("Spotify","NBA Player Stats")
    )

    if dataset_choice == "Spotify":
        @st.cache_data
        def load_data():
            df = pd.read_csv('Spotify_songs/Most Streamed Spotify Songs 2024.csv', encoding='ISO-8859-1')
            columns_to_convert = ['Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach',
                                  'YouTube Views', 'YouTube Likes', 'TikTok Posts', 'TikTok Likes',
                                  'TikTok Views', 'YouTube Playlist Reach', 'AirPlay Spins', 'SiriusXM Spins',
                                  'Pandora Streams', 'Pandora Track Stations', 'Soundcloud Streams', 'Shazam Counts']
            for column in columns_to_convert:
                df[column] = df[column].str.replace(',', '').astype(float)
            df = df.drop(columns=['TIDAL Popularity'])
            return df

        st.title('Spotify Top Streamed Songs (2024)')
        df = load_data()

        st.header('Dataset Overview')
        st.write(df.head())

        st.header('Top 10 Songs by Spotify Streams')
        top_10_songs = df[['Track', 'Artist', 'Spotify Streams']].sort_values(by='Spotify Streams', ascending=False).head(10)
        st.write(top_10_songs)

        st.header('Correlation between Streams, Popularity, and Playlist Count')
        correlation_data = df[['Spotify Streams', 'Spotify Popularity', 'Spotify Playlist Count']].corr()
        st.write(correlation_data)

        st.header('YouTube Views vs TikTok Engagement')
        st.write(df[['YouTube Views', 'TikTok Views', 'TikTok Likes']].describe())

        st.header('Visualizations')
        st.bar_chart(top_10_songs.set_index('Track')['Spotify Streams'])

        st.write("Data Source: Most Streamed Spotify Songs of 2024")
    
    elif dataset_choice == "NBA Player Stats":
        @st.cache_data
        def load_nba_data():
            return pd.read_csv('NBAFiles/final_data.csv')
        
        st.title('NBA Player Performance Analysis')
        df = load_nba_data()

        st.header('Dataset Overview')
        st.write(df.head())

        st.header('Player Statistics Overview')
        st.write(df.describe())

        st.header('Top 10 Players by Points')
        top_10_players_pts = df[['PLAYER_NAME', 'PTS']].sort_values(by='PTS', ascending=False).head(10)
        st.write(top_10_players_pts)

        st.header('Correlation between Points, Assists, and Rebounds')
        correlation_data = df[['PTS', 'AST', 'REB']].corr()
        st.write(correlation_data)