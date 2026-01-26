"""
問題2（2025年）: デルタ関数ポテンシャルの波動関数の可視化
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
lambda_val = -1.0  # 引力ポテンシャル
hbar = 1.0

# 単一デルタ関数ポテンシャルの束縛状態
kappa = -m * lambda_val / (hbar**2)  # lambda < 0 のとき kappa > 0
E = -hbar**2 * kappa**2 / (2*m)

# 位置座標
x = np.linspace(-3, 3, 1000)
x_neg = x[x < 0]
x_pos = x[x >= 0]

# 波動関数（規格化定数は適当に選ぶ）
A = 1.0
psi_single = np.zeros_like(x)
psi_single[x < 0] = A * np.exp(kappa * x_neg)
psi_single[x >= 0] = A * np.exp(-kappa * x_pos)

# 確率密度
prob_single = psi_single**2

# 図の作成
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('問題2（2025年）: デルタ関数ポテンシャルの波動関数', fontsize=16, fontweight='bold')

# 左上: 単一デルタ関数の波動関数
ax1 = axes[0, 0]
ax1.plot(x, psi_single, 'b-', linewidth=2, label='$\\psi(x)$')
ax1.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
ax1.axvline(x=0, color='r', linestyle='--', linewidth=1, alpha=0.5, label='$x=0$ (デルタ関数)')
ax1.set_xlabel('$x$', fontsize=14)
ax1.set_ylabel('$\\psi(x)$', fontsize=14)
ax1.set_title('単一デルタ関数ポテンシャルの束縛状態', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_xlim(-3, 3)

# 右上: 単一デルタ関数の確率密度
ax2 = axes[0, 1]
ax2.fill_between(x, 0, prob_single, alpha=0.3, color='blue', label='$|\\psi(x)|^2$')
ax2.plot(x, prob_single, 'b-', linewidth=2)
ax2.axvline(x=0, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax2.set_xlabel('$x$', fontsize=14)
ax2.set_ylabel('$|\\psi(x)|^2$', fontsize=14)
ax2.set_title('単一デルタ関数ポテンシャルの確率密度', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_xlim(-3, 3)

# 二重デルタ関数ポテンシャル（対称な場合）
a = 2.0
lambda_double = -1.5

# 簡易的な計算（実際の計算は複雑）
# ここでは、対称な束縛状態を仮定
kappa_double = 0.8  # 適当な値
x_double = np.linspace(-4, 4, 1000)
x_double_neg = x_double[x_double < 0]
x_double_mid = x_double[(x_double >= 0) & (x_double < a)]
x_double_pos = x_double[x_double >= a]

psi_double = np.zeros_like(x_double)
# 簡易的な形（実際の計算では接続条件を満たす必要がある）
psi_double[x_double < 0] = np.exp(kappa_double * x_double_neg)
psi_double[(x_double >= 0) & (x_double < a)] = np.exp(-kappa_double * x_double_mid) + 0.3 * np.exp(kappa_double * (x_double_mid - a))
psi_double[x_double >= a] = 0.5 * np.exp(-kappa_double * (x_double_pos - a))

# 規格化（簡易的）
psi_double = psi_double / np.sqrt(np.trapz(psi_double**2, x_double))
prob_double = psi_double**2

# 左下: 二重デルタ関数の波動関数
ax3 = axes[1, 0]
ax3.plot(x_double, psi_double, 'g-', linewidth=2, label='$\\psi(x)$')
ax3.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
ax3.axvline(x=0, color='r', linestyle='--', linewidth=1, alpha=0.5, label='デルタ関数')
ax3.axvline(x=a, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax3.set_xlabel('$x$', fontsize=14)
ax3.set_ylabel('$\\psi(x)$', fontsize=14)
ax3.set_title('二重デルタ関数ポテンシャルの束縛状態（概形）', fontsize=13, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.legend()
ax3.set_xlim(-4, 4)

# 右下: 二重デルタ関数の確率密度
ax4 = axes[1, 1]
ax4.fill_between(x_double, 0, prob_double, alpha=0.3, color='green', label='$|\\psi(x)|^2$')
ax4.plot(x_double, prob_double, 'g-', linewidth=2)
ax4.axvline(x=0, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax4.axvline(x=a, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax4.set_xlabel('$x$', fontsize=14)
ax4.set_ylabel('$|\\psi(x)|^2$', fontsize=14)
ax4.set_title('二重デルタ関数ポテンシャルの確率密度（概形）', fontsize=13, fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.legend()
ax4.set_xlim(-4, 4)

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/量子力学過去問/problem2_2025_delta_potential.png', dpi=300, bbox_inches='tight')
print("図を保存しました: problem2_2025_delta_potential.png")
plt.close()
