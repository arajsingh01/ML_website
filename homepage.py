import streamlit as st
from PIL import Image


def resize_image(image_path, width, height):
    img = Image.open(image_path)
    resized_img = img.resize((width, height))
    return resized_img

st.set_page_config(page_title="DevComm ML Project", layout="wide")

st.title("Welcome to DevComm ML Nexus")
st.subheader("An Integrated Platform for Machine Learning and Data Analysis")

st.write("""
👋 Hi there! Curious about Machine Learning and Data Analysis? You're in the right place! 
Welcome to DevComm ML Nexus — a hub where you can explore different ML models, try out data analysis projects, and even test them yourself.

🚀 Want to create your own models? This project gives you a glimpse of what's possible, and next year, when you become part of the Junior Council, you'll get the chance to add *your* own models here. 📈 Add your name to the contributors list and flex it with pride! 💪

So go ahead, explore, learn, and most importantly, have fun! 🎉 Happy Learning! 💡
""")

st.write("## Explore the Project")

st.write("Click on the page named App in sidebar to access the main application.")



st.write("## Project Goals")
st.write("""
- **Model Development:** Implement multiple machine learning models to solve real-world problems.
- **Data Analysis:** Provide comprehensive data insights through visualizations and metrics.
- **Collaboration:** Encourage collaboration among DevComm society members.
""")

st.write("---")

st.markdown(
    """
    <style>
    .container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f9f9f9;
        padding: 10px 50px;
        width: 100%;
    }
    .footer, .contact {
        flex: 1;
        text-align: center;
    }
    .footer {
        color: black;
    }
    .contact {
        font-size: 18px;
    }
    .contact a {
        text-decoration: none;
        font-weight: bold;
    }
    .contact .linkedin {
        color: #1DA1F2;
    }
    .contact .instagram {
        color: #F2087C;
    }
    .contact a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <div class="container">
        <div class="footer">
            <p>© 2024 DevComm. All Rights Reserved.</p>
            <p>Made with ❤️ using Streamlit</p>
        </div>
        <div class="contact">
            <h3 style="color:black;">🌐 Connect with Us</h3>
            <p style="color:black;">
                Follow us on our social platforms: <br>
                <a href="https://www.linkedin.com/company/devcommnsut/" target="_blank" class="linkedin">LinkedIn</a> |
                <a href="https://www.instagram.com/devcomm.nsut/" target="_blank" class="instagram">Instagram</a>
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True
)
