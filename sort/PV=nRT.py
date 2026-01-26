import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 日本語フォントの設定
plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False  # マイナス記号の文字化け対策

# 定数設定
n = 1.0  # モル数
R = 8.314  # 気体定数 [J/(mol·K)]

# 軸の範囲設定
T_range = np.linspace(200, 600, 50)  # 温度 [K]
p_range = np.linspace(1, 10, 50)  # 圧力 [atm]
T_grid, p_grid = np.meshgrid(T_range, p_range)

# 状態方程式: V = nRT/p
V_grid = n * R * T_grid / (p_grid * 100)  # スケール調整

# 3Dプロット作成
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# 状態方程式の曲面をプロット
surf = ax.plot_surface(T_grid, p_grid, V_grid, alpha=0.3, cmap='viridis', 
                       edgecolor='none')

# 等温線 (T一定) の追加
T_constants = [250, 350, 450, 550]  # 温度の値
for T_const in T_constants:
    V_iso = n * R * T_const / (p_range * 100)  # V = nRT/p
    T_iso = np.full_like(p_range, T_const)
    ax.plot(T_iso, p_range, V_iso, 'r-', linewidth=2, label='等温線' if T_const == T_constants[0] else '')

# 等圧線 (p一定) の追加
p_constants = [2, 4, 6, 8]  # 圧力の値
for p_const in p_constants:
    V_isobar = n * R * T_range / (p_const * 100)  # V = nRT/p
    p_isobar = np.full_like(T_range, p_const)
    ax.plot(T_range, p_isobar, V_isobar, 'b-', linewidth=2, label='等圧線' if p_const == p_constants[0] else '')

# 等積線 (V一定) の追加
V_constants = [0.5, 1.0, 1.5, 2.0]  # 体積の値
for V_const in V_constants:
    p_isochore = n * R * T_range / (V_const * 100)  # p = nRT/V
    V_isochore = np.full_like(T_range, V_const)
    ax.plot(T_range, p_isochore, V_isochore, 'g-', linewidth=2, label='等積線' if V_const == V_constants[0] else '')

# 軸ラベルとタイトル
ax.set_xlabel('絶対温度 T [K]', fontsize=12, labelpad=10)
ax.set_ylabel('圧力 p [atm]', fontsize=12, labelpad=10)
ax.set_zlabel('体積 V [L]', fontsize=12, labelpad=10)
ax.set_title('理想気体の状態方程式 pV = nRT の3次元可視化', fontsize=14, pad=20)

# 視点の調整
ax.view_init(elev=25, azim=45)

# 凡例の追加
ax.legend(loc='upper left', fontsize=10)

# カラーバーの追加
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='体積 V [L]')

# グリッドの表示
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

