import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定
plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False

# データファイルを読み込む
colors = ['blue', 'red', 'green', 'orange']
labels = ['r0=0.7', 'r0=1.0', 'r0=2.0', 'r0=3.0']

# 角運動量 vs 時間のグラフ
plt.figure(figsize=(10, 6))
for i in range(4):
    filename = f'lesson11-1_case{i+1}.dat'
    try:
        data = np.loadtxt(filename)
        t = data[:, 0]
        Lz = data[:, 1]
        plt.plot(t, Lz, color=colors[i], linewidth=2, label=labels[i])
    except FileNotFoundError:
        print(f"警告: {filename} が見つかりません。")

plt.xlabel('t', fontsize=14)
plt.ylabel('Lz', fontsize=14)
plt.title('062400506', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig('lesson11-1_Lz.png', dpi=300, bbox_inches='tight')
print("グラフを lesson11-1_Lz.png に保存しました。")
plt.close()

# x-y平面上の軌道のグラフ
plt.figure(figsize=(10, 10))
for i in range(4):
    filename = f'lesson11-1_case{i+1}.dat'
    try:
        data = np.loadtxt(filename)
        x = data[:, 2]
        y = data[:, 3]
        plt.plot(x, y, color=colors[i], linewidth=2, label=labels[i])
        # 初期点をプロット
        plt.plot(x[0], y[0], 'o', color=colors[i], markersize=8)
    except FileNotFoundError:
        print(f"警告: {filename} が見つかりません。")

# 原点をプロット
plt.plot(0, 0, 'k*', markersize=15, label='原点')

plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('062400506', fontsize=14)
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.legend(fontsize=10)

# x, yの範囲を適切に設定
plt.xlim(-4, 4)
plt.ylim(-4, 4)

plt.tight_layout()
plt.savefig('lesson11-1_orbit.png', dpi=300, bbox_inches='tight')
print("グラフを lesson11-1_orbit.png に保存しました。")
plt.close()

