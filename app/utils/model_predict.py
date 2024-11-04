from typing import Any
import numpy as np
import pandas as pd
from utils.config import (
    MODEL,
    STANDARD_SCALER,
    HARDNESS_ENCODER,
    STATE_ENCODER,
    DISTRICT_ENCODER,
)
from utils.helper import df
from dataclasses import dataclass, asdict


@dataclass
class ModelParams:
    state: str | None
    district: str | None
    latitude: float | Any | None
    longitude: float | Any | None
    ph: float | Any | None
    ec: float | Any | None
    co3: float | Any | None
    hco3: float | Any | None
    cl: float | Any | None
    so4: float | Any | None
    no3: float | Any | None
    po4: float | Any | None
    th: float | Any | None
    ca: float | Any | None
    mg: float | Any | None
    na: float | Any | None
    k: float | Any | None
    f: float | Any | None
    sio2: float | Any | None
    tds: float | Any | None
    hardness: str | None


def label_encode(state: str, district: str, hardness: str) -> tuple[Any, Any, Any]:
    encoded_district = int(DISTRICT_ENCODER[district])
    encoded_state = int(STATE_ENCODER[state])
    encoded_hardness = int(HARDNESS_ENCODER.transform([hardness])[0])
    return (encoded_state, encoded_district, encoded_hardness)


def predict(params: ModelParams) -> Any:
    """Predict water quality based on user input values

    Args:
        params (ModelParams): water quality params

    Returns:
        Any: Prediction result
    """
    list_values = list(asdict(params).values())
    _state = list_values[0]
    _district = list_values[1]
    _hardness = list_values[-1]
    print(_state)
    print(_district)
    print(_hardness)

    print("Default Values: ")
    print(list_values)

    list_values[0], list_values[1], list_values[-1] = label_encode(_state, _district, _hardness) 

    print("Encoded Values: ")
    print(list_values)

    np_array = np.array(list_values)
    
    scaled_values = STANDARD_SCALER.transform(np_array.reshape(1,-1))

    print("Scaled Values: ")
    print(scaled_values)

    df_x = pd.DataFrame(scaled_values, columns=df.columns[:-1])
    y_pred = MODEL.predict(df_x)

    if y_pred == 0:
        print("Moderately Safe")
    elif y_pred == 1:
         # return "Safe"
         print("Safe")
    elif y_pred == 2:
        # return "Unsafe"
        print("Unsafe")
