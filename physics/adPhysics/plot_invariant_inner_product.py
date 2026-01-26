"""
4元運動量の内積の不変性を説明するための図を生成するスクリプト
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
import platform

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
    else:
        # Linux/Windows用の設定
        plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP', 'Yu Gothic', 'Meiryo', 'MS Gothic']
        print("Linux/Windows用の日本語フォント設定を使用します")
    
    plt.rcParams['axes.unicode_minus'] = False

# フォント設定を実行
setup_japanese_font()

# 図1: 衝突前後の4元運動量ベクトルの保存と内積の不変性
def plot_momentum_conservation():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 軸の設定
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 4)
    ax.set_xlabel('空間成分 $P^1$ (運動量)', fontsize=12)
    ax.set_ylabel('時間成分 $P^0 = E/c$', fontsize=12)
    ax.set_title('衝突前後の4元運動量保存と内積の不変性', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    # 衝突前の4元運動量ベクトル
    P1 = np.array([2.0, 1.5])  # (E/c, p1)
    P2 = np.array([1.0, 0.0])  # (mc, 0)
    Pi = P1 + P2  # 全4元運動量
    
    # 衝突後の4元運動量ベクトル（例として）
    P3 = np.array([1.8, 0.5])  # 粒子3
    P4 = np.array([1.2, -0.5])  # 粒子4
    Pf = P3 + P4  # 全4元運動量（保存される）
    
    # 衝突前のベクトルを描画
    ax.arrow(0, 0, P1[1], P1[0], head_width=0.1, head_length=0.1, 
             fc='blue', ec='blue', linewidth=2, label='$P_1^\\mu$ (粒子1)')
    ax.arrow(P1[1], P1[0], P2[1], P2[0], head_width=0.1, head_length=0.1, 
             fc='green', ec='green', linewidth=2, label='$P_2^\\mu$ (粒子2)')
    ax.arrow(0, 0, Pi[1], Pi[0], head_width=0.15, head_length=0.15, 
             fc='red', ec='red', linewidth=3, linestyle='--', 
             label='$P_i^\\mu = P_1^\\mu + P_2^\\mu$ (衝突前の全4元運動量)')
    
    # 衝突後のベクトルを描画
    ax.arrow(0, 0, P3[1], P3[0], head_width=0.1, head_length=0.1, 
             fc='purple', ec='purple', linewidth=2, alpha=0.6, label='$P_3^\\mu$ (粒子3)')
    ax.arrow(P3[1], P3[0], P4[1], P4[0], head_width=0.1, head_length=0.1, 
             fc='orange', ec='orange', linewidth=2, alpha=0.6, label='$P_4^\\mu$ (粒子4)')
    ax.arrow(0, 0, Pf[1], Pf[0], head_width=0.15, head_length=0.15, 
             fc='red', ec='red', linewidth=3, linestyle=':', 
             label='$P_f^\\mu = P_3^\\mu + P_4^\\mu$ (衝突後の全4元運動量)')
    
    # 点をマーク
    ax.plot([Pi[1]], [Pi[0]], 'ro', markersize=10, label='$P_i^\\mu$ の端点')
    ax.plot([Pf[1]], [Pf[0]], 'r^', markersize=10, label='$P_f^\\mu$ の端点（同じ点）')
    
    # テキスト注釈
    ax.text(Pi[1]+0.3, Pi[0]+0.2, '$P_i^\\mu = P_f^\\mu$\n(4元運動量保存)', 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    ax.text(1.5, 0.5, '内積: $P_i^\\mu P_{i,\\mu} = P_f^\\mu P_{f,\\mu}$\n(どの座標系でも同じ)', 
            fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    ax.legend(loc='upper left', fontsize=10)
    ax.set_aspect('equal', adjustable='box')
    
    plt.tight_layout()
    plt.savefig('/Users/yuto/itphy/physics/adPhysics/momentum_conservation.png', dpi=300, bbox_inches='tight')
    print("図1を保存しました: momentum_conservation.png")
    plt.close()

# 図2: 異なる座標系での4元運動量の内積
def plot_lorentz_invariance():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # 共通のパラメータ
    P0 = 3.0  # 時間成分
    P1 = 2.0  # 空間成分
    
    # 左図: 初期の系（粒子1が運動する系）
    ax1.set_xlim(-1, 4)
    ax1.set_ylim(-1, 5)
    ax1.set_xlabel('空間成分 $P^1$', fontsize=12)
    ax1.set_ylabel('時間成分 $P^0$', fontsize=12)
    ax1.set_title('初期の系での4元運動量', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    
    # 初期状態の全4元運動量
    Pi = np.array([P0, P1])
    ax1.arrow(0, 0, Pi[1], Pi[0], head_width=0.2, head_length=0.2, 
             fc='red', ec='red', linewidth=3, label='$P_i^\\mu$')
    
    # 内積の計算を表示
    inner_product = -(P0)**2 + (P1)**2
    formula_text = r'内積: $P_i^\mu P_{i,\mu} = -(P^0)^2 + (P^1)^2$'
    ax1.text(0.2, 4.5, formula_text, 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax1.text(0.2, 4.0, f'$= -{P0:.1f}^2 + {P1:.1f}^2 = {inner_product:.1f}$', 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    ax1.plot([Pi[1]], [Pi[0]], 'ro', markersize=10)
    ax1.legend(loc='upper right', fontsize=11)
    ax1.set_aspect('equal', adjustable='box')
    
    # 右図: 重心系
    ax2.set_xlim(-1, 4)
    ax2.set_ylim(-1, 5)
    ax2.set_xlabel('空間成分 $P^1$', fontsize=12)
    ax2.set_ylabel('時間成分 $P^0$', fontsize=12)
    ax2.set_title('重心系での4元運動量', fontsize=13, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)
    
    # 重心系では空間成分が0
    P0_CM = np.sqrt(-inner_product)  # 内積が同じなので時間成分を逆算
    Pf_CM = np.array([P0_CM, 0.0])
    ax2.arrow(0, 0, Pf_CM[1], Pf_CM[0], head_width=0.2, head_length=0.2, 
             fc='blue', ec='blue', linewidth=3, label='$P_f^\\mu$ (重心系)')
    
    # 内積の計算を表示
    formula_text2 = r'内積: $P_f^\mu P_{f,\mu} = -(P^0)^2 + (P^1)^2$'
    ax2.text(0.2, 4.5, formula_text2, 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax2.text(0.2, 4.0, f'$= -{P0_CM:.1f}^2 + 0^2 = {inner_product:.1f}$', 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax2.text(0.2, 3.3, '同じ値！\n(ローレンツ不変量)', 
            fontsize=12, fontweight='bold', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    ax2.plot([Pf_CM[1]], [Pf_CM[0]], 'bo', markersize=10)
    ax2.legend(loc='upper right', fontsize=11)
    ax2.set_aspect('equal', adjustable='box')
    
    plt.suptitle('異なる座標系での4元運動量の内積は同じ値を持つ', 
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('/Users/yuto/itphy/physics/adPhysics/lorentz_invariance.png', dpi=300, bbox_inches='tight')
    print("図2を保存しました: lorentz_invariance.png")
    plt.close()

# 図3: 時空図での4元運動量の可視化
def plot_spacetime_diagram():
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 軸の設定
    ax.set_xlim(-2, 4)
    ax.set_ylim(-2, 4)
    ax.set_xlabel('空間座標 $x$ (相対的な単位)', fontsize=12)
    ax.set_ylabel('時間座標 $ct$ (相対的な単位)', fontsize=12)
    ax.set_title('時空図での衝突前後の4元運動量', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    # 光円錐
    t = np.linspace(-2, 4, 100)
    ax.plot(t, t, 'k--', linewidth=1, alpha=0.5, label='光円錐 ($x=ct$)')
    ax.plot(t, -t, 'k--', linewidth=1, alpha=0.5)
    
    # 衝突前の軌跡（簡略化）
    t_before = np.linspace(-1, 0, 50)
    x1 = 0.8 * t_before + 0.5  # 粒子1の軌跡
    x2 = np.zeros_like(t_before)  # 粒子2の軌跡
    
    ax.plot(x1, t_before, 'b-', linewidth=2, label='粒子1の軌跡')
    ax.plot(x2, t_before, 'g-', linewidth=2, label='粒子2の軌跡')
    
    # 衝突点
    ax.plot(0, 0, 'ro', markersize=15, label='衝突点', zorder=5)
    
    # 衝突後の軌跡
    t_after = np.linspace(0, 2, 50)
    x3 = 0.3 * t_after  # 粒子3の軌跡
    x4 = -0.3 * t_after  # 粒子4の軌跡
    
    ax.plot(x3, t_after, 'm-', linewidth=2, label='粒子3の軌跡')
    ax.plot(x4, t_after, 'orange', linewidth=2, label='粒子4の軌跡')
    
    # 4元運動量ベクトルを描画（衝突点から）
    # 衝突前の全4元運動量（時間方向に強い）
    ax.arrow(0, 0, 0.2, 0.8, head_width=0.1, head_length=0.1, 
             fc='red', ec='red', linewidth=3, label='全4元運動量 $P^\\mu$')
    
    # テキスト注釈
    ax.text(0.5, 0.5, '衝突前:\n$P_i^\\mu = P_1^\\mu + P_2^\\mu$', 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    ax.text(-1.5, 1.5, '衝突後:\n$P_f^\\mu = P_3^\\mu + P_4^\\mu$', 
            fontsize=11, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax.text(1.5, 2.5, '$P_i^\\mu = P_f^\\mu$\n(4元運動量保存)', 
            fontsize=12, fontweight='bold', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    ax.legend(loc='upper left', fontsize=10)
    ax.set_aspect('equal', adjustable='box')
    
    plt.tight_layout()
    plt.savefig('/Users/yuto/itphy/physics/adPhysics/spacetime_diagram.png', dpi=300, bbox_inches='tight')
    print("図3を保存しました: spacetime_diagram.png")
    plt.close()

# 図4: 内積の不変性の概念的説明
def plot_inner_product_concept():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title('なぜ衝突前後で内積が変わらないのか', fontsize=16, fontweight='bold', pad=20)
    
    # ステップ1: 4元運動量の保存
    ax.text(5, 7.5, 'ステップ1: 4元運動量の保存', fontsize=14, fontweight='bold', 
            ha='center', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    ax.text(2, 6.5, '衝突前:', fontsize=12, fontweight='bold')
    ax.text(2, 6, '$P_i^\\mu = P_1^\\mu + P_2^\\mu$', fontsize=12)
    
    ax.text(7, 6.5, '衝突後:', fontsize=12, fontweight='bold')
    ax.text(7, 6, '$P_f^\\mu = P_3^\\mu + P_4^\\mu$', fontsize=12)
    
    ax.annotate('', xy=(6, 6), xytext=(4, 6), 
                arrowprops=dict(arrowstyle='<->', lw=2, color='red'))
    ax.text(5, 5.7, '保存則により\n$P_i^\\mu = P_f^\\mu$', 
            fontsize=11, ha='center', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    # ステップ2: 内積の定義
    ax.text(5, 5, 'ステップ2: 内積は同じベクトルの性質', fontsize=14, fontweight='bold', 
            ha='center', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    ax.text(2.5, 4.2, '$P_i^\\mu P_{i,\\mu}$', fontsize=14, 
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    ax.text(6.5, 4.2, '$P_f^\\mu P_{f,\\mu}$', fontsize=14, 
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    
    ax.annotate('', xy=(7.2, 4.2), xytext=(4.8, 4.2), 
                arrowprops=dict(arrowstyle='<->', lw=2, color='blue'))
    ax.text(5, 3.7, '同じベクトルなので\n内積は同じ値', 
            fontsize=11, ha='center', bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.7))
    
    # ステップ3: ローレンツ不変性
    ax.text(5, 3.2, 'ステップ3: ローレンツ不変性', fontsize=14, fontweight='bold', 
            ha='center', bbox=dict(boxstyle='round', facecolor='plum', alpha=0.7))
    
    ax.text(1.5, 2.2, '初期の系で計算', fontsize=11)
    ax.text(1.5, 1.8, '$P_{i,\\mu} P_i^\\mu$', fontsize=12, 
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    ax.text(5, 2.2, '重心系で計算', fontsize=11)
    ax.text(5, 1.8, '$P_{f,\\mu} P_f^\\mu$', fontsize=12, 
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    ax.text(8.5, 2.2, 'どちらでも', fontsize=11)
    ax.text(8.5, 1.8, '同じ値', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    ax.annotate('', xy=(5.5, 1.8), xytext=(3.2, 1.8), 
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax.annotate('', xy=(6.5, 1.8), xytext=(8.2, 1.8), 
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    
    # 結論
    ax.text(5, 1.2, '結論: どの座標系で計算しても、同じベクトルの内積は同じ値を持つ', 
            fontsize=13, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round', facecolor='gold', alpha=0.8))
    
    # 数式の説明
    ax.text(5, 0.5, r'$P_i^\mu P_{i,\mu} = P_f^\mu P_{f,\mu}$ \n（どの慣性系でも成立）', 
            fontsize=13, ha='center', style='italic',
            bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('/Users/yuto/itphy/physics/adPhysics/inner_product_concept.png', dpi=300, bbox_inches='tight')
    print("図4を保存しました: inner_product_concept.png")
    plt.close()

if __name__ == '__main__':
    print("図を生成しています...")
    plot_momentum_conservation()
    plot_lorentz_invariance()
    plot_spacetime_diagram()
    plot_inner_product_concept()
    print("すべての図の生成が完了しました！")
