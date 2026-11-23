from add_class_label import add_class_label
from add_image_sizes import add_image_sizes
from grouping import add_pixel_count
from histogram_plot import plot_histogram
from load_annotation import load_annotation
from rename_columns import rename_columns


def build_full_dataframe(annotation_csv):
    df = load_annotation(annotation_csv)
    df = rename_columns(df)
    df = add_class_label(df)
    df = add_image_sizes(df)
    df = add_pixel_count(df)
    return df


if __name__ == "__main__":
    df = build_full_dataframe("D://Programming//University//Python//NewTechsLab2//annotation.csv")
    df.to_csv("annotation_full.csv", index=False)
    print(df.head())
    print(df.dtypes)
    plot_histogram(df, 0)
