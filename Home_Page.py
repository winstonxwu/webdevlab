import streamlit as st

# Title of App
st.title("Web Development Lab01")

base="light"
backgroundColor="white"
secondaryBackgroundColor="lavender"
codeBackgroundColor="powderBlue"

st.set_page_config(
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Web Development - Section C")
st.subheader("Winston Wu")


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to our Streamlit Web Development Lab01 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. **Winston's Portfolio**: A portfolio page to show my background, experience, and skills.
2. **Media Quiz**: A short, fun quiz about favorite movie, music, and book genres!
""")

st.subheader("Elevator music to keep you company:")
spanish_flea = st.audio("Images/Spanish Flea (Herb Alpert).mp3", format="audio/mpeg", loop=True, autoplay=True)

