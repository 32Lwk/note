#!/usr/bin/env python3
"""
ゼロ点振動の説明用の図を作成するスクリプト
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

# 位置の範囲
x_max = 4 * sigma
x = np.linspace(-x_max, x_max, 1000)

# 波動関数と確率密度
u0 = c0 * np.exp(-m * omega / (2 * hbar) * x**2)
prob_density = u0**2

# 図1: 古典力学と量子力学の比較（位置分布）
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# 左図: 古典力学（完全に静止）
ax1.axvline(x=0, color='r', linewidth=3, label='古典的粒子（完全静止）')
ax1.set_xlabel(r'位置 $x$', fontsize=12)
ax1.set_ylabel(r'確率密度', fontsize=12)
ax1.set_title('古典力学：基底状態（$E=0$）', fontsize=14, pad=10)
ax1.set_xlim(-x_max, x_max)
ax1.set_ylim(0, c0**2 * 1.2)
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=11)
ax1.text(0, c0**2 * 1.1, r'$\Delta x = 0$（完全に静止）', ha='center', fontsize=10, 
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 右図: 量子力学（ゼロ点振動）
ax2.plot(x, prob_density, 'b-', linewidth=2, label=r'量子力学的確率密度 $|u_0(x)|^2$')
ax2.axvline(x=-sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax2.axvline(x=sigma, color='r', linestyle=':', alpha=0.5, linewidth=1)
ax2.fill_between(x, 0, prob_density, where=(np.abs(x) <= sigma), alpha=0.3, color='blue', label=r'$|x| < \sigma$（約68%）')
ax2.axvline(x=0, color='k', linestyle='--', alpha=0.3, linewidth=1)
ax2.set_xlabel(r'位置 $x$', fontsize=12)
ax2.set_ylabel(r'確率密度 $|u_0(x)|^2$', fontsize=12)
ax2.set_title(r'量子力学：基底状態（$E_0 = \frac{1}{2}\hbar\omega$）', fontsize=14, pad=10)
ax2.set_xlim(-x_max, x_max)
ax2.set_ylim(0, c0**2 * 1.2)
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=11, loc='upper right')
ax2.text(0, c0**2 * 1.1, r'$\Delta x = \sigma = \sqrt{\frac{\hbar}{2m\omega}} > 0$（ゼロ点振動）', 
         ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
ax2.text(-sigma, -c0**2 * 0.08, r'$-\sigma$', ha='center', fontsize=9, color='r')
ax2.text(sigma, -c0**2 * 0.08, r'$+\sigma$', ha='center', fontsize=9, color='r')

plt.tight_layout()
plt.savefig('physics/quantum_mechanics_exercise6_classical_vs_quantum.png', dpi=300, bbox_inches='tight')
print("古典力学と量子力学の比較図を保存しました: physics/quantum_mechanics_exercise6_classical_vs_quantum.png")

# 図2: 不確定性関係とゼロ点エネルギーの関係
fig2, ax3 = plt.subplots(figsize=(10, 6))

# 不確定性関係の境界（Δx * Δp = ħ/2）
delta_x_range = np.linspace(0.1*sigma, 3*sigma, 1000)
delta_p_min = hbar / (2 * delta_x_range)

# エネルギーの等高線
delta_x_grid = np.linspace(0.1*sigma, 3*sigma, 200)
delta_p_grid = np.linspace(0.1*np.sqrt(m*hbar*omega/2), 3*np.sqrt(m*hbar*omega/2), 200)
delta_x_mesh, delta_p_mesh = np.meshgrid(delta_x_grid, delta_p_grid)

# エネルギー: E = (Δp)^2/(2m) + (1/2)mω^2(Δx)^2
energy = (delta_p_mesh**2) / (2*m) + 0.5 * m * omega**2 * delta_x_mesh**2

# 不確定性関係を満たす曲線
ax3.plot(delta_x_range, delta_p_min, 'r-', linewidth=2, label=r'不確定性関係: $\Delta x \cdot \Delta p = \frac{\hbar}{2}$')

# 最小エネルギー点（Δx = σ, Δp = √(mℏω/2)）
optimal_delta_x = sigma
optimal_delta_p = np.sqrt(m * hbar * omega / 2)
optimal_energy = (optimal_delta_p**2) / (2*m) + 0.5 * m * omega**2 * optimal_delta_x**2

ax3.plot(optimal_delta_x, optimal_delta_p, 'ro', markersize=10, zorder=5, label='最適点（最小エネルギー）')
ax3.axvline(x=optimal_delta_x, color='gray', linestyle='--', alpha=0.5)
ax3.axhline(y=optimal_delta_p, color='gray', linestyle='--', alpha=0.5)

# 等高線プロット
contour = ax3.contour(delta_x_mesh, delta_p_mesh, energy, levels=20, alpha=0.3, cmap='viridis')
ax3.clabel(contour, inline=True, fontsize=8)

# 禁止領域（不確定性関係を満たさない領域）を塗りつぶす
ax3.fill_between(delta_x_range, 0, delta_p_min, alpha=0.2, color='red', label='禁止領域（不確定性関係違反）')

ax3.set_xlabel(r'位置の不確定性 $\Delta x$', fontsize=12)
ax3.set_ylabel(r'運動量の不確定性 $\Delta p$', fontsize=12)
ax3.set_title(r'不確定性関係とゼロ点エネルギー', fontsize=14, pad=10)
ax3.grid(True, alpha=0.3)
ax3.legend(fontsize=11, loc='upper left')
ax3.set_xlim(0, 3*sigma)
ax3.set_ylim(0, 3*np.sqrt(m*hbar*omega/2))

# テキスト注釈
ax3.text(optimal_delta_x * 1.2, optimal_delta_p * 1.2, 
         rf'$E_0 = \frac{{1}}{{2}}\hbar\omega = {optimal_energy:.3f}$', 
         fontsize=11, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
ax3.text(optimal_delta_x * 0.5, optimal_delta_p * 0.7, 
         rf'$\Delta x = \sigma = {optimal_delta_x:.3f}$\n$\Delta p = {optimal_delta_p:.3f}$', 
         fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

plt.tight_layout()
plt.savefig('physics/quantum_mechanics_exercise6_uncertainty_relation.png', dpi=300, bbox_inches='tight')
print("不確定性関係とゼロ点エネルギーの関係図を保存しました: physics/quantum_mechanics_exercise6_uncertainty_relation.png")

# 図3: 基底状態での位置と運動量の不確定性（確率分布の可視化）
fig3, (ax4, ax5) = plt.subplots(2, 1, figsize=(10, 8))

# 上図: 位置の確率分布
ax4.plot(x, prob_density, 'b-', linewidth=2, label=r'位置の確率密度 $|u_0(x)|^2$')
ax4.fill_between(x, 0, prob_density, where=(np.abs(x) <= sigma), alpha=0.3, color='blue')
ax4.axvline(x=-sigma, color='r', linestyle=':', alpha=0.7, linewidth=2)
ax4.axvline(x=sigma, color='r', linestyle=':', alpha=0.7, linewidth=2)
ax4.axvline(x=0, color='k', linestyle='--', alpha=0.3, linewidth=1)
ax4.set_xlabel(r'位置 $x$', fontsize=12)
ax4.set_ylabel(r'確率密度', fontsize=12)
ax4.set_title(r'位置の不確定性: $\Delta x = \sigma = \sqrt{\frac{\hbar}{2m\omega}}$', fontsize=14, pad=10)
ax4.grid(True, alpha=0.3)
ax4.legend(fontsize=11)
ax4.set_xlim(-x_max, x_max)
ax4.text(-sigma, c0**2 * 0.5, r'$-\sigma$', ha='center', fontsize=11, color='r', weight='bold')
ax4.text(sigma, c0**2 * 0.5, r'$+\sigma$', ha='center', fontsize=11, color='r', weight='bold')
ax4.text(0, c0**2 * 1.05, r'約68%の確率で $|x| < \sigma$ の範囲に存在', 
         ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

# 下図: 運動量の確率分布（フーリエ変換から）
# 運動量表示での波動関数: u_0(p) のフーリエ変換
p_max = 4 * np.sqrt(m * hbar * omega / 2)
p = np.linspace(-p_max, p_max, 1000)
sigma_p = np.sqrt(m * hbar * omega / 2)

# 運動量表示での確率密度はガウス分布: |u_0(p)|^2 ∝ exp(-p^2/(2(Δp)^2))
prob_density_p = (1 / (np.sqrt(2 * np.pi) * sigma_p)) * np.exp(-p**2 / (2 * sigma_p**2))

ax5.plot(p, prob_density_p, 'r-', linewidth=2, label=r'運動量の確率密度 $|u_0(p)|^2$')
ax5.fill_between(p, 0, prob_density_p, where=(np.abs(p) <= sigma_p), alpha=0.3, color='red')
ax5.axvline(x=-sigma_p, color='b', linestyle=':', alpha=0.7, linewidth=2)
ax5.axvline(x=sigma_p, color='b', linestyle=':', alpha=0.7, linewidth=2)
ax5.axvline(x=0, color='k', linestyle='--', alpha=0.3, linewidth=1)
ax5.set_xlabel(r'運動量 $p$', fontsize=12)
ax5.set_ylabel(r'確率密度', fontsize=12)
ax5.set_title(r'運動量の不確定性: $\Delta p = \sqrt{\frac{m\hbar\omega}{2}}$', fontsize=14, pad=10)
ax5.grid(True, alpha=0.3)
ax5.legend(fontsize=11)
ax5.set_xlim(-p_max, p_max)
ax5.text(-sigma_p, np.max(prob_density_p) * 0.5, r'$-\Delta p$', ha='center', fontsize=11, color='b', weight='bold')
ax5.text(sigma_p, np.max(prob_density_p) * 0.5, r'$+\Delta p$', ha='center', fontsize=11, color='b', weight='bold')
ax5.text(0, np.max(prob_density_p) * 1.05, r'約68%の確率で $|p| < \Delta p$ の範囲に存在', 
         ha='center', fontsize=10, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.tight_layout()
plt.savefig('physics/quantum_mechanics_exercise6_uncertainty_distributions.png', dpi=300, bbox_inches='tight')
print("位置と運動量の不確定性分布図を保存しました: physics/quantum_mechanics_exercise6_uncertainty_distributions.png")

# 図4: エネルギーの等分配
fig4, ax6 = plt.subplots(figsize=(10, 6))

# エネルギーの内訳
E0 = 0.5 * hbar * omega
E_kin = 0.25 * hbar * omega  # 運動エネルギー
E_pot = 0.25 * hbar * omega  # 位置エネルギー

categories = ['運動エネルギー\n$\\langle \\frac{\\hat{p}^2}{2m} \\rangle$', 
              '位置エネルギー\n$\\langle \\frac{1}{2}m\\omega^2\\hat{x}^2 \\rangle$',
              '全エネルギー\n$E_0$']
values = [E_kin, E_pot, E0]
colors = ['skyblue', 'lightcoral', 'lightgreen']
bars = ax6.bar(categories, values, color=colors, edgecolor='black', linewidth=2, width=0.6)

# バーの上に値を表示
for i, (bar, val) in enumerate(zip(bars, values)):
    height = bar.get_height()
    ax6.text(bar.get_x() + bar.get_width()/2., height,
             rf'$\frac{{\hbar\omega}}{{4}} = {val:.3f}$',
             ha='center', va='bottom', fontsize=12, weight='bold')

ax6.set_ylabel(r'エネルギー', fontsize=12)
ax6.set_title(r'基底状態のエネルギーの等分配: $E_0 = \frac{1}{2}\hbar\omega = E_{\text{kin}} + E_{\text{pot}}$', 
              fontsize=14, pad=15)
ax6.grid(True, alpha=0.3, axis='y')
ax6.set_ylim(0, E0 * 1.3)

# テキスト注釈
ax6.text(1, E0 * 1.15, rf'$E_0 = \frac{{1}}{{2}}\hbar\omega = {E0:.3f}$', 
         ha='center', fontsize=13, weight='bold',
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
ax6.text(0, E_kin * 0.5, '等分配', ha='center', fontsize=11, color='white', weight='bold')
ax6.text(1, E_pot * 0.5, '等分配', ha='center', fontsize=11, color='white', weight='bold')

plt.tight_layout()
plt.savefig('physics/quantum_mechanics_exercise6_energy_partition.png', dpi=300, bbox_inches='tight')
print("エネルギーの等分配図を保存しました: physics/quantum_mechanics_exercise6_energy_partition.png")

plt.show()

