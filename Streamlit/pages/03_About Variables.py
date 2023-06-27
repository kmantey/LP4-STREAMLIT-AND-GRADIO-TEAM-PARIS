import pandas as pd
import streamlit as st 
import pickle 
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#pip install pandas-profiling
#conda install -c conda-forge pandas-profiling

st.set_page_config(
    page_title="TEAM PARIS STREAMLIT APP")

st.markdown("<hr>", unsafe_allow_html=True)
st.title('About the variables to use')
st.markdown("<hr>", unsafe_allow_html=True)

st.header("BASIC EDA ANALYSIS ON THE LEARNING DATA")
st.markdown("<hr>", unsafe_allow_html=True)
st.write(''' #In our Training Dataset , This is how the variables related to each other 

''')

st.write(''' ## OIL Dataset 
               There was a year which experienced an earthquake, which explains the drastic decrease uin the oil prices 

''')
oil = pd.read_csv('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP2-FINAL-PROJECT---TEAM-PARIS/oil.csv')

x = oil['date']
y = oil['dcoilwtico']
plt.figure(figsize=(20, 6))
fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel('Date (from 2013 - 2017)')
plt.ylabel('Price')
plt.title('Oil Price Over Time')

# Display the plot using Streamlit
st.pyplot(fig)

st.write(''' ## Holiday Events Dataset 
             
''')

holiday = pd.read_csv('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP2-FINAL-PROJECT---TEAM-PARIS/holidays_events.csv')

st.write(holiday.head(20))
st.write('''#### Ratio of the holiday counts 
''')
# Plotting a count of the type of holiday
# Calculate the value counts of the 'type' column
type_counts = holiday['type'].value_counts()

# Create a horizontal bar plot using Matplotlib
fig, ax = plt.subplots()
type_counts.plot.barh(ax=ax)
plt.xlabel('Count')
plt.ylabel('Type')
plt.title('Holiday Types')

# Display the plot using Streamlit
st.pyplot(fig)

st.write(holiday.head(20))
st.write('''#### Ratio of the holiday counts with locale name
''')
# Plotting a count of the type of holiday
# Calculate the value counts of the 'type' column
type_counts = holiday['locale_name'].value_counts()

# Create a horizontal bar plot using Matplotlib
fig, ax = plt.subplots()
type_counts.plot.barh(ax=ax)
plt.xlabel('Count per locality ')
plt.ylabel('Type')
plt.title('Holiday Types')

# Display the plot using Streamlit
st.pyplot(fig)

st.write(''' ### Ratio of holiday tranferred and holiday not transferred 
''')
# Create a bar chart
fig, ax = plt.subplots(figsize=(20, 6))
counts = holiday['transferred'].value_counts()

# Create a pie chart
fig2, ax2 = plt.subplots()
transferred_counts = holiday['transferred'].value_counts()
ax2.pie(transferred_counts, labels=transferred_counts.index, autopct='%1.1f%%', startangle=90)
ax2.set_title('RATIO OF HOLIDAYS TRANSFERRED TO HOLIDAYS NOT TRANSFERRED')

# Display the pie chart using Streamlit
st.pyplot(fig2)

final = pd.read_csv('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP2-FINAL-PROJECT---TEAM-PARIS/train.csv')
# Generate the Pandas Profiling report
profile = ProfileReport(train)

# Display the report in Streamlit
st.write(profile.to_html(), unsafe_allow_html=True)
