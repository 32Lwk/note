import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定
plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False

# 定数
GM = 1.0  # GM = 1の単位系
m = 1.0   # 質点の質量（単位として1）

# 初期条件（4つ）
x0_list = [0.7, 1.0, 2.0, 3.0]
y0_list = [0.0, 0.0, 0.0, 0.0]
vx0_list = [0.0, 0.0, 0.0, 0.0]
vy0_list = [1.0, 1.0, 1.0, 1.0]

# 角運動量を計算
Lz_list = []
for i in range(len(x0_list)):
    Lz = m * (x0_list[i] * vy0_list[i] - y0_list[i] * vx0_list[i])
    Lz_list.append(Lz)

print("各初期条件の角運動量:")
for i, Lz in enumerate(Lz_list):
    print(f"  初期条件{i+1}: x0={x0_list[i]}, Lz={Lz:.3f}")

# 有効ポテンシャル Ueff(r) = -GM/r + Lz^2/(2*m*r^2)
def ueff(r, Lz):
    if r <= 0:
        return np.nan
    return -GM / r + Lz * Lz / (2.0 * m * r * r)

# rの範囲
r = np.linspace(0.1, 5.0, 1000)

# グラフを作成
plt.figure(figsize=(10, 7))
colors = ['blue', 'red', 'green', 'orange']
labels = ['r0=0.7', 'r0=1.0', 'r0=2.0', 'r0=3.0']

# 各初期条件に対する有効ポテンシャルを描画
for i, Lz in enumerate(Lz_list):
    ueff_values = [ueff(r_val, Lz) for r_val in r]
    plt.plot(r, ueff_values, color=colors[i], linewidth=2, label=labels[i])

# 初期点をプロット
for i in range(len(x0_list)):
    r0 = np.sqrt(x0_list[i]**2 + y0_list[i]**2)
    ueff0 = ueff(r0, Lz_list[i])
    plt.plot(r0, ueff0, 'o', color=colors[i], markersize=8, markeredgecolor='black', markeredgewidth=1)

# グラフの設定
plt.xlabel('r', fontsize=14)
plt.ylabel('Ueff', fontsize=14)
plt.title('062400506', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.xlim(0, 5)
plt.ylim(-1.1, 0.5)

plt.tight_layout()
plt.savefig('lesson11-1_potential.png', dpi=300, bbox_inches='tight')
print("グラフを lesson11-1_potential.png に保存しました。")
plt.close()

