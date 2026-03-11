import pandas as pd
from pandas import DataFrame
import os

def load(path: str) -> DataFrame: 
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        ext = os.path.splitext(path)[1].lower()
        if ext not in {".csv"}:
            raise ValueError("only .csv files are supported")
        df = pd.read_csv(path)
        if df.empty:
            raise ValueError("Empty file")
        pd.set_option("display.show_dimensions", False)
        print(f"Loading dataset of dimensions {df.shape}")
        return df.to_string()
    except Exception as exc:
            print(f"Error: {exc}")
    return None

def main() -> None:
     print(load("life_expectancy_years.csv"))

if __name__ == "__main__":
    main()