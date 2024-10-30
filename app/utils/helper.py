import os
from typing import Any
import joblib
from matplotlib.pylab import rand
from streamlit import page_link, sidebar, cache_data
from pathlib import Path
import pandas as pd
import numpy as np


PROJECT_DIR = Path(__file__).resolve().parent.parent.parent


def get_page_link() -> None:
    with sidebar:
        page_link("main.py", label="Home", icon=":material/home:")
        page_link("pages/insights.py", label="Insights", icon=":material/analytics:")
        page_link("pages/predict.py", label="Predict", icon=":material/psychology:")


@cache_data()
def convert_df(df: pd.DataFrame) -> Any:
    return df.to_csv().encode("utf-8")


@cache_data()
def get_df() -> pd.DataFrame:
    df_path = os.path.join(PROJECT_DIR, "data/preprocessed.csv")
    return pd.read_csv(df_path)


df = get_df()
STATE = df.groupby("STATE")["DISTRICT"].unique().to_dict()


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
    file_path = os.path.join(PROJECT_DIR, "app/utils/bin/coordinates.joblib")
    coordinates = joblib.load(file_path)

    longitudes = coordinates[district]["LONGITUDE"]
    latitudes = coordinates[district]["LATITUDE"]

    rand_longitude = np.random.choice(longitudes)
    rand_latitude = np.random.choice(latitudes)

    return (rand_latitude, rand_longitude)
