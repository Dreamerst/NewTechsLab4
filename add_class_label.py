import pandas as pd


def add_class_label(df, column="class_name"):
    df = df.copy()
    df["class_label"] = pd.Categorical(df[column]).codes
    return df
