"""
問題1: 無限に深い1次元井戸型ポテンシャルの波動関数の可視化
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
a = 1.0  # 井戸の幅
x = np.linspace(0, a, 1000)

# 規格化定数
norm = np.sqrt(2/a)

# 基底状態 (n=1)
n1 = 1
u1 = norm * np.sin(n1 * np.pi * x / a)
E1 = (n1**2 * np.pi**2) / (2 * a**2)  # 規格化定数は省略（相対的な値）

# 第1励起状態 (n=2)
n2 = 2
u2 = norm * np.sin(n2 * np.pi * x / a)
E2 = (n2**2 * np.pi**2) / (2 * a**2)

# 確率密度
prob1 = u1**2
prob2 = u2**2

# 図の作成
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('問題1: 無限に深い1次元井戸型ポテンシャルの波動関数', fontsize=16, fontweight='bold')

# 左上: 基底状態の波動関数
ax1 = axes[0, 0]
ax1.plot(x, u1, 'b-', linewidth=2, label=f'$u_1(x)$ (n=1)')
ax1.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
ax1.axvline(x=0, color='r', linestyle='--', linewidth=1, alpha=0.5, label='境界')
ax1.axvline(x=a, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax1.set_xlabel('$x$', fontsize=14)
ax1.set_ylabel('$u_1(x)$', fontsize=14)
ax1.set_title('基底状態の波動関数 $u_1(x)$', fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_xlim(-0.1*a, 1.1*a)

# 右上: 第1励起状態の波動関数
ax2 = axes[0, 1]
ax2.plot(x, u2, 'g-', linewidth=2, label=f'$u_2(x)$ (n=2)')
ax2.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
ax2.axvline(x=0, color='r', linestyle='--', linewidth=1, alpha=0.5, label='境界')
ax2.axvline(x=a, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax2.axvline(x=a/2, color='orange', linestyle=':', linewidth=1, alpha=0.7, label='節 (n=2)')
ax2.set_xlabel('$x$', fontsize=14)
ax2.set_ylabel('$u_2(x)$', fontsize=14)
ax2.set_title('第1励起状態の波動関数 $u_2(x)$', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_xlim(-0.1*a, 1.1*a)

# 左下: 基底状態の確率密度
ax3 = axes[1, 0]
ax3.fill_between(x, 0, prob1, alpha=0.3, color='blue', label='$|u_1(x)|^2$')
ax3.plot(x, prob1, 'b-', linewidth=2)
ax3.axvline(x=0, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax3.axvline(x=a, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax3.set_xlabel('$x$', fontsize=14)
ax3.set_ylabel('$|u_1(x)|^2$', fontsize=14)
ax3.set_title('基底状態の確率密度 $|u_1(x)|^2$', fontsize=13, fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.legend()
ax3.set_xlim(-0.1*a, 1.1*a)

# 右下: 第1励起状態の確率密度
ax4 = axes[1, 1]
ax4.fill_between(x, 0, prob2, alpha=0.3, color='green', label='$|u_2(x)|^2$')
ax4.plot(x, prob2, 'g-', linewidth=2)
ax4.axvline(x=0, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax4.axvline(x=a, color='r', linestyle='--', linewidth=1, alpha=0.5)
ax4.axvline(x=a/2, color='orange', linestyle=':', linewidth=1, alpha=0.7)
ax4.set_xlabel('$x$', fontsize=14)
ax4.set_ylabel('$|u_2(x)|^2$', fontsize=14)
ax4.set_title('第1励起状態の確率密度 $|u_2(x)|^2$', fontsize=13, fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.legend()
ax4.set_xlim(-0.1*a, 1.1*a)

plt.tight_layout()
plt.savefig('/Users/yuto/itphy/量子力学過去問/problem1_wavefunctions.png', dpi=300, bbox_inches='tight')
print("図を保存しました: problem1_wavefunctions.png")
plt.show()
