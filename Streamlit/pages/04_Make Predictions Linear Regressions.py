import pandas as pd
import streamlit as st 
import pickle 
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Importing Models 
# Model 1
pickle_in1 = open("C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 - STREAMLIT -- TEAM PARIS/src/model22.pkl","rb")
linear_reg = pickle.load(pickle_in1)
# Model 2
pickle_in2 = open("C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/ARIMA.pkl","rb")
ARIMA = pickle.load(pickle_in2)

# Model 3
pickle_in3 = open("C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/xgb_model.pkl","rb")
xgb_model = pickle.load(pickle_in3)

# Model 4 
# pickle_in5 = open("C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/model22.pkl","rb")
# model22 = pickle.load(pickle_in1)


# define a function with our regression model
def run_regression (date, dcoilwitco , id,promotion,store_nbr, transactions):
    # Use the extracted values as features in your regression model
    #prediction = model22.predict([[year, month, day, dcoilwitco, id, promotion, store_nbr, transactions]])
    prediction = model22.predict([[ordinal_date, dcoilwitco , id,promotion,store_nbr, transactions]])
    print(prediction)
    return(prediction)

# Define function for linear reg model 2 
def run_regression2 (date ,store_nbr, family, promotion , transactions , holiday_type,  dcoilwitco , city, state, store_type, cluster):
    # Use the extracted values as features in your regression model
    #prediction = model22.predict([[year, month, day, dcoilwitco, id, promotion, store_nbr, transactions]])
    prediction = linear_reg.predict([[ordinal_date, dcoilwitco , id,promotion,store_nbr, transactions]])
    print(prediction)
    return(prediction)

# Define function for ARIMA model 3 
def run_regression2 (date ,store_nbr, family, promotion , transactions , holiday_type,  dcoilwitco , city, state, store_type, cluster):
    # Use the extracted values as features in your regression model
    #prediction = model22.predict([[year, month, day, dcoilwitco, id, promotion, store_nbr, transactions]])
    prediction2 = ARIMA.predict([[ordinal_date, dcoilwitco , id,promotion,store_nbr, transactions]])
    print(prediction2)
    return(prediction2)

# Define function for XGB Boost Model 4
def run_regression2 (date ,store_nbr, family, promotion , transactions , holiday_type,  dcoilwitco , city, state, store_type, cluster):
    # Use the extracted values as features in your regression model
    #prediction = model22.predict([[year, month, day, dcoilwitco, id, promotion, store_nbr, transactions]])
    prediction3 = xgb_model.predict([[ordinal_date, dcoilwitco , id,promotion,store_nbr, transactions]])
    print(prediction3)
    return(prediction3)


st.set_page_config(
    page_title="TEAM PARIS STREAMLIT APP")
spanner = "\U0001F527"

st.markdown("<hr>", unsafe_allow_html=True)
st.write(''' # MODELS USED 
    1. ARIMA Models 
    2. Linear Regression Model
    3. XGB Boost
''')
computer_emoji = "\U0001F4BB"
st.write(computer_emoji, computer_emoji, computer_emoji, computer_emoji, computer_emoji, computer_emoji, computer_emoji, computer_emoji, computer_emoji)
st.markdown("<hr>", unsafe_allow_html=True)

# Ask for user input
# name = st.text_input("Enter your name:")
# if name:
#     st.write(f"Welcome, {name}, to **Team Paris** Streamlit app.:smiling_face_with_tear:")
#     st.write("Here we will have two projects to work on.:slot_machine:")
#     st.write("**Project 1** is a Time Series Machine Learning model used to predict **Sales** with different variables.")
#     st.write("**Project 2** is a Regression project focused on churn analysis and predicts a **YES/NO** based on existing input data.")
#     st.write()

st.subheader("Linear Regression Model with less features")
st.write('''This is a Time Series Problem.
Here we want to predict the sales price based on your input data''')
date2 = st.date_input("Select a date for Model 1", key="date2_key")
ordinal_date = date2.toordinal()
# Assuming `date` is a `datetime.date` object
year = date2.year
month = date2.month
day = date2.day
dcoilwitco1 = st.number_input("Enter the dcoilwitco value ", min_value= 0, max_value= 35)
id1 = st.slider ( "What is the likely customer Id (14792 onwards)", min_value = 13999, max_value=3999999 )
promotion1 = st.slider( "Is the product on promotion, if **YES** slide through to the promotion value, If **NO** set it to value 0 (between 0-677)" ,min_value=0, max_value=677)
store_nbr1 = st.number_input ("What is the store number ")
transactions1 = st.number_input ("What is the number of transactions yearly")
result1 = ""
if st.button("See selected variables"):
    df1 = pd.DataFrame (
                {
                'date' : [date2], 'dcoilwitco' : [dcoilwitco1], 'id' : [id1], 'promotion' : [promotion1],'store_nbr' : [store_nbr1], 'transactions' : [transactions1]
                }
            )
    st.write(df1)
if st.button("Predict"):
    result = run_regression (date2,  dcoilwitco1,id1, promotion1,  store_nbr1, transactions1)
    st.write ("your predicted result is :", result)
    st.write(result)

st.subheader("Predictions using ARIMA MODEL")
#st.write('''This is a Time Series Problem.
#Here we want to predict the sales price based on your input data''')
date3 = st.date_input("Select a date")
ordinal_date = date3.toordinal()
# project = st.selectbox(" **Select the Project to classify**", ["Time Series problem","Regression Project", "None"])



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
state2 = st.selectbox ("Select the state which the product comes from " ['Pichincha', 'Guayas', 'Tungurahua',  'Azuay', 'Santo Domingo de los Tsachilas', 'Los Rios', 'El Oro', 'Cotopaxi','Manabi',  'Loja',  'Chimborazo ',  'Imbabura',  'Esmeraldas','Bolivar' 'Pastaza' ])
store_type2 = st.selectbox ("Select the store type ", ["A", "B", "C", "D"])
cluster2 = st.number_input("Enter the cluster of the product", min_value= 0, max_value= 35)
holiday2 = st.selectbox("On which holiday does our product fall", ["Holiday", "Event", "Additional", "Transfer", "Bridge", "Workday"])
result2 = ""
if st.button("See selected variables"):
    df11 = pd.DataFrame (
                {
                'date' : [date1], 'dcoilwitco' : [dcoilwitco2], 'id' : [id2], 'promotion' : [promotion2],'store_nbr' : [store_nbr2], 'transactions' : [transactions2]
                }
            )
    st.write(df11)
    if st.button("Predict"):
        result = run_ARIMA (date1, store_nbr2, family2, promotion2, transactions2, holiday2, dcoilwitco2, city2 ,state2, store_type2, cluster2)
        st.write = ("your predicted result is :", result)
        st.write(result)

st.subheader("Predictions using XG BOOST MODEL")
#st.write('''This is a Time Series Problem.
#Here we want to predict the sales price based on your input data''')
date4 = st.date_input("Select a date")
ordinal_date = date4.toordinal()
# project = st.selectbox(" **Select the Project to classify**", ["Time Series problem","Regression Project", "None"])


date4 = st.date_input("Select a date")
ordinal_date4 = date4.toordinal()
# Assuming `date` is a `datetime.date` object
year = date4.year
month = date4.month
day = date4.day
dcoilwitco4 = st.number_input("Enter the dcoilwitco value ", min_value= 0, max_value= 35)
#id = st.slider ( "What is the likely customer Id (14792 onwards)", min_value = 13999, max_value=3999999 )
promotion4 = st.slider( "Is the product on promotion, if **YES** slide through to the promotion value, If **NO** set it to value 0 (between 0-677)" ,min_value=0, max_value=677)
store_nbr4 = st.number_input ("What is the store number ")
transactions4 = st.number_input ("What is the number of transactions yearly")
family4 = st.selectbox(" Which family does the product belong to", ['AUTOMOTIVE', 'BABYCARE', 'BEAUTY', 'BEVERAGES', 'BOOKS', 'POULTRY', 'PREPARED FOODS', 'SCHOOL AND OFFICE SUPPLIES'])
city4 = st.selectbox("Which city is our produc from", ['Quito', 'Guayaquil', 'Ambato', 'Cuenca', 'Santo Domingo', 'Cayambe', 'Machala', 'Latacunga', 'Loja', 'Daule', 'Babahoyo', 'Riobamba', 'Ibarra', 'Esmeraldas', 'Guaranda', 'Quevedo', 'Libertad', 'Salinas', 'Manta', 'El Carmen', 'Playas', 'Puyo'])
state4 = st.selectbox ("Select the state which the product comes from " ['Pichincha', 'Guayas', 'Tungurahua',  'Azuay', 'Santo Domingo de los Tsachilas', 'Los Rios', 'El Oro', 'Cotopaxi','Manabi',  'Loja',  'Chimborazo ',  'Imbabura',  'Esmeraldas','Bolivar' 'Pastaza' ])
store_type4 = st.selectbox ("Select the store type ", ["A", "B", "C", "D"])
cluster4 = st.number_input("Enter the cluster of the product" , min_value= 0, max_value= 35)
holiday4 = st.selectbox("On which holiday does our product fall", ["Holiday", "Event", "Additional", "Transfer", "Bridge", "Workday"])
result4 = ""
if st.button("See selected variables"):
    df4 = pd.DataFrame (
                {
                'date' : [date4], 'dcoilwitco' : [dcoilwitco4], 'id' : [id4], 'promotion' : [promotion],'store_nbr' : [store_nbr], 'transactions' : ['transactions']
                }
            )
    st.write(df4)
    if st.button("Predict"):
        result = run_xgb(date, store_nbr, family, promotion, transactions, holiday, dcoilwitco, city ,state, store_type, cluster)
        st.write = ("your predicted result is :", result)
        st.write(result)


#     if project == "Regression Project":
#         st.subheader("Regression Challenge")
#         st.write('''This is a **Regression Problem**.
#                  Here we want to predict the sales price based on your input data''')
#         senior_citizen = st.selectbox("Is the customer a senior citizen", [0, 1])
#         dependents = st.selectbox("Does the customer have dependents ", ['Yes', 'No'])
#         phone_service = st.selectbox("Does the customer have a phone service", ['Yes', 'No'])
#         multiple_lines = st.selectbox("Is the customer on Multiple Lines", ['No','No Phone Service'])
#         Internet_service = st.selectbox(" ", ['DSL', 'FibreOptic', 'No'])
#         online_security = st.selectbox(" Does the customer use online security" ,['Yes', 'No'])
#         online_backup = st.selectbox("Does the customer use an Online Back up",['Yes', 'No'])
#         device_protection = st.selectbox("Does the customer have a device protection",['Yes', 'No'])
#         tech_support = st.selectbox('Does the customer use tech support services', ['Yes', 'No'])
#         streaming_tv = st.selectbox("Does the customer stream TV",['Yes', 'No'])
#         contract = st.selectbox("Which contract bouquet are these people on ", ['Yes', 'No', '2 year contract'])
#         paperless_billing = st.selectbox("Is the payment method paperless ",['Yes', 'No'])
#         monthly_charges = st.slider("What is the customer's monthly charges ", min_value=20, max_value=100 )
#         total_charge = st.slider ("What is the customers total Charges", min_value= 20, max_value=3000)
#         if st.button("See selected variables"):
#             df2 = pd.DataFrame (
#                 {
#                 "senior_citizen ": [senior_citizen ], dependents : ['dependents'], phone_service : ['phone_service'], multiple_lines : ['multiple_lines'],Internet_service : ['Internet_service'], online_security : ['online_security'], online_backup : ['online_backup'], device_protection: ['device_protection'], tech_support : ['tech_support'], streaming_tv: ['streaming_tv'], contract:['contract'], paperless_billing:['paperless_billing'],monthly_charges:['monthly_charges'],  total_charge:['total_charge']
#                 }
#             )
#             st.write(df2)
        
#     if project == "None":
#         st.write("Sorry, There's no other option available here")