"""
問題2: 1次元調和振動子の波動関数の可視化
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.font_manager as fm

# 日本語フォントの設定（macOS用）
# 利用可能な日本語フォントを検索
japanese_fonts = ['Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Arial Unicode MS', 'AppleGothic', 'Osaka']
font_found = None
for font_name in japanese_fonts:
    try:
        font_path = fm.findfont(fm.FontProperties(family=font_name))
        if font_path:
            font_found = font_name
            break
    except:
        continue

if font_found:
    rcParams['font.family'] = font_found
    print(f"日本語フォントを使用: {font_found}")
else:
    # フォールバック: システムのデフォルトフォントを使用
    import platform
    if platform.system() == 'Darwin':  # macOS
        rcParams['font.family'] = 'Hiragino Sans'
    else:
        rcParams['font.family'] = 'sans-serif'
    print("デフォルトフォントを使用")

rcParams['font.size'] = 12
# マイナス記号の文字化けを防ぐ
rcParams['axes.unicode_minus'] = False

# パラメータ
m = 1.0  # 質量
omega = 1.0  # 角振動数
hbar = 1.0  # プランク定数（自然単位系）

# 長さのスケール
x0 = np.sqrt(hbar / (m * omega))

# 位置座標（無次元変数を使用）
xi = np.linspace(-4, 4, 1000)
x = xi * x0

# 規格化定数
A0 = (m * omega / (np.pi * hbar))**(1/4)

# 基底状態 (n=0)
eta0 = A0 * np.exp(-0.5 * (m * omega / hbar) * x**2)
prob0 = eta0**2

# 第1励起状態 (n=1)
eta1 = A0 * np.sqrt(2 * m * omega / hbar) * x * np.exp(-0.5 * (m * omega / hbar) * x**2)
prob1 = eta1**2

# 図の作成
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('問題2: 1次元調和振動子の波動関数', fontsize=16, fontweight='bold')

# 左上: 基底状態の波動関数
ax1 = axes[0, 0]
ax1.plot(x/x0, eta0, 'b-', linewidth=2, label=r'$\eta_0(x)$ (n=0)')
ax1.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
ax1.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.5)
ax1.set_xlabel(r'$x/x_0$ (無次元)', fontsize=14)
ax1.set_ylabel(r'$\eta_0(x)$', fontsize=14)
ax1.set_title('基底状態の波動関数 $\\eta_0(x)$', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_xlim(-4, 4)

# 右上: 第1励起状態の波動関数
ax2 = axes[0, 1]
ax2.plot(x/x0, eta1, 'g-', linewidth=2, label=r'$\eta_1(x)$ (n=1)')
ax2.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
ax2.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.5)
ax2.axvline(x=0, color='orange', linestyle=':', linewidth=1, alpha=0.7, label='節 (n=1)')
ax2.set_xlabel(r'$x/x_0$ (無次元)', fontsize=14)
ax2.set_ylabel(r'$\eta_1(x)$', fontsize=14)
ax2.set_title('第1励起状態の波動関数 $\\eta_1(x)$', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_xlim(-4, 4)

# 左下: 基底状態の確率密度
ax3 = axes[1, 0]
ax3.fill_between(x/x0, 0, prob0, alpha=0.3, color='blue', label=r'$|\eta_0(x)|^2$')
ax3.plot(x/x0, prob0, 'b-', linewidth=2)
ax3.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.5)
ax3.set_xlabel(r'$x/x_0$ (無次元)', fontsize=14)
ax3.set_ylabel(r'$|\eta_0(x)|^2$', fontsize=14)
ax3.set_title('基底状態の確率密度 $|\\eta_0(x)|^2$', fontsize=13, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.legend()
ax3.set_xlim(-4, 4)

# 右下: 第1励起状態の確率密度
ax4 = axes[1, 1]
ax4.fill_between(x/x0, 0, prob1, alpha=0.3, color='green', label=r'$|\eta_1(x)|^2$')
ax4.plot(x/x0, prob1, 'g-', linewidth=2)
ax4.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.5)
ax4.set_xlabel(r'$x/x_0$ (無次元)', fontsize=14)
ax4.set_ylabel(r'$|\eta_1(x)|^2$', fontsize=14)
ax4.set_title('第1励起状態の確率密度 $|\\eta_1(x)|^2$', fontsize=13, fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.legend()
ax4.set_xlim(-4, 4)

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/量子力学過去問/problem2_wavefunctions.png', dpi=300, bbox_inches='tight')
print("図を保存しました: problem2_wavefunctions.png")
plt.show()

# 追加: ポテンシャルとエネルギー準位の図
fig2, ax = plt.subplots(1, 1, figsize=(10, 8))

# ポテンシャル
V = 0.5 * m * omega**2 * x**2
ax.plot(x/x0, V/(hbar*omega), 'r-', linewidth=2, label='ポテンシャル $V(x)/(\\hbar\\omega)$')

# エネルギー準位
E0 = 0.5 * hbar * omega
E1 = 1.5 * hbar * omega
ax.axhline(y=E0/(hbar*omega), color='b', linestyle='--', linewidth=2, label=f'$E_0/(\\hbar\\omega) = {E0/(hbar*omega):.1f}$')
ax.axhline(y=E1/(hbar*omega), color='g', linestyle='--', linewidth=2, label=f'$E_1/(\\hbar\\omega) = {E1/(hbar*omega):.1f}$')

# 波動関数をエネルギー準位上にプロット（スケール調整）
scale0 = 0.3
scale1 = 0.3
ax.plot(x/x0, E0/(hbar*omega) + scale0 * eta0 / np.max(eta0), 'b-', linewidth=1.5, alpha=0.7, label='$\\eta_0(x)$ (スケール調整)')
ax.plot(x/x0, E1/(hbar*omega) + scale1 * eta1 / np.max(np.abs(eta1)), 'g-', linewidth=1.5, alpha=0.7, label='$\\eta_1(x)$ (スケール調整)')

ax.set_xlabel(r'$x/x_0$ (無次元)', fontsize=14)
ax.set_ylabel(r'エネルギー $/(\hbar\omega)$', fontsize=14)
ax.set_title('調和振動子のポテンシャルとエネルギー準位', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10)
ax.set_xlim(-4, 4)
ax.set_ylim(-0.5, 3)

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/量子力学過去問/problem2_energy_levels.png', dpi=300, bbox_inches='tight')
print("図を保存しました: problem2_energy_levels.png")
plt.show()
