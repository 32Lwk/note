#!/usr/bin/env python3
"""
問題8-1と8-2の図を生成するスクリプト
- ハイゼンベルク描像とシュレーディンガー描像の概念図
- 調和振動子の位置・運動量の時間発展
- エルミート多項式のグラフ
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches
from scipy.special import hermite
import platform
import matplotlib.font_manager as fm

# 日本語フォントの設定
def setup_japanese_font():
    """日本語フォントを設定する関数"""
    if platform.system() == 'Darwin':  # macOS
        # macOSで利用可能な日本語フォントを検索
        japanese_fonts = ['Hiragino Sans', 'Hiragino Maru Gothic Pro', 'Hiragino Mincho ProN', 
                         'Yu Gothic', 'Yu Mincho', 'Meiryo', 'Takao']
        available_fonts = [f.name for f in fm.fontManager.ttflist]
        
        # 利用可能なフォントを優先順位で検索
        for font_name in japanese_fonts:
            if font_name in available_fonts:
                plt.rcParams['font.family'] = font_name
                print(f"日本語フォントを設定しました: {font_name}")
                break
        else:
            # フォールバック: システムのデフォルト日本語フォント
            plt.rcParams['font.sans-serif'] = ['Hiragino Sans', 'Hiragino Maru Gothic Pro', 
                                               'Yu Gothic', 'Meiryo', 'Takao', 
                                               'IPAexGothic', 'IPAPGothic', 'VL PGothic', 
                                               'Noto Sans CJK JP']
            print("デフォルトの日本語フォント設定を使用します")
    elif platform.system() == 'Windows':
        plt.rcParams['font.family'] = 'MS Gothic'
        print("日本語フォントを設定しました: MS Gothic")
    else:  # Linux
        plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP', 'Yu Gothic', 'Meiryo', 'MS Gothic']
        print("Linux用の日本語フォント設定を使用します")
    
    plt.rcParams['axes.unicode_minus'] = False  # 負の符号の表示を正しくする
    plt.rcParams['font.size'] = 10

# フォント設定を実行
setup_japanese_font()

# 出力ディレクトリ
output_dir = '../figures'

# ============================================================================
# 図1: ハイゼンベルク描像とシュレーディンガー描像の概念図
# ============================================================================
def plot_heisenberg_schrodinger_picture():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # シュレーディンガー描像
    ax1.set_xlim(-0.5, 3.5)
    ax1.set_ylim(-0.5, 2.5)
    ax1.axis('off')
    ax1.set_title('Schrödinger Picture\n(シュレーディンガー描像)', fontsize=14, fontweight='bold')
    
    # 状態ベクトル（時間変化）
    t_values = np.linspace(0, 2*np.pi, 8)
    for i, t in enumerate(t_values):
        x = 0.5 + i * 0.4
        y = 1.0 + 0.3 * np.sin(t)
        ax1.arrow(x, 0.2, 0, y-0.2, head_width=0.08, head_length=0.1, 
                 fc='blue', ec='blue', alpha=0.6)
        ax1.text(x, -0.2, f't={i}', ha='center', fontsize=8)
    
    # 演算子（固定）
    ax1.text(1.5, 1.8, r'$\hat{x}$, $\hat{p}$', fontsize=14, 
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax1.text(1.5, 1.5, '(時間に依存しない)', fontsize=9, ha='center')
    
    # ハイゼンベルク描像
    ax2.set_xlim(-0.5, 3.5)
    ax2.set_ylim(-0.5, 2.5)
    ax2.axis('off')
    ax2.set_title('Heisenberg Picture\n(ハイゼンベルク描像)', fontsize=14, fontweight='bold')
    
    # 状態ベクトル（固定）
    ax2.arrow(1.5, 0.2, 0, 0.8, head_width=0.15, head_length=0.1, 
             fc='blue', ec='blue', linewidth=2)
    ax2.text(1.5, 1.3, r'$|\psi\rangle$', fontsize=14, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax2.text(1.5, 0.0, '(時間に依存しない)', fontsize=9, ha='center')
    
    # 演算子（時間変化）
    for i, t in enumerate(t_values):
        x = 0.5 + i * 0.4
        y = 1.8 + 0.2 * np.sin(t)
        ax2.text(x, y, r'$\hat{x}(t)$', fontsize=10, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.6))
        ax2.text(x, -0.2, f't={i}', ha='center', fontsize=8)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/problem8_1_pictures.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_dir}/problem8_1_pictures.png")

# ============================================================================
# 図2: 調和振動子の位置・運動量の時間発展
# ============================================================================
def plot_harmonic_oscillator_time_evolution():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # パラメータ
    omega = 1.0
    t = np.linspace(0, 4*np.pi, 1000)
    
    # 初期条件（演算子の期待値として解釈）
    x0 = 1.0  # 初期位置
    p0 = 0.5  # 初期運動量
    m = 1.0
    
    # 位置の時間発展
    x_t = x0 * np.cos(omega * t) + (p0 / (m * omega)) * np.sin(omega * t)
    
    # 運動量の時間発展
    p_t = p0 * np.cos(omega * t) - m * omega * x0 * np.sin(omega * t)
    
    # 位置のプロット
    ax1.plot(t, x_t, 'b-', linewidth=2, label=r'$\hat{x}(t)$ (位置演算子)')
    ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax1.set_xlabel('時間 $t$', fontsize=12)
    ax1.set_ylabel('位置 $x$', fontsize=12)
    ax1.set_title('調和振動子の位置演算子の時間発展', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=11)
    ax1.set_xlim(0, 4*np.pi)
    
    # 運動量のプロット
    ax2.plot(t, p_t, 'r-', linewidth=2, label=r'$\hat{p}(t)$ (運動量演算子)')
    ax2.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax2.set_xlabel('時間 $t$', fontsize=12)
    ax2.set_ylabel('運動量 $p$', fontsize=12)
    ax2.set_title('調和振動子の運動量演算子の時間発展', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=11)
    ax2.set_xlim(0, 4*np.pi)
    
    # 位相空間のプロット（追加）
    fig2, ax3 = plt.subplots(1, 1, figsize=(8, 8))
    ax3.plot(x_t, p_t, 'purple', linewidth=2, alpha=0.7)
    ax3.plot(x_t[0], p_t[0], 'go', markersize=10, label='初期状態')
    ax3.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax3.axvline(x=0, color='k', linestyle='--', alpha=0.3)
    ax3.set_xlabel('位置 $x$', fontsize=12)
    ax3.set_ylabel('運動量 $p$', fontsize=12)
    ax3.set_title('位相空間での軌道（調和振動子）', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.legend(fontsize=11)
    ax3.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/problem8_1_time_evolution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/problem8_1_phase_space.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Saved: {output_dir}/problem8_1_time_evolution.png")
    print(f"Saved: {output_dir}/problem8_1_phase_space.png")

# ============================================================================
# 図3: エルミート多項式のグラフ
# ============================================================================
def plot_hermite_polynomials():
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    
    xi = np.linspace(-4, 4, 1000)
    
    # エルミート多項式を計算
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    labels = []
    
    for n in range(6):
        H_n = hermite(n)
        H_n_vals = H_n(xi)
        ax.plot(xi, H_n_vals, color=colors[n], linewidth=2, 
               label=f'$H_{n}(\\xi)$')
    
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    ax.set_xlabel('$\\xi = \\sqrt{\\frac{m\\omega}{\\hbar}}x$', fontsize=14)
    ax.set_ylabel('$H_n(\\xi)$', fontsize=14)
    ax.set_title('エルミート多項式 $H_n(\\xi)$ ($n = 0, 1, 2, 3, 4, 5$)', 
                fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', fontsize=11)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-30, 30)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/problem8_2_hermite_polynomials.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_dir}/problem8_2_hermite_polynomials.png")

# ============================================================================
# 図4: 位置固有ベクトルの概念図
# ============================================================================
def plot_position_eigenvector_concept():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 3.5)
    ax.axis('off')
    ax.set_title('位置固有ベクトル $|x\\rangle$ の構成', fontsize=14, fontweight='bold')
    
    # 基底状態
    ax.text(1, 2.5, r'$|0\rangle$', fontsize=16, ha='center',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax.text(1, 2.0, '(基底状態)', fontsize=10, ha='center')
    
    # 生成演算子の作用
    arrow1 = FancyArrowPatch((1.5, 2.5), (4.5, 2.5), 
                             arrowstyle='->', mutation_scale=20, 
                             color='green', linewidth=2)
    ax.add_patch(arrow1)
    ax.text(3, 2.8, r'$f(\hat{a}^\dagger)$', fontsize=12, ha='center',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    # 位置固有ベクトル
    ax.text(5, 2.5, r'$|x\rangle$', fontsize=16, ha='center',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax.text(5, 2.0, r'$= f(\hat{a}^\dagger)|0\rangle$', fontsize=11, ha='center')
    
    # 固有値方程式
    ax.text(5, 1.0, r'$\hat{x}|x\rangle = x|x\rangle$', fontsize=14, ha='center',
           bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    
    # エネルギー固有状態での展開
    arrow2 = FancyArrowPatch((5.5, 1.5), (8.5, 1.5), 
                             arrowstyle='->', mutation_scale=20, 
                             color='purple', linewidth=2)
    ax.add_patch(arrow2)
    ax.text(7, 1.8, 'エルミート多項式で展開', fontsize=10, ha='center')
    
    ax.text(9, 1.5, r'$\sum_n c_n|n\rangle$', fontsize=14, ha='center',
           bbox=dict(boxstyle='round', facecolor='lightpink', alpha=0.7))
    ax.text(9, 1.0, '(エネルギー固有状態)', fontsize=9, ha='center')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/problem8_2_position_eigenvector.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {output_dir}/problem8_2_position_eigenvector.png")

# ============================================================================
# メイン関数
# ============================================================================
if __name__ == '__main__':
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    print("問題8の図を生成中...")
    plot_heisenberg_schrodinger_picture()
    plot_harmonic_oscillator_time_evolution()
    plot_hermite_polynomials()
    plot_position_eigenvector_concept()
    print("完了！")
