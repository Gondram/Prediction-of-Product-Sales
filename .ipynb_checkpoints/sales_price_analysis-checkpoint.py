# Import standard packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns',100)

from io import StringIO

def load_data():
    fpath = "data/prepped_sales_predictions_2023.csv"
    df = pd.read_csv(fpath)
    return df

df = load_data()
df.head()

st.title('Sales Price Analysis')
st.header("Product Sales Data")
st.dataframe(df, width=800)

# Display descriptive statistics
st.markdown('#### Descriptive Statistics')
if st.button("Descriptive Statistics"):
    st.dataframe(df.describe().round(2))

# Capture .info()
# Create a string buffer to capture the content
buffer = StringIO()
# Write the info into the buffer
df.info(buf=buffer)
# Retrieve the content from the buffer
summary_info = buffer.getvalue()
# Use Streamlit to display the info
st.markdown("#### Summary Info")
if st.button("Summary Info"):
    st.text(summary_info)

# display as dataframe
st.markdown("#### Null Values")
nulls =df.isna().sum()
if st.button('Null Values'):
    st.dataframe(nulls)

