import pandas as pd
import numpy as np
import streamlit as st 
# models use files 
import pickle 
# Visualization folders 
from PIL import Image
import matplotlib.pyplot as plt
# Scalers 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import category_encoders as ce
from datetime import date

# Create instance of imputer and scaler 
scaler = StandardScaler()
imputer = SimpleImputer()
# Load the .pkl files
# Model 1
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/model22.pkl', 'rb') as file:
    model1 = pickle.load(file)
# Model 2
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/ARIMA.pkl', 'rb') as file:
    model2 = pickle.load(file)
# Model 3
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/xgb_model.pkl', 'rb') as file:
    model3 = pickle.load(file)


#LINEAR REGRESSION MODEL 
pickle_in1 = open("C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 - STREAMLIT -- TEAM PARIS/src/model22.pkl","rb")
model22 = pickle.load(pickle_in1)
# LOAD the preprocessing used in the training 
# 1 category encoders 
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/category_encoder_object.pkl', 'rb') as file:
    imputer = pickle.load(file)
# 2. Standard Scaler 
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/standard_scaler_object.pkl', 'rb') as file:
    scaler = pickle.load(file)
# 3. Simple Imputer 
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/imputer_object.pkl', 'rb') as file:
    encoder = pickle.load(file)


# Define function for model 1

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

# Define function for model 1
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
# Define function for model 2
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
# Define function for model 3
def run_model3(ordinal_date, dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday):
    transformed_data = [[ordinal_date, dcoilwitco, promotion, store_nbr, transactions, family, city, state, cluster, holiday]]
    if imputer is not None:
        transformed_data = imputer.transform(transformed_data)

    if scaler is not None:
        transformed_data = scaler.transform(transformed_data)

    if encoder is not None:
        transformed_data = encoder.transform(transformed_data)

    prediction3 = model2.predict(transformed_data)
    return prediction3


st.set_page_config(
    page_title="TEAM PARIS STREAMLIT APP")
spanner = "\U0001F527"

# Take in user input 
date1 = st.date_input("Select a date for Model 1", key="date1_key")
ordinal_date = date1.toordinal()
# Assuming `date` is a `datetime.date` object
year = date1.year
month = date1.month
day = date1.day
dcoilwitco2 = st.number_input("Enter the dcoilwitco value ", min_value= 0, max_value= 35)
#id = st.slider ( "What is the likely customer Id (14792 onwards)", min_value = 13999, max_value=3999999 )
promotion2 = st.slider( "Is the product on promotion, if **YES** slide through to the promotion value, If **NO** set it to value 0 (between 0-677)" ,min_value=0, max_value=677)
store_nbr2 = st.number_input ("What is the store number ")
transactions2 = st.number_input ("What is the number of transactions yearly")
family2 = st.selectbox(" Which family does the product belong to", ['AUTOMOTIVE', 'BABYCARE', 'BEAUTY', 'BEVERAGES', 'BOOKS', 'POULTRY', 'PREPARED FOODS', 'SCHOOL AND OFFICE SUPPLIES'])
city2 = st.selectbox("Which city is our produc from", ['Quito', 'Guayaquil', 'Ambato', 'Cuenca', 'Santo Domingo', 'Cayambe', 'Machala', 'Latacunga', 'Loja', 'Daule', 'Babahoyo', 'Riobamba', 'Ibarra', 'Esmeraldas', 'Guaranda', 'Quevedo', 'Libertad', 'Salinas', 'Manta', 'El Carmen', 'Playas', 'Puyo'])
state2 = st.selectbox("Select the state which the product comes from ",['Pichincha', 'Guayas', 'Tungurahua',  'Azuay', 'Santo Domingo de los Tsachilas', 'Los Rios', 'El Oro', 'Cotopaxi','Manabi',  'Loja',  'Chimborazo ',  'Imbabura',  'Esmeraldas','Bolivar' 'Pastaza' ])
store_type2 = st.selectbox ("Select the store type ", ["A", "B", "C", "D"])
cluster2 = st.number_input("Enter the cluster of the product", min_value= 0, max_value= 35)
holiday2 = st.selectbox("On which holiday does our product fall", ["Holiday", "Event", "Additional", "Transfer", "Bridge", "Workday"])
result2 = ""
if st.button("See selected variables"):
    df11 = pd.DataFrame (
                {
                'date' : [date1], 'dcoilwitco' : [dcoilwitco2], 'promotion' : [promotion2],'store_nbr' : [store_nbr2], 'transactions' : [transactions2], 'family2' :[family2], 'city2' : [city2], 'state2': [state2], 'cluster2':[cluster2], 'holiday2':[holiday2]
                }
            )
    st.write(df11.T)
    # Convert the dictionary values to a list
    #values = [value for value in df11.values()]
    #values2 = [value for value in df11.values()]
    #st.write(values2)
    if st.button('Make Predictions'):
        
        result2 = model1 (ordinal_date,  dcoilwitco2, promotion2, store_nbr2, transactions2 , family2, city2, state2 , cluster2,holiday2)
        st.write(result2)
    st.write(result2)
        # # Apply SimpleImputer if applicable
        # if imputer is not None:
        #     values2 = imputer.transform(values2)

        # # Apply StandardScaler if applicable
        # if scaler is not None:
        #     values2 = scaler.transform(values2)

        # # Apply CategoryEncoders if applicable
        # if encoder is not None:
        #     values2 = encoder.transform(values2)
        # # Assign the transformed values back to the dictionary
        # transformed_data = {key: value for key, value in zip(values2.keys(), values2)}
        # st.write(transformed_data)
        # prediction1 = model1.predict(transformed_data)
        # prediction2 = model2.predict(transformed_data)
        # prediction3 = model3.predict(transformed_data)
        # st.write("Prediction 1:", prediction1)
        # st.write("Prediction 2:", prediction2)
        # st.write("Prediction 3:", prediction3)
#if st.button("Predict"):
           # result = run_regression (date, dcoilwitco , id,promotion,store_nbr, transactions)

    #if st.button("Predict"):
     #   result = run_ARIMA (date1, store_nbr2, family2, promotion2, transactions2, holiday2, dcoilwitco2, city2 ,state2, store_type2, cluster2)
      #  st.write = ("your predicted result is :", result)
       # st.write(result)
# st.markdown("<hr>", unsafe_allow_html=True)
# st.title('Linear Regression')
# st.write(spanner, spanner, spanner , spanner, spanner, spanner, spanner, spanner , spanner, spanner, spanner, spanner)
# st.markdown("<hr>", unsafe_allow_html=True)


# st.subheader("Time Series Challenge")
# st.write('''This is a Time Series Problem.
# Here we want to predict the sales price based on your input data but use a different model''')
# date = st.date_input("Select a date")
# ordinal_date = date.toordinal()
# # Assuming `date` is a `datetime.date` object
# year = date.year
# month = date.month
# day = date.day
# dcoilwitco = st.number_input("Enter the dcoilwitco value ", min_value= 0, max_value= 35)
# id = st.slider ( "What is the likely customer Id (14792 onwards)", min_value = 13999, max_value=3999999 )
# promotion = st.slider( "Is the product on promotion, if **YES** slide through to the promotion value, If **NO** set it to value 0 (between 0-677)" ,min_value=0, max_value=677)
# store_nbr = st.number_input ("What is the store number ")
# transactions = st.number_input ("What is the number of transactions yearly")
# result = ""
# if st.button("See selected variables"):
#     df2 = pd.DataFrame (
#                 {
#                 'date' : [date], 'dcoilwitco' : [dcoilwitco], 'id' : [id], 'promotion' : [promotion],'store_nbr' : [store_nbr], 'transactions' : ['transactions']
#                 }
#             )
# st.write(df2)