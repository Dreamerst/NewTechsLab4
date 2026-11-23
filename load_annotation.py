from pathlib import Path
import pandas as pd


def load_annotation(annotation_csv):
    df = pd.read_csv(annotation_csv, usecols=["output_class", "absolute_path"])
    return df.rename(columns={"output_class": "class_name"})


if __name__ == "__main__":
    annotation_path = "D://Programming//University//Python//NewTechsLab2//annotation.csv"
    df = load_annotation(annotation_path)
    print(df.head())
    print(df.shape)