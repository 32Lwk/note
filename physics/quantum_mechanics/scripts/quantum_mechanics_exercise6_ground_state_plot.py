#!/usr/bin/env python3
"""
調和振動子の基底状態の波動関数と確率密度をプロットするスクリプト
問題6-3(v)用
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントの設定
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Sans', 'Yu Gothic', 'Meiryo', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
rcParams['axes.unicode_minus'] = False  # マイナス記号の文字化け対策

# パラメータ設定（無次元化: m=1, ω=1, ħ=1）
m = 1.0
omega = 1.0
hbar = 1.0

# 規格化定数と標準偏差
c0 = (m * omega / (np.pi * hbar))**(1/4)
sigma = np.sqrt(hbar / (2 * m * omega))

# 位置の範囲（標準偏差の±4倍まで）
x_max = 4 * sigma
x = np.linspace(-x_max, x_max, 1000)

# 波動関数 u_0(x)
u0 = c0 * np.exp(-m * omega / (2 * hbar) * x**2)

# 確率密度 |u_0(x)|^2
prob_density = u0**2

# 特徴的な位置での値
x_sigma = np.array([-2*sigma, -sigma, 0, sigma, 2*sigma])
u0_sigma = c0 * np.exp(-m * omega / (2 * hbar) * x_sigma**2)
prob_sigma = u0_sigma**2

# 図1: 波動関数 u_0(x)
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(x, u0, 'b-', linewidth=2, label=r'$u_0(x)$')
ax1.axvline(x=0, color='k', linestyle='--', alpha=0.3, linewidth=1)
ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3, linewidth=1)

# 標準偏差の位置に縦線を引く
ax1.axvline(x=-sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax1.axvline(x=sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax1.axvline(x=-2*sigma, color='g', linestyle=':', alpha=0.5, linewidth=1)
ax1.axvline(x=2*sigma, color='g', linestyle=':', alpha=0.5, linewidth=1)

# 特徴的な点をプロット
ax1.plot(x_sigma, u0_sigma, 'ro', markersize=8, zorder=5)
ax1.plot([-sigma, -sigma], [0, u0_sigma[1]], 'r:', alpha=0.5)
ax1.plot([sigma, sigma], [0, u0_sigma[3]], 'r:', alpha=0.5)
ax1.plot([-2*sigma, -2*sigma], [0, u0_sigma[0]], 'g:', alpha=0.5)
ax1.plot([2*sigma, 2*sigma], [0, u0_sigma[4]], 'g:', alpha=0.5)

# 最大値の水平線
ax1.axhline(y=c0, color='gray', linestyle='--', alpha=0.3, linewidth=1)

# ラベルとタイトル
ax1.set_xlabel(r'位置 $x$', fontsize=14)
ax1.set_ylabel(r'波動関数 $u_0(x)$', fontsize=14)
ax1.set_title(r'調和振動子の基底状態の波動関数 $u_0(x)$', fontsize=16, pad=10)
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=12, loc='upper right')

# テキスト注釈
ax1.text(0, c0 * 1.05, rf'$c_0 = {c0:.3f}$', ha='center', fontsize=11)
ax1.text(-sigma, -c0 * 0.1, r'$-\sigma$', ha='center', fontsize=10, color='r')
ax1.text(sigma, -c0 * 0.1, r'$+\sigma$', ha='center', fontsize=10, color='r')
ax1.text(-2*sigma, -c0 * 0.15, r'$-2\sigma$', ha='center', fontsize=10, color='g')
ax1.text(2*sigma, -c0 * 0.15, r'$+2\sigma$', ha='center', fontsize=10, color='g')
ax1.text(sigma * 0.3, u0_sigma[1] * 0.9, rf'$u_0(\sigma) \approx {u0_sigma[1]:.3f}$', fontsize=10)

# 範囲の設定
ax1.set_xlim(-x_max, x_max)
ax1.set_ylim(-c0 * 0.2, c0 * 1.15)

plt.tight_layout()
plt.savefig('physics/quantum_mechanics_exercise6_ground_state_wavefunction.png', dpi=300, bbox_inches='tight')
print("波動関数のグラフを保存しました: physics/quantum_mechanics_exercise6_ground_state_wavefunction.png")

# 図2: 確率密度 |u_0(x)|^2
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(x, prob_density, 'r-', linewidth=2, label=r'$|u_0(x)|^2$')
ax2.axvline(x=0, color='k', linestyle='--', alpha=0.3, linewidth=1)
ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3, linewidth=1)

# 標準偏差の位置に縦線を引く
ax2.axvline(x=-sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax2.axvline(x=sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax2.axvline(x=-2*sigma, color='g', linestyle=':', alpha=0.5, linewidth=1)
ax2.axvline(x=2*sigma, color='g', linestyle=':', alpha=0.5, linewidth=1)

# 特徴的な点をプロット
ax2.plot(x_sigma, prob_sigma, 'ro', markersize=8, zorder=5)

# 最大値の水平線
ax2.axhline(y=c0**2, color='gray', linestyle='--', alpha=0.3, linewidth=1)

# ラベルとタイトル
ax2.set_xlabel(r'位置 $x$', fontsize=14)
ax2.set_ylabel(r'確率密度 $|u_0(x)|^2$', fontsize=14)
ax2.set_title(r'調和振動子の基底状態の確率密度 $|u_0(x)|^2$', fontsize=16, pad=10)
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=12, loc='upper right')

# テキスト注釈
ax2.text(0, c0**2 * 1.05, rf'$c_0^2 = {c0**2:.3f}$', ha='center', fontsize=11)
ax2.text(-sigma, -c0**2 * 0.1, r'$-\sigma$', ha='center', fontsize=10, color='r')
ax2.text(sigma, -c0**2 * 0.1, r'$+\sigma$', ha='center', fontsize=10, color='r')
ax2.text(-2*sigma, -c0**2 * 0.15, r'$-2\sigma$', ha='center', fontsize=10, color='g')
ax2.text(2*sigma, -c0**2 * 0.15, r'$+2\sigma$', ha='center', fontsize=10, color='g')
ax2.text(sigma * 0.3, prob_sigma[3] * 0.9, rf'$|u_0(\sigma)|^2 \approx {prob_sigma[3]:.3f}$', fontsize=10)

# 範囲の設定
ax2.set_xlim(-x_max, x_max)
ax2.set_ylim(-c0**2 * 0.2, c0**2 * 1.15)

plt.tight_layout()
plt.savefig('physics/quantum_mechanics_exercise6_ground_state_probability.png', dpi=300, bbox_inches='tight')
print("確率密度のグラフを保存しました: physics/quantum_mechanics_exercise6_ground_state_probability.png")

# 図3: 両方を並べて表示
fig3, (ax3, ax4) = plt.subplots(2, 1, figsize=(10, 10))

# 波動関数
ax3.plot(x, u0, 'b-', linewidth=2, label=r'$u_0(x)$')
ax3.axvline(x=0, color='k', linestyle='--', alpha=0.3, linewidth=1)
ax3.axvline(x=-sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax3.axvline(x=sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax3.axvline(x=-2*sigma, color='g', linestyle=':', alpha=0.5, linewidth=1)
ax3.axvline(x=2*sigma, color='g', linestyle=':', alpha=0.5, linewidth=1)
ax3.plot(x_sigma, u0_sigma, 'ro', markersize=6, zorder=5)
ax3.set_xlabel(r'位置 $x$', fontsize=12)
ax3.set_ylabel(r'波動関数 $u_0(x)$', fontsize=12)
ax3.set_title(r'基底状態の波動関数 $u_0(x)$', fontsize=14)
ax3.grid(True, alpha=0.3)
ax3.legend(fontsize=11)
ax3.set_xlim(-x_max, x_max)
ax3.set_ylim(-c0 * 0.2, c0 * 1.15)
ax3.text(-sigma, -c0 * 0.08, r'$-\sigma$', ha='center', fontsize=9, color='r')
ax3.text(sigma, -c0 * 0.08, r'$+\sigma$', ha='center', fontsize=9, color='r')

# 確率密度
ax4.plot(x, prob_density, 'r-', linewidth=2, label=r'$|u_0(x)|^2$')
ax4.axvline(x=0, color='k', linestyle='--', alpha=0.3, linewidth=1)
ax4.axvline(x=-sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax4.axvline(x=sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax4.axvline(x=-2*sigma, color='g', linestyle=':', alpha=0.5, linewidth=1)
ax4.axvline(x=2*sigma, color='g', linestyle=':', alpha=0.5, linewidth=1)
ax4.plot(x_sigma, prob_sigma, 'ro', markersize=6, zorder=5)
ax4.set_xlabel(r'位置 $x$', fontsize=12)
ax4.set_ylabel(r'確率密度 $|u_0(x)|^2$', fontsize=12)
ax4.set_title(r'基底状態の確率密度 $|u_0(x)|^2$', fontsize=14)
ax4.grid(True, alpha=0.3)
ax4.legend(fontsize=11)
ax4.set_xlim(-x_max, x_max)
ax4.set_ylim(-c0**2 * 0.2, c0**2 * 1.15)
ax4.text(-sigma, -c0**2 * 0.08, r'$-\sigma$', ha='center', fontsize=9, color='r')
ax4.text(sigma, -c0**2 * 0.08, r'$+\sigma$', ha='center', fontsize=9, color='r')

plt.tight_layout()
plt.savefig('physics/quantum_mechanics_exercise6_ground_state_combined.png', dpi=300, bbox_inches='tight')
print("結合グラフを保存しました: physics/quantum_mechanics_exercise6_ground_state_combined.png")

plt.show()

