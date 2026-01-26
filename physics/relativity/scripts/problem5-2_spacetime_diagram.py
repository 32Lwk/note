import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定
plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False

# パラメータ設定
c = 1.0  # 光速（規格化）
v = 0.6  # 宇宙船の速度（光速の60%）
beta = v / c
gamma = 1 / np.sqrt(1 - beta**2)

# 時刻設定
t1 = 1.0  # 点P到達時刻
t_total = 2 * t1  # 往復時間

# 宇宙船の軌跡
# 往路: x = v t (0 ≤ t ≤ t₁)
t_out = np.linspace(0, t1, 100)
x_out = v * t_out
ct_out = c * t_out

# 復路: x = 2v t₁ - v t (t₁ ≤ t ≤ 2t₁)
t_back = np.linspace(t1, t_total, 100)
x_back = 2 * v * t1 - v * t_back
ct_back = c * t_back

# 点Pの座標
x_P = v * t1
ct_P = c * t1

# 光の軌跡（45度の線、参考用）
x_light = np.linspace(-0.5, 2.5, 100)
ct_light_forward = x_light  # 正方向の光
ct_light_backward = -x_light  # 負方向の光

# S'系の座標軸（往路時）
# S'系のct'軸: x' = 0 より x = v t
# S'系のx'軸: t' = 0 より ct = (v/c) x = beta x
x_Sprime_axis = np.linspace(0, 1.5, 100)
ct_Sprime_t_axis = v * x_Sprime_axis / c  # ct'軸（x' = 0）
ct_Sprime_x_axis = beta * x_Sprime_axis  # x'軸（t' = 0）

# 図の作成
fig, ax = plt.subplots(figsize=(10, 10))

# 光の軌跡（薄いグレー）
ax.plot(x_light, ct_light_forward, 'k--', alpha=0.2, linewidth=0.5, label='光の軌跡 (c)')
ax.plot(x_light, ct_light_backward, 'k--', alpha=0.2, linewidth=0.5)

# S'系の座標軸（往路時、薄い青）
ax.plot(x_Sprime_axis, ct_Sprime_t_axis, 'b--', alpha=0.3, linewidth=1, label='S\'系のct\'軸（往路時）')
ax.plot(x_Sprime_axis, ct_Sprime_x_axis, 'b--', alpha=0.3, linewidth=1, label='S\'系のx\'軸（往路時）')

# 宇宙船の軌跡
ax.plot(x_out, ct_out, 'r-', linewidth=2.5, label='宇宙船の軌跡（往路）')
ax.plot(x_back, ct_back, 'r-', linewidth=2.5, label='宇宙船の軌跡（復路）')

# 点Pをマーク
ax.plot(x_P, ct_P, 'ro', markersize=10, label='点P（速度変化点）')
ax.annotate('P', xy=(x_P, ct_P), xytext=(x_P+0.1, ct_P+0.1),
            fontsize=14, fontweight='bold', color='red')

# 原点Oをマーク
ax.plot(0, 0, 'ko', markersize=8, label='原点O（出発点）')
ax.annotate('O', xy=(0, 0), xytext=(0.05, 0.05),
            fontsize=14, fontweight='bold')

# 再会点をマーク
ax.plot(0, c * t_total, 'go', markersize=8, label='再会点')
ax.annotate('再会', xy=(0, c * t_total), xytext=(0.05, c * t_total + 0.1),
            fontsize=12, fontweight='bold', color='green')

# S系の座標軸（グリッド）
ax.axhline(y=0, color='k', linewidth=0.5, alpha=0.3)
ax.axvline(x=0, color='k', linewidth=0.5, alpha=0.3)
ax.grid(True, alpha=0.3, linestyle='--')

# 軸ラベル
ax.set_xlabel('位置 x [規格化単位]', fontsize=14)
ax.set_ylabel('ct [規格化単位]', fontsize=14)
ax.set_title('双子のパラドックスの時空図（S系）', fontsize=16, fontweight='bold')

# 軸の範囲
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 2.5)

# アスペクト比を1:1に
ax.set_aspect('equal', adjustable='box')

# 凡例
ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

# テキスト注釈
ax.text(0.7, 0.3, f'v = {v:.1f}c\nβ = {beta:.2f}\nγ = {gamma:.2f}',
        fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('physics/problem5-2_spacetime_diagram.png', dpi=300, bbox_inches='tight')
print('時空図を保存しました: physics/problem5-2_spacetime_diagram.png')

