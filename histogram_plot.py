import matplotlib.pyplot as plt
from histogram_cv import build_histogram


def plot_histogram(df, class_identifier):
    hist_b, hist_g, hist_r = build_histogram(df, class_identifier)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(hist_b, color="blue", label="Синий канал (B)")
    ax.plot(hist_g, color="green", label="Зелёный канал (G)")
    ax.plot(hist_r, color="red", label="Красный канал (R)")

    ax.set_xlabel("Значение пикселя (0–255)")
    ax.set_ylabel("Частота")
    ax.set_title(f"Гистограмма RGB для класса '{class_identifier}'")
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
