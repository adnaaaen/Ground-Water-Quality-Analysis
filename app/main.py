import streamlit as st
from utils import helpers

st.title("GROUND WATER QUALITY DATA ANALYSIS")

helpers.get_page_link()


# data
data = helpers.get_df()

st.write(data.head())
cols = data.columns

cols_options = st.multiselect("Select Columns to view", cols)
st.write(data[cols_options].head())


