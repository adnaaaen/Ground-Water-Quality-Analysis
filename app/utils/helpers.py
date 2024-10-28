import streamlit as st
from pathlib import Path
import pandas as pd



def get_page_link() -> None:
    with st.sidebar:
        st.page_link("main.py", label="Home", icon=":material/home:")
        st.page_link("pages/insights.py", label="Insights", icon=":material/analytics:")
        st.page_link("pages/predict.py", label="Predict", icon=":material/psychology:")

@st.cache_data()
def get_df() -> pd.DataFrame:
    df_path = Path("../data/preprocessed.csv").resolve()
    print(df_path)
    return pd.read_csv(df_path)
    
