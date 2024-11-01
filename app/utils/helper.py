from typing import Any
import pandas as pd
import numpy as np
import streamlit as st
from .config import DF_PATH, COORDINATES


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


def get_random_num(start: float, end: float) -> float:
    return round(np.random.uniform(start, end), 5)


def get_coordinates_by_district(district: str) -> tuple[float, float]:
    """generate coordinates by given district which included in dataset

    Args:
        district (str): district available also in dataset
    Returns:
        tuple[float, float]: latitude, longitude
    """
    longitudes = COORDINATES[district]["LONGITUDE"]
    latitudes = COORDINATES[district]["LATITUDE"]

    rand_longitude = np.random.choice(longitudes)
    rand_latitude = np.random.choice(latitudes)

    return (rand_latitude, rand_longitude)
