from pathlib import Path
import pandas as pd
from PIL import Image


def get_image_size(path):
    with Image.open(path) as img:
        width, height = img.size
        depth = len(img.getbands())
    return height, width, depth


def add_image_sizes(df, path_column="absolute_path"):
    df = df.copy()
    sizes = df[path_column].map(get_image_size)
    df["height"] = [t[0] for t in sizes]
    df["width"] = [t[1] for t in sizes]
    df["depth"] = [t[2] for t in sizes]
    return df
