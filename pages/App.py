import streamlit as st
from PIL import Image
import base64
import pandas as pd
import io
from NBA_Predictor import predict_trade
from Recruitment_predictor import prepare_input_data, predict_hiring_decision
from Purchase_predictor import predict_purchase
from social_media import predict_impact
import matplotlib.pyplot as plt

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
    <div class="logo-container" style="text-align: center;">
        <img src="data:image/png;base64,{img_str}" alt="Logo" style="width:50px; margin-right:10px;">
        <h1 style="display:inline; vertical-align: middle;">Devcomm</h1>
    </div>
    </br>
    <div>
        <h1 style="display:inline; vertical-align: middle;">Devcomm ML Nexus</h1>
    </div>
    </br>
    """,
    unsafe_allow_html=True
)

category = st.sidebar.selectbox(
    "Select",
    ("Home", "ML Model", "Data Analysis")
)

def resize_image(image_path, width, height):
    img = Image.open(image_path)
    resized_img = img.resize((width, height))
    return resized_img

if category == "Home":
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>MEET OUR TEAM</h1>
            <p><i>"A dedicated group of innovators driving the group forward"</i></p>
        </div>
        """, unsafe_allow_html=True
    )

    st.header("Mentors")
    col1, col2 = st.columns(2)

    with col1:
        image1 = resize_image("profileimg/Rashid Siddiqui.png", 400, 450)
        st.image(image1)
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>Rashid Siddiqui</h3>
                <p>ML Head, DevComm</p>
            </div>
            """, unsafe_allow_html=True)
        linkedin_url = "https://www.linkedin.com/in/rashid-siddiqui2004/"
        linkedin_icon = "profileimg/icon.png"
        with open(linkedin_icon, "rb") as image_file:
            encoded_icon = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <div style="text-align: center;">
                <a href="{linkedin_url}" target="_blank">
                    <img src="data:image/png;base64,{encoded_icon}" alt="LinkedIn Icon" style="width:30px; height:30px;">
                </a>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        image2 = resize_image("profileimg/Ishita Srivasava.jpg", 400, 450)
        st.image(image2)
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>Ishita Srivastava</h3>
                <p>ML Head, DevComm</p>
            </div>
            """, unsafe_allow_html=True)
        linkedin_url = "https://www.linkedin.com/in/ishita-srivastava-313b27264/"
        with open(linkedin_icon, "rb") as image_file:
            encoded_icon = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <div style="text-align: center;">
                <a href="{linkedin_url}" target="_blank">
                    <img src="data:image/png;base64,{encoded_icon}" alt="LinkedIn Icon" style="width:30px; height:30px;">
                </a>
            </div>
            """, unsafe_allow_html=True
        )

    st.header("Development Team")
    col3, col4 = st.columns(2)

    with col3:
        image3 = resize_image("profileimg/aditya.jpeg", 400, 450)
        st.image(image3)
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>Aditya Raj Singh</h3>
                <p>JC, ML Department</p>
            </div>
            """, unsafe_allow_html=True)
        linkedin_url = "https://www.linkedin.com/in/aditya-raj-singh-4134262a6/"
        with open(linkedin_icon, "rb") as image_file:
            encoded_icon = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <div style="text-align: center;">
                <a href="{linkedin_url}" target="_blank">
                    <img src="data:image/png;base64,{encoded_icon}" alt="LinkedIn Icon" style="width:30px; height:30px;">
                </a>
            </div>
            """, unsafe_allow_html=True
        )

    with col4:
        image4 = resize_image("profileimg/Dhruv_Bhardwaj.jpg", 400, 450)
        st.image(image4)
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>Dhruv Bhardwaj</h3>
                <p>JC, ML Department</p>
            </div>
            """, unsafe_allow_html=True)
        linkedin_url = "https://www.linkedin.com/in/dhruv-bhardwaj-a422481b1"
        with open(linkedin_icon, "rb") as image_file:
            encoded_icon = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <div style="text-align: center;">
                <a href="{linkedin_url}" target="_blank">
                    <img src="data:image/png;base64,{encoded_icon}" alt="LinkedIn Icon" style="width:30px; height:30px;">
                </a>
            </div>
            """, unsafe_allow_html=True
        )

    st.header("ML Team Members")
    col5, col6 = st.columns(2)

    with col5:
        image5 = resize_image("profileimg/nikunj.jpeg", 400, 450)
        st.image(image5)
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>Nikunj Kumar</h3>
                <p>JC, ML Department</p>
            </div>
            """, unsafe_allow_html=True)
        linkedin_url = "https://www.linkedin.com/in/nikunjkumar1405/"
        with open(linkedin_icon, "rb") as image_file:
            encoded_icon = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <div style="text-align: center;">
                <a href="{linkedin_url}" target="_blank">
                    <img src="data:image/png;base64,{encoded_icon}" alt="LinkedIn Icon" style="width:30px; height:30px;">
                </a>
            </div>
            """, unsafe_allow_html=True
        )

    with col6:
        image6 = resize_image("profileimg/Suryansh Malhotra. Jpg.jpg", 400, 450)
        st.image(image6)
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>Suryansh Malhotra</h3>
                <p>JC, ML Department</p>
            </div>
            """, unsafe_allow_html=True)
        linkedin_url = "https://www.linkedin.com/in/suryansh-malhotra-864a601b9"
        with open(linkedin_icon, "rb") as image_file:
            encoded_icon = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <div style="text-align: center;">
                <a href="{linkedin_url}" target="_blank">
                    <img src="data:image/png;base64,{encoded_icon}" alt="LinkedIn Icon" style="width:30px; height:30px;">
                </a>
            </div>
            """, unsafe_allow_html=True
        )
        
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
        ("Spotify","NBA Player Stats","Youtube Analytics")
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

        # Load the data
        st.title('NBA Player Performance Analysis')
        df = load_nba_data()

        # Dataset Overview
        st.header('Dataset Overview')
        st.write(df.head())

        # 4. Top Players by Efficiency (Field Goal %, 3-Point %, and Defensive Rating)
        st.header('Top Players by Efficiency')
        efficiency_players = df[['PLAYER_NAME', 'FG_PCT', 'FG3M', 'FG3A', 'DEF_RATING_RANK']].copy()
        efficiency_players['3P_PCT'] = efficiency_players['FG3M'] / efficiency_players['FG3A']
        top_efficiency_players = efficiency_players.sort_values(by=['FG_PCT', '3P_PCT'], ascending=False).head(10)

        st.write(top_efficiency_players)

        # 1. Home vs Away Performance Comparison
        st.header('Home vs. Away Performance Comparison')
        home_away_performance = df.groupby(['LOCATION', 'PLAYER_NAME']).agg({
            'PTS': 'mean', 'AST': 'mean', 'REB': 'mean', 'FG_PCT': 'mean'
        }).reset_index()

        home_performance = home_away_performance[home_away_performance['LOCATION'] == 'HOME']
        away_performance = home_away_performance[home_away_performance['LOCATION'] == 'AWAY']

        st.subheader('Home Performance')
        st.write(home_performance.sort_values(by='PTS', ascending=False).head(10))

        st.subheader('Away Performance')
        st.write(away_performance.sort_values(by='PTS', ascending=False).head(10))

        # 2. Team Performance Analysis
        st.header('Team Performance Analysis')
        team_performance = df.groupby('TEAM_NAME_x').agg({
            'PTS': 'mean', 'AST': 'mean', 'REB': 'mean', 'DEF_RATING_RANK': 'mean'
        }).reset_index()

        st.write(team_performance.sort_values(by='PTS', ascending=False).head(10))

        # 5. Player Consistency Analysis
        st.header('Player Consistency Analysis (Variance in Points, Assists, Rebounds)')
        player_consistency = df.groupby('PLAYER_NAME').agg({
            'PTS': 'var', 'AST': 'var', 'REB': 'var'
        }).reset_index()

        player_consistency.columns = ['PLAYER_NAME', 'PTS_VARIANCE', 'AST_VARIANCE', 'REB_VARIANCE']
        top_consistent_players = player_consistency.sort_values(by=['PTS_VARIANCE', 'AST_VARIANCE', 'REB_VARIANCE']).head(10)

        st.write(top_consistent_players)

    elif dataset_choice == "Youtube Analytics":
        @st.cache_data
        def load_data():
            try:
            # Try reading the CSV file with 'utf-8' encoding first
                return pd.read_csv('Youtube Analytics/Global Youtube Statistics.csv', encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    # If utf-8 fails, try reading with 'ISO-8859-1' (Latin-1) encoding
                    return pd.read_csv('Youtube Analytics/Global Youtube Statistics.csv', encoding='ISO-8859-1')
                except UnicodeDecodeError:
                    # If both fail, try 'utf-16' encoding
                    return pd.read_csv('Youtube Analytics/Global Youtube Statistics.csv', encoding='utf-16')

        df = load_data()

        # Check if the necessary columns exist in the dataset to avoid errors
        st.header('Top 10 YouTubers by Subscribers')
        top_youtubers = df[['Youtuber', 'subscribers']].sort_values(by='subscribers', ascending=False).head(10)
        st.write(top_youtubers)

        # 2. Correlation Between Subscribers, Video Views, and Earnings
        st.header('Correlation Between Subscribers, Video Views, and Earnings')
        correlation_data = df[['subscribers', 'video views', 'lowest_yearly_earnings', 'highest_yearly_earnings']].corr()
        st.write(correlation_data)

        # 3. Top 10 Countries by Total YouTube Views
        st.header('Top 10 Countries by Total YouTube Views')
        top_countries = df.groupby('Country')['video views'].sum().sort_values(ascending=False).head(10)
        st.write(top_countries)

        # 5. Category-wise Average Subscribers
        st.header('Average Subscribers by Video Category')
        category_avg_subscribers = df.groupby('category')['subscribers'].mean().sort_values(ascending=False)
        st.write(category_avg_subscribers)

        # 6. Viewer Engagement Analysis (Subscribers vs Video Views)
        st.header('Viewer Engagement Analysis (Subscribers vs Video Views)')
        df['Views_to_Subscribers'] = df['video views'] / df['subscribers']
        engagement_data = df[['Youtuber', 'Views_to_Subscribers']].sort_values(by='Views_to_Subscribers', ascending=False).head(10)
        st.write(engagement_data)

        # 8. Distribution of Channel Types (Pie Chart)
        st.header('Distribution of Channel Types')

        # Get the channel type distribution
        channel_type_distribution = df['channel_type'].value_counts(dropna=False)

        # Calculate the total and percentage
        total = channel_type_distribution.sum()
        channel_type_distribution_percent = (channel_type_distribution / total) * 100

        # Group categories with less than 3% into 'Other'
        other_threshold = 3
        small_categories = channel_type_distribution_percent[channel_type_distribution_percent < other_threshold].index
        channel_type_distribution_grouped = channel_type_distribution.copy()

        channel_type_distribution_grouped.loc[small_categories] = 'Other'
        channel_type_distribution_grouped = channel_type_distribution_grouped.value_counts()

        # Plot pie chart
        fig, ax = plt.subplots()
        ax.pie(channel_type_distribution_grouped, labels=channel_type_distribution_grouped.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the pie chart in Streamlit
        st.pyplot(fig)

        # 9. Distribution of YouTube Channels by Country (Pie Chart)
        st.header('Distribution of YouTube Channels by Country')

        # Count the number of channels by country
        country_distribution = df['Country'].value_counts(dropna=False)

        # Calculate total number of channels
        total_channels = country_distribution.sum()

        # Create a threshold for categorizing smaller countries as "Others"
        threshold = 0.02  # 2%
        small_countries = country_distribution[country_distribution / total_channels < threshold]

        # Aggregate small countries into "Others"
        if not small_countries.empty:
            others_count = small_countries.sum()
            country_distribution = country_distribution[country_distribution / total_channels >= threshold]
            country_distribution['Others'] = others_count

        # Plot the pie chart
        fig2, ax2 = plt.subplots()
        ax2.pie(country_distribution, labels=country_distribution.index, autopct='%1.1f%%', startangle=90)
        ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig2)