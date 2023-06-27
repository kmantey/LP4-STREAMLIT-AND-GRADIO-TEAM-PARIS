import pandas as pd
import streamlit as st 
import pickle 
from PIL import Image

st.set_page_config(
    page_title="TEAM PARIS STREAMLIT APP")
spanner = "\U0001F527"

st.markdown("<hr>", unsafe_allow_html=True)
st.title('About the app')
st.write(spanner, spanner, spanner , spanner, spanner, spanner, spanner, spanner , spanner, spanner, spanner, spanner)
st.markdown("<hr>", unsafe_allow_html=True)
st.write('''
To get a good overview of what the app does, we shall answer the following question: 
1. Who can use the app ? 
2. Why use the app ? 
3. What Questions does the app answer ?
4. What problems does the problem help solve ?
5. What solution does the app offer ? 
''')

st.write('''
 ### Who can use the app. 
Using the app does not need any Tech backround or knowledge. Therefore anyone in understanding, predicting, visualizing the trends of the oil prices can use the app. 

### Why use the app 
To learn
Make predictive analysis
Visualize trends , seasonality and patterns

### What Questions does the App answer
What is the most likely average price of oil for a specific date, week or even month
What is the most likely future general trend of oil prices in a future week, date or even month

### Scope Of use
Therefore business enthusiats , business analysts , staticicians and mathematicians in conjuction with general managers can use the app to make informed business decisions. 
Marketting salespersons can also use the app to forecast the rise and fall of oil prices thereby levereging on them. 
Operations managers can use the app to make sure they have enought stock in the event of a negative price surge and capital on the same also 
''')

st.header("The dataset used to build the Models")

st.write('''
The Models to be used here are 2 models Model 1 is Linear Regression and Model 2 is a SARIMA Model
''')

st.header(' Datasets')
st.write('''
### 1. Holiday Events dataset
''')
image2 = Image.open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/holiday.png')
st.image(image2, caption = 'SALES PREDICTION / ANALYSIS TEAM PARIS', use_column_width=False)
st.write(''' *Here* the dataset has all the holiday events from 2013 - 2017
Columns are as follows 
* type        -  lists the holiday as either holiday or Additional
* locale      - listsed as either National, Local or Regional
* locale name - lists 25 locations to choose from , spanning from Equado to cayambe 
* description - Describes the Holday as either transfered or not 
''')


st.write('''
### 2. Oil dataset
''')
image3 = Image.open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/oil.png')
st.image(image3, caption = 'SALES PREDICTION / ANALYSIS TEAM PARIS', use_column_width=False)

st.write(''' *Here* our dataset lists the dc_oil_WITCO_CoOperation oil value. 
              The value has a minimum value of 26.19, experienced immediately the 2017 earthquake
              The maximum value stood at 110.62 which was experienced before the earthquake
''')
st.write('''

### 3. Store dataset
''')
image4 = Image.open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/stores.png')
st.image(image4, caption = 'SALES PREDICTION / ANALYSIS TEAM PARIS', use_column_width=False)
st.write(''' *Here* we get the store information per country , per state and the number of state
             The store_nbr has 54 stores , with 25 total number of store listed. 19 of which are in Pivhincha state and Guayas has 11 entries , and the other entries share the other number of stores
             The city , Lists the number of stores per country 
             State - Lists the number of stores per state
             type - spanning from A - D , this one list the type of the company
             cluster - /This column was dropped as not relevant/
''')

st.write('''
### 4. Transactions dataset
''')
image5 = Image.open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/transactions.png')
st.image(image5, caption = 'SALES PREDICTION / ANALYSIS TEAM PARIS', use_column_width=False)
st.write('''*Here* We get the frequency of the transactions 
             store_nbr - we get the number of the store 
             transactions - Here we get the number of trancastions per store 
''')

st.write('''
### 5. COMBINED CSV
''')
# image5 = Image.open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4/src/transactions.png')
# st.image(image5, caption = 'SALES PREDICTION / ANALYSIS TEAM PARIS', use_column_width=False)
st.write('''
*Here* We combine our datasets and do the following to the combined data
     Cleaning 
     Missing Values handling 
     EDA analysis 
     Columns/feature dropping 
''')

st.markdown("<hr>", unsafe_allow_html=True)
