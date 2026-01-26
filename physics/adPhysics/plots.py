"""
力学特論演習問題の図を作成するスクリプト
"""

import matplotlib
matplotlib.use('Agg')  # 非インタラクティブバックエンド（並列処理対応）

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D

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

# ============================================
# 問題1-2: 単振り子
# ============================================

def plot_pendulum():
    """単振り子の図を作成"""
    fig, ax = plt.subplots(figsize=(8, 10))
    
    # 固定点
    x0, y0 = 0, 0
    ax.plot(x0, y0, 'ko', markersize=10, label='固定点')
    
    # 糸の長さ
    l = 1.0
    theta = np.pi / 4  # 45度
    
    # 振り子の位置
    x_pendulum = l * np.sin(theta)
    y_pendulum = -l * np.cos(theta)
    
    # 糸
    ax.plot([x0, x_pendulum], [y0, y_pendulum], 'k-', linewidth=2, label='糸')
    
    # おもり
    circle = Circle((x_pendulum, y_pendulum), 0.05, color='blue', zorder=5)
    ax.add_patch(circle)
    
    # 角度の表示
    arc_radius = 0.3
    arc = mpatches.Arc((x0, y0), arc_radius, arc_radius, angle=0, 
                       theta1=0, theta2=np.degrees(theta), 
                       color='red', linewidth=1.5)
    ax.add_patch(arc)
    ax.text(0.15, -0.05, r'$\theta$', fontsize=14, color='red')
    
    # 重力の方向
    ax.arrow(x_pendulum, y_pendulum, 0, -0.2, 
             head_width=0.05, head_length=0.05, fc='green', ec='green', linewidth=2)
    ax.text(x_pendulum + 0.1, y_pendulum - 0.15, r'$mg$', fontsize=12, color='green')
    
    # 座標軸
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    
    # 設定
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 0.5)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, 'x', fontsize=12)
    safe_set_label(ax.set_ylabel, 'y', fontsize=12)
    ax.set_title('単振り子', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('fig1_pendulum.png', dpi=300, bbox_inches='tight')
    print("単振り子の図を保存しました: fig1_pendulum.png")
    plt.close()

# ============================================
# 問題1-3: 2次元調和振動子
# ============================================

def plot_harmonic_oscillator():
    """2次元調和振動子の軌道を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # パラメータ
    m = 1.0
    k = 1.0
    l = 1.0  # 自然長
    p_phi = 0.5  # 角運動量
    E = 1.5  # エネルギー
    
    # 時間
    t = np.linspace(0, 10, 1000)
    
    # 軌道の計算（簡略化）
    r0 = l + 0.3  # 初期半径
    omega_phi = p_phi / (m * r0**2)  # 角速度
    omega_r = np.sqrt(k / m)  # 半径方向の角振動数
    
    r = l + 0.3 * np.cos(omega_r * t)
    phi = omega_phi * t
    
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    
    # 左図: 軌道
    ax1.plot(x, y, 'b-', linewidth=1.5, label='軌道')
    ax1.plot(0, 0, 'ko', markersize=8, label='中心')
    circle = Circle((0, 0), l, color='r', fill=False, linestyle='--', 
                    linewidth=2, label=f'自然長 $r = l = {l}$')
    ax1.add_patch(circle)
    
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_aspect('equal')
    safe_set_label(ax1.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax1.set_ylabel, '$y$', fontsize=12)
    ax1.set_title('2次元調和振動子の軌道', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 右図: 半径の時間変化
    ax2.plot(t, r, 'b-', linewidth=2, label=r'$r(t)$')
    ax2.axhline(y=l, color='r', linestyle='--', linewidth=2, label=f'自然長 $l = {l}$')
    safe_set_label(ax2.set_xlabel, '時間 $t$', fontsize=12)
    safe_set_label(ax2.set_ylabel, '半径 $r$', fontsize=12)
    ax2.set_title('半径の時間変化', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('fig2_harmonic_oscillator.png', dpi=300, bbox_inches='tight')
    print("2次元調和振動子の図を保存しました: fig2_harmonic_oscillator.png")
    plt.close()

# ============================================
# 問題6-3, 6-4: ローレンツ変換
# ============================================

def plot_lorentz_transformation():
    """ローレンツ変換の時空図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # パラメータ
    c = 1.0  # 光速
    beta = 0.6  # v/c
    gamma = 1.0 / np.sqrt(1 - beta**2)
    
    # 左図: 時空図（ct-x平面）
    # 静止系の座標軸
    ct = np.linspace(-2, 2, 100)
    x = np.linspace(-2, 2, 100)
    
    # 光の世界線
    ax1.plot(ct, ct, 'r--', linewidth=1.5, alpha=0.5, label='光の世界線 $x = ct$')
    ax1.plot(ct, -ct, 'r--', linewidth=1.5, alpha=0.5, label='光の世界線 $x = -ct$')
    
    # 静止系の座標軸
    ax1.axhline(y=0, color='k', linestyle='-', linewidth=1, alpha=0.5)
    ax1.axvline(x=0, color='k', linestyle='-', linewidth=1, alpha=0.5)
    
    # 運動系の座標軸
    # ct'軸: x' = 0, すなわち x = beta * ct
    ct_prime_axis = ct
    x_prime_axis = beta * ct
    ax1.plot(ct_prime_axis, x_prime_axis, 'b-', linewidth=2, label=r"$ct'$軸 ($x' = 0$)")
    
    # x'軸: ct' = 0, すなわち ct = beta * x
    x_prime_axis2 = x
    ct_prime_axis2 = beta * x
    ax1.plot(ct_prime_axis2, x_prime_axis2, 'g-', linewidth=2, label=r"$x'$軸 ($ct' = 0$)")
    
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    safe_set_label(ax1.set_xlabel, '$ct$', fontsize=12)
    safe_set_label(ax1.set_ylabel, '$x$', fontsize=12)
    ax1.set_title('ローレンツ変換の時空図', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper left')
    ax1.set_aspect('equal')
    
    # 右図: エネルギー運動量ベクトルの変換
    # 静止系でのエネルギー運動量
    m = 1.0
    v1 = 0.5 * c
    gamma1 = 1.0 / np.sqrt(1 - (v1/c)**2)
    
    E1 = gamma1 * m * c**2
    p1 = gamma1 * m * v1
    
    # ローレンツ変換後のエネルギー運動量
    E2 = gamma * (E1 - beta * c * p1)
    p2 = gamma * (p1 - beta * E1 / c)
    
    # プロット
    systems = ['静止系 $O_1$', '運動系 $O_2$']
    energies = [E1, E2]
    momenta = [p1, p2]
    
    x_pos = np.arange(len(systems))
    width = 0.35
    
    ax2.bar(x_pos - width/2, energies, width, label='エネルギー $E$', alpha=0.7)
    ax2.bar(x_pos + width/2, momenta, width, label='運動量 $p$', alpha=0.7)
    
    safe_set_label(ax2.set_xlabel, '慣性系', fontsize=12)
    safe_set_label(ax2.set_ylabel, '値', fontsize=12)
    ax2.set_title('エネルギー運動量ベクトルの変換', fontsize=14, fontweight='bold')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(systems)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('fig3_lorentz_transformation.png', dpi=300, bbox_inches='tight')
    print("ローレンツ変換の図を保存しました: fig3_lorentz_transformation.png")
    plt.close()

# ============================================
# 問題1-2: ポテンシャルエネルギー
# ============================================

def plot_pendulum_potential():
    """単振り子のポテンシャルエネルギー"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    theta = np.linspace(-np.pi, np.pi, 1000)
    m = 1.0
    g = 9.8
    l = 1.0
    
    V = m * g * l * (1 - np.cos(theta))
    
    ax.plot(theta, V, 'b-', linewidth=2, label=r'$V(\theta) = mg\ell(1 - \cos\theta)$')
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    
    safe_set_label(ax.set_xlabel, r'$\theta$ (rad)', fontsize=12)
    safe_set_label(ax.set_ylabel, r'$V(\theta)$', fontsize=12)
    ax.set_title('単振り子のポテンシャルエネルギー', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig4_pendulum_potential.png', dpi=300, bbox_inches='tight')
    print("単振り子のポテンシャルエネルギーの図を保存しました: fig4_pendulum_potential.png")
    plt.close()

# ============================================
# 問題2-1: 重心（扇形の板、円錐）
# ============================================

def plot_center_of_mass():
    """重心の問題の図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 扇形の板
    alpha = np.pi / 3
    a = 1.0
    theta = np.linspace(-alpha, alpha, 100)
    r = np.linspace(0, a, 50)
    Theta, R = np.meshgrid(theta, r)
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    
    ax1.fill_between([0, a*np.cos(alpha)], [0, a*np.sin(alpha)], alpha=0.3, color='blue')
    ax1.fill_between([0, a*np.cos(alpha)], [0, -a*np.sin(alpha)], alpha=0.3, color='blue')
    ax1.plot([0, a*np.cos(alpha)], [0, a*np.sin(alpha)], 'k-', linewidth=2)
    ax1.plot([0, a*np.cos(alpha)], [0, -a*np.sin(alpha)], 'k-', linewidth=2)
    arc = mpatches.Arc((0, 0), 2*a, 2*a, angle=0, theta1=-np.degrees(alpha), 
                       theta2=np.degrees(alpha), color='k', linewidth=2)
    ax1.add_patch(arc)
    ax1.plot(0, 0, 'ko', markersize=8)
    ax1.set_xlim(-0.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal')
    safe_set_label(ax1.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax1.set_ylabel, '$y$', fontsize=12)
    ax1.set_title('扇形の板', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # 右図: 円錐
    fig2 = plt.figure(figsize=(8, 8))
    ax3 = fig2.add_subplot(111, projection='3d')
    
    h = 2.0
    a = 1.0
    z = np.linspace(0, h, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    Z, Theta = np.meshgrid(z, theta)
    R = a * (1 - Z / h)
    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)
    
    ax3.plot_surface(X, Y, Z, alpha=0.7, color='blue')
    safe_set_label(ax3.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax3.set_ylabel, '$y$', fontsize=12)
    safe_set_label(ax3.set_zlabel, '$z$', fontsize=12)
    ax3.set_title('直円錐', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('fig5_center_of_mass.png', dpi=300, bbox_inches='tight')
    print("重心の問題の図を保存しました: fig5_center_of_mass.png")
    plt.close()
    plt.close(fig2)

# ============================================
# 問題2-2: 主慣性モーメント
# ============================================

def plot_moments_of_inertia():
    """主慣性モーメントの問題の図を作成"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    
    # (i) 円環
    ax = axes[0, 0]
    circle = Circle((0, 0), 1.0, fill=False, linewidth=3, color='blue')
    ax.add_patch(circle)
    ax.plot(0, 0, 'ko', markersize=8)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_title('円環', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # (ii) 円板
    ax = axes[0, 1]
    circle = Circle((0, 0), 1.0, fill=True, alpha=0.5, color='blue')
    ax.add_patch(circle)
    ax.plot(0, 0, 'ko', markersize=8)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_title('円板', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # (iii) 球殻
    ax = axes[1, 0]
    circle = Circle((0, 0), 1.0, fill=False, linewidth=3, color='blue')
    ax.add_patch(circle)
    ax.plot(0, 0, 'ko', markersize=8)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_title('球殻（断面）', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # (iv) 球
    ax = axes[1, 1]
    circle = Circle((0, 0), 1.0, fill=True, alpha=0.5, color='blue')
    ax.add_patch(circle)
    ax.plot(0, 0, 'ko', markersize=8)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_title('球（断面）', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('fig6_moments_of_inertia.png', dpi=300, bbox_inches='tight')
    print("主慣性モーメントの問題の図を保存しました: fig6_moments_of_inertia.png")
    plt.close()

# ============================================
# 問題2-4: 2次元剛体の運動
# ============================================

def plot_2d_rigid_body():
    """2次元剛体の運動の図を作成"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 重心
    R = np.array([2.0, 1.0])
    ax.plot(R[0], R[1], 'ko', markersize=10, label='重心')
    
    # 2つの質点
    theta = np.pi / 6
    r1_prime = 0.5
    r2_prime = 0.3
    r1 = R + r1_prime * np.array([np.cos(theta), np.sin(theta)])
    r2 = R - r2_prime * np.array([np.cos(theta), np.sin(theta)])
    
    ax.plot(r1[0], r1[1], 'bo', markersize=15, label='質点1')
    ax.plot(r2[0], r2[1], 'ro', markersize=15, label='質点2')
    
    # 棒
    ax.plot([r1[0], r2[0]], [r1[1], r2[1]], 'k-', linewidth=3, label='棒')
    
    # 重心からのベクトル
    ax.arrow(R[0], R[1], r1[0]-R[0], r1[1]-R[1], head_width=0.1, head_length=0.1, 
             fc='blue', ec='blue', linewidth=2, alpha=0.5)
    ax.arrow(R[0], R[1], r2[0]-R[0], r2[1]-R[1], head_width=0.1, head_length=0.1, 
             fc='red', ec='red', linewidth=2, alpha=0.5)
    
    # 重力
    ax.arrow(r1[0], r1[1], 0, -0.3, head_width=0.1, head_length=0.1, 
             fc='green', ec='green', linewidth=2)
    ax.arrow(r2[0], r2[1], 0, -0.3, head_width=0.1, head_length=0.1, 
             fc='green', ec='green', linewidth=2)
    
    ax.set_xlim(0, 4)
    ax.set_ylim(-1, 3)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    ax.set_title('2次元空間上での剛体の運動', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig7_2d_rigid_body.png', dpi=300, bbox_inches='tight')
    print("2次元剛体の運動の図を保存しました: fig7_2d_rigid_body.png")
    plt.close()

# ============================================
# 問題3-2: 剛体振り子
# ============================================

def plot_rigid_pendulum():
    """剛体振り子の図を作成"""
    fig, ax = plt.subplots(figsize=(8, 10))
    
    # 固定点
    x0, y0 = 0, 0
    ax.plot(x0, y0, 'ko', markersize=10, label='固定点')
    
    # 重心の位置
    l = 1.0
    theta = np.pi / 4
    x_cm = l * np.sin(theta)
    y_cm = -l * np.cos(theta)
    
    # 棒
    ax.plot([x0, x_cm], [y0, y_cm], 'k-', linewidth=3, label='剛体')
    
    # 重心
    ax.plot(x_cm, y_cm, 'ro', markersize=12, label='重心')
    
    # 角度
    arc = mpatches.Arc((x0, y0), 0.3, 0.3, angle=0, theta1=-90, 
                       theta2=-90+np.degrees(theta), color='red', linewidth=1.5)
    ax.add_patch(arc)
    ax.text(0.15, -0.05, r'$\theta$', fontsize=14, color='red')
    
    # 重力
    ax.arrow(x_cm, y_cm, 0, -0.3, head_width=0.05, head_length=0.05, 
             fc='green', ec='green', linewidth=2)
    ax.text(x_cm + 0.1, y_cm - 0.2, r'$Mg$', fontsize=12, color='green')
    
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 0.5)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$z$', fontsize=12)
    ax.set_title('剛体振り子', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig8_rigid_pendulum.png', dpi=300, bbox_inches='tight')
    print("剛体振り子の図を保存しました: fig8_rigid_pendulum.png")
    plt.close()

# ============================================
# 問題3-4: 転がる物体
# ============================================

def plot_rolling_objects():
    """転がる物体の図を作成"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # 坂
    x_slope = np.linspace(0, 3, 100)
    alpha = np.pi / 6
    y_slope = -np.tan(alpha) * x_slope
    
    for i, ax in enumerate(axes):
        ax.plot(x_slope, y_slope, 'k-', linewidth=2, label='坂')
        
        # 物体
        x_obj = 1.5
        y_obj = -np.tan(alpha) * x_obj
        circle = Circle((x_obj, y_obj), 0.3, color='blue', alpha=0.7)
        ax.add_patch(circle)
        
        # 回転の矢印
        arrow = mpatches.FancyArrowPatch((x_obj-0.2, y_obj), (x_obj+0.2, y_obj),
                                          arrowstyle='->', mutation_scale=20, 
                                          color='red', linewidth=2)
        ax.add_patch(arrow)
        
        labels = ['A: 球殻', 'B: 円盤6枚', 'C: 円筒']
        ax.set_title(labels[i], fontsize=12, fontweight='bold')
        ax.set_xlim(-0.5, 3.5)
        ax.set_ylim(-2, 0.5)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        if i == 0:
            safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
            safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('fig9_rolling_objects.png', dpi=300, bbox_inches='tight')
    print("転がる物体の図を保存しました: fig9_rolling_objects.png")
    plt.close()

# ============================================
# 問題4-2: 対称コマ
# ============================================

def plot_symmetric_top():
    """対称コマの図を作成"""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # 原点
    ax.plot([0], [0], [0], 'ko', markersize=10, label='固定点')
    
    # コマの軸
    l = 1.0
    theta = np.pi / 6
    phi = np.pi / 4
    
    # 重心の位置
    x_cm = l * np.sin(theta) * np.cos(phi)
    y_cm = l * np.sin(theta) * np.sin(phi)
    z_cm = -l * np.cos(theta)
    
    ax.plot([0, x_cm], [0, y_cm], [0, z_cm], 'b-', linewidth=3, label='コマの軸')
    ax.plot([x_cm], [y_cm], [z_cm], 'ro', markersize=12, label='重心')
    
    # 重力
    ax.quiver(x_cm, y_cm, z_cm, 0, 0, -0.3, color='green', arrow_length_ratio=0.3, linewidth=2)
    
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    safe_set_label(ax.set_zlabel, '$z$', fontsize=12)
    ax.set_title('対称コマ', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig10_symmetric_top.png', dpi=300, bbox_inches='tight')
    print("対称コマの図を保存しました: fig10_symmetric_top.png")
    plt.close()

# ============================================
# 問題4-3: マイケルソン・モーレー実験
# ============================================

def plot_michelson_morley():
    """マイケルソン・モーレー実験の図を作成（改善版）"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 光源（より大きく、目立つように）
    ax.plot(-1.5, 0, 'yo', markersize=20, label='光源', zorder=5)
    ax.text(-1.5, 0.3, '光源', fontsize=14, ha='center', fontweight='bold', color='orange')
    
    # 半透明ミラー M（より大きく、正方形を明確に）
    square = mpatches.Rectangle((-0.15, -0.15), 0.3, 0.3, 
                                facecolor='gray', edgecolor='black', linewidth=2, zorder=4)
    ax.add_patch(square)
    ax.text(0, 0.4, 'M（半透明ミラー）', fontsize=12, ha='center', fontweight='bold')
    
    # ミラー M1（より大きく、反射面を示す）
    ax.plot(2.5, 0, 'ks', markersize=18, label='M1', zorder=4)
    # 反射面を示す線
    ax.plot([2.3, 2.7], [0.2, -0.2], 'k-', linewidth=3, alpha=0.7)
    ax.text(2.5, 0.4, 'M1', fontsize=14, ha='center', fontweight='bold')
    # 距離の表示
    ax.plot([0, 2.5], [0, 0], 'k--', linewidth=1, alpha=0.3, dashes=(5, 5))
    ax.annotate('', xy=(2.5, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5, alpha=0.5))
    ax.text(1.25, 0.25, '$l_1$', fontsize=14, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # ミラー M2（より大きく、反射面を示す）
    ax.plot(0, -2.5, 'ks', markersize=18, label='M2', zorder=4)
    # 反射面を示す線
    ax.plot([-0.2, 0.2], [-2.3, -2.7], 'k-', linewidth=3, alpha=0.7)
    ax.text(0.4, -2.5, 'M2', fontsize=14, ha='left', fontweight='bold')
    # 距離の表示
    ax.plot([0, 0], [0, -2.5], 'k--', linewidth=1, alpha=0.3, dashes=(5, 5))
    ax.annotate('', xy=(0, -2.5), xytext=(0, 0),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5, alpha=0.5))
    ax.text(0.3, -1.25, '$l_2$', fontsize=14, ha='left', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # 干渉計（より大きく、目立つように）
    ax.plot(0, 1.2, 'ro', markersize=18, label='干渉計', zorder=5)
    ax.text(0, 1.5, '干渉計', fontsize=14, ha='center', fontweight='bold', color='red')
    
    # 光路1: 光源→M→M1→M→干渉計（より太く、矢印を追加）
    path1_x = [-1.5, 0, 2.5, 0, 0]
    path1_y = [0, 0, 0, 0, 1.2]
    ax.plot(path1_x, path1_y, 'b-', linewidth=3, alpha=0.8, label='光路1', zorder=2)
    # 矢印を追加
    for i in range(len(path1_x)-1):
        dx = path1_x[i+1] - path1_x[i]
        dy = path1_y[i+1] - path1_y[i]
        if abs(dx) > 0.1 or abs(dy) > 0.1:
            ax.annotate('', xy=(path1_x[i+1], path1_y[i+1]), 
                       xytext=(path1_x[i], path1_y[i]),
                       arrowprops=dict(arrowstyle='->', color='blue', lw=2, alpha=0.7))
    
    # 光路2: 光源→M→M2→M→干渉計（より太く、矢印を追加）
    path2_x = [-1.5, 0, 0, 0, 0]
    path2_y = [0, 0, -2.5, 0, 1.2]
    ax.plot(path2_x, path2_y, 'r-', linewidth=3, alpha=0.8, label='光路2', zorder=2)
    # 矢印を追加
    for i in range(len(path2_x)-1):
        dx = path2_x[i+1] - path2_x[i]
        dy = path2_y[i+1] - path2_y[i]
        if abs(dx) > 0.1 or abs(dy) > 0.1:
            ax.annotate('', xy=(path2_x[i+1], path2_y[i+1]), 
                       xytext=(path2_x[i], path2_y[i]),
                       arrowprops=dict(arrowstyle='->', color='red', lw=2, alpha=0.7))
    
    # 装置の運動方向を示す矢印
    ax.arrow(-1.2, -3, 0.8, 0, head_width=0.15, head_length=0.2, 
             fc='green', ec='green', linewidth=3, zorder=6)
    ax.text(-0.5, -3.3, r'装置の運動方向（速度$v$）', fontsize=12, ha='center', 
            color='green', fontweight='bold')
    
    ax.set_xlim(-2, 3)
    ax.set_ylim(-3.5, 2)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, '$x$', fontsize=14)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=14)
    ax.set_title('マイケルソン・モーレー実験装置', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='upper left', fontsize=12, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig('fig11_michelson_morley.png', dpi=300, bbox_inches='tight')
    print("マイケルソン・モーレー実験の図を保存しました: fig11_michelson_morley.png")
    plt.close()

# ============================================
# 問題5-2: 双子のパラドックス
# ============================================

def plot_twin_paradox():
    """双子のパラドックスの時空図を作成"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # パラメータ
    c = 1.0
    v = 0.6 * c
    beta = v / c
    gamma = 1.0 / np.sqrt(1 - beta**2)
    
    # 地点Pの位置
    x_P = 1.0
    t_P = x_P / v
    
    # 宇宙船の軌跡
    # 出発から地点Pまで
    t1 = np.linspace(0, t_P, 100)
    x1 = v * t1
    ax.plot(c*t1, x1, 'b-', linewidth=2, label='宇宙船の軌跡（往路）')
    
    # 地点Pから原点への帰還
    t2 = np.linspace(t_P, 2*t_P, 100)
    x2 = x_P - v * (t2 - t_P)
    ax.plot(c*t2, x2, 'b-', linewidth=2, label='宇宙船の軌跡（復路）')
    
    # 地点P
    ax.plot(c*t_P, x_P, 'ro', markersize=10, label='地点P')
    
    # 地球の軌跡（原点に静止）
    ax.axvline(x=0, color='k', linestyle='--', linewidth=1, alpha=0.5, label='地球（原点）')
    
    # 光の世界線
    ct = np.linspace(0, 2*t_P, 100)
    ax.plot(ct, ct, 'r--', linewidth=1, alpha=0.5, label='光の世界線')
    ax.plot(ct, -ct, 'r--', linewidth=1, alpha=0.5)
    
    safe_set_label(ax.set_xlabel, '$ct$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$x$', fontsize=12)
    ax.set_title('双子のパラドックスの時空図', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig('fig12_twin_paradox.png', dpi=300, bbox_inches='tight')
    print("双子のパラドックスの時空図を保存しました: fig12_twin_paradox.png")
    plt.close()

# ============================================
# 問題6-1: 横ドップラー効果
# ============================================

def plot_transverse_doppler():
    """横ドップラー効果の図を作成"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 観測者（原点）
    ax.plot(0, 0, 'ko', markersize=15, label='観測者')
    
    # 光源の軌跡
    y0 = 2.0
    x = np.linspace(-3, 3, 100)
    y = np.ones_like(x) * y0
    ax.plot(x, y, 'b--', linewidth=1, alpha=0.5, label='光源の軌跡')
    
    # 光源の位置
    x_source = 1.0
    ax.plot(x_source, y0, 'ro', markersize=12, label='光源')
    
    # 速度ベクトル
    ax.arrow(x_source, y0, 0.5, 0, head_width=0.2, head_length=0.1, 
             fc='red', ec='red', linewidth=2)
    ax.text(x_source + 0.7, y0 + 0.2, '$V$', fontsize=12, color='red')
    
    # 光の経路
    ax.plot([x_source, 0], [y0, 0], 'r-', linewidth=2, alpha=0.7, label='光の経路')
    
    # 角度
    angle = np.arctan2(y0, x_source)
    arc = mpatches.Arc((0, 0), 0.5, 0.5, angle=0, theta1=0, 
                       theta2=np.degrees(angle), color='green', linewidth=1.5)
    ax.add_patch(arc)
    ax.text(0.3, 0.3, r'$\theta$', fontsize=12, color='green')
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    ax.set_title('横ドップラー効果', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig13_transverse_doppler.png', dpi=300, bbox_inches='tight')
    print("横ドップラー効果の図を保存しました: fig13_transverse_doppler.png")
    plt.close()

# ============================================
# メイン実行
# ============================================

def plot_proper_time():
    """固有時の説明図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # 左図: 時空図での固有時
    t = np.linspace(0, 2, 100)
    x1 = 0.3 * t  # 静止している時計
    x2 = 0.7 * t  # 運動している時計（速度0.7c）
    
    # 静止時計の世界線
    ax1.plot(x1, t, 'b-', linewidth=2, label='静止時計の世界線')
    ax1.plot([0, 0.6], [0, 2], 'b--', alpha=0.3)
    
    # 運動時計の世界線
    ax1.plot(x2, t, 'r-', linewidth=2, label='運動時計の世界線（v=0.7c）')
    ax1.plot([0, 1.4], [0, 2], 'r--', alpha=0.3)
    
    # 固有時の説明
    ax1.annotate('固有時 = 座標時', xy=(0.3, 1), xytext=(0.5, 1.5),
                arrowprops=dict(arrowstyle='->', color='blue'),
                fontsize=12, color='blue')
    ax1.annotate('固有時 < 座標時', xy=(0.7, 1), xytext=(1.0, 1.5),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=12, color='red')
    
    safe_set_label(ax1.set_xlabel, '位置 x (光年)', fontsize=14)
    safe_set_label(ax1.set_ylabel, '時間 ct (年)', fontsize=14)
    ax1.set_title('固有時と時空図', fontsize=16, fontweight='bold')
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    
    # 右図: 時間の遅れのグラフ
    beta = np.linspace(0, 0.99, 100)
    gamma = 1 / np.sqrt(1 - beta**2)
    time_dilation = gamma
    
    ax2.plot(beta, time_dilation, 'g-', linewidth=2, label='γ = 1/√(1-β²)')
    ax2.axhline(y=1, color='k', linestyle='--', alpha=0.5, label='γ = 1（古典論）')
    ax2.axvline(x=0.9, color='r', linestyle='--', alpha=0.5)
    ax2.axvline(x=0.99, color='r', linestyle='--', alpha=0.5)
    
    ax2.annotate('v = 0.9c\nγ ≈ 2.3', xy=(0.9, 2.3), xytext=(0.7, 4),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=12, color='red')
    ax2.annotate('v = 0.99c\nγ ≈ 7.1', xy=(0.99, 7.1), xytext=(0.8, 9),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=12, color='red')
    
    safe_set_label(ax2.set_xlabel, 'β = v/c', fontsize=14)
    safe_set_label(ax2.set_ylabel, 'ローレンツ因子 γ', fontsize=14)
    ax2.set_title('時間の遅れ（ローレンツ因子）', fontsize=16, fontweight='bold')
    ax2.legend(fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 10)
    
    plt.tight_layout()
    plt.savefig('fig14_proper_time.png', dpi=150, bbox_inches='tight')
    print("固有時の図を保存しました: fig14_proper_time.png")
    plt.close()

# ============================================
# 問題7-1: パイ中間子の崩壊
# ============================================

def plot_pion_decay():
    """パイ中間子の崩壊過程の図を作成"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # パイ中間子（静止）
    ax.plot(0, 0, 'ko', markersize=20, label='パイ中間子（静止）')
    ax.text(0, 0.3, r'$m_1$', fontsize=16, ha='center', fontweight='bold')
    ax.text(0, -0.3, r'$\pi^+$', fontsize=14, ha='center', color='black')
    
    # 崩壊の矢印
    ax.arrow(0, -0.5, 0, -0.3, head_width=0.15, head_length=0.1, 
             fc='red', ec='red', linewidth=3)
    ax.text(0.3, -0.7, '崩壊', fontsize=14, color='red', fontweight='bold')
    
    # ミュー粒子（左側）
    ax.plot(-1.5, -1.5, 'bo', markersize=18, label='ミュー粒子')
    ax.text(-1.5, -1.2, r'$m_2$', fontsize=14, ha='center', color='blue', fontweight='bold')
    ax.text(-1.5, -1.8, r'$\mu^+$', fontsize=12, ha='center', color='blue')
    
    # 運動量ベクトル（ミュー粒子）
    ax.arrow(-1.5, -1.5, -0.8, 0, head_width=0.15, head_length=0.15, 
             fc='blue', ec='blue', linewidth=2.5)
    ax.text(-2.5, -1.3, r'$\vec{p}_2$', fontsize=14, color='blue', fontweight='bold')
    
    # ニュートリノ（右側）
    ax.plot(1.5, -1.5, 'go', markersize=18, label='ニュートリノ')
    ax.text(1.5, -1.2, r'$m_3 = 0$', fontsize=14, ha='center', color='green', fontweight='bold')
    ax.text(1.5, -1.8, r'$\nu_\mu$', fontsize=12, ha='center', color='green')
    
    # 運動量ベクトル（ニュートリノ）
    ax.arrow(1.5, -1.5, 0.8, 0, head_width=0.15, head_length=0.15, 
             fc='green', ec='green', linewidth=2.5)
    ax.text(2.5, -1.3, r'$\vec{p}_3$', fontsize=14, color='green', fontweight='bold')
    
    # 崩壊前後の接続線
    ax.plot([0, -1.5], [0, -1.5], 'k--', linewidth=1, alpha=0.3)
    ax.plot([0, 1.5], [0, -1.5], 'k--', linewidth=1, alpha=0.3)
    
    # 4元運動量の表示
    ax.text(-2.2, 0.5, r'崩壊前: $p_1^\mu = (m_1c, \mathbf{0})$', 
            fontsize=12, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    ax.text(-2.2, -2.5, r'崩壊後: $\vec{p}_2 + \vec{p}_3 = \mathbf{0}$', 
            fontsize=12, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2.5, 1)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, '$x$', fontsize=14)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=14)
    ax.set_title('パイ中間子の崩壊過程', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('fig15_pion_decay.png', dpi=300, bbox_inches='tight')
    print("パイ中間子の崩壊の図を保存しました: fig15_pion_decay.png")
    plt.close()

# ============================================
# 問題8-1: 電磁場の相対論的統一
# ============================================

def plot_em_field_unification():
    """電磁場の相対論的統一の図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # 左図: 古典的な見方
    ax1.text(0.5, 0.9, '古典的な見方', fontsize=16, ha='center', fontweight='bold', 
             transform=ax1.transAxes)
    
    # 電場
    ax1.text(0.2, 0.7, r'$\vec{E}$', fontsize=20, ha='center', color='red', fontweight='bold',
             transform=ax1.transAxes)
    ax1.arrow(0.2, 0.6, 0, -0.15, head_width=0.03, head_length=0.05, 
             fc='red', ec='red', linewidth=3, transform=ax1.transAxes)
    ax1.text(0.2, 0.4, r'$\phi$', fontsize=16, ha='center', color='red',
             transform=ax1.transAxes)
    
    # 矢印
    ax1.arrow(0.2, 0.35, 0, -0.1, head_width=0.02, head_length=0.03, 
             fc='black', ec='black', linewidth=1, transform=ax1.transAxes)
    
    # 磁場
    ax1.text(0.8, 0.7, r'$\vec{B}$', fontsize=20, ha='center', color='blue', fontweight='bold',
             transform=ax1.transAxes)
    circle = mpatches.Circle((0.8, 0.55), 0.08, fill=False, linewidth=3, color='blue',
                            transform=ax1.transAxes)
    ax1.add_patch(circle)
    ax1.text(0.8, 0.4, r'$\vec{A}$', fontsize=16, ha='center', color='blue',
             transform=ax1.transAxes)
    
    # 右図: 相対論的な見方
    ax2.text(0.5, 0.9, '相対論的な見方', fontsize=16, ha='center', fontweight='bold',
             transform=ax2.transAxes)
    
    # 4元ベクトルポテンシャル
    ax2.text(0.5, 0.7, r'$A^\mu = (\phi/c, \vec{A})$', fontsize=18, ha='center', 
             color='purple', fontweight='bold', transform=ax2.transAxes,
             bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))
    
    # 矢印
    ax2.arrow(0.5, 0.6, 0, -0.1, head_width=0.05, head_length=0.05, 
             fc='black', ec='black', linewidth=2, transform=ax2.transAxes)
    
    # 電磁場テンソル
    ax2.text(0.5, 0.45, r'$F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$', 
             fontsize=16, ha='center', color='darkgreen', fontweight='bold',
             transform=ax2.transAxes,
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    # 矢印
    ax2.arrow(0.5, 0.35, 0, -0.1, head_width=0.05, head_length=0.05, 
             fc='black', ec='black', linewidth=2, transform=ax2.transAxes)
    
    # 統合された電場と磁場
    ax2.text(0.3, 0.2, r'$\vec{E}$', fontsize=18, ha='center', color='red', fontweight='bold',
             transform=ax2.transAxes)
    ax2.text(0.7, 0.2, r'$\vec{B}$', fontsize=18, ha='center', color='blue', fontweight='bold',
             transform=ax2.transAxes)
    ax2.text(0.5, 0.1, '統合される', fontsize=14, ha='center', color='darkgreen',
             transform=ax2.transAxes)
    
    ax1.axis('off')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig('fig16_em_field_unification.png', dpi=300, bbox_inches='tight')
    print("電磁場の相対論的統一の図を保存しました: fig16_em_field_unification.png")
    plt.close()

# ============================================
# 問題8-2: 電磁場中の粒子の運動
# ============================================

def plot_charged_particle_in_em_field():
    """電磁場中の粒子の運動の図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # 左図: 電場中の粒子
    # 電場のベクトル場
    x = np.linspace(-2, 2, 10)
    y = np.linspace(-2, 2, 10)
    X, Y = np.meshgrid(x, y)
    
    # 一様電場（下向き）
    Ex = np.zeros_like(X)
    Ey = -np.ones_like(Y) * 0.5
    
    ax1.quiver(X, Y, Ex, Ey, scale=3, color='red', alpha=0.6, width=0.005)
    ax1.text(0, 1.8, r'$\vec{E}$ (一様電場)', fontsize=14, ha='center', color='red', fontweight='bold')
    
    # 荷電粒子
    ax1.plot(0, 0, 'bo', markersize=15, label='荷電粒子 $q > 0$')
    ax1.text(0.3, 0.2, r'$q$', fontsize=14, color='blue', fontweight='bold')
    
    # 力のベクトル
    ax1.arrow(0, 0, 0, -0.8, head_width=0.15, head_length=0.15, 
             fc='green', ec='green', linewidth=3)
    ax1.text(0.3, -0.5, r'$q\vec{E}$', fontsize=14, color='green', fontweight='bold')
    
    # 速度ベクトル（初期速度）
    ax1.arrow(0, 0, 0.6, 0.3, head_width=0.1, head_length=0.1, 
             fc='blue', ec='blue', linewidth=2, linestyle='--', alpha=0.7)
    ax1.text(0.7, 0.4, r'$\vec{v}$', fontsize=14, color='blue')
    
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-2.5, 2.5)
    ax1.set_aspect('equal')
    safe_set_label(ax1.set_xlabel, '$x$', fontsize=14)
    safe_set_label(ax1.set_ylabel, '$y$', fontsize=14)
    ax1.set_title('電場中の荷電粒子', fontsize=16, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right')
    
    # 右図: 磁場中の粒子
    # 磁場のベクトル場（一様磁場、画面に垂直）
    ax2.text(0, 1.8, r'$\vec{B}$ (一様磁場、画面に垂直)', fontsize=14, ha='center', 
             color='blue', fontweight='bold')
    
    # 磁場の方向を示す円
    circle = Circle((0, 0), 1.5, fill=False, linewidth=3, color='blue', linestyle='--', alpha=0.5)
    ax2.add_patch(circle)
    ax2.text(0, 0, r'$\otimes$', fontsize=30, ha='center', va='center', color='blue')
    ax2.text(0, -0.3, r'$\vec{B}$', fontsize=16, ha='center', color='blue', fontweight='bold')
    
    # 荷電粒子
    ax2.plot(1.5, 0, 'ro', markersize=15, label='荷電粒子 $q > 0$')
    ax2.text(1.8, 0.3, r'$q$', fontsize=14, color='red', fontweight='bold')
    
    # 速度ベクトル
    ax2.arrow(1.5, 0, 0, 0.8, head_width=0.15, head_length=0.15, 
             fc='red', ec='red', linewidth=2.5)
    ax2.text(1.8, 0.5, r'$\vec{v}$', fontsize=14, color='red', fontweight='bold')
    
    # ローレンツ力のベクトル
    ax2.arrow(1.5, 0, -0.8, 0, head_width=0.15, head_length=0.15, 
             fc='green', ec='green', linewidth=3)
    ax2.text(0.5, 0.3, r'$q\vec{v} \times \vec{B}$', fontsize=14, color='green', fontweight='bold')
    
    # 軌道（円運動）
    theta = np.linspace(0, 2*np.pi, 100)
    r = 1.5
    x_orbit = r * np.cos(theta)
    y_orbit = r * np.sin(theta)
    ax2.plot(x_orbit, y_orbit, 'g--', linewidth=2, alpha=0.5, label='軌道（円運動）')
    
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-2.5, 2.5)
    ax2.set_aspect('equal')
    safe_set_label(ax2.set_xlabel, '$x$', fontsize=14)
    safe_set_label(ax2.set_ylabel, '$y$', fontsize=14)
    ax2.set_title('磁場中の荷電粒子', fontsize=16, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('fig17_charged_particle_em.png', dpi=300, bbox_inches='tight')
    print("電磁場中の粒子の運動の図を保存しました: fig17_charged_particle_em.png")
    plt.close()

# ============================================
# 問題8-1: ローレンツ変換による電場・磁場の変換
# ============================================

def plot_em_field_transformation():
    """ローレンツ変換による電場・磁場の変換の図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # 左図: O系（静止系）
    ax1.text(0.5, 0.95, 'O系（静止系）', fontsize=16, ha='center', fontweight='bold',
             transform=ax1.transAxes)
    
    # 電場
    ax1.arrow(0.3, 0.7, 0, -0.3, head_width=0.05, head_length=0.08, 
             fc='red', ec='red', linewidth=3, transform=ax1.transAxes)
    ax1.text(0.3, 0.75, r'$\vec{E}$', fontsize=18, ha='center', color='red', fontweight='bold',
             transform=ax1.transAxes)
    
    # 磁場
    circle = Circle((0.7, 0.55), 0.1, fill=False, linewidth=3, color='blue',
                   transform=ax1.transAxes)
    ax1.add_patch(circle)
    ax1.text(0.7, 0.55, r'$\otimes$', fontsize=20, ha='center', va='center', color='blue',
             transform=ax1.transAxes)
    ax1.text(0.7, 0.35, r'$\vec{B}$', fontsize=18, ha='center', color='blue', fontweight='bold',
             transform=ax1.transAxes)
    
    # 右図: O'系（運動系、速度vでx方向に運動）
    ax2.text(0.5, 0.95, r"O'系（運動系、速度$v$で$x$方向に運動）", fontsize=16, ha='center', 
             fontweight='bold', transform=ax2.transAxes)
    
    # 速度ベクトル
    ax2.arrow(0.5, 0.85, 0.2, 0, head_width=0.03, head_length=0.05, 
             fc='black', ec='black', linewidth=2, transform=ax2.transAxes)
    ax2.text(0.7, 0.88, r'$\vec{v}$', fontsize=14, ha='left', color='black', fontweight='bold',
             transform=ax2.transAxes)
    
    # 変換後の電場（平行成分は不変、垂直成分は変化）
    ax2.arrow(0.3, 0.7, 0, -0.3, head_width=0.05, head_length=0.08, 
             fc='red', ec='red', linewidth=3, transform=ax2.transAxes)
    ax2.text(0.3, 0.75, r"$E'_x = E_x$", fontsize=14, ha='center', color='red', fontweight='bold',
             transform=ax2.transAxes)
    ax2.text(0.3, 0.25, r"（平行成分は不変）", fontsize=12, ha='center', color='red',
             transform=ax2.transAxes)
    
    # 変換後の磁場（平行成分は不変、垂直成分は変化）
    circle2 = Circle((0.7, 0.55), 0.1, fill=False, linewidth=3, color='blue',
                    transform=ax2.transAxes)
    ax2.add_patch(circle2)
    ax2.text(0.7, 0.55, r'$\otimes$', fontsize=20, ha='center', va='center', color='blue',
             transform=ax2.transAxes)
    ax2.text(0.7, 0.35, r"$B'_x = B_x$", fontsize=14, ha='center', color='blue', fontweight='bold',
             transform=ax2.transAxes)
    ax2.text(0.7, 0.25, r"（平行成分は不変）", fontsize=12, ha='center', color='blue',
             transform=ax2.transAxes)
    
    # 変換式の表示
    ax2.text(0.5, 0.1, r"$E'_y = \gamma(E_y - vB_z)$, $E'_z = \gamma(E_z + vB_y)$", 
             fontsize=12, ha='center', color='darkgreen', transform=ax2.transAxes,
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax2.text(0.5, 0.05, r"$B'_y = \gamma(B_y + vE_z/c^2)$, $B'_z = \gamma(B_z - vE_y/c^2)$", 
             fontsize=12, ha='center', color='darkgreen', transform=ax2.transAxes,
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    ax1.axis('off')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig('fig18_em_field_transformation.png', dpi=300, bbox_inches='tight')
    print("ローレンツ変換による電場・磁場の変換の図を保存しました: fig18_em_field_transformation.png")
    plt.close()

# ============================================
# 2023年度過去問: 問題1 剛体振り子（正方形板）
# ============================================

def plot_2023_rigid_pendulum():
    """2023年度問題1: 剛体振り子（正方形板）の図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 剛体振り子の全体像
    # パラメータ
    l = 1.0
    theta = np.pi / 6  # 30度
    a = 0.3  # 正方形板の一辺の長さ
    
    # 回転軸（原点）
    ax1.plot(0, 0, 'ko', markersize=10, label='回転軸 O')
    
    # 重心の位置
    x_cm = l * np.sin(theta)
    z_cm = l * np.cos(theta)
    ax1.plot(x_cm, z_cm, 'ro', markersize=8, label='重心')
    
    # 棒（回転軸から重心まで）
    ax1.plot([0, x_cm], [0, z_cm], 'k-', linewidth=2, label='棒')
    
    # 正方形板（ケースA: 板面が回転軸に垂直）
    # 板の中心が重心にあり、板面がxy平面に平行
    square_size = a / 2
    square_x = [x_cm - square_size, x_cm + square_size, x_cm + square_size, x_cm - square_size, x_cm - square_size]
    square_z = [z_cm - square_size, z_cm - square_size, z_cm + square_size, z_cm + square_size, z_cm - square_size]
    ax1.plot(square_x, square_z, 'b-', linewidth=2, alpha=0.5, label='正方形板（ケースA）')
    
    # 角度の表示
    angle_arc = np.linspace(0, theta, 50)
    arc_radius = 0.3
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
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper right')
    ax1.set_title('剛体振り子の設定（ケースA）', fontsize=14, fontweight='bold')
    
    # 右図: 正方形板の主慣性モーメントの説明
    # 板の中心を原点とする座標系
    square_half = a / 2
    square_coords = np.array([
        [-square_half, -square_half],
        [square_half, -square_half],
        [square_half, square_half],
        [-square_half, square_half],
        [-square_half, -square_half]
    ])
    
    ax2.plot(square_coords[:, 0], square_coords[:, 1], 'b-', linewidth=2, label='正方形板')
    ax2.plot(0, 0, 'ro', markersize=8, label='重心')
    
    # 主軸の表示
    ax2.arrow(-square_half*1.2, 0, square_half*2.4, 0, head_width=0.05, head_length=0.05, fc='r', ec='r', linewidth=1.5)
    ax2.arrow(0, -square_half*1.2, 0, square_half*2.4, head_width=0.05, head_length=0.05, fc='r', ec='r', linewidth=1.5)
    ax2.text(square_half*1.3, 0.1, r'$x$', fontsize=12, color='r')
    ax2.text(0.1, square_half*1.3, r'$y$', fontsize=12, color='r')
    ax2.text(0.1, -0.1, r'$z$', fontsize=12, color='g')
    
    # z軸（板面に垂直）
    ax2.plot([0, 0], [0, 0], 'go', markersize=10)
    ax2.text(0.15, 0.15, r'$z$軸（板面に垂直）', fontsize=10, color='g')
    
    ax2.set_xlim(-square_half*1.5, square_half*1.5)
    ax2.set_ylim(-square_half*1.5, square_half*1.5)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    ax2.set_title('正方形板の主慣性モーメント', fontsize=14, fontweight='bold')
    safe_set_label(ax2.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax2.set_ylabel, '$y$', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('fig19_2023_rigid_pendulum.png', dpi=300, bbox_inches='tight')
    print("2023年度問題1: 剛体振り子の図を保存しました: fig19_2023_rigid_pendulum.png")
    plt.close()

# ============================================
# 2023年度過去問: 問題2 双子のパラドックス（詳細版）
# ============================================

def plot_2023_twin_paradox_detailed():
    """2023年度問題2: 双子のパラドックスの詳細な時空図を作成"""
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
    # 往路（出発から地点Pまで）
    t1 = np.linspace(0, t_P, 100)
    x1 = v * t1
    ax.plot(c*t1, x1, 'b-', linewidth=3, label='宇宙船の軌跡（往路）')
    
    # 復路（地点Pから原点への帰還）
    t2 = np.linspace(t_P, 2*t_P, 100)
    x2 = x_P - v * (t2 - t_P)
    ax.plot(c*t2, x2, 'b-', linewidth=3, label='宇宙船の軌跡（復路）')
    
    # 地点P
    ax.plot(c*t_P, x_P, 'ro', markersize=12, label='地点P', zorder=5)
    
    # 地球の軌跡（原点に静止）
    ax.axvline(x=0, color='k', linestyle='--', linewidth=2, alpha=0.7, label='地球（原点）')
    
    # 光の世界線
    ct = np.linspace(0, 2*t_P, 100)
    ax.plot(ct, ct, 'r--', linewidth=1, alpha=0.3, label='光の世界線')
    ax.plot(ct, -ct, 'r--', linewidth=1, alpha=0.3)
    
    # 同時線の描画
    # 往路の同時線（S'系）: 地点Pを通る、傾きbetaの直線
    # ct = ct_P + beta * (x - x_P)
    x_simultaneous = np.linspace(-0.5, 1.5, 100)
    ct_simultaneous_forward = c*t_P + beta * (x_simultaneous - x_P)
    ax.plot(ct_simultaneous_forward, x_simultaneous, 'g--', linewidth=2, alpha=0.7, label='往路の同時線（S\'系）')
    
    # 復路の同時線（S''系）: 地点Pを通る、傾き-betaの直線
    # ct = ct_P - beta * (x - x_P)
    ct_simultaneous_backward = c*t_P - beta * (x_simultaneous - x_P)
    ax.plot(ct_simultaneous_backward, x_simultaneous, 'm--', linewidth=2, alpha=0.7, label='復路の同時線（S\'\'系）')
    
    # 時刻のマーカー
    # t1, t2, t3の位置を表示
    t1_marker = c*t_P
    t3_marker = gamma * c*t_P / gamma  # 簡略化
    # 実際には、t3は往路の同時線と地球の軌跡の交点
    t3_actual = gamma * (c*t_P / gamma + beta * 0)  # S'系から見たS系の原点の時刻
    
    # より正確に計算
    # 往路の同時線: ct = ct_P + beta * x
    # 地球の軌跡: x = 0
    # 交点: ct = ct_P
    # しかし、これはS'系での同時線なので、S系での時刻は異なる
    # 実際には、S'系から見て、地点P到達時（S'系の時刻t2）に、S系の原点の時刻はt3 = gamma * t2
    # t2 = t_P / gamma より、t3 = gamma * (t_P / gamma) = t_P
    # しかし、これは同時の相対性を考慮していない
    
    # 正しくは、S'系の同時線（ct' = ct_P'）が、S系では ct = gamma(ct' + beta x')
    # 地点Pでは、S'系で x' = 0, ct' = ct_P / gamma
    # したがって、S系の原点（x' = -vt_P'）での時刻は...
    
    # 簡略化して、t1, t3の位置を表示
    ax.axhline(y=0, xmin=0, xmax=t1_marker/(2*c*t_P), color='orange', linestyle=':', linewidth=1, alpha=0.5)
    ax.text(t1_marker/2, -0.15, r'$t_1$', fontsize=12, ha='center')
    
    # 往路の同時線と地球の交点
    t3_line = c*t_P  # 往路の同時線がx=0を通る点
    ax.plot(t3_line, 0, 'go', markersize=8, zorder=5)
    ax.text(t3_line, -0.25, r'$t_3$', fontsize=12, ha='center', color='g')
    
    # 復路の同時線と地球の交点
    t1_prime_line = 2*c*t_P - t3_line  # 対称性より
    ax.plot(t1_prime_line, 0, 'mo', markersize=8, zorder=5)
    ax.text(t1_prime_line, -0.25, r"$t_1'$", fontsize=12, ha='center', color='m')
    
    safe_set_label(ax.set_xlabel, '$ct$', fontsize=14)
    safe_set_label(ax.set_ylabel, '$x$', fontsize=14)
    ax.set_title('2023年度問題2: 双子のパラドックスの詳細な時空図', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_aspect('equal')
    ax.set_xlim(-0.2, 2.2*c*t_P)
    ax.set_ylim(-0.5, 1.5)
    
    plt.tight_layout()
    plt.savefig('fig20_2023_twin_paradox_detailed.png', dpi=300, bbox_inches='tight')
    print("2023年度問題2: 双子のパラドックスの詳細な時空図を保存しました: fig20_2023_twin_paradox_detailed.png")
    plt.close()

# ============================================
# 2023年度過去問: 問題3 GZKカットオフ
# ============================================

def plot_2023_gzk_cutoff():
    """2023年度問題3: GZKカットオフの概念図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 衝突過程の概念図
    # 陽子（右から左へ）
    proton_x = np.linspace(0.3, 0.7, 50)
    proton_y = 0.5 + 0.1 * np.sin(10 * np.pi * proton_x)
    ax1.plot(proton_x, proton_y, 'b-', linewidth=3, label='陽子 P')
    ax1.arrow(0.65, 0.5, 0.05, 0, head_width=0.03, head_length=0.02, fc='b', ec='b', linewidth=2)
    ax1.text(0.5, 0.65, r'$p$', fontsize=14, color='b', ha='center')
    
    # 光子（左から右へ）
    photon_x = np.linspace(0.7, 0.3, 50)
    photon_y = 0.5 - 0.1 * np.sin(10 * np.pi * photon_x)
    ax1.plot(photon_x, photon_y, 'r--', linewidth=2, label='光子 $\gamma$')
    ax1.arrow(0.35, 0.5, -0.05, 0, head_width=0.03, head_length=0.02, fc='r', ec='r', linewidth=2)
    ax1.text(0.5, 0.35, r'$p_\gamma$', fontsize=14, color='r', ha='center')
    
    # 衝突点
    ax1.plot(0.5, 0.5, 'ko', markersize=10, zorder=5)
    ax1.text(0.5, 0.25, '衝突', fontsize=12, ha='center')
    
    # 終状態
    # 核子
    ax1.arrow(0.5, 0.5, 0.1, 0.1, head_width=0.03, head_length=0.02, fc='g', ec='g', linewidth=2)
    ax1.text(0.65, 0.65, r'$N$', fontsize=14, color='g')
    
    # 中間子
    ax1.arrow(0.5, 0.5, -0.1, 0.1, head_width=0.03, head_length=0.02, fc='orange', ec='orange', linewidth=2)
    ax1.text(0.35, 0.65, r'$\pi$', fontsize=14, color='orange')
    
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.axis('off')
    safe_set_label(ax1.set_title, '衝突過程: $P + \gamma \\to N + \pi$', fontsize=14, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=10)
    
    # 右図: エネルギー閾値の説明
    # 横軸: 陽子のエネルギー、縦軸: 過程の確率（概念図）
    E_p = np.logspace(17, 21, 100)  # 10^17 から 10^21 eV
    E_GZK = 3.1e20  # GZKカットオフエネルギー（eV）
    
    # 過程が起こる確率（概念図）
    # E_p < E_GZK では確率が低い、E_p > E_GZK では確率が高いが、実際にはエネルギーを失う
    probability = np.where(E_p < E_GZK, 0.1 * (E_p / E_GZK)**2, 0.9 * np.exp(-(E_p - E_GZK) / (0.1 * E_GZK)))
    
    ax2.semilogx(E_p, probability, 'b-', linewidth=2, label='過程の確率（概念図）')
    ax2.axvline(x=E_GZK, color='r', linestyle='--', linewidth=2, label=f'GZKカットオフ\n$E_p = {E_GZK/1e20:.1f} \\times 10^{{20}}$ eV')
    
    # 宇宙線の数（概念図）
    # GZKカットオフ以上のエネルギーでは、宇宙線の数が急激に減少
    cosmic_ray_flux = np.where(E_p < E_GZK, 1.0, np.exp(-(E_p - E_GZK) / (0.2 * E_GZK)))
    ax2_twin = ax2.twinx()
    ax2_twin.semilogx(E_p, cosmic_ray_flux, 'g--', linewidth=2, alpha=0.7, label='宇宙線の数（概念図）')
    safe_set_label(ax2_twin.set_ylabel, '相対的な宇宙線の数', fontsize=12, color='g')
    ax2_twin.tick_params(axis='y', labelcolor='g')
    
    safe_set_label(ax2.set_xlabel, '陽子のエネルギー $E_p$ (eV)', fontsize=12)
    safe_set_label(ax2.set_ylabel, '過程の確率（相対値）', fontsize=12, color='b')
    ax2.tick_params(axis='y', labelcolor='b')
    ax2.set_title('GZKカットオフの効果', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper left', fontsize=10)
    ax2_twin.legend(loc='upper right', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('fig21_2023_gzk_cutoff.png', dpi=300, bbox_inches='tight')
    print("2023年度問題3: GZKカットオフの図を保存しました: fig21_2023_gzk_cutoff.png")
    plt.close()

# ============================================
# 2024年度過去問: 問題1 剛体の運動
# ============================================

def plot_2024_rigid_body_motion():
    """2024年度問題1: 剛体の運動の図を作成"""
    fig = plt.figure(figsize=(16, 10))
    
    # グリッドレイアウト
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)
    
    # 物体A: 球殻
    ax1 = fig.add_subplot(gs[0, 0])
    circle = plt.Circle((0, 0), 1, fill=False, linewidth=3, color='b')
    ax1.add_patch(circle)
    ax1.plot([-1, 1], [0, 0], 'k-', linewidth=2)
    ax1.text(0, 0, 'R', fontsize=14, ha='center', va='center')
    ax1.text(0, -1.3, '2R', fontsize=12, ha='center')
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('A: 半径Rの球殻', fontsize=14, fontweight='bold')
    
    # 物体B: 円盤6枚
    ax2 = fig.add_subplot(gs[0, 1])
    for i in range(6):
        y_pos = -0.5 + i * 0.2
        circle = plt.Circle((0, y_pos), 0.8, fill=False, linewidth=2, color='g')
        ax2.add_patch(circle)
    ax2.plot([-0.8, 0.8], [-0.5, -0.5], 'k-', linewidth=1, alpha=0.5)
    ax2.plot([-0.8, 0.8], [0.5, 0.5], 'k-', linewidth=1, alpha=0.5)
    ax2.plot([0, 0], [-0.7, 0.7], 'r-', linewidth=3, label='車軸')
    ax2.text(1.1, 0, '2R', fontsize=12, va='center')
    ax2.text(0, -0.9, '2R', fontsize=12, ha='center')
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.2, 1.2)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('B: 円盤6枚', fontsize=14, fontweight='bold')
    ax2.legend(loc='upper right', fontsize=10)
    
    # 物体C: 円筒
    ax3 = fig.add_subplot(gs[0, 2])
    # 円筒の側面
    rectangle = plt.Rectangle((-0.8, -0.5), 1.6, 1.0, fill=False, linewidth=3, color='orange')
    ax3.add_patch(rectangle)
    # 円筒の端（円）
    circle_top = plt.Circle((0, 0.5), 0.8, fill=False, linewidth=2, color='orange', linestyle='--')
    circle_bottom = plt.Circle((0, -0.5), 0.8, fill=False, linewidth=2, color='orange', linestyle='--')
    ax3.add_patch(circle_top)
    ax3.add_patch(circle_bottom)
    ax3.text(1.1, 0, '2R', fontsize=12, va='center')
    ax3.text(0, -0.9, '2R', fontsize=12, ha='center')
    ax3.set_xlim(-1.5, 1.5)
    ax3.set_ylim(-1.2, 1.2)
    ax3.set_aspect('equal')
    ax3.axis('off')
    ax3.set_title('C: 半径R、長さ2Rの円筒', fontsize=14, fontweight='bold')
    
    # 転がり運動の図
    ax4 = fig.add_subplot(gs[1, :])
    
    # 坂の描画
    alpha = np.pi / 6  # 30度
    slope_length = 3.0
    slope_x = np.linspace(0, slope_length * np.cos(alpha), 100)
    slope_y = -slope_x * np.tan(alpha)
    ax4.plot(slope_x, slope_y, 'k-', linewidth=3, label='坂')
    
    # 転がる物体（3つの位置）
    for i, (x_pos, color, label) in enumerate([(0.5, 'b', '物体A'), (1.0, 'g', '物体B'), (1.5, 'orange', '物体C')]):
        y_pos = -x_pos * np.tan(alpha)
        circle = plt.Circle((x_pos, y_pos), 0.15, fill=True, color=color, alpha=0.7)
        ax4.add_patch(circle)
        # 回転の矢印
        angle = x_pos / 0.15  # 回転角
        arrow_x = x_pos + 0.15 * np.cos(angle)
        arrow_y = y_pos + 0.15 * np.sin(angle)
        ax4.arrow(x_pos, y_pos, 0.1 * np.cos(angle), 0.1 * np.sin(angle), 
                 head_width=0.05, head_length=0.03, fc=color, ec=color)
        ax4.text(x_pos, y_pos - 0.3, label, fontsize=10, ha='center', color=color)
    
    # 角度の表示
    arc_angle = np.linspace(0, alpha, 50)
    arc_radius = 0.3
    ax4.plot(arc_radius * np.cos(arc_angle), -arc_radius * np.sin(arc_angle), 'r--', linewidth=1)
    ax4.text(0.2, -0.1, r'$\alpha$', fontsize=14, color='r')
    
    # 座標の表示
    ax4.arrow(0, 0, 0.3, 0, head_width=0.05, head_length=0.03, fc='k', ec='k')
    ax4.text(0.35, 0.05, r'$x$', fontsize=12)
    ax4.text(0.1, 0.15, r'$\theta$', fontsize=12)
    
    ax4.set_xlim(-0.2, 3.5)
    ax4.set_ylim(-2.0, 0.5)
    ax4.set_aspect('equal')
    safe_set_label(ax4.set_xlabel, '距離', fontsize=12)
    safe_set_label(ax4.set_ylabel, '高さ', fontsize=12)
    ax4.set_title('転がり運動の様子', fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    ax4.legend(loc='upper right', fontsize=10)
    
    plt.suptitle('2024年度問題1: 剛体の運動', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('fig22_2024_rigid_body_motion.png', dpi=300, bbox_inches='tight')
    print("2024年度問題1: 剛体の運動の図を保存しました: fig22_2024_rigid_body_motion.png")
    plt.close()

# ============================================
# 2025年度過去問: 問題3 粒子衝突
# ============================================

def plot_2025_particle_collision():
    """2025年度問題3: 粒子衝突の概念図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 衝突前
    # 粒子1（右から左へ）
    ax1.arrow(0.3, 0.5, 0.3, 0, head_width=0.05, head_length=0.03, fc='b', ec='b', linewidth=2)
    ax1.text(0.5, 0.65, r'粒子1 ($p_1$)', fontsize=12, color='b', ha='center')
    ax1.text(0.5, 0.55, r'質量 $m$', fontsize=10, color='b', ha='center')
    
    # 粒子2（静止）
    ax1.plot(0.7, 0.5, 'ro', markersize=12, label='粒子2（静止）')
    ax1.text(0.7, 0.35, r'質量 $m$', fontsize=10, color='r', ha='center')
    
    # x軸
    ax1.arrow(0, 0.5, 1.0, 0, head_width=0.02, head_length=0.02, fc='k', ec='k', linewidth=1)
    ax1.text(1.05, 0.48, r'$x$', fontsize=12)
    
    ax1.set_xlim(0, 1.2)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('衝突前', fontsize=14, fontweight='bold')
    
    # 右図: 衝突後
    # 粒子3（右上へ）
    ax2.arrow(0.5, 0.5, 0.2, 0.2, head_width=0.05, head_length=0.03, fc='g', ec='g', linewidth=2)
    ax2.text(0.75, 0.75, r'粒子3 ($p_3$)', fontsize=12, color='g')
    ax2.text(0.75, 0.68, r'質量 $M$', fontsize=10, color='g')
    
    # 粒子4（右下へ）
    ax2.arrow(0.5, 0.5, 0.2, -0.2, head_width=0.05, head_length=0.03, fc='orange', ec='orange', linewidth=2)
    ax2.text(0.75, 0.25, r'粒子4 ($p_4$)', fontsize=12, color='orange')
    ax2.text(0.75, 0.18, r'質量 $M$', fontsize=10, color='orange')
    
    # 衝突点
    ax2.plot(0.5, 0.5, 'ko', markersize=10, zorder=5)
    ax2.text(0.5, 0.4, '衝突点', fontsize=10, ha='center')
    
    # 座標軸
    ax2.arrow(0.5, 0.5, 0.3, 0, head_width=0.02, head_length=0.02, fc='k', ec='k', linewidth=1)
    ax2.arrow(0.5, 0.5, 0, 0.3, head_width=0.02, head_length=0.02, fc='k', ec='k', linewidth=1)
    ax2.text(0.85, 0.48, r'$x$', fontsize=12)
    ax2.text(0.52, 0.85, r'$y$', fontsize=12)
    
    ax2.set_xlim(0, 1.0)
    ax2.set_ylim(0, 1.0)
    ax2.set_aspect('equal')
    ax2.axis('off')
    safe_set_label(ax2.set_title, '衝突後（$xy$平面内）', fontsize=14, fontweight='bold')
    
    plt.suptitle('2025年度問題3: 粒子衝突', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('fig23_2025_particle_collision.png', dpi=300, bbox_inches='tight')
    print("2025年度問題3: 粒子衝突の図を保存しました: fig23_2025_particle_collision.png")
    plt.close()

# ============================================
# 新しく追加した図の生成関数
# ============================================

def plot_orthogonal_transformation():
    """直交変換の可視化図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 変換前
    v1 = np.array([2, 1])
    v2 = np.array([1, 2])
    ax1.arrow(0, 0, v1[0], v1[1], head_width=0.15, head_length=0.1, fc='blue', ec='blue', linewidth=2, label=r'$\vec{v}$')
    ax1.arrow(0, 0, v2[0], v2[1], head_width=0.15, head_length=0.1, fc='green', ec='green', linewidth=2, label=r'$\vec{u}$')
    ax1.set_xlim(-0.5, 3)
    ax1.set_ylim(-0.5, 3)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.set_title('変換前', fontsize=14, fontweight='bold')
    ax1.legend()
    
    # 右図: 変換後（90度回転）
    theta = np.pi/2
    O = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
    v1_rot = O @ v1
    v2_rot = O @ v2
    ax2.arrow(0, 0, v1_rot[0], v1_rot[1], head_width=0.15, head_length=0.1, fc='blue', ec='blue', linewidth=2, label=r"$\vec{v}'$")
    ax2.arrow(0, 0, v2_rot[0], v2_rot[1], head_width=0.15, head_length=0.1, fc='green', ec='green', linewidth=2, label=r"$\vec{u}'$")
    ax2.set_xlim(-3, 0.5)
    ax2.set_ylim(-0.5, 3)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.set_title('変換後（回転）', fontsize=14, fontweight='bold')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('fig_orthogonal_transformation.png', dpi=300, bbox_inches='tight')
    print("直交変換の可視化図を保存しました: fig_orthogonal_transformation.png")
    plt.close()

def plot_orthogonal_columns():
    """直交行列の列ベクトルが正規直交基底をなす様子"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 3つの列ベクトル（正規直交基底）
    e1 = np.array([1, 0, 0])
    e2 = np.array([0, 1, 0])
    e3 = np.array([0, 0, 1])
    
    # ベクトルを描画
    ax.quiver(0, 0, 0, e1[0], e1[1], e1[2], color='blue', arrow_length_ratio=0.2, linewidth=2, label=r'$\vec{E}_1$')
    ax.quiver(0, 0, 0, e2[0], e2[1], e2[2], color='green', arrow_length_ratio=0.2, linewidth=2, label=r'$\vec{E}_2$')
    ax.quiver(0, 0, 0, e3[0], e3[1], e3[2], color='red', arrow_length_ratio=0.2, linewidth=2, label=r'$\vec{E}_3$')
    
    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([-0.5, 1.5])
    ax.set_zlim([-0.5, 1.5])
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    safe_set_label(ax.set_zlabel, '$z$', fontsize=12)
    ax.set_title('直交行列の列ベクトル（正規直交基底）', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig_orthogonal_columns.png', dpi=300, bbox_inches='tight')
    print("直交行列の列ベクトルの図を保存しました: fig_orthogonal_columns.png")
    plt.close()

def plot_polar_coordinates():
    """極座標の説明図を作成"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # 点の位置
    r = 2.0
    phi = np.pi / 4
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    
    # 原点から点への線
    ax.plot([0, x], [0, y], 'b-', linewidth=2)
    ax.plot(x, y, 'ro', markersize=10, label=f'点 $(r, \\phi) = ({r:.1f}, {phi:.2f})$')
    
    # 角度の弧
    arc_radius = 0.5
    arc = mpatches.Arc((0, 0), arc_radius, arc_radius, angle=0, 
                       theta1=0, theta2=np.degrees(phi), 
                       color='red', linewidth=1.5)
    ax.add_patch(arc)
    ax.text(0.3, 0.15, r'$\phi$', fontsize=14, color='red')
    
    # 距離の表示
    ax.text(x/2 + 0.2, y/2, f'$r = {r:.1f}$', fontsize=12, color='blue')
    
    # 座標軸
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    
    # 変換式の表示
    ax.text(-2.5, 2.5, f'$x = r\\cos\\phi = {x:.2f}$\n$y = r\\sin\\phi = {y:.2f}$', 
            fontsize=12, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    safe_set_label(ax.set_title, '極座標 $(r, \\phi)$ と直交座標 $(x, y)$ の関係', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig_polar_coordinates.png', dpi=300, bbox_inches='tight')
    print("極座標の説明図を保存しました: fig_polar_coordinates.png")
    plt.close()

def plot_angular_momentum_conservation():
    """角運動量保存の可視化（面積速度一定）"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 軌道（楕円）
    a, b = 2.0, 1.0
    t = np.linspace(0, 2*np.pi, 100)
    x_orbit = a * np.cos(t)
    y_orbit = b * np.sin(t)
    ax.plot(x_orbit, y_orbit, 'b-', linewidth=2, label='軌道')
    
    # 原点
    ax.plot(0, 0, 'ko', markersize=8, label='原点')
    
    # 2つの時刻での位置
    t1, t2 = np.pi/6, np.pi/3
    x1, y1 = a * np.cos(t1), b * np.sin(t1)
    x2, y2 = a * np.cos(t2), b * np.sin(t2)
    
    # 位置ベクトル
    ax.plot([0, x1], [0, y1], 'g--', linewidth=1.5, alpha=0.7)
    ax.plot([0, x2], [0, y2], 'g--', linewidth=1.5, alpha=0.7)
    ax.plot(x1, y1, 'go', markersize=8)
    ax.plot(x2, y2, 'go', markersize=8)
    
    # 掃いた面積（扇形）
    theta_range = np.linspace(t1, t2, 50)
    x_sector = a * np.cos(theta_range)
    y_sector = b * np.sin(theta_range)
    ax.fill(np.concatenate([[0], x_sector, [0]]), 
            np.concatenate([[0], y_sector, [0]]), 
            color='yellow', alpha=0.3, label='掃いた面積')
    
    ax.text(0.5, 0.3, '面積速度 = 一定', fontsize=12, 
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    ax.set_title('角運動量保存（面積速度一定）', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig_angular_momentum_conservation.png', dpi=300, bbox_inches='tight')
    print("角運動量保存の図を保存しました: fig_angular_momentum_conservation.png")
    plt.close()

def plot_tensor_transformation():
    """テンソル変換の可視化"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 変換前のテンソル（2階テンソルの例）
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    U = X
    V = Y
    ax1.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=0.5, alpha=0.6)
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-2.5, 2.5)
    ax1.set_aspect('equal')
    ax1.set_title('変換前のテンソル場', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # 右図: 変換後（45度回転）
    theta = np.pi/4
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    X_rot = R[0,0]*X + R[0,1]*Y
    Y_rot = R[1,0]*X + R[1,1]*Y
    U_rot = R[0,0]*U + R[0,1]*V
    V_rot = R[1,0]*U + R[1,1]*V
    ax2.quiver(X_rot, Y_rot, U_rot, V_rot, angles='xy', scale_units='xy', scale=0.5, alpha=0.6)
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-2.5, 2.5)
    ax2.set_aspect('equal')
    ax2.set_title('変換後のテンソル場（回転）', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('fig_tensor_transformation.png', dpi=300, bbox_inches='tight')
    print("テンソル変換の図を保存しました: fig_tensor_transformation.png")
    plt.close()

def plot_cross_product():
    """外積の可視化"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 2つのベクトル
    A = np.array([2, 0, 0])
    B = np.array([0, 2, 0])
    C = np.cross(A, B)
    
    # ベクトルを描画
    ax.quiver(0, 0, 0, A[0], A[1], A[2], color='blue', arrow_length_ratio=0.2, linewidth=2, label=r'$\vec{A}$')
    ax.quiver(0, 0, 0, B[0], B[1], B[2], color='green', arrow_length_ratio=0.2, linewidth=2, label=r'$\vec{B}$')
    ax.quiver(0, 0, 0, C[0], C[1], C[2], color='red', arrow_length_ratio=0.2, linewidth=2, label=r'$\vec{A} \times \vec{B}$')
    
    ax.set_xlim([-0.5, 2.5])
    ax.set_ylim([-0.5, 2.5])
    ax.set_zlim([-0.5, 2.5])
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    safe_set_label(ax.set_zlabel, '$z$', fontsize=12)
    safe_set_label(ax.set_title, r'外積 $\vec{A} \times \vec{B}$ (右手の法則)', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig_cross_product.png', dpi=300, bbox_inches='tight')
    print("外積の図を保存しました: fig_cross_product.png")
    plt.close()

def plot_rolling_condition():
    """転がり条件の説明図"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 円形物体
    circle = Circle((2, 2), 1.0, fill=False, linewidth=3, color='blue')
    ax.add_patch(circle)
    
    # 重心
    ax.plot(2, 2, 'ro', markersize=10, label='重心')
    
    # 接触点
    ax.plot(2, 1, 'ko', markersize=8, label='接触点')
    
    # 重心の速度
    ax.arrow(2, 2, 0.5, 0, head_width=0.1, head_length=0.1, fc='green', ec='green', linewidth=2)
    ax.text(2.7, 2.2, r'$\dot{x}$', fontsize=14, color='green')
    
    # 回転による速度
    ax.arrow(2, 1, -0.5, 0, head_width=0.1, head_length=0.1, fc='blue', ec='blue', linewidth=2)
    ax.text(1.2, 1.2, r'$R\dot{\theta}$', fontsize=14, color='blue')
    
    # 地面
    ax.plot([-1, 5], [1, 1], 'k-', linewidth=3, label='地面')
    
    # 条件の説明
    ax.text(0.5, 3.5, '滑らない条件:\n接触点の速度 = 0\n$\dot{x} = R\dot{\theta}$', 
            fontsize=12, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(0, 4)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    ax.set_title('転がり条件（滑らずに転がる）', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig_rolling_condition.png', dpi=300, bbox_inches='tight')
    print("転がり条件の図を保存しました: fig_rolling_condition.png")
    plt.close()

def plot_precession_nutation():
    """歳差運動と章動の図"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 歳差運動の円（自転軸の先端の軌跡）
    phi = np.linspace(0, 2*np.pi, 100)
    r_precession = 1.0
    x_prec = r_precession * np.cos(phi)
    y_prec = r_precession * np.sin(phi)
    z_prec = np.ones_like(phi) * 2.0
    ax.plot(x_prec, y_prec, z_prec, 'b-', linewidth=2, label='歳差運動')
    
    # 章動の振動（角度θの変化）
    theta_base = np.pi/6
    theta_variation = 0.1 * np.sin(2*phi)
    theta = theta_base + theta_variation
    
    # 自転軸の軌跡（歳差運動と章動の組み合わせ）
    for i in range(0, len(phi), 10):
        x_axis = np.sin(theta[i]) * np.cos(phi[i])
        y_axis = np.sin(theta[i]) * np.sin(phi[i])
        z_axis = np.cos(theta[i])
        ax.plot([0, 2*x_axis], [0, 2*y_axis], [0, 2*z_axis], 'r--', alpha=0.3, linewidth=1)
    
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([0, 2.5])
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    safe_set_label(ax.set_zlabel, '$z$', fontsize=12)
    ax.set_title('歳差運動と章動', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig_precession_nutation.png', dpi=300, bbox_inches='tight')
    print("歳差運動と章動の図を保存しました: fig_precession_nutation.png")
    plt.close()

def plot_euler_angles():
    """オイラー角の定義図"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 固定座標系の軸
    ax.quiver(0, 0, 0, 1.5, 0, 0, color='black', arrow_length_ratio=0.15, linewidth=1.5, alpha=0.5)
    ax.quiver(0, 0, 0, 0, 1.5, 0, color='black', arrow_length_ratio=0.15, linewidth=1.5, alpha=0.5)
    ax.quiver(0, 0, 0, 0, 0, 1.5, color='black', arrow_length_ratio=0.15, linewidth=1.5, alpha=0.5)
    ax.text(1.6, 0, 0, '$x$', fontsize=12)
    ax.text(0, 1.6, 0, '$y$', fontsize=12)
    ax.text(0, 0, 1.6, '$z$', fontsize=12)
    
    # 自転軸（θの傾き）
    theta = np.pi/6
    phi = np.pi/4
    axis_x = np.sin(theta) * np.cos(phi)
    axis_y = np.sin(theta) * np.sin(phi)
    axis_z = np.cos(theta)
    
    ax.quiver(0, 0, 0, axis_x, axis_y, axis_z, color='red', arrow_length_ratio=0.2, linewidth=3, label='自転軸')
    
    # 角度の表示
    ax.text(0.3, 0.3, 0.5, r'$\theta$', fontsize=14, color='red')
    ax.text(0.5, 0.5, 0, r'$\phi$', fontsize=14, color='blue')
    
    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([-0.5, 1.5])
    ax.set_zlim([0, 1.5])
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    safe_set_label(ax.set_zlabel, '$z$', fontsize=12)
    safe_set_label(ax.set_title, 'オイラー角 $\\theta$（章動角）, $\\phi$（歳差角）, $\\psi$（自転角）', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig_euler_angles.png', dpi=300, bbox_inches='tight')
    print("オイラー角の図を保存しました: fig_euler_angles.png")
    plt.close()

def plot_length_contraction():
    """長さの収縮の説明図"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 静止系
    L0 = 2.0
    ax1.plot([0, L0], [0, 0], 'b-', linewidth=5, label=f'棒の長さ $L_0 = {L0:.1f}$ m')
    ax1.plot([0, 0], [-0.2, 0.2], 'k-', linewidth=2)
    ax1.plot([L0, L0], [-0.2, 0.2], 'k-', linewidth=2)
    ax1.set_xlim(-0.5, 2.5)
    ax1.set_ylim(-0.5, 0.5)
    ax1.set_aspect('equal')
    safe_set_label(ax1.set_title, '静止系（固有長 $L_0$）', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 右図: 運動系
    beta = 0.9
    gamma = 1/np.sqrt(1-beta**2)
    L = L0 / gamma
    ax2.plot([0, L], [0, 0], 'r-', linewidth=5, label=f'見かけの長さ $L = L_0/\\gamma = {L:.2f}$ m')
    ax2.plot([0, 0], [-0.2, 0.2], 'k-', linewidth=2)
    ax2.plot([L, L], [-0.2, 0.2], 'k-', linewidth=2)
    ax2.arrow(L+0.2, 0, 0.3, 0, head_width=0.1, head_length=0.1, fc='green', ec='green', linewidth=2)
    ax2.text(L+0.6, 0.2, f'$V = {beta:.1f}c$', fontsize=12, color='green')
    ax2.set_xlim(-0.5, 2.5)
    ax2.set_ylim(-0.5, 0.5)
    ax2.set_aspect('equal')
    safe_set_label(ax2.set_title, f'運動系（速度 $V = {beta:.1f}c$）', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('fig_length_contraction.png', dpi=300, bbox_inches='tight')
    print("長さの収縮の図を保存しました: fig_length_contraction.png")
    plt.close()

def plot_time_dilation():
    """時間の遅れの説明（光時計）"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
    
    # 左図: 静止している光時計
    L = 1.0
    ax1.plot([0, 0], [0, L], 'k-', linewidth=3, label='光時計')
    ax1.plot([-0.1, 0.1], [0, 0], 'k-', linewidth=3)
    ax1.plot([-0.1, 0.1], [L, L], 'k-', linewidth=3)
    
    # 光の経路（上下往復）
    ax1.plot([0, 0], [0, L], 'r--', linewidth=2, alpha=0.7, label='光の経路')
    ax1.plot([0, 0], [L, 0], 'r--', linewidth=2, alpha=0.7)
    ax1.text(0.2, L/2, r"$\Delta t'$", fontsize=14, color='red')
    
    ax1.set_xlim(-0.5, 0.5)
    ax1.set_ylim(-0.2, 1.2)
    ax1.set_aspect('equal')
    ax1.set_title('静止している光時計', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 右図: 運動している光時計
    beta = 0.6
    gamma = 1/np.sqrt(1-beta**2)
    v = beta
    
    ax2.plot([0, 2], [0, L], 'k-', linewidth=3, label='光時計（運動中）')
    ax2.plot([-0.1, 0.1], [0, 0], 'k-', linewidth=3)
    ax2.plot([1.9, 2.1], [L, L], 'k-', linewidth=3)
    
    # 光の経路（斜め）
    ax2.plot([0, 1], [0, L], 'r--', linewidth=2, alpha=0.7, label='光の経路')
    ax2.plot([1, 2], [L, 0], 'r--', linewidth=2, alpha=0.7)
    ax2.text(1.2, L/2, r"$\Delta t = \gamma\Delta t'$", fontsize=14, color='red')
    
    # 速度の表示
    ax2.arrow(1, 0, 0.3, 0, head_width=0.05, head_length=0.05, fc='green', ec='green', linewidth=2)
    ax2.text(1.4, -0.15, f'$V = {beta:.1f}c$', fontsize=12, color='green')
    
    ax2.set_xlim(-0.5, 2.5)
    ax2.set_ylim(-0.2, 1.2)
    ax2.set_aspect('equal')
    ax2.set_title('運動している光時計（時間の遅れ）', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('fig_time_dilation.png', dpi=300, bbox_inches='tight')
    print("時間の遅れの図を保存しました: fig_time_dilation.png")
    plt.close()

def plot_velocity_transformation():
    """速度の変換の比較（古典論 vs 相対論）"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 速度の範囲
    beta = np.linspace(0, 0.99, 100)
    V = beta  # 相対速度（光速単位）
    v = 0.5  # 元の速度（光速単位）
    
    # 古典論
    v_classical = v + V
    
    # 相対論
    v_relativistic = (v + V) / (1 + v * V)
    
    ax.plot(beta, v_classical, 'b-', linewidth=2, label='古典論 $v\' = v + V$')
    ax.plot(beta, v_relativistic, 'r-', linewidth=2, label='相対論 $v\' = \\frac{v + V}{1 + vV/c^2}$')
    ax.axhline(y=1, color='k', linestyle='--', linewidth=1, alpha=0.5, label='光速 $c$')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.5)
    safe_set_label(ax.set_xlabel, '相対速度 $\\beta = V/c$', fontsize=12)
    safe_set_label(ax.set_ylabel, '変換後の速度 $v\'/c$', fontsize=12)
    ax.set_title('速度の変換（古典論 vs 相対論）', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig_velocity_transformation.png', dpi=300, bbox_inches='tight')
    print("速度の変換の図を保存しました: fig_velocity_transformation.png")
    plt.close()

def plot_four_vector_transformation():
    """4元ベクトルの変換"""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 4元位置ベクトル（時空）
    t = np.linspace(0, 2, 50)
    x = 0.5 * t
    y = np.zeros_like(t)
    z = np.zeros_like(t)
    
    # 世界線
    ax.plot(x, y, t, 'b-', linewidth=2, label='世界線')
    
    # ローレンツ変換後の世界線
    beta = 0.6
    gamma = 1/np.sqrt(1-beta**2)
    t_prime = gamma * (t - beta * x)
    x_prime = gamma * (x - beta * t)
    y_prime = y
    ax.plot(x_prime, y_prime, t_prime, 'r--', linewidth=2, label='ローレンツ変換後')
    
    safe_set_label(ax.set_xlabel, '$x$', fontsize=12)
    safe_set_label(ax.set_ylabel, '$y$', fontsize=12)
    safe_set_label(ax.set_zlabel, '$ct$', fontsize=12)
    ax.set_title('4元ベクトルのローレンツ変換', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig_four_vector_transformation.png', dpi=300, bbox_inches='tight')
    print("4元ベクトルの変換の図を保存しました: fig_four_vector_transformation.png")
    plt.close()

# ============================================
# 2024年度過去問: 問題1 (iv) 転がり運動の順番
# ============================================

def plot_2024_rolling_order():
    """2024年度問題1(iv): 転がり運動の順番を示す図を作成"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 坂の描画
    alpha = np.pi / 6  # 30度
    slope_length = 4.0
    slope_x = np.linspace(0, slope_length * np.cos(alpha), 100)
    slope_y = -slope_x * np.tan(alpha)
    ax.plot(slope_x, slope_y, 'k-', linewidth=3, label='斜面')
    
    # 3つの物体の位置（順番を示す）
    positions = [
        (0.8, 'B', 'g', 1),  # 最も速い
        (1.5, 'A', 'b', 2),   # 中間
        (2.2, 'C', 'orange', 3)  # 最も遅い
    ]
    
    for x_pos, label, color, order in positions:
        y_pos = -x_pos * np.tan(alpha)
        # 物体の円
        circle = Circle((x_pos, y_pos), 0.15, fill=True, color=color, alpha=0.7)
        ax.add_patch(circle)
        # 順番の表示
        ax.text(x_pos, y_pos - 0.4, f'{order}. {label}', fontsize=14, ha='center', 
                color=color, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        # 回転の矢印
        angle = x_pos / 0.15
        arrow_x = x_pos + 0.12 * np.cos(angle)
        arrow_y = y_pos + 0.12 * np.sin(angle)
        ax.arrow(x_pos, y_pos, 0.08 * np.cos(angle), 0.08 * np.sin(angle), 
                head_width=0.04, head_length=0.02, fc=color, ec=color)
    
    # 角度の表示
    arc_angle = np.linspace(0, alpha, 50)
    arc_radius = 0.3
    ax.plot(arc_radius * np.cos(arc_angle), -arc_radius * np.sin(arc_angle), 'r--', linewidth=1)
    ax.text(0.2, -0.1, r'$\alpha$', fontsize=14, color='r')
    
    # 説明テキスト
    ax.text(3.5, -0.5, '転がり運動の順番:\nB → A → C', fontsize=14, 
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7),
            verticalalignment='top')
    
    ax.set_xlim(-0.2, 4.5)
    ax.set_ylim(-2.5, 0.5)
    ax.set_aspect('equal')
    safe_set_label(ax.set_xlabel, '距離 (m)', fontsize=12)
    safe_set_label(ax.set_ylabel, '高さ (m)', fontsize=12)
    ax.set_title('2024年度問題1(iv): 転がり運動の順番', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('fig24_2024_rolling_order.png', dpi=300, bbox_inches='tight')
    print("2024年度問題1(iv): 転がり運動の順番の図を保存しました: fig24_2024_rolling_order.png")
    plt.close()

# ============================================
# 2025年度過去問: 問題1 (iv) ケースAとケースB
# ============================================

# ============================================
# 2023年度過去問: 問題1 追加の図
# ============================================

def plot_2023_rigid_pendulum_potential():
    """2023年度問題1(i): 剛体振り子のポテンシャルエネルギーの図を作成"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    theta = np.linspace(-np.pi, np.pi, 1000)
    M = 1.0
    g = 9.8
    l = 1.0
    
    # 基準点をθ=π/2とする場合
    V1 = -M * g * l * np.cos(theta)
    
    # 基準点をθ=0とする場合
    V2 = M * g * l * (1 - np.cos(theta))
    
    ax.plot(theta, V1, 'b-', linewidth=2, label=r'$V = -Mg\ell\cos\theta$ (基準点: $\theta = \pi/2$)')
    ax.plot(theta, V2, 'r--', linewidth=2, label=r'$V = Mg\ell(1 - \cos\theta)$ (基準点: $\theta = 0$)')
    
    # 重要な点をマーク
    ax.plot(0, -M*g*l, 'go', markersize=10, label=r'最下点 ($\theta = 0$)')
    ax.plot(np.pi/2, 0, 'ro', markersize=10, label=r'水平位置 ($\theta = \pi/2$)')
    ax.plot(np.pi, M*g*l, 'mo', markersize=10, label=r'最上点 ($\theta = \pi$)')
    
    ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    
    safe_set_label(ax.set_xlabel, r'$\theta$ (rad)', fontsize=12)
    safe_set_label(ax.set_ylabel, r'$V(\theta)$', fontsize=12)
    ax.set_title('2023年度問題1(i): 剛体振り子のポテンシャルエネルギー', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('fig26_2023_rigid_pendulum_potential.png', dpi=300, bbox_inches='tight')
    print("2023年度問題1(i): 剛体振り子のポテンシャルエネルギーの図を保存しました: fig26_2023_rigid_pendulum_potential.png")
    plt.close()

def plot_2023_rigid_pendulum_cases():
    """2023年度問題1(iv): ケースAとケースBの剛体振り子の図を作成"""
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
    # 板の中心が重心にあり、板面がxy平面に平行（z軸に垂直）
    # 側面から見ると、板は線として見える
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
    # 側面から見ると、板は正方形として見える
    square_coords = np.array([
        [-square_size, -square_size],
        [square_size, -square_size],
        [square_size, square_size],
        [-square_size, square_size],
        [-square_size, -square_size]
    ])
    # 板を重心の位置に配置し、回転面（xz平面）に垂直に配置
    # 側面から見ると、板はy方向に伸びた線として見える
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
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    ax2.set_title('ケースB: 板の面が回転面に垂直', fontsize=14, fontweight='bold')
    ax2.text(0.5, -0.4, r'$I_B = M\left(\frac{a^2}{12} + \ell^2\right)$', 
            fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    plt.suptitle('2023年度問題1(iv): ケースAとケースBの剛体振り子', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('fig27_2023_rigid_pendulum_cases.png', dpi=300, bbox_inches='tight')
    print("2023年度問題1(iv): ケースAとケースBの図を保存しました: fig27_2023_rigid_pendulum_cases.png")
    plt.close()

def plot_2023_rigid_pendulum_oscillation():
    """2023年度問題1(v): 小振動の周期を示す図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左図: 振動の様子
    t = np.linspace(0, 4*np.pi, 1000)
    theta0 = 0.2  # 小振幅
    omega = 1.0
    theta = theta0 * np.cos(omega * t)
    
    ax1.plot(t, theta, 'b-', linewidth=2, label=r'$\theta(t) = \theta_0\cos(\omega t)$')
    ax1.axhline(y=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    ax1.axvline(x=0, color='k', linestyle='--', linewidth=0.5, alpha=0.3)
    
    # 周期の表示
    T = 2 * np.pi / omega
    ax1.axvline(x=T, color='r', linestyle='--', linewidth=1, alpha=0.5, label=f'周期 $T = {T:.2f}$')
    ax1.plot([0, T], [theta0, theta0], 'r-', linewidth=1, alpha=0.5)
    ax1.text(T/2, theta0 + 0.05, r'$T$', fontsize=12, ha='center', color='r')
    
    safe_set_label(ax1.set_xlabel, '時間 $t$', fontsize=12)
    safe_set_label(ax1.set_ylabel, r'角度 $\theta$ (rad)', fontsize=12)
    ax1.set_title('小振動の時間変化', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 右図: 周期の依存性
    l_vals = np.linspace(0.5, 2.0, 100)
    a = 0.3
    g = 9.8
    # I_A = M(a^2/6 + l^2), 周期 T = 2π√(I_A/(Mg l))
    # Mで割ると T = 2π√((a^2/6 + l^2)/(g l))
    T_vals = 2 * np.pi * np.sqrt((a**2/6 + l_vals**2) / (g * l_vals))
    
    ax2.plot(l_vals, T_vals, 'g-', linewidth=2, label='剛体振り子')
    
    # 単振り子の周期（比較用）
    T_simple = 2 * np.pi * np.sqrt(l_vals / g)
    ax2.plot(l_vals, T_simple, 'r--', linewidth=2, label='単振り子（比較）')
    
    safe_set_label(ax2.set_xlabel, r'重心までの距離 $\ell$ (m)', fontsize=12)
    safe_set_label(ax2.set_ylabel, '周期 $T$ (s)', fontsize=12)
    ax2.set_title('周期の依存性', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.suptitle('2023年度問題1(v): 小振動の周期', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('fig28_2023_rigid_pendulum_oscillation.png', dpi=300, bbox_inches='tight')
    print("2023年度問題1(v): 小振動の周期の図を保存しました: fig28_2023_rigid_pendulum_oscillation.png")
    plt.close()

# ============================================
# 2023年度過去問: 問題2 追加の図
# ============================================

def plot_2023_twin_paradox_spacetime():
    """2023年度問題2(iii): 宇宙船の軌跡を時空図に描く"""
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
    # 往路（t = 0 から t = t_P まで）
    t1 = np.linspace(0, t_P, 100)
    x1 = v * t1  # x = vt = beta * ct
    ax.plot(c*t1, x1, 'b-', linewidth=3, label='宇宙船の軌跡（往路）')
    
    # 復路（t = t_P から t = 2*t_P まで）
    t2 = np.linspace(t_P, 2*t_P, 100)
    x2 = x_P - v * (t2 - t_P)  # x = vt_P - v(t - t_P) = v(2t_P - t)
    ax.plot(c*t2, x2, 'b-', linewidth=3, label='宇宙船の軌跡（復路）')
    
    # 地点P（折り返し点）
    ax.plot(c*t_P, x_P, 'ro', markersize=12, label='地点P', zorder=5)
    ax.text(c*t_P + 0.05, x_P + 0.05, 'P', fontsize=14, color='red', fontweight='bold')
    
    # 地球の軌跡（x = 0 の縦線）
    ct_earth = np.linspace(0, 2*c*t_P, 100)
    ax.axvline(x=0, color='k', linestyle='--', linewidth=2, alpha=0.7, label='地球の軌跡（$x = 0$）')
    
    # 光の世界線（x = ±ct）
    ct_light = np.linspace(0, 2*c*t_P, 100)
    ax.plot(ct_light, ct_light, 'r--', linewidth=1, alpha=0.3, label='光の世界線（$x = ct$）')
    ax.plot(ct_light, -ct_light, 'r--', linewidth=1, alpha=0.3, label='光の世界線（$x = -ct$）')
    
    # 座標軸の設定
    safe_set_label(ax.set_xlabel, '$ct$', fontsize=14)
    safe_set_label(ax.set_ylabel, '$x$', fontsize=14)
    ax.set_title('2023年度問題2(iii): 宇宙船の軌跡の時空図', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_aspect('equal')
    ax.set_xlim(-0.2, 2.2*c*t_P)
    ax.set_ylim(-0.5, 1.5)
    
    # 説明テキスト
    ax.text(0.5*c*t_P, 1.3, '時空図: 宇宙船の軌跡', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7), ha='center')
    ax.text(0.5*c*t_P, 1.1, r'往路: $x = \beta ct$ (傾き $\beta$)', fontsize=12, ha='center', color='blue')
    ax.text(0.5*c*t_P, 0.9, r'復路: $x = \beta c(2t_1 - t)$ (傾き $-\beta$)', fontsize=12, ha='center', color='blue')
    
    plt.tight_layout()
    plt.savefig('fig31_2023_twin_paradox_spacetime.png', dpi=300, bbox_inches='tight')
    print("2023年度問題2(iii): 宇宙船の軌跡の時空図を保存しました: fig31_2023_twin_paradox_spacetime.png")
    plt.close()

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
    ax.plot(ct_sim, x_sim, 'g--', linewidth=2, alpha=0.7, label=r"$S'$系の同時線 ($ct' = ct_2$)")
    
    # S系の同時線（t=t1）
    ax.axhline(y=0, xmin=0, xmax=c*t_P/(2*c*t_P), color='orange', linestyle=':', linewidth=2, alpha=0.7, label=r'$S$系の同時線 ($t = t_1$)')
    
    # t3の位置
    t3 = gamma * (t_P / gamma)  # S'系から見たS系の原点の時刻
    # 実際には、S'系の同時線がx=0を通る点
    # Lorentz変換で t3 = gamma*(t_P - beta*x_P/c) = gamma*(t_P - beta*x_P)
    t3_actual = gamma * (t_P - beta * x_P)
    ax.plot(c * t3_actual, 0, 'go', markersize=10, zorder=5, label=r'$t_3$ ($S\'$系から見た$S$系の時刻)')
    ax.text(c * t3_actual, -0.15, r'$t_3 = \gamma (t_2 - \beta x_P/c)$', fontsize=12, ha='center', color='g')
    
    # t1の位置
    ax.plot(c*t_P, 0, 'mo', markersize=10, zorder=5, label=r'$t_1$ ($S$系の時刻)')
    ax.text(c*t_P, -0.3, r'$t_1$', fontsize=12, ha='center', color='m')
    
    # 説明テキスト
    ax.text(0.5*c*t_P, 1.3, '同時の相対性:', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    ax.text(0.5*c*t_P, 1.1, r'$S$系では$t_1$が同時', fontsize=12, ha='center')
    ax.text(0.5*c*t_P, 0.9, r"$S'$系では$t_2$が同時", fontsize=12, ha='center')
    ax.text(0.5*c*t_P, 0.7, r"$S'$系から見ると、$S$系の原点の時刻は$t_3$", fontsize=12, ha='center')
    
    try:
        safe_set_label(ax.set_xlabel, r'$ct$', fontsize=14)
        safe_set_label(ax.set_ylabel, r'$x$', fontsize=14)
    except:
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

def plot_2023_twin_paradox_time_jump():
    """2023年度問題2(iv): 時空図による時間のジャンプの説明図を作成"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
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
    
    # 往路の同時線（S'系）
    x_sim = np.linspace(-0.5, 1.5, 100)
    ct_sim_forward = c*t_P + beta * (x_sim - x_P)
    ax.plot(ct_sim_forward, x_sim, 'g--', linewidth=2, alpha=0.7, label=r"往路の同時線 ($S'$系)")
    
    # 復路の同時線（S''系）
    ct_sim_backward = c*t_P - beta * (x_sim - x_P)
    ax.plot(ct_sim_backward, x_sim, 'm--', linewidth=2, alpha=0.7, label=r"復路の同時線 ($S''$系)")
    
    # t3の位置（往路の同時線と地球の交点）
    t3 = c*t_P
    ax.plot(t3, 0, 'go', markersize=10, zorder=5)
    ax.text(t3, -0.15, r'$t_3$', fontsize=12, ha='center', color='g')
    
    # t3'の位置（復路の同時線と地球の交点）
    t3_prime = 2*c*t_P - t3
    ax.plot(t3_prime, 0, 'mo', markersize=10, zorder=5)
    ax.text(t3_prime, -0.15, r"$t_3'$", fontsize=12, ha='center', color='m')
    
    # 時間のジャンプを示す矢印
    ax.annotate('', xy=(t3_prime, 0), xytext=(t3, 0),
                arrowprops=dict(arrowstyle='<->', color='red', lw=3, alpha=0.7))
    ax.text((t3 + t3_prime)/2, 0.2, r'$2(t_1 - t_3)$', fontsize=14, ha='center', 
            color='red', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    # t1の位置
    ax.plot(c*t_P, 0, 'ko', markersize=10, zorder=5)
    ax.text(c*t_P, -0.3, r'$t_1$', fontsize=12, ha='center', color='k')
    
    # 説明テキスト
    ax.text(0.5*c*t_P, 1.3, '折り返しの瞬間に地球の時計がジャンプ', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7), ha='center')
    ax.text(0.5*c*t_P, 1.1, r'往路の同時線: 地球の時刻$t_3$', fontsize=12, ha='center', color='g')
    ax.text(0.5*c*t_P, 0.9, r"復路の同時線: 地球の時刻$t_3'$", fontsize=12, ha='center', color='m')
    ax.text(0.5*c*t_P, 0.7, r'進んだ時間: $2(t_1 - t_3)$', fontsize=12, ha='center', color='red', fontweight='bold')
    
    safe_set_label(ax.set_xlabel, '$ct$', fontsize=14)
    safe_set_label(ax.set_ylabel, '$x$', fontsize=14)
    ax.set_title('2023年度問題2(iv): 時空図による時間のジャンプの説明', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_aspect('equal')
    ax.set_xlim(-0.2, 2.2*c*t_P)
    ax.set_ylim(-0.5, 1.5)
    
    plt.tight_layout()
    plt.savefig('fig30_2023_twin_paradox_time_jump.png', dpi=300, bbox_inches='tight')
    print("2023年度問題2(iv): 時空図による時間のジャンプの図を保存しました: fig30_2023_twin_paradox_time_jump.png")
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
    try:
        safe_set_label(ax1.set_xlabel, r'$x$', fontsize=12)
        safe_set_label(ax1.set_ylabel, r'$z$', fontsize=12)
    except:
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
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper right')
    ax2.set_title('ケースB: 板の面が回転面に垂直', fontsize=14, fontweight='bold')
    ax2.text(0.5, -0.4, r'$I_B = M\left(\frac{a^2}{12} + \ell^2\right)$', 
            fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    try:
        safe_set_label(ax2.set_xlabel, r'$x$', fontsize=12)
        safe_set_label(ax2.set_ylabel, r'$z$', fontsize=12)
    except:
        safe_set_label(ax2.set_xlabel, 'x', fontsize=12)
        safe_set_label(ax2.set_ylabel, 'z', fontsize=12)
    
    plt.suptitle('2025年度問題1(iv): ケースAとケースBの剛体振り子', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('fig25_2025_rigid_pendulum_cases.png', dpi=300, bbox_inches='tight')
    print("2025年度問題1(iv): ケースAとケースBの図を保存しました: fig25_2025_rigid_pendulum_cases.png")
    plt.close()

def plot_2025_light_direction_transformation():
    """2025年度問題2(iii): 光の方向の変換の図を作成"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # パラメータ
    beta = 0.6  # V/c
    gamma = 1.0 / np.sqrt(1 - beta**2)
    theta = np.pi / 3  # 60度
    
    # O_1系での光の速度成分
    v_x1 = np.cos(theta)
    v_y1 = np.sin(theta)
    
    # O_2系での光の速度成分（ローレンツ変換）
    v_x2 = (v_x1 - beta) / (1 - beta * v_x1)
    v_y2 = v_y1 / (gamma * (1 - beta * v_x1))
    
    # O_2系での角度
    theta_prime = np.arctan2(v_y2, v_x2)
    cos_theta_prime = (np.cos(theta) - beta) / (1 - beta * np.cos(theta))
    
    # 左図: O_1系
    ax1.text(0.5, 0.95, r'$O_1$系（静止系）', fontsize=16, ha='center', fontweight='bold',
             transform=ax1.transAxes)
    
    # 観測者（原点）
    ax1.plot(0, 0, 'ko', markersize=12, label='観測者')
    
    # 光の方向（矢印）
    light_length = 1.5
    ax1.arrow(0, 0, light_length * np.cos(theta), light_length * np.sin(theta),
              head_width=0.15, head_length=0.2, fc='red', ec='red', linewidth=3, 
              label='光の方向')
    
    # 角度の表示
    arc_radius = 0.4
    angle_arc = np.linspace(0, theta, 50)
    ax1.plot(arc_radius * np.cos(angle_arc), arc_radius * np.sin(angle_arc), 
             'g--', linewidth=1.5)
    ax1.text(0.25, 0.15, r'$\theta$', fontsize=14, color='green', fontweight='bold')
    
    # x軸
    ax1.arrow(-0.3, 0, 1.8, 0, head_width=0.05, head_length=0.08, 
             fc='black', ec='black', linewidth=1.5)
    ax1.text(1.6, -0.15, r'$x$', fontsize=14, fontweight='bold')
    
    # y軸
    ax1.arrow(0, -0.3, 0, 1.8, head_width=0.05, head_length=0.08, 
             fc='black', ec='black', linewidth=1.5)
    ax1.text(-0.15, 1.6, r'$y$', fontsize=14, fontweight='bold')
    
    # 速度成分の表示
    ax1.arrow(0, 0, light_length * np.cos(theta), 0,
              head_width=0.08, head_length=0.1, fc='blue', ec='blue', 
              linewidth=2, alpha=0.6, linestyle='--')
    ax1.text(light_length * np.cos(theta) / 2, -0.2, 
             r'$c\cos\theta$', fontsize=12, color='blue', ha='center')
    
    ax1.arrow(light_length * np.cos(theta), 0, 0, light_length * np.sin(theta),
              head_width=0.08, head_length=0.1, fc='blue', ec='blue', 
              linewidth=2, alpha=0.6, linestyle='--')
    ax1.text(light_length * np.cos(theta) + 0.2, light_length * np.sin(theta) / 2, 
             r'$c\sin\theta$', fontsize=12, color='blue', va='center')
    
    ax1.set_xlim(-0.5, 2.0)
    ax1.set_ylim(-0.5, 2.0)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper left', fontsize=11)
    
    # 右図: O_2系
    ax2.text(0.5, 0.95, r"$O_2$系（速度$V$で$x$方向に運動）", fontsize=16, ha='center', 
             fontweight='bold', transform=ax2.transAxes)
    
    # 観測者（原点）
    ax2.plot(0, 0, 'ko', markersize=12, label='観測者')
    
    # 速度ベクトル（O_2系の運動方向）
    ax2.arrow(0.2, 1.6, 0.4, 0, head_width=0.08, head_length=0.1, 
             fc='purple', ec='purple', linewidth=2.5)
    ax2.text(0.7, 1.7, r'$V$', fontsize=14, color='purple', fontweight='bold')
    
    # 光の方向（矢印）
    ax2.arrow(0, 0, light_length * np.cos(theta_prime), light_length * np.sin(theta_prime),
              head_width=0.15, head_length=0.2, fc='red', ec='red', linewidth=3, 
              label='光の方向')
    
    # 角度の表示
    angle_arc2 = np.linspace(0, theta_prime, 50)
    ax2.plot(arc_radius * np.cos(angle_arc2), arc_radius * np.sin(angle_arc2), 
             'g--', linewidth=1.5)
    ax2.text(0.25, 0.1, r"$\theta'$", fontsize=14, color='green', fontweight='bold')
    
    # x'軸
    ax2.arrow(-0.3, 0, 1.8, 0, head_width=0.05, head_length=0.08, 
             fc='black', ec='black', linewidth=1.5)
    ax2.text(1.6, -0.15, r"$x'$", fontsize=14, fontweight='bold')
    
    # y'軸
    ax2.arrow(0, -0.3, 0, 1.8, head_width=0.05, head_length=0.08, 
             fc='black', ec='black', linewidth=1.5)
    ax2.text(-0.15, 1.6, r"$y'$", fontsize=14, fontweight='bold')
    
    # 速度成分の表示
    ax2.arrow(0, 0, light_length * np.cos(theta_prime), 0,
              head_width=0.08, head_length=0.1, fc='blue', ec='blue', 
              linewidth=2, alpha=0.6, linestyle='--')
    ax2.text(light_length * np.cos(theta_prime) / 2, -0.2, 
             r"$c\cos\theta'$", fontsize=12, color='blue', ha='center')
    
    ax2.arrow(light_length * np.cos(theta_prime), 0, 0, light_length * np.sin(theta_prime),
              head_width=0.08, head_length=0.1, fc='blue', ec='blue', 
              linewidth=2, alpha=0.6, linestyle='--')
    ax2.text(light_length * np.cos(theta_prime) + 0.2, light_length * np.sin(theta_prime) / 2, 
             r"$c\sin\theta'$", fontsize=12, color='blue', va='center')
    
    # 公式の表示
    formula_text = r"$\cos\theta' = \frac{\cos\theta - \beta}{1 - \beta\cos\theta}$"
    ax2.text(0.5, -0.35, formula_text, fontsize=13, ha='center', 
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
             transform=ax2.transAxes)
    
    ax2.set_xlim(-0.5, 2.0)
    ax2.set_ylim(-0.5, 2.0)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.legend(loc='upper left', fontsize=11)
    
    plt.suptitle('2025年度問題2(iii): 光の方向の変換（光行差）', fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('fig32_2025_light_direction_transformation.png', dpi=300, bbox_inches='tight')
    print("2025年度問題2(iii): 光の方向の変換の図を保存しました: fig32_2025_light_direction_transformation.png")
    plt.close()

def plot_2025_light_aberration_pi2():
    """2025年度問題2(iii)(b): θ = π/2の場合の光行差の図を作成"""
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # パラメータ
    beta = 0.6  # V/c
    theta = np.pi / 2  # 90度
    
    # O_1系での光の方向（垂直方向）
    light_length = 1.5
    
    # O_2系での角度
    cos_theta_prime = (np.cos(theta) - beta) / (1 - beta * np.cos(theta))
    theta_prime = np.arccos(cos_theta_prime)
    delta_theta = theta_prime - theta
    
    # 観測者（原点）
    ax.plot(0, 0, 'ko', markersize=12, label='観測者')
    
    # O_1系での光の方向（垂直方向、y軸方向）
    ax.arrow(0, 0, 0, light_length,
             head_width=0.15, head_length=0.2, fc='blue', ec='blue', linewidth=3, 
             label=r'$O_1$系での光の方向（$\theta = \pi/2$）')
    
    # O_2系での光の方向
    ax.arrow(0, 0, light_length * np.cos(theta_prime), light_length * np.sin(theta_prime),
             head_width=0.15, head_length=0.2, fc='red', ec='red', linewidth=3, 
             label=r"$O_2$系での光の方向（$\theta' = \pi/2 + \Delta\theta$）")
    
    # 速度ベクトル（O_2系の運動方向）
    ax.arrow(0.3, 1.3, 0.4, 0, head_width=0.08, head_length=0.1, 
             fc='purple', ec='purple', linewidth=2.5)
    ax.text(0.8, 1.4, r'$V$', fontsize=14, color='purple', fontweight='bold')
    
    # 角度の表示
    # θ = π/2
    ax.plot([0, 0], [0, 0.4], 'g--', linewidth=1.5)
    ax.text(-0.15, 0.2, r'$\theta = \frac{\pi}{2}$', fontsize=14, color='green', 
            fontweight='bold', ha='right')
    
    # θ' = π/2 + Δθ
    arc_radius = 0.5
    angle_arc = np.linspace(np.pi/2, theta_prime, 50)
    ax.plot(arc_radius * np.cos(angle_arc), arc_radius * np.sin(angle_arc), 
            'r--', linewidth=1.5)
    ax.text(0.3, 0.3, r"$\theta'$", fontsize=14, color='red', fontweight='bold')
    
    # Δθの表示
    delta_arc_radius = 0.3
    delta_angle_arc = np.linspace(np.pi/2, theta_prime, 30)
    ax.plot(delta_arc_radius * np.cos(delta_angle_arc), 
            delta_arc_radius * np.sin(delta_angle_arc), 
            'orange', linewidth=2, linestyle=':')
    ax.text(0.15, 0.15, r'$\Delta\theta$', fontsize=14, color='orange', 
            fontweight='bold')
    
    # x軸
    ax.arrow(-0.3, 0, 1.8, 0, head_width=0.05, head_length=0.08, 
             fc='black', ec='black', linewidth=1.5)
    ax.text(1.6, -0.15, r'$x$', fontsize=14, fontweight='bold')
    
    # y軸
    ax.arrow(0, -0.3, 0, 1.8, head_width=0.05, head_length=0.08, 
             fc='black', ec='black', linewidth=1.5)
    ax.text(-0.15, 1.6, r'$y$', fontsize=14, fontweight='bold')
    
    # 公式の表示
    formula_text = r"$\sin\Delta\theta = \beta = \frac{V}{c}$"
    ax.text(0.5, -0.25, formula_text, fontsize=14, ha='center', 
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8),
            transform=ax.transAxes)
    
    # 数値の表示
    sin_delta_theta = beta
    delta_theta_deg = np.degrees(delta_theta)
    info_text = f"$\sin\Delta\theta = {beta:.2f}$\n$\Delta\theta = {delta_theta_deg:.1f}^\\circ$"
    ax.text(1.2, 0.8, info_text, fontsize=12, 
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    ax.set_xlim(-0.5, 2.0)
    ax.set_ylim(-0.5, 2.0)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=11)
    try:
        ax.set_title('2025年度問題2(iii)(b): $\\theta = \\pi/2$の場合の光行差', 
                    fontsize=16, fontweight='bold')
    except:
        ax.set_title('2025年度問題2(iii)(b): theta = pi/2の場合の光行差', 
                    fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('fig33_2025_light_aberration_pi2.png', dpi=300, bbox_inches='tight')
    print("2025年度問題2(iii)(b): θ = π/2の場合の光行差の図を保存しました: fig33_2025_light_aberration_pi2.png")
    plt.close()

import argparse
import os
from functools import wraps
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# 図の生成関数と出力ファイル名のマッピング
PLOT_FUNCTIONS = {
    'fig1_pendulum.png': plot_pendulum,
    'fig2_harmonic_oscillator.png': plot_harmonic_oscillator,
    'fig3_lorentz_transformation.png': plot_lorentz_transformation,
    'fig4_pendulum_potential.png': plot_pendulum_potential,
    'fig5_center_of_mass.png': plot_center_of_mass,
    'fig6_moments_of_inertia.png': plot_moments_of_inertia,
    'fig7_2d_rigid_body.png': plot_2d_rigid_body,
    'fig8_rigid_pendulum.png': plot_rigid_pendulum,
    'fig9_rolling_objects.png': plot_rolling_objects,
    'fig10_symmetric_top.png': plot_symmetric_top,
    'fig11_michelson_morley.png': plot_michelson_morley,
    'fig12_twin_paradox.png': plot_twin_paradox,
    'fig13_transverse_doppler.png': plot_transverse_doppler,
    'fig14_proper_time.png': plot_proper_time,
    'fig15_pion_decay.png': plot_pion_decay,
    'fig16_em_field_unification.png': plot_em_field_unification,
    'fig17_charged_particle_em.png': plot_charged_particle_in_em_field,
    'fig18_em_field_transformation.png': plot_em_field_transformation,
    'fig19_2023_rigid_pendulum.png': plot_2023_rigid_pendulum,
    'fig20_2023_twin_paradox_detailed.png': plot_2023_twin_paradox_detailed,
    'fig21_2023_gzk_cutoff.png': plot_2023_gzk_cutoff,
    'fig22_2024_rigid_body_motion.png': plot_2024_rigid_body_motion,
    'fig24_2024_rolling_order.png': plot_2024_rolling_order,
    'fig23_2025_particle_collision.png': plot_2025_particle_collision,
    'fig25_2025_rigid_pendulum_cases.png': plot_2025_rigid_pendulum_cases,
    'fig32_2025_light_direction_transformation.png': plot_2025_light_direction_transformation,
    'fig33_2025_light_aberration_pi2.png': plot_2025_light_aberration_pi2,
    'fig26_2023_rigid_pendulum_potential.png': plot_2023_rigid_pendulum_potential,
    'fig27_2023_rigid_pendulum_cases.png': plot_2023_rigid_pendulum_cases,
    'fig28_2023_rigid_pendulum_oscillation.png': plot_2023_rigid_pendulum_oscillation,
    'fig29_2023_twin_paradox_simultaneity.png': plot_2023_twin_paradox_simultaneity,
    'fig30_2023_twin_paradox_time_jump.png': plot_2023_twin_paradox_time_jump,
    'fig31_2023_twin_paradox_spacetime.png': plot_2023_twin_paradox_spacetime,
    'fig_orthogonal_transformation.png': plot_orthogonal_transformation,
    'fig_orthogonal_columns.png': plot_orthogonal_columns,
    'fig_polar_coordinates.png': plot_polar_coordinates,
    'fig_angular_momentum_conservation.png': plot_angular_momentum_conservation,
    'fig_tensor_transformation.png': plot_tensor_transformation,
    'fig_cross_product.png': plot_cross_product,
    'fig_rolling_condition.png': plot_rolling_condition,
    'fig_precession_nutation.png': plot_precession_nutation,
    'fig_euler_angles.png': plot_euler_angles,
    'fig_length_contraction.png': plot_length_contraction,
    'fig_time_dilation.png': plot_time_dilation,
    'fig_velocity_transformation.png': plot_velocity_transformation,
    'fig_four_vector_transformation.png': plot_four_vector_transformation,
}

def plot_with_cache(plot_func, output_file):
    """キャッシュ機能付きで図を生成"""
    if os.path.exists(output_file):
        print(f"スキップ: {output_file} は既に存在します")
        return output_file
    
    try:
        plot_func()
        return output_file
    except Exception as e:
        print(f"エラー: {output_file} の生成に失敗しました: {e}")
        return None

def generate_plots(plot_names=None, use_cache=True, parallel=True, max_workers=4):
    """図を生成する（並列処理対応）"""
    if plot_names is None:
        plot_names = list(PLOT_FUNCTIONS.keys())
    
    # 存在しない図のみを生成
    if use_cache:
        plot_names = [name for name in plot_names if not os.path.exists(name)]
    
    if not plot_names:
        print("すべての図が既に存在します。")
        return
    
    print(f"図の作成中... ({len(plot_names)} 個)")
    
    if parallel and len(plot_names) > 1:
        # 並列処理（threadingを使用、matplotlibはマルチプロセスで問題が発生する可能性があるため）
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(plot_with_cache, PLOT_FUNCTIONS[name], name): name
                for name in plot_names if name in PLOT_FUNCTIONS
            }
            
            completed = 0
            for future in as_completed(futures):
                result = future.result()
                completed += 1
                if result:
                    print(f"[{completed}/{len(futures)}] 完了: {result}")
    else:
        # 逐次処理
        for i, name in enumerate(plot_names, 1):
            if name in PLOT_FUNCTIONS:
                result = plot_with_cache(PLOT_FUNCTIONS[name], name)
                if result:
                    print(f"[{i}/{len(plot_names)}] 完了: {result}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='力学特論演習問題の図を作成')
    parser.add_argument('--plots', nargs='+', help='生成する図のファイル名（指定しない場合はすべて生成）')
    parser.add_argument('--no-cache', action='store_true', help='キャッシュを使用しない（既存ファイルを上書き）')
    parser.add_argument('--no-parallel', action='store_true', help='並列処理を無効化')
    parser.add_argument('--workers', type=int, default=4, help='並列処理のワーカー数（デフォルト: 4）')
    
    args = parser.parse_args()
    
    start_time = time.time()
    generate_plots(
        plot_names=args.plots,
        use_cache=not args.no_cache,
        parallel=not args.no_parallel,
        max_workers=args.workers
    )
    elapsed_time = time.time() - start_time
    print(f"\nすべての図の作成が完了しました。（所要時間: {elapsed_time:.2f} 秒）")
