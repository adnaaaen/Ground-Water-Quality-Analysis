import os
from typing import Any
import pandas as pd
import numpy as np
import streamlit as st
from .config import DF_PATH, PROJECT_DIR
from ydata_profiling import ProfileReport


def create_sidebar() -> list:
    return [
        {
            "label": "Home",
            "page": "main.py",
            "icon": ":material/home:",
        },
        {
            "label": "Insights",
            "page": "pages/insights.py",
            "icon": ":material/monitoring:",
        },
        {
            "label": "Predict",
            "page": "pages/predict.py",
            "icon": ":material/psychology:",
        },
    ]


def convert_df(df: pd.DataFrame) -> Any:
    return df.to_csv().encode("utf-8")


@st.cache_data
def get_df(name: str) -> pd.DataFrame:
    return pd.read_csv(f"{DF_PATH}/{name}")


df = get_df("preprocessed.csv")
STATE = df.groupby("STATE")["DISTRICT"].unique().to_dict()


def get_values_by_locality(state: str, district: str) -> pd.DataFrame:
    state_filter = df["STATE"] == state
    district_filter = df["DISTRICT"] == district
    result_df = df[state_filter & district_filter][
        ["pH", "TDS", "EC", "NO3", "Cl", "TH", "SO4", "Ca", "HARDNESS", "QUALITY"]
    ]
    return result_df


def get_unique_values(column: str) -> list[str]:
    return list(df[column].unique())


def get_random_category(column: str) -> str:
    return str(np.random.choice(df[column].unique()))


def get_random_district_by_state(state: str) -> str:
    return str(np.random.choice(list(STATE[state])))


def get_normal_num(column: str) -> float:
    _mean = df[column].mean()
    _std = df[column].std()
    return round(np.random.normal(_mean, _std), 5)


@st.cache_data
def generate_df_report() -> Any:
    path_to_html = os.path.join(PROJECT_DIR, "app/utils/static/report.html")
    if os.path.exists(path_to_html):
        print("the report is already generated")
        return path_to_html
    df = get_df("preprocessed.csv")
    profile = ProfileReport(df)
    profile.to_file(path_to_html)
    print(f"Report file saved in {path_to_html}")
    return path_to_html
