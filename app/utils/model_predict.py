from typing import Any
from utils.config import MODEL, STANDARD_SCALER
from dataclasses import dataclass, asdict
import numpy as np


@dataclass
class ModelParams:
    state: str | None
    district: str | None
    hardness: str | None
    latitude: float | Any | None
    longitude: float | Any | None
    ph: float | Any | None
    cl: float | Any | None
    ca: float | Any | None
    k: float | Any | None
    ec: float | Any | None
    co3: float | Any | None
    hco3: float | Any | None
    so4: float | Any | None
    no3: float | Any | None
    po4: float | Any | None
    th: float | Any | None
    mg: float | Any | None
    na: float | Any | None
    f: float | Any | None
    sio2: float | Any | None
    tds: float | Any | None


def predict(params: ModelParams) -> Any:
    """Predict water quality based on user input values

    Args:
        params (ModelParams): water quality params

    Returns:
        Any: Prediction result
    """

    data = ""
    values = list(asdict(params).values())
    print("default feature array: ")
    print(values)

    need_values = values[3:]
    print("after remove categorical feature")
    print(need_values)

    ext_list = [1, 2, 3]
    new_val = ext_list.extend(need_values)
    print("after extend array ")
    print(new_val)

    # print(values)
    # int_values = np.array(values)
    # y_pred = MODEL.predict(data)
    np_values = np.array(new_val).reshape(1, -1)
    print(STANDARD_SCALER.transform(np_values))


# if y_pred == 0:
#     return "Moderately Safe"
# elif y_pred == 1:
#     return "Safe"
# elif y_pred == 2:
#     return "Unsafe"
