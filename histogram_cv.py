import cv2
from filter_by_class import filter_by_class


def build_histogram(df, class_identifier):
    filtered = filter_by_class(df, class_identifier)

    row = filtered.sample(1).iloc[0]
    img = cv2.imread(row["absolute_path"])
    if img is None:
        raise OSError(f"Не удалось прочитать {row['absolute_path']}")

    def channel_hist(idx):
        hist = cv2.calcHist([img], [idx], None, [256], [0, 256])
        return hist.flatten()

    return channel_hist(0), channel_hist(1), channel_hist(2)
