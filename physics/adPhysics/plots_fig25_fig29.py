"""
fig25とfig29の図を作成するスクリプト
"""

import matplotlib
matplotlib.use('Agg')  # 非インタラクティブバックエンド

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import matplotlib.patches as mpatches

# 日本語フォントの設定
import platform
if platform.system() == 'Darwin':  # macOS
    plt.rcParams['font.family'] = 'Hiragino Sans'
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'MS Gothic'
else:  # Linux
    plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['text.usetex'] = False  # LaTeXレンダリングを無効化（ParseExceptionエラーを回避）

# mathtextパーサーの問題を回避するためのヘルパー関数
def safe_set_label(ax_method, label, *args, **kwargs):
    """mathtextパーサーエラーを回避してラベルを設定"""
    try:
        ax_method(label, *args, **kwargs)
    except Exception:
        # エラーが発生した場合は、$記号を削除して再試行
        fallback_label = label.replace('$', '') if isinstance(label, str) else str(label).replace('$', '')
        try:
            ax_method(fallback_label, *args, **kwargs)
        except Exception:
            # それでもエラーが発生した場合は、空文字列を設定
            ax_method('', *args, **kwargs)

def plot_2023_twin_paradox_simultaneity():
    """2023年度問題2(ii): 同時の相対性を示す図を作成"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # パラメータ
    c = 1.0
    v = 0.6 * c
    beta = v / c
    gamma = 1.0 / np.sqrt(1 - beta**2)
    
    # 地点Pの位置
    x_P = 1.0
    t_P = x_P / v
    
    # 宇宙船の軌跡
    t1 = np.linspace(0, t_P, 100)
    x1 = v * t1
    ax.plot(c*t1, x1, 'b-', linewidth=3, label='宇宙船の軌跡 (往路)')
    
    t2 = np.linspace(t_P, 2*t_P, 100)
    x2 = x_P - v * (t2 - t_P)
    ax.plot(c*t2, x2, 'b-', linewidth=3, label='宇宙船の軌跡 (復路)')
    
    # 地点P
    ax.plot(c*t_P, x_P, 'ro', markersize=12, label='地点P', zorder=5)
    
    # 地球の軌跡
    ax.axvline(x=0, color='k', linestyle='--', linewidth=2, alpha=0.7, label='地球 (原点)')
    
    # S'系の同時線（往路）
    # 地点P到達時（S'系の時刻t2）の同時線
    x_sim = np.linspace(-0.5, 1.5, 100)
    ct_sim = c*t_P + beta * (x_sim - x_P)
    ax.plot(ct_sim, x_sim, 'g--', linewidth=2, alpha=0.7, label="S'系の同時線")
    
    # S系の同時線（t=t1）
    ax.axhline(y=0, xmin=0, xmax=c*t_P/(2*c*t_P), color='orange', linestyle=':', linewidth=2, alpha=0.7, label='S系の同時線')
    
    # t3の位置
    t3 = gamma * (t_P / gamma)  # S'系から見たS系の原点の時刻
    # 実際には、S'系の同時線がx=0を通る点
    # Lorentz変換で t3 = gamma*(t_P - beta*x_P/c) = gamma*(t_P - beta*x_P)
    t3_actual = gamma * (t_P - beta * x_P)
    ax.plot(c * t3_actual, 0, 'go', markersize=10, zorder=5, label="t3 (S'系から見たS系の時刻)")
    ax.text(c * t3_actual, -0.15, r'$t_3 = \gamma (t_2 - \beta x_P/c)$', fontsize=12, ha='center', color='g')
    
    # t1の位置
    ax.plot(c*t_P, 0, 'mo', markersize=10, zorder=5, label='t1 (S系の時刻)')
    ax.text(c*t_P, -0.3, r'$t_1$', fontsize=12, ha='center', color='m')
    
    # 説明テキスト
    ax.text(0.5*c*t_P, 1.3, '同時の相対性:', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    ax.text(0.5*c*t_P, 1.1, 'S系ではt1が同時', fontsize=12, ha='center')
    ax.text(0.5*c*t_P, 0.9, "S'系ではt2が同時", fontsize=12, ha='center')
    ax.text(0.5*c*t_P, 0.7, "S'系から見ると、S系の原点の時刻はt3", fontsize=12, ha='center')
    
    safe_set_label(ax.set_xlabel, 'ct', fontsize=14)
    safe_set_label(ax.set_ylabel, 'x', fontsize=14)
    ax.set_title('2023年度問題2(ii): 同時の相対性', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_aspect('equal')
    ax.set_xlim(-0.2, 2.2*c*t_P)
    ax.set_ylim(-0.5, 1.5)
    
    plt.tight_layout()
    plt.savefig('fig29_2023_twin_paradox_simultaneity.png', dpi=300, bbox_inches='tight')
    print("2023年度問題2(ii): 同時の相対性の図を保存しました: fig29_2023_twin_paradox_simultaneity.png")
    plt.close()

def plot_2025_rigid_pendulum_cases():
    """2025年度問題1(iv): ケースAとケースBの剛体振り子の図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # 共通パラメータ
    l = 1.0
    theta = np.pi / 6  # 30度
    a = 0.3  # 正方形板の一辺の長さ
    
    # 回転軸（原点）
    x0, y0 = 0, 0
    
    # 重心の位置
    x_cm = l * np.sin(theta)
    z_cm = l * np.cos(theta)
    
    # ケースA: 板の面が回転軸に垂直
    ax1.plot(x0, y0, 'ko', markersize=10, label='回転軸 O')
    ax1.plot([x0, x_cm], [y0, z_cm], 'k-', linewidth=2, label='棒')
    ax1.plot(x_cm, z_cm, 'ro', markersize=8, label='重心')
    
    # 正方形板（板面が回転軸に垂直、つまりxy平面に平行）
    square_size = a / 2
    square_x = [x_cm - square_size * np.cos(theta), x_cm + square_size * np.cos(theta)]
    square_z = [z_cm - square_size * np.sin(theta), z_cm + square_size * np.sin(theta)]
    ax1.plot(square_x, square_z, 'b-', linewidth=3, label='正方形板（ケースA）')
    ax1.fill_between(square_x, square_z, square_z, alpha=0.3, color='blue')
    
    # 角度の表示
    arc_radius = 0.3
    angle_arc = np.linspace(0, theta, 50)
    ax1.plot(arc_radius * np.sin(angle_arc), arc_radius * np.cos(angle_arc), 'r--', linewidth=1)
    ax1.text(0.15, 0.15, r'$\theta$', fontsize=14)
    
    # 重力の表示
    ax1.arrow(x_cm, z_cm, 0, -0.2, head_width=0.05, head_length=0.05, fc='g', ec='g', linewidth=2)
    ax1.text(x_cm + 0.1, z_cm - 0.1, r'$Mg$', fontsize=12, color='g')
    
    # 座標軸
    ax1.arrow(-0.5, 0, 1.5, 0, head_width=0.05, head_length=0.05, fc='k', ec='k', linewidth=1)
    ax1.arrow(0, -0.5, 0, 1.5, head_width=0.05, head_length=0.05, fc='k', ec='k', linewidth=1)
    ax1.text(1.3, -0.1, r'$x$', fontsize=12)
    ax1.text(-0.1, 1.3, r'$z$', fontsize=12)
    
    ax1.set_xlim(-0.5, 1.5)
    ax1.set_ylim(-0.5, 1.5)
    ax1.set_aspect('equal')
    safe_set_label(ax1.set_xlabel, 'x', fontsize=12)
    safe_set_label(ax1.set_ylabel, 'z', fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right')
    ax1.set_title('ケースA: 板の面が回転軸に垂直', fontsize=14, fontweight='bold')
    ax1.text(0.5, -0.4, r'$I_A = M\left(\frac{a^2}{6} + \ell^2\right)$', 
            fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    # ケースB: 板の面が回転面に垂直
    ax2.plot(x0, y0, 'ko', markersize=10, label='回転軸 O')
    ax2.plot([x0, x_cm], [y0, z_cm], 'k-', linewidth=2, label='棒')
    ax2.plot(x_cm, z_cm, 'ro', markersize=8, label='重心')
    
    # 正方形板（板面が回転面に垂直、つまりxz平面に垂直、y軸に平行）
    square_x_b = [x_cm - square_size * np.sin(theta), x_cm + square_size * np.sin(theta)]
    square_z_b = [z_cm - square_size * np.cos(theta), z_cm + square_size * np.cos(theta)]
    ax2.plot(square_x_b, square_z_b, 'g-', linewidth=3, label='正方形板（ケースB）')
    # 板の厚みを示す
    ax2.plot([square_x_b[0], square_x_b[0]], [square_z_b[0] - 0.05, square_z_b[0] + 0.05], 
            'g-', linewidth=2)
    ax2.plot([square_x_b[1], square_x_b[1]], [square_z_b[1] - 0.05, square_z_b[1] + 0.05], 
            'g-', linewidth=2)
    
    # 角度の表示
    ax2.plot(arc_radius * np.sin(angle_arc), arc_radius * np.cos(angle_arc), 'r--', linewidth=1)
    ax2.text(0.15, 0.15, r'$\theta$', fontsize=14)
    
    # 重力の表示
    ax2.arrow(x_cm, z_cm, 0, -0.2, head_width=0.05, head_length=0.05, fc='g', ec='g', linewidth=2)
    ax2.text(x_cm + 0.1, z_cm - 0.1, r'$Mg$', fontsize=12, color='g')
    
    # 座標軸
    ax2.arrow(-0.5, 0, 1.5, 0, head_width=0.05, head_length=0.05, fc='k', ec='k', linewidth=1)
    ax2.arrow(0, -0.5, 0, 1.5, head_width=0.05, head_length=0.05, fc='k', ec='k', linewidth=1)
    ax2.text(1.3, -0.1, r'$x$', fontsize=12)
    ax2.text(-0.1, 1.3, r'$z$', fontsize=12)
    
    ax2.set_xlim(-0.5, 1.5)
    ax2.set_ylim(-0.5, 1.5)
    ax2.set_aspect('equal')
    safe_set_label(ax2.set_xlabel, 'x', fontsize=12)
    safe_set_label(ax2.set_ylabel, 'z', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    ax2.set_title('ケースB: 板の面が回転面に垂直', fontsize=14, fontweight='bold')
    ax2.text(0.5, -0.4, r'$I_B = M\left(\frac{a^2}{12} + \ell^2\right)$', 
            fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    plt.suptitle('2025年度問題1(iv): ケースAとケースBの剛体振り子', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('fig25_2025_rigid_pendulum_cases.png', dpi=300, bbox_inches='tight')
    print("2025年度問題1(iv): ケースAとケースBの図を保存しました: fig25_2025_rigid_pendulum_cases.png")
    plt.close()

if __name__ == '__main__':
    print("fig25とfig29の図を作成中...")
    plot_2025_rigid_pendulum_cases()
    plot_2023_twin_paradox_simultaneity()
    print("完了しました。")
