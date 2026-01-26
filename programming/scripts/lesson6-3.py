from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def load_butterfly(path: Path) -> np.ndarray:
    data = np.loadtxt(path)
    if data.ndim != 2 or data.shape[1] < 2:
        raise ValueError("butterfly.dat の形式が不正です")
    return data


def plot_butterfly(data: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(data[:, 0], data[:, 1])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Butterfly Curve")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("butterfly.png", dpi=200)


def main() -> None:
    data_path = Path("butterfly.dat")
    if not data_path.exists():
        raise FileNotFoundError("butterfly.dat が見つかりません。先に C プログラムを実行してください。")
    data = load_butterfly(data_path)
    plot_butterfly(data)


if __name__ == "__main__":
    main()
