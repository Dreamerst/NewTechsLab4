import pandas as pd

from filter_by_class import filter_by_class


def filter_by_class_and_size(df, class_identifier, max_width, max_height):
    filtered = filter_by_class(df, class_identifier)
    return filtered[(filtered["height"] <= max_height) & (filtered["width"] <= max_width)].copy()
