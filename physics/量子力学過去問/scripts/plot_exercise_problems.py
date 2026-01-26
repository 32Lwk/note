"""
量子力学演習問題の図を作成するスクリプト
問題3-3, 3-4, 5-1, 5-2, 5-3の可視化
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.font_manager as fm

# 日本語フォントの設定
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

# 物理定数（単位を適切に設定）
hbar = 1.0  # 簡略化のため
m = 1.0

# ============================================
# 問題3-3: 箱の中の粒子の固有関数
# ============================================
def plot_problem3_3():
    """問題3-3: 箱の中の粒子の固有関数とポテンシャル"""
    a = 1.0
    x = np.linspace(-1.5*a, 1.5*a, 1000)
    
    # ポテンシャル
    V = np.zeros_like(x)
    V[np.abs(x) > a] = np.inf
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # 上段: ポテンシャル
    ax1 = axes[0]
    ax1.plot(x[np.abs(x) <= a], V[np.abs(x) <= a], 'k-', linewidth=2, label='$V(x)$')
    ax1.axvline(-a, color='k', linewidth=3)
    ax1.axvline(a, color='k', linewidth=3)
    ax1.axvline(-a, ymin=0.5, ymax=1, color='k', linewidth=3)
    ax1.axvline(a, ymin=0.5, ymax=1, color='k', linewidth=3)
    ax1.set_xlim(-1.5*a, 1.5*a)
    ax1.set_ylim(-0.5, 2)
    ax1.set_xlabel('$x$', fontsize=14)
    ax1.set_ylabel('$V(x)$', fontsize=14)
    ax1.set_title('問題3-3: 箱の中の粒子のポテンシャル', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 下段: 固有関数
    ax2 = axes[1]
    x_in = np.linspace(-a, a, 500)
    
    # n=1,2,3の固有関数
    for n in [1, 2, 3]:
        if n % 2 == 1:  # 奇数の場合: 余弦
            u = (1/np.sqrt(a)) * np.cos(n*np.pi*x_in/(2*a))
            label = f'$u_{n}(x)$ (偶関数)'
        else:  # 偶数の場合: 正弦
            u = (1/np.sqrt(a)) * np.sin(n*np.pi*x_in/(2*a))
            label = f'$u_{n}(x)$ (奇関数)'
        
        # エネルギー固有値
        E_n = (hbar**2 * np.pi**2 * n**2) / (8*m*a**2)
        ax2.plot(x_in, u + E_n, label=label, linewidth=2)
        ax2.axhline(E_n, color='gray', linestyle='--', alpha=0.5)
    
    ax2.axvline(-a, color='k', linewidth=2)
    ax2.axvline(a, color='k', linewidth=2)
    ax2.set_xlim(-1.5*a, 1.5*a)
    ax2.set_xlabel('$x$', fontsize=14)
    ax2.set_ylabel('$u_n(x)$ (エネルギー基準でシフト)', fontsize=14)
    ax2.set_title('問題3-3: 箱の中の粒子の固有関数', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('../figures/problem3_3_wavefunctions.png', dpi=300, bbox_inches='tight')
    print("問題3-3の図を保存: figures/problem3_3_wavefunctions.png")
    plt.close()

# ============================================
# 問題3-4: 箱の中の粒子の期待値
# ============================================
def plot_problem3_4():
    """問題3-4: 箱の中の粒子の確率密度"""
    a = 1.0
    x = np.linspace(0, a, 1000)
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # 上段: 確率密度 |u_n(x)|^2
    ax1 = axes[0]
    for n in [1, 2, 3]:
        u = np.sqrt(2/a) * np.sin(n*np.pi*x/a)
        prob_density = u**2
        ax1.plot(x, prob_density, label=f'$n={n}$: $|u_n(x)|^2$', linewidth=2)
    
    ax1.axvline(0, color='k', linewidth=2)
    ax1.axvline(a, color='k', linewidth=2)
    ax1.axvline(a/2, color='r', linestyle='--', alpha=0.5, label='箱の中心')
    ax1.set_xlim(-0.1*a, 1.1*a)
    ax1.set_xlabel('$x$', fontsize=14)
    ax1.set_ylabel('$|u_n(x)|^2$', fontsize=14)
    ax1.set_title('問題3-4: 箱の中の粒子の確率密度', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 下段: 基底状態の詳細
    ax2 = axes[1]
    n = 1
    u1 = np.sqrt(2/a) * np.sin(np.pi*x/a)
    prob_density_1 = u1**2
    
    ax2.plot(x, prob_density_1, 'b-', linewidth=2, label='$|u_1(x)|^2$')
    ax2.fill_between(x, 0, prob_density_1, alpha=0.3)
    ax2.axvline(a/2, color='r', linestyle='--', linewidth=2, label='期待値 $\\langle x \\rangle = a/2$')
    ax2.axvline(0, color='k', linewidth=2)
    ax2.axvline(a, color='k', linewidth=2)
    
    # 不確定性の範囲を示す
    kappa = np.sqrt((np.pi**2 - 6) / 12)
    delta_x = a * kappa / np.pi
    ax2.axvspan(a/2 - delta_x, a/2 + delta_x, alpha=0.2, color='green', label='$\\Delta x$の範囲')
    
    ax2.set_xlim(-0.1*a, 1.1*a)
    ax2.set_xlabel('$x$', fontsize=14)
    ax2.set_ylabel('$|u_1(x)|^2$', fontsize=14)
    ax2.set_title('問題3-4: 基底状態の確率密度と不確定性', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('../figures/problem3_4_probability_density.png', dpi=300, bbox_inches='tight')
    print("問題3-4の図を保存: figures/problem3_4_probability_density.png")
    plt.close()

# ============================================
# 問題5-1: トンネル効果
# ============================================
def plot_problem5_1():
    """問題5-1: トンネル効果の波動関数とポテンシャル"""
    V0 = 1.0
    a = 1.0
    E = 0.5 * V0  # E < V0
    k = np.sqrt(2*m*E) / hbar
    kappa = np.sqrt(2*m*(V0 - E)) / hbar
    
    # 簡略化のため、透過率を計算（詳細は省略）
    # 実際の計算では連続条件からB, Cを求める必要がある
    
    x_left = np.linspace(-3*a, -a, 500)
    x_barrier = np.linspace(-a, a, 500)
    x_right = np.linspace(a, 3*a, 500)
    
    # 入射波と反射波（簡略化）
    A = 1.0
    B = 0.3  # 仮の値
    u_left = A * np.exp(1j*k*x_left) + B * np.exp(-1j*k*x_left)
    
    # 障壁内（指数減衰）
    F = 0.5  # 仮の値
    G = 0.3  # 仮の値
    u_barrier = F * np.exp(kappa*x_barrier) + G * np.exp(-kappa*x_barrier)
    
    # 透過波
    C = 0.2  # 仮の値
    u_right = C * np.exp(1j*k*x_right)
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # 上段: ポテンシャル
    ax1 = axes[0]
    x_all = np.concatenate([x_left, x_barrier, x_right])
    V_all = np.zeros_like(x_all)
    V_all[(x_all >= -a) & (x_all <= a)] = V0
    
    ax1.plot(x_all, V_all, 'k-', linewidth=2, label='$V(x)$')
    ax1.axhline(E, color='r', linestyle='--', linewidth=2, label=f'$E = {E:.2f}V_0$')
    ax1.set_xlim(-3*a, 3*a)
    ax1.set_ylim(-0.2*V0, 1.5*V0)
    ax1.set_xlabel('$x$', fontsize=14)
    ax1.set_ylabel('$V(x)$', fontsize=14)
    ax1.set_title('問題5-1: トンネル効果のポテンシャル障壁', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 下段: 波動関数の絶対値
    ax2 = axes[1]
    ax2.plot(x_left, np.abs(u_left), 'b-', linewidth=2, label='入射波+反射波')
    ax2.plot(x_barrier, np.abs(u_barrier), 'g-', linewidth=2, label='障壁内（減衰）')
    ax2.plot(x_right, np.abs(u_right), 'r-', linewidth=2, label='透過波')
    ax2.axvline(-a, color='k', linestyle='--', alpha=0.5)
    ax2.axvline(a, color='k', linestyle='--', alpha=0.5)
    ax2.set_xlim(-3*a, 3*a)
    ax2.set_xlabel('$x$', fontsize=14)
    ax2.set_ylabel('$|u(x)|$', fontsize=14)
    ax2.set_title('問題5-1: トンネル効果の波動関数', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('../figures/problem5_1_tunnel_effect.png', dpi=300, bbox_inches='tight')
    print("問題5-1の図を保存: figures/problem5_1_tunnel_effect.png")
    plt.close()

# ============================================
# 問題5-2: ポテンシャル井戸での束縛状態
# ============================================
def plot_problem5_2():
    """問題5-2: ポテンシャル井戸での束縛状態"""
    V0 = 2.0
    a = 1.0
    
    x_left = np.linspace(-0.5*a, 0, 200)
    x_well = np.linspace(0, a, 500)
    x_right = np.linspace(a, 3*a, 500)
    
    # ポテンシャル
    V_left = np.full_like(x_left, np.inf)
    V_well = np.full_like(x_well, -V0)
    V_right = np.zeros_like(x_right)
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # 上段: ポテンシャル
    ax1 = axes[0]
    ax1.plot(x_left, np.zeros_like(x_left), 'k-', linewidth=2)
    ax1.axvline(0, color='k', linewidth=3, ymin=0.3, ymax=0.7)
    ax1.plot(x_well, V_well, 'b-', linewidth=2, label='$V(x) = -V_0$')
    ax1.plot(x_right, V_right, 'k-', linewidth=2, label='$V(x) = 0$')
    ax1.axhline(0, color='k', linestyle='-', linewidth=1)
    ax1.set_xlim(-0.5*a, 3*a)
    ax1.set_ylim(-1.5*V0, 0.5*V0)
    ax1.set_xlabel('$x$', fontsize=14)
    ax1.set_ylabel('$V(x)$', fontsize=14)
    ax1.set_title('問題5-2: ポテンシャル井戸', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 下段: 束縛状態の波動関数（概形）
    ax2 = axes[1]
    # 簡略化のため、典型的な束縛状態の形を描画
    q = 2.0  # 仮の値
    kappa = 1.5  # 仮の値
    
    u_well = np.sin(q*x_well)
    u_right = np.exp(-kappa*(x_right - a))
    
    # 規格化
    norm_well = np.sqrt(np.trapz(u_well**2, x_well))
    norm_right = np.sqrt(np.trapz(u_right**2, x_right))
    u_well = u_well / norm_well
    u_right = u_right / norm_right
    
    ax2.plot(x_well, u_well, 'b-', linewidth=2, label='井戸内（振動）')
    ax2.plot(x_right, u_right, 'r-', linewidth=2, label='井戸外（減衰）')
    ax2.axvline(0, color='k', linewidth=2)
    ax2.axvline(a, color='k', linestyle='--', alpha=0.5)
    ax2.axhline(0, color='k', linestyle='-', linewidth=1)
    ax2.set_xlim(-0.5*a, 3*a)
    ax2.set_xlabel('$x$', fontsize=14)
    ax2.set_ylabel('$u(x)$', fontsize=14)
    ax2.set_title('問題5-2: 束縛状態の波動関数（概形）', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('../figures/problem5_2_bound_state.png', dpi=300, bbox_inches='tight')
    print("問題5-2の図を保存: figures/problem5_2_bound_state.png")
    plt.close()

# ============================================
# 問題5-3: デルタ関数型ポテンシャル
# ============================================
def plot_problem5_3():
    """問題5-3: デルタ関数型ポテンシャルでの束縛状態"""
    lambda_val = 1.0
    kappa = m * lambda_val / (hbar**2)
    E = -m * lambda_val**2 / (2 * hbar**2)
    A = np.sqrt(kappa)
    
    x_left = np.linspace(-3, 0, 500)
    x_right = np.linspace(0, 3, 500)
    
    # 波動関数
    u_left = A * np.exp(kappa * x_left)
    u_right = A * np.exp(-kappa * x_right)
    
    # 確率密度
    prob_left = u_left**2
    prob_right = u_right**2
    
    fig, axes = plt.subplots(3, 1, figsize=(10, 10))
    
    # 上段: ポテンシャル（デルタ関数）
    ax1 = axes[0]
    ax1.axvline(0, color='r', linewidth=3, label='$V(x) = -\\lambda\\delta(x)$')
    ax1.axhline(0, color='k', linestyle='-', linewidth=1)
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-0.5, 0.5)
    ax1.set_xlabel('$x$', fontsize=14)
    ax1.set_ylabel('$V(x)$', fontsize=14)
    ax1.set_title('問題5-3: デルタ関数型ポテンシャル', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.text(0.2, -0.3, '$x=0$', fontsize=12)
    
    # 中段: 波動関数
    ax2 = axes[1]
    ax2.plot(x_left, u_left, 'b-', linewidth=2, label='$u(x) = Ae^{\\kappa x}$')
    ax2.plot(x_right, u_right, 'b-', linewidth=2, label='$u(x) = Ae^{-\\kappa x}$')
    ax2.axvline(0, color='r', linestyle='--', alpha=0.5)
    ax2.axhline(0, color='k', linestyle='-', linewidth=1)
    ax2.set_xlim(-3, 3)
    ax2.set_xlabel('$x$', fontsize=14)
    ax2.set_ylabel('$u(x)$', fontsize=14)
    ax2.set_title('問題5-3: 束縛状態の波動関数', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # 下段: 確率密度
    ax3 = axes[2]
    ax3.plot(x_left, prob_left, 'g-', linewidth=2, label='$|u(x)|^2$')
    ax3.plot(x_right, prob_right, 'g-', linewidth=2)
    ax3.fill_between(x_left, 0, prob_left, alpha=0.3, color='green')
    ax3.fill_between(x_right, 0, prob_right, alpha=0.3, color='green')
    ax3.axvline(0, color='r', linestyle='--', alpha=0.5, label='$x=0$ (最大)')
    ax3.axhline(0, color='k', linestyle='-', linewidth=1)
    ax3.set_xlim(-3, 3)
    ax3.set_xlabel('$x$', fontsize=14)
    ax3.set_ylabel('$|u(x)|^2$', fontsize=14)
    ax3.set_title('問題5-3: 確率密度', fontsize=14)
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    
    plt.tight_layout()
    plt.savefig('../figures/problem5_3_delta_potential.png', dpi=300, bbox_inches='tight')
    print("問題5-3の図を保存: figures/problem5_3_delta_potential.png")
    plt.close()

# ============================================
# メイン実行
# ============================================
if __name__ == '__main__':
    print("量子力学演習問題の図を作成中...")
    print("=" * 50)
    
    try:
        plot_problem3_3()
    except Exception as e:
        print(f"問題3-3の図作成でエラー: {e}")
    
    try:
        plot_problem3_4()
    except Exception as e:
        print(f"問題3-4の図作成でエラー: {e}")
    
    try:
        plot_problem5_1()
    except Exception as e:
        print(f"問題5-1の図作成でエラー: {e}")
    
    try:
        plot_problem5_2()
    except Exception as e:
        print(f"問題5-2の図作成でエラー: {e}")
    
    try:
        plot_problem5_3()
    except Exception as e:
        print(f"問題5-3の図作成でエラー: {e}")
    
    print("=" * 50)
    print("すべての図の作成が完了しました。")
