import streamlit as st 
import pandas as pd
import pickle 
from PIL import Image

st.set_page_config(
    page_title="TEAM PARIS STREAMLIT APP")

st.markdown("<hr>", unsafe_allow_html=True)
st.title('Home Page :rocket::rocket::rocket:')
st.markdown("<hr>", unsafe_allow_html=True)


st.header('''WELCOME TO TEAM PARIS STREAMLIT APP SALES PREDICTION APP
''' )

# Inser welcoming descriptive image
image = Image.open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 - STREAMLIT -- TEAM PARIS/src/sales.png')
st.image(image, caption = 'SALES PREDICTION / ANALYSIS TEAM PARIS', use_column_width=True)

st.write('Welcome to oil sales prediction sales app. This is a Machine Learning Graphical User platform where you get to use our built machine larning model')

# Ask for user input
name = st.text_input("Enter your name:")
email = st.text_input("Enter your email address:")

if name:
    st.write(f''' Congratulations {name} on your first step of making informed business 
             :bulb: :bulb:
''')
    st.write("")
    st.write(' Feel free to dive into our app, key in your data and get more insights on the oil prices by date')
    st.write("")
    st.write('To Continue select the second panel **THE ABOUT APP** on the left to get an more insights on the app before proceeding to the predictions part ')

st.write()
st.markdown("<hr>", unsafe_allow_html=True)
