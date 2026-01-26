"""
量子力学演習問題6-3, 6-4, 7-1の図を作成するスクリプト
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.font_manager as fm

# 日本語フォント設定
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
else:
    import platform
    if platform.system() == 'Darwin':
        rcParams['font.family'] = 'Hiragino Sans'
    else:
        rcParams['font.family'] = 'DejaVu Sans'

rcParams['font.size'] = 12
rcParams['axes.unicode_minus'] = False

# 物理定数
hbar = 1.0
m = 1.0
omega = 1.0

# 問題6-4: 基底状態の波動関数
def plot_problem6_4():
    """問題6-4: 調和振動子の基底状態"""
    xi = np.sqrt(m*omega/hbar)
    x = np.linspace(-4, 4, 1000)
    xi_var = xi * x
    
    # 基底状態の波動関数 (H_0(xi) = 1)
    c0 = (m*omega/(np.pi*hbar))**(1/4)
    u0 = c0 * np.exp(-xi_var**2 / 2)
    prob_density = u0**2
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # 上段: 波動関数
    ax1 = axes[0]
    ax1.plot(x, u0, 'b-', linewidth=2, label='$u_0(x)$')
    ax1.axhline(0, color='k', linestyle='-', linewidth=1)
    ax1.axvline(0, color='k', linestyle='--', alpha=0.5)
    ax1.set_xlim(-4, 4)
    ax1.set_xlabel('$x$', fontsize=14)
    ax1.set_ylabel('$u_0(x)$', fontsize=14)
    ax1.set_title('問題6-4: 調和振動子の基底状態の波動関数', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 下段: 確率密度
    ax2 = axes[1]
    ax2.plot(x, prob_density, 'g-', linewidth=2, label='$|u_0(x)|^2$')
    ax2.fill_between(x, 0, prob_density, alpha=0.3, color='green')
    ax2.axhline(0, color='k', linestyle='-', linewidth=1)
    ax2.axvline(0, color='k', linestyle='--', alpha=0.5)
    ax2.set_xlim(-4, 4)
    ax2.set_xlabel('$x$', fontsize=14)
    ax2.set_ylabel('$|u_0(x)|^2$', fontsize=14)
    ax2.set_title('問題6-4: 基底状態の確率密度（ゼロ点振動）', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('../figures/problem6_4_ground_state.png', dpi=300, bbox_inches='tight')
    print("問題6-4の図を保存: figures/problem6_4_ground_state.png")
    plt.close()

if __name__ == '__main__':
    print("量子力学演習問題6-4の図を作成中...")
    try:
        plot_problem6_4()
    except Exception as e:
        print(f"エラー: {e}")
    print("完了しました。")
