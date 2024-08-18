import streamlit as st
from PIL import Image
import base64
import pickle
import io

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
    ("Model 1", "Model 2", "Model 3")
)

# Function to load the model
def load_model(model_name):
    with open(f'models/{model_name}.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Display form and handle prediction based on selected model
if model_choice == "Model 1":
    st.header("Model 1: Example Name")
    feature_1 = st.text_input("Feature 1:")
    feature_2 = st.text_input("Feature 2:")
    if st.button("Predict"):
        model = load_model("model1")
        # Assume features are passed as a list
        prediction = model.predict([[feature_1, feature_2]])
        st.write("Prediction:", prediction)

elif model_choice == "Model 2":
    st.header("Model 2: Example Name")
    feature_a = st.text_input("Feature A:")
    feature_b = st.text_input("Feature B:")
    if st.button("Predict"):
        model = load_model("model2")
        prediction = model.predict([[feature_a, feature_b]])
        st.write("Prediction:", prediction)

elif model_choice == "Model 3":
    st.header("Model 3: Example Name")
    feature_x = st.text_input("Feature X:")
    feature_y = st.text_input("Feature Y:")
    if st.button("Predict"):
        model = load_model("model3")
        prediction = model.predict([[feature_x, feature_y]])
        st.write("Prediction:", prediction)