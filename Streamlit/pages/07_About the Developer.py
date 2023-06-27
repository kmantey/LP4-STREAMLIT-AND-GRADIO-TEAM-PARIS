import streamlit as st 
from PIL import Image
import pandas as pd

st.header('''ABOUT THE DEVELOPERS
             MORE INFORMATION ON THE PROJECT
             THIS APP HAS BEEN DEVELOPED BY AZUBI STUDENTS TEAM PARIS
''' )
st.markdown(
    "###### Made with streamlit app [![Streamlit](https://your_streamlit_image_link.png)](https://your_streamlit_link) :fire: :fire: :fire: "
    "follow the converation on linkedIn concerning our app[![Twitter](https://your_twitter_image_link.png)](https://your_twitter_link) "
    "see the gitub link to the repository with all the files [LinkedIn](https://www.linkedin.com)"
)
# Inser welcoming descriptive image
image3 = Image.open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/authors2.png')
st.image(image3, caption = 'SALES PREDICTION / ANALYSIS TEAM PARIS', use_column_width=True)




st.write('''
Elly Okumu \n
Awudu Jamal\n
Jonas Afutu\n
Vincent Kipkorir \n
David Mantey \n
''')

import pandas as pd
import numpy as np
import streamlit as st
import pickle
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import category_encoders as ce

# Load the models
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/model22.pkl', 'rb') as file:
    model1 = pickle.load(file)

with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/ARIMA.pkl', 'rb') as file:
    model2 = pickle.load(file)

with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/xgb_model.pkl', 'rb') as file:
    model3 = pickle.load(file)

# Load the preprocessing objects
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/category_encoder_object.pkl', 'rb') as file:
    encoder = pickle.load(file)

with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/standard_scaler_object.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/imputer_object.pkl', 'rb') as file:
    imputer = pickle.load(file)

def run_regression2(date, dcoilwitco, id, promotion, store_nbr, transactions):
    ordinal_date = date.toordinal()
    transformed_data = [[ordinal_date, dcoilwitco, id, promotion, store_nbr, transactions]]
    if imputer is not None:
        transformed_data = imputer.transform(transformed_data)

    if scaler is not None:
        transformed_data = scaler.transform(transformed_data)

    if encoder is not None:
        transformed_data = encoder.transform(transformed_data)

    prediction1 = model1.predict(transformed_data)
    return prediction1

def run_model1(ordinal_date, dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday):
    transformed_data = [[ordinal_date, dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday]]
    if imputer is not None:
        transformed_data = imputer.transform(transformed_data)

    if scaler is not None:
        transformed_data = scaler.transform(transformed_data)

    if encoder is not None:
        transformed_data = encoder.transform(transformed_data)

    prediction1 = model1.predict(transformed_data)
    return prediction1

def run_model2(ordinal_date, dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday):
    transformed_data = [[ordinal_date, dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday]]
    if imputer is not None:
        transformed_data = imputer.transform(transformed_data)

    if scaler is not None:
        transformed_data = scaler.transform(transformed_data)

    if encoder is not None:
        transformed_data = encoder.transform(transformed_data)

    prediction2 = model2.predict(transformed_data)
    return prediction2

def run_model3(ordinal_date, dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday):
    transformed_data = [[ordinal_date, dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday]]
    if imputer is not None:
        transformed_data = imputer.transform(transformed_data)

    if scaler is not None:
        transformed_data = scaler.transform(transformed_data)

    if encoder is not None:
        transformed_data = encoder.transform(transformed_data)

    prediction3 = model3.predict(transformed_data)
    return prediction3

# Take user input
date = pd.Timestamp('2023-06-16')
dcoilwitco = 1.25
id = 12345
promotion = 1
store_nbr = 10
transactions = 1000
family = "Bread"
city = "New York"
state = "New York"
cluster = 1
holiday = 0

prediction1 = run_regression2(date, dcoilwitco, id, promotion, store_nbr, transactions)
prediction2 = run_model1(date.toordinal(), dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday)
prediction3 = run_model2(date.toordinal(), dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday)

print("Prediction 1:", prediction1)
print("Prediction 2:", prediction2)
print("Prediction 3:", prediction3)
