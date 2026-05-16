from pathlib import Path
import pandas as pd


def load_sensor_features():
    root = Path(__file__).resolve().parents[1]
    data_file = root / "sensor_features.csv"
    return pd.read_csv(data_file)


def main():
    df = load_sensor_features()
    print("Loaded sensor_features.csv with rows:", len(df))
    print(df.head())


if __name__ == "__main__":
    main()
