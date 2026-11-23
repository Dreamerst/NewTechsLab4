import re
import pandas as pd


def normalize_column_name(name):
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name)
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s)
    return s.strip("_").lower()


def rename_columns(df):
    return df.rename(columns={c: normalize_column_name(c) for c in df.columns})
