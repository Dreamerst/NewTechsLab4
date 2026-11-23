def filter_by_class(df, class_identifier):
    if isinstance(class_identifier, str):
        return df[df["class_name"] == class_identifier].copy()
    return df[df["class_label"] == int(class_identifier)].copy()
