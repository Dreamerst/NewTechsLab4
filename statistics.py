import matplotlib.pyplot as plt
import pandas as pd


def describe_sizes(df):
    return df[["height", "width", "depth", "class_label"]].describe()


def class_counts(df, column="class_name"):
    return df[column].value_counts().sort_index()


def is_balanced(counts, tolerance=0.1):
    if counts.empty or counts.min() == 0:
        return False
    return counts.max() / counts.min() <= 1 + tolerance


def plot_balance(counts):
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Распределение классов")
    plt.tight_layout()
    plt.show()
