import os
import streamlit as st
from typing import Any
from pathlib import Path
import pandas as pd
import numpy as np


PROJECT_DIR = Path(__file__).resolve().parent.parent.parent


def get_page_link() -> None:
    with st.sidebar:
        st.page_link("main.py", label="Home", icon=":material/home:")
        st.page_link("pages/insights.py", label="Insights", icon=":material/analytics:")
        st.page_link("pages/predict.py", label="Predict", icon=":material/psychology:")


@st.cache_data()
def convert_df(df: pd.DataFrame) -> Any:
    return df.to_csv().encode("utf-8")


@st.cache_data()
def get_df() -> pd.DataFrame:
    df_path = os.path.join(PROJECT_DIR, "data/preprocessed.csv")
    return pd.read_csv(df_path)

df = get_df()
STATE = df.groupby("STATE")["DISTRICT"].unique().to_dict()

def get_random_catagory(column: str) -> str:
    return str(np.random.choice(df[column].unique()))

def get_random_district_by_state(state: str) -> str:
    return str(np.random.choice(list(STATE[state])))

def get_random_num(start: float, end: float) -> float:
    return round(np.random.uniform(start, end), 5)
