import joblib
import os
from pathlib import Path

# dirs
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
BINARY_DIR = os.path.join(PROJECT_DIR, "app/utils/bin")

DF_PATH = os.path.join(PROJECT_DIR, "data")


STANDARD_SCALER = joblib.load(os.path.join(BINARY_DIR, "standard_scaler.joblib"))
COORDINATES = joblib.load(os.path.join(BINARY_DIR, "coordinates.joblib"))

# TODO
# LABEL_ENCODER = ""


MODEL = joblib.load(os.path.join(PROJECT_DIR, "model/model.joblib"))


if __name__ == "__main__":
    print(PROJECT_DIR)
