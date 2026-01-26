"""
問題3（2025年）: 調和振動子の波動関数の可視化
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.font_manager as fm

# 日本語フォントの設定（macOS用）
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
    import platform
    if platform.system() == 'Darwin':
        rcParams['font.family'] = 'Hiragino Sans'
    else:
        rcParams['font.family'] = 'sans-serif'
    print("デフォルトフォントを使用")

rcParams['font.size'] = 12
rcParams['axes.unicode_minus'] = False

# パラメータ
m = 1.0
omega = 1.0
hbar = 1.0

# 長さのスケール
x0 = np.sqrt(hbar / (m * omega))

# 位置座標（無次元変数を使用）
xi = np.linspace(-4, 4, 1000)
x = xi * x0

# 規格化定数（規格化は実行しないが、比較のため適当な値を選ぶ）
A0 = 1.0
A1 = 1.0

# 基底状態 (n=0)
eta0 = A0 * np.exp(-0.5 * (m * omega / hbar) * x**2)
prob0 = eta0**2

# 第1励起状態 (n=1)
eta1 = A1 * np.sqrt(2 * m * omega / hbar) * x * np.exp(-0.5 * (m * omega / hbar) * x**2)
prob1 = eta1**2

# 図の作成
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('問題3（2025年）: 1次元調和振動子の波動関数', fontsize=16, fontweight='bold')

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
ax2.axvline(x=0, color='orange', linestyle=':', linewidth=1, alpha=0.7, label='節')
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
ax4.axvline(x=0, color='orange', linestyle=':', linewidth=1, alpha=0.7)
ax4.set_xlabel(r'$x/x_0$ (無次元)', fontsize=14)
ax4.set_ylabel(r'$|\eta_1(x)|^2$', fontsize=14)
ax4.set_title('第1励起状態の確率密度 $|\\eta_1(x)|^2$', fontsize=13, fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.legend()
ax4.set_xlim(-4, 4)

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/量子力学過去問/problem3_2025_harmonic_oscillator.png', dpi=300, bbox_inches='tight')
print("図を保存しました: problem3_2025_harmonic_oscillator.png")
plt.close()
