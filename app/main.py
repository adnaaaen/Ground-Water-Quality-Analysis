import streamlit as st
import numpy as np
from utils import helper

# page configuration
st.set_page_config(page_title="Home | Water Quality Analysis")

helper.get_page_link()

st.markdown("## **Ground Water Quality Analysis**")


st.markdown("#### **Objective**")
objective_text = """
This project aims to develop an interactive machine learning (ML) application that assesses and predicts the quality of ground water in various regions of India. The application uses data-driven insights to determine water quality levels, ultimately helping policymakers, researchers, and the general public make informed decisions about water consumption and safety
"""
st.caption(objective_text)


st.markdown("#### **About Data**")
dataset_caption = """
This dataset, titled "Ground Water Quality 2021," provides comprehensive information on groundwater quality across various states and districts in India. The data has been collected for the year 2021 and is essential for understanding water quality patterns at the regional level, facilitating informed decisions in environmental monitoring, policy-making, and public health assessments
"""
st.caption(dataset_caption)

# about dataset
df = helper.get_df()

st.write(df.sample(5))
# download dataset
downloadable_df = helper.convert_df(df)
st.download_button(label="Download Dataset", data=downloadable_df, file_name="ground_water_quality.csv", mime="text/csv", icon=":material/download:")



one, two, three = st.columns(3)
with one:
    st.metric(label="Rows", value=df.shape[0])
    st.metric(label="Catagorical Features", value=len(df.select_dtypes(include="O").columns))

with two:
    st.metric(label="Columns", value=df.shape[1])
    st.metric(label="No.of States", value=df['STATE'].nunique())

with three:
    st.metric(label="Numerical Features", value=len(df.select_dtypes(include=np.number).columns))
    st.metric(label="No.of Districts", value=df['DISTRICT'].nunique())
