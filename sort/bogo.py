import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def is_sorted(data):
    """データが昇順に並んでいるか判定"""
    return all(data[i] <= data[i+1] for i in range(len(data)-1))

def pray_sort(data):
    """祈り（ボゴ）ソートの生成器：1ステップごとにシャッフルしてyield"""
    while not is_sorted(data):
        random.shuffle(data)
        yield data
    yield data  # 最後のソート済み状態

# --- 可視化設定 ---
def visualize_pray_sort():
    n = 8  # 要素数（大きいと祈りが長引きます…）
    data = list(range(1, n+1))
    random.shuffle(data)

    fig, ax = plt.subplots()
    bars = ax.bar(range(len(data)), data, color="skyblue")
    ax.set_title("Pray Sort Visualization 🙏 (Bogo Sort)")
    ax.set_ylim(0, n + 1)

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update(data):
        for bar, val in zip(bars, data):
            bar.set_height(val)
        text.set_text(f"Current: {data}")
        return bars

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=pray_sort(data),
        repeat=False,
        blit=False,
        interval=300,  # 速度 (ms)
    )

    plt.show()

if __name__ == "__main__":
    visualize_pray_sort()
