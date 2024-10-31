import os
import joblib
import helper


def generate_coordinate_joblib(file_path: str) -> None:
    """generate coordinate binary file from dataset, key=> district

    Args:
        file_path (Path): fle path to store the binary file
    """

    df = helper.get_df("preprocessed.csv")
    coordinates = {}
    districts = df["DISTRICT"].unique()
    for each in districts:
        contain_each = df[df["DISTRICT"] == each]
        coordinates[each] = {
            "LONGITUDE": contain_each["LONGITUDE"],
            "LATITUDE": contain_each["LATITUDE"],
        }

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    joblib.dump(coordinates, file_path, compress=3)
    print(f"coordinates file created at {file_path}")


if __name__ == "__main__":
    joblib_path = os.path.join(helper.PROJECT_DIR, "app/utils/bin/coordinates.joblib")
    generate_coordinate_joblib(joblib_path)
