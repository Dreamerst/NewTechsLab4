import pandas as pd


def add_pixel_count(df):
    df = df.copy()
    df["pixel_count"] = df["height"] * df["width"]
    return df


def group_by_class(df):
    return df.groupby("class_name")["pixel_count"].agg(["min", "max", "mean"])
