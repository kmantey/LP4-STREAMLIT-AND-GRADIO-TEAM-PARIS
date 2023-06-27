import pandas as pd
import streamlit as st 
import pickle 
from PIL import Image

st.set_page_config(
    page_title="TEAM PARIS STREAMLIT APP")

st.title('Home Page')
st.sidebar.success("Select a page above")
st.header('''WELCOME TO TEAM PARIS STREAMLIT APP
''' )

# Importing LP2 Model 
#LINEAR REGRESSION MODEL 
pickle_in1 = open("C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 - STREAMLIT -- TEAM PARIS/src/model22.pkl","rb")
model22 = pickle.load(pickle_in1)


# define a function with our regression model
def run_regression (date, dcoilwitco , id,promotion,store_nbr, transactions):
    # Use the extracted values as features in your regression model
    #prediction = model22.predict([[year, month, day, dcoilwitco, id, promotion, store_nbr, transactions]])
    prediction = model22.predict([[ordinal_date, dcoilwitco , id,promotion,store_nbr, transactions]])
    print(prediction)
    return(prediction)

# Inser welcoming descriptive image
image = Image.open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 - STREAMLIT -- TEAM PARIS/src/sales.png')
st.image(image, caption = 'SALES PREDICTION / ANALYSIS TEAM PARIS', use_column_width=True)

# Ask for user input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Welcome, {name}, to **Team Paris** Streamlit app.:smiling_face_with_tear:")
    st.write("Here we will have two projects to work on.:slot_machine:")
    st.write("**Project 1** is a Time Series Machine Learning model used to predict **Sales** with different variables.")
    st.write("**Project 2** is a Regression project focused on churn analysis and predicts a **YES/NO** based on existing input data.")
    st.write()

project = st.selectbox(" **Select the Project to classify**", ["Time Series problem","Regression Project", "None"])

if project and project != "None":
    if project == "Time Series problem":
        st.subheader("Time Series Challenge")
        st.write('''This is a Time Series Problem.
                 Here we want to predict the sales price based on your input data''')
        date = st.date_input("Select a date")
        ordinal_date = date.toordinal()
        # Assuming `date` is a `datetime.date` object
        year = date.year
        month = date.month
        day = date.day
        dcoilwitco = st.number_input("Enter the dcoilwitco value ", min_value= 0, max_value= 35)
        id = st.slider ( "What is the likely customer Id (14792 onwards)", min_value = 13999, max_value=3999999 )
        promotion = st.slider( "Is the product on promotion, if **YES** slide through to the promotion value, If **NO** set it to value 0 (between 0-677)" ,min_value=0, max_value=677)
        store_nbr = st.number_input ("What is the store number ")
        transactions = st.number_input ("What is the number of transactions yearly")
        result = ""
        if st.button("See selected variables"):
            df1 = pd.DataFrame (
                {
                'date' : [date], 'dcoilwitco' : [dcoilwitco], 'id' : [id], 'promotion' : [promotion],'store_nbr' : [store_nbr], 'transactions' : ['transactions']
                }
            )
            st.write(df1)
        if st.button("Predict"):
            result = run_regression (date, dcoilwitco , id,promotion,store_nbr, transactions)
            #st.write = ("your predicted result is :"{date}, result)



    if project == "Regression Project":
        st.subheader("Regression Challenge")
        st.write('''This is a **Regression Problem**.
                 Here we want to predict the sales price based on your input data''')
        senior_citizen = st.selectbox("Is the customer a senior citizen", [0, 1])
        dependents = st.selectbox("Does the customer have dependents ", ['Yes', 'No'])
        phone_service = st.selectbox("Does the customer have a phone service", ['Yes', 'No'])
        multiple_lines = st.selectbox("Is the customer on Multiple Lines", ['No','No Phone Service'])
        Internet_service = st.selectbox(" ", ['DSL', 'FibreOptic', 'No'])
        online_security = st.selectbox(" Does the customer use online security" ,['Yes', 'No'])
        online_backup = st.selectbox("Does the customer use an Online Back up",['Yes', 'No'])
        device_protection = st.selectbox("Does the customer have a device protection",['Yes', 'No'])
        tech_support = st.selectbox('Does the customer use tech support services', ['Yes', 'No'])
        streaming_tv = st.selectbox("Does the customer stream TV",['Yes', 'No'])
        contract = st.selectbox("Which contract bouquet are these people on ", ['Yes', 'No', '2 year contract'])
        paperless_billing = st.selectbox("Is the payment method paperless ",['Yes', 'No'])
        monthly_charges = st.slider("What is the customer's monthly charges ", min_value=20, max_value=100 )
        total_charge = st.slider ("What is the customers total Charges", min_value= 20, max_value=3000)
        if st.button("See selected variables"):
            df2 = pd.DataFrame (
                {
                "senior_citizen ": [senior_citizen ], dependents : ['dependents'], phone_service : ['phone_service'], multiple_lines : ['multiple_lines'],Internet_service : ['Internet_service'], online_security : ['online_security'], online_backup : ['online_backup'], device_protection: ['device_protection'], tech_support : ['tech_support'], streaming_tv: ['streaming_tv'], contract:['contract'], paperless_billing:['paperless_billing'],monthly_charges:['monthly_charges'],  total_charge:['total_charge']
                }
            )
            st.write(df2)
        
    if project == "None":
        st.write("Sorry, There's no other option available here")

