"""
物理実験学期末試験の図を生成するスクリプト
"""

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, FancyBboxPatch
import matplotlib.patches as mpatches
import os

# 日本語フォントの設定
import platform
if platform.system() == 'Darwin':  # macOS
    plt.rcParams['font.family'] = 'Hiragino Sans'
elif platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'MS Gothic'
else:  # Linux
    plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# figuresディレクトリを作成
os.makedirs('figures', exist_ok=True)

# ============================================
# 大問1: グラフの図
# ============================================

def plot_graph_improvements():
    """グラフの問題点と改善例を描画"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左：問題のあるグラフ
    hours = np.array([0, 6, 12, 18, 24])
    aug_temp_bad = [28, 29, np.nan, 32.5, 33]
    jan_temp = [5, 2.5, 9.5, 10, 7.5]
    
    # 欠損データを直線で結んだ場合
    hours_aug = [0, 6, 10, 18, 24]
    aug_temp_conn = [28, 29, 29, 32.5, 33]
    
    ax1.plot(hours_aug, aug_temp_conn, 'g^-', linewidth=2, label='Aug 1, 2024')
    ax1.plot(hours, jan_temp, 'ro-', linewidth=2, label='Jan 1, 2025')
    ax1.set_xlim(-1, 25)
    ax1.set_ylim(0, 40)
    ax1.set_xlabel('時刻', fontsize=12)
    ax1.set_ylabel('温度 (℃)', fontsize=12)
    ax1.set_title('不適切なグラフの例', fontsize=14, fontweight='bold')
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    
    # 右：改善されたグラフ
    hours_full = np.arange(0, 25)
    aug_temp_good = [28, 28.5, 29, np.nan, 32, 32.5, 33, 33, 32.5]
    jan_temp_full = [5, 4, 2.5, 3, 4, 5, 7, 9.5, 10, 9.5, 9, 8, 7.5, 7, 6.5, 6, 6.5, 7, 7.5, 7, 7.5, 7, 7.5, 7.5, 7.5]
    
    ax2.plot([0, 6, 10], [28, 29, 29], 'g^-', linewidth=2, label='Aug 1, 2024', markersize=8)
    ax2.plot([18, 24], [32.5, 33], 'g^-', linewidth=2, markersize=8)
    ax2.plot(hours_full, jan_temp_full, 'ro-', linewidth=2, label='Jan 1, 2025', markersize=5)
    ax2.set_xlim(-1, 25)
    ax2.set_ylim(0, 40)
    ax2.set_xlabel('時刻 (時)', fontsize=12)
    ax2.set_ylabel('温度 (℃)', fontsize=12)
    ax2.set_title('改善されたグラフの例', fontsize=14, fontweight='bold')
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)
    ax2.set_xticks([0, 3, 6, 9, 12, 15, 18, 21, 24])
    
    plt.tight_layout()
    plt.savefig('figures/fig1_graph_improvements.png', dpi=300, bbox_inches='tight')
    print("グラフの問題点の図を保存しました: figures/fig1_graph_improvements.png")
    plt.close()

def plot_loglog_example():
    """ログロググラフの例（波長と振動数）"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 波長と振動数の関係: f = c/λ
    wavelength = np.logspace(-12, 3, 1000)  # 10^-12 から 10^3 m
    frequency = 3e8 / wavelength  # c = 3e8 m/s
    
    ax.loglog(wavelength, frequency, 'b-', linewidth=2)
    ax.set_xlabel('波長 λ (m)', fontsize=12)
    ax.set_ylabel('振動数 f (Hz)', fontsize=12)
    ax.set_title('ログロググラフの例：波長と振動数の関係', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig('figures/fig1_loglog.png', dpi=300, bbox_inches='tight')
    print("ログロググラフの例を保存しました: figures/fig1_loglog.png")
    plt.close()

def plot_semilog_example():
    """片対数グラフの例（放射性崩壊）"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 放射性崩壊: N(t) = N0 * exp(-λt)
    t = np.linspace(0, 5, 1000)
    lambda_val = 0.693  # 半減期が1の場合
    N0 = 1000
    N = N0 * np.exp(-lambda_val * t)
    
    ax.semilogy(t, N, 'b-', linewidth=2)
    ax.set_xlabel('時間 t (半減期単位)', fontsize=12)
    ax.set_ylabel('原子核数 N', fontsize=12)
    ax.set_title('片対数グラフの例：放射性崩壊', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig('figures/fig1_semilog.png', dpi=300, bbox_inches='tight')
    print("片対数グラフの例を保存しました: figures/fig1_semilog.png")
    plt.close()

# ============================================
# 大問2: パイプの図
# ============================================

def plot_pipe_section():
    """パイプの断面図"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # 外径と内径
    D = 108.50  # mm
    d = 82.05   # mm
    
    # 外円
    outer_circle = Circle((0, 0), D/2/20, fill=False, linewidth=3, color='black')
    ax.add_patch(outer_circle)
    
    # 内円
    inner_circle = Circle((0, 0), d/2/20, fill=True, linewidth=2, color='lightgray', edgecolor='black')
    ax.add_patch(inner_circle)
    
    # 壁厚の矢印
    ax.annotate('', xy=(d/2/20, 0), xytext=(D/2/20, 0),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text((d/2 + D/2)/2/20, -0.02, f'壁厚 t = {(D-d)/2:.2f} mm', 
            ha='center', fontsize=12, color='red', fontweight='bold')
    
    # 直径の矢印
    ax.annotate('', xy=(-D/2/20, -D/2/20 - 0.15), xytext=(D/2/20, -D/2/20 - 0.15),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
    ax.text(0, -D/2/20 - 0.2, f'外径 D = {D:.2f} mm', 
            ha='center', fontsize=12, color='blue', fontweight='bold')
    
    ax.set_xlim(-D/2/20 - 0.3, D/2/20 + 0.3)
    ax.set_ylim(-D/2/20 - 0.3, D/2/20 + 0.3)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('パイプの断面図', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('figures/fig2_pipe.png', dpi=300, bbox_inches='tight')
    print("パイプの断面図を保存しました: figures/fig2_pipe.png")
    plt.close()

# ============================================
# 大問3: 装置の図
# ============================================

def plot_vernier():
    """ノギスの読み取り方法"""
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # 主尺（1mm刻み、10mmごとに長い目盛り）
    main_scale_x = np.arange(0, 25)
    for x in main_scale_x:
        if x % 10 == 0:
            ax.plot([x, x], [0, 0.8], 'k-', linewidth=2.5)
            ax.text(x, -0.4, str(x), ha='center', fontsize=11, fontweight='bold')
        elif x % 5 == 0:
            ax.plot([x, x], [0, 0.6], 'k-', linewidth=2)
        else:
            ax.plot([x, x], [0, 0.3], 'k-', linewidth=1.2)
    
    # バーニア尺（0.05mm刻み、10目盛りで0.5mm）
    # 18.40mmの読み取りを例に
    vernier_base = 18.4
    vernier_scale_x = np.arange(0, 10) * 0.95 + vernier_base - 0.4  # 0.05 mm 刻み
    for i, x in enumerate(vernier_scale_x):
        if i == 0:
            ax.plot([x, x], [1.2, 1.9], 'r-', linewidth=3, label='バーニア尺のゼロ線', zorder=5)
        if i == 8:
            ax.plot([x, x], [1.2, 1.9], 'g-', linewidth=3, label='一致する目盛（8）', zorder=5)
        elif i % 5 == 0:
            ax.plot([x, x], [1.2, 1.7], 'b-', linewidth=2)
        else:
            ax.plot([x, x], [1.2, 1.5], 'b-', linewidth=1.5)
        if i < 10:
            ax.text(x, 2.0, str(i), ha='center', fontsize=9, color='blue', fontweight='bold')
    
    # 主尺とバーニア尺の背景を区別
    ax.axhspan(0, 0.8, alpha=0.1, color='gray', zorder=0)
    ax.axhspan(1.2, 1.9, alpha=0.1, color='lightblue', zorder=0)
    
    # 補助線
    ax.axvline(18, color='gray', linestyle='--', linewidth=1.5, alpha=0.6, zorder=1)
    ax.axvline(19, color='gray', linestyle='--', linewidth=1.5, alpha=0.6, zorder=1)
    ax.axvline(18.4, color='green', linestyle=':', linewidth=2, alpha=0.7, zorder=2, label='読み取り位置 (18.40 mm)')
    
    # 読み取り値の説明
    ax.text(18.4, 2.4, '読み取り値: 18.40 mm', ha='center', fontsize=12, 
            fontweight='bold', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    ax.set_xlim(15, 22)
    ax.set_ylim(-0.6, 2.8)
    ax.set_xlabel('主尺の読み取り (mm)', fontsize=13, fontweight='bold')
    ax.set_title('ノギスの読み取り方法（18.40 mm の例）', fontsize=15, fontweight='bold', pad=20)
    ax.legend(loc='upper right', fontsize=10)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('figures/fig3_vernier.png', dpi=300, bbox_inches='tight')
    print("ノギスの読み取り方法を保存しました: figures/fig3_vernier.png")
    plt.close()

def plot_multimeter():
    """アナログテスターのスケール"""
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 円形のスケールを模擬（半円）
    theta = np.linspace(0, np.pi, 200)
    radius = 4
    ax.plot(radius * np.cos(theta), radius * np.sin(theta), 'k-', linewidth=3)
    
    # OHMSスケール（緑色、右端が0、左端が∞）
    # 非線形スケールを模擬（実際のOHMSスケールは対数的）
    ohms_values = [0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i, val in enumerate(ohms_values):
        # 非線形配置（右端から左端へ）
        if val == 0:
            angle = np.pi  # 右端
        elif val == 10:
            angle = 0  # 左端
        else:
            # 対数的に配置
            angle = np.pi * (1 - np.log10(val + 0.1) / np.log10(10.1))
        
        if val in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            ax.plot([0, radius*0.85*np.cos(angle)], [0, radius*0.85*np.sin(angle)], 
                   'g-', linewidth=2, alpha=0.8)
            if val <= 10:
                ax.text(radius*1.15*np.cos(angle), radius*1.15*np.sin(angle), str(val), 
                       ha='center', va='center', fontsize=9, color='green', fontweight='bold')
    
    # 針の位置（抵抗計: 0.49Ω、R×10レンジなので読み取り値は約0.49）
    # OHMSスケールで0.49の位置
    angle_resistance = np.pi * (1 - np.log10(0.49 + 0.1) / np.log10(10.1))
    ax.plot([0, radius*1.0*np.cos(angle_resistance)], [0, radius*1.0*np.sin(angle_resistance)], 
           'r-', linewidth=4, label='針の位置（抵抗計: 0.49Ω）', zorder=10)
    
    # DCV/mAスケール（0-50、青色）
    for i in range(0, 11):
        angle = np.pi * (1 - i*5/50)
        if i % 2 == 0:
            ax.plot([0, radius*0.75*np.cos(angle)], [0, radius*0.75*np.sin(angle)], 
                   'b-', linewidth=2, alpha=0.8)
            ax.text(radius*0.9*np.cos(angle), radius*0.9*np.sin(angle), str(i*5), 
                   ha='center', va='center', fontsize=9, color='blue', fontweight='bold')
        else:
            ax.plot([0, radius*0.7*np.cos(angle)], [0, radius*0.7*np.sin(angle)], 
                   'b-', linewidth=1, alpha=0.6)
    
    # 針の位置（電圧計: 6.72V）
    angle_voltage = np.pi * (1 - 6.72/50)
    ax.plot([0, radius*0.98*np.cos(angle_voltage)], [0, radius*0.98*np.sin(angle_voltage)], 
           'orange', linewidth=4, linestyle='--', label='針の位置（電圧計: 6.72V）', zorder=10)
    
    # 針の位置（電流計: 137.0mA、250mAレンジなので6.72V相当）
    # 137.0mA / 250mA * 50 = 27.4 → 実際は6.72Vスケールを使用
    angle_current = np.pi * (1 - 6.72/50)  # 電圧計と同じ位置
    ax.plot([0, radius*0.96*np.cos(angle_current)], [0, radius*0.96*np.sin(angle_current)], 
           'purple', linewidth=4, linestyle=':', label='針の位置（電流計: 137.0mA）', zorder=10)
    
    # スケールの説明
    ax.text(0, -0.8, 'OHMSスケール（緑）', ha='center', fontsize=11, color='green', fontweight='bold')
    ax.text(0, -1.2, 'DCV/mAスケール（青、0-50）', ha='center', fontsize=11, color='blue', fontweight='bold')
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-1.5, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('アナログテスターのスケール', fontsize=16, fontweight='bold', pad=20)
    ax.legend(loc='lower center', fontsize=9, ncol=1, framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig('figures/fig3_multimeter.png', dpi=300, bbox_inches='tight')
    print("アナログテスターのスケールを保存しました: figures/fig3_multimeter.png")
    plt.close()

def plot_oscilloscope():
    """オシロスコープの波形"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # パルス波形
    t = np.linspace(0, 10, 1000)
    pulse = np.zeros_like(t)
    pulse[(t >= 3.0) & (t <= 7.0)] = 250.0  # 250 mV
    
    ax.plot(t, pulse, 'y-', linewidth=3, label='波形')
    
    # グラウンドレベル
    ax.axhline(0, color='gray', linestyle='--', linewidth=1, alpha=0.5, label='グラウンドレベル')
    
    # 半値高さの線
    half_height = 125.0
    ax.axhline(half_height, color='red', linestyle=':', linewidth=2, label='半値高さ (125.0 mV)')
    
    # 波高の矢印
    ax.annotate('', xy=(1, 250), xytext=(1, 0),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=3))
    ax.text(1.5, 125, '波高\n250.0 mV', ha='left', va='center', 
           fontsize=12, color='blue', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # 半値幅の矢印
    ax.annotate('', xy=(7.0, 125), xytext=(3.0, 125),
                arrowprops=dict(arrowstyle='<->', color='green', lw=3))
    ax.text(5, 140, '半値幅\n400.0 ns', ha='center', va='bottom', 
           fontsize=12, color='green', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-50, 300)
    ax.set_xlabel('時間 (div, 100 ns/div)', fontsize=12)
    ax.set_ylabel('電圧 (mV)', fontsize=12)
    ax.set_title('オシロスコープの波形', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('figures/fig3_oscilloscope.png', dpi=300, bbox_inches='tight')
    print("オシロスコープの波形を保存しました: figures/fig3_oscilloscope.png")
    plt.close()

# ============================================
# 大問4: 論理回路の図
# ============================================

def plot_logic_circuit():
    """論理回路図（NANDとNOT）"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # 左：NANDゲート
    # 電源
    ax1.plot([0, 2], [4, 4], 'r-', linewidth=2)
    ax1.text(1, 4.2, 'Vcc (+5V)', ha='center', fontsize=10)
    
    # 抵抗
    ax1.plot([2, 2], [4, 3], 'k-', linewidth=3)
    ax1.text(2.3, 3.5, '470Ω', ha='left', fontsize=9)
    
    # トランジスタ（簡略化）
    ax1.plot([2, 2], [3, 1], 'k-', linewidth=2)
    ax1.plot([1.5, 2.5], [1, 1], 'k-', linewidth=2)
    ax1.plot([2, 2], [1, 0], 'k-', linewidth=2)
    
    # 入力
    ax1.plot([0, 1.5], [2.5, 2.5], 'b-', linewidth=2)
    ax1.text(-0.3, 2.5, 'In 1', ha='right', fontsize=10)
    ax1.plot([0, 1.5], [1.5, 1.5], 'b-', linewidth=2)
    ax1.text(-0.3, 1.5, 'In 2', ha='right', fontsize=10)
    
    # 出力
    ax1.plot([2, 4], [3, 3], 'g-', linewidth=2)
    ax1.text(4.2, 3, 'Out 1', ha='left', fontsize=10)
    
    ax1.set_xlim(-1, 5)
    ax1.set_ylim(-0.5, 5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('NANDゲート', fontsize=14, fontweight='bold')
    
    # 右：NOTゲート
    # 電源
    ax2.plot([0, 2], [4, 4], 'r-', linewidth=2)
    ax2.text(1, 4.2, 'Vcc (+5V)', ha='center', fontsize=10)
    
    # 抵抗
    ax2.plot([2, 2], [4, 3], 'k-', linewidth=3)
    ax2.text(2.3, 3.5, '470Ω', ha='left', fontsize=9)
    
    # トランジスタ
    ax2.plot([2, 2], [3, 1], 'k-', linewidth=2)
    ax2.plot([1.5, 2.5], [1, 1], 'k-', linewidth=2)
    ax2.plot([2, 2], [1, 0], 'k-', linewidth=2)
    
    # 入力
    ax2.plot([0, 1.5], [2, 2], 'b-', linewidth=2)
    ax2.text(-0.3, 2, 'In 3', ha='right', fontsize=10)
    
    # 出力
    ax2.plot([2, 4], [3, 3], 'g-', linewidth=2)
    ax2.text(4.2, 3, 'Out 2', ha='left', fontsize=10)
    
    ax2.set_xlim(-1, 5)
    ax2.set_ylim(-0.5, 5)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('NOTゲート', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('figures/fig4_logic_circuit.png', dpi=300, bbox_inches='tight')
    print("論理回路図を保存しました: figures/fig4_logic_circuit.png")
    plt.close()

def plot_counter_waveform():
    """4ビットカウンタの波形"""
    fig, axes = plt.subplots(5, 1, figsize=(12, 8), sharex=True)
    
    t = np.array([0, 1, 2, 3, 4, 5])
    
    # 入力 A
    input_wave = [0, 5, 0, 5, 0, 5]
    axes[0].plot(t, input_wave, 'b-', linewidth=2, drawstyle='steps-post')
    axes[0].set_ylabel('入力 A\n(V)', fontsize=10)
    axes[0].set_ylim(-1, 6)
    axes[0].grid(True, alpha=0.3)
    
    # 1ビット目
    bit1 = [5, 0, 5, 0, 5, 0]
    axes[1].plot(t, bit1, 'r-', linewidth=2, drawstyle='steps-post')
    axes[1].set_ylabel('1ビット目 Q\n(V)', fontsize=10)
    axes[1].set_ylim(-1, 6)
    axes[1].grid(True, alpha=0.3)
    
    # 2ビット目
    bit2 = [5, 0, 0, 5, 5, 0]
    axes[2].plot(t, bit2, 'g-', linewidth=2, drawstyle='steps-post')
    axes[2].set_ylabel('2ビット目 Q\n(V)', fontsize=10)
    axes[2].set_ylim(-1, 6)
    axes[2].grid(True, alpha=0.3)
    
    # 3ビット目
    bit3 = [5, 5, 5, 0, 0, 0]
    axes[3].plot(t, bit3, 'm-', linewidth=2, drawstyle='steps-post')
    axes[3].set_ylabel('3ビット目 Q\n(V)', fontsize=10)
    axes[3].set_ylim(-1, 6)
    axes[3].grid(True, alpha=0.3)
    
    # 4ビット目
    bit4 = [5, 5, 5, 0, 0, 0]
    axes[4].plot(t, bit4, 'c-', linewidth=2, drawstyle='steps-post')
    axes[4].set_ylabel('4ビット目 Q\n(V)', fontsize=10)
    axes[4].set_xlabel('時間 (クロック周期)', fontsize=12)
    axes[4].set_ylim(-1, 6)
    axes[4].grid(True, alpha=0.3)
    axes[4].set_xticks(t)
    
    fig.suptitle('4ビットカウンタの波形', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('figures/fig4_counter_waveform.png', dpi=300, bbox_inches='tight')
    print("4ビットカウンタの波形を保存しました: figures/fig4_counter_waveform.png")
    plt.close()

# ============================================
# 大問5: 確率と統計の図
# ============================================

def plot_gamma_detection():
    """ガンマ線検出の概念図"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 放射源（点）
    source = np.array([0, 0, 0])
    ax.scatter(*source, color='red', s=200, label='放射源')
    
    # 検出器（平面）
    detector_size = 0.2
    detector_x = np.array([-detector_size/2, detector_size/2, detector_size/2, -detector_size/2])
    detector_y = np.array([-detector_size/2, -detector_size/2, detector_size/2, detector_size/2])
    detector_z = np.array([1, 1, 1, 1])
    ax.plot_trisurf(detector_x, detector_y, detector_z, alpha=0.3, color='blue', label='検出器')
    
    # 距離の矢印
    ax.plot([0, 0], [0, 0], [0, 1], 'k--', linewidth=2, alpha=0.5)
    ax.text(0, 0, 0.5, 'r = 1.00 m', ha='center', fontsize=10)
    
    # 放射線（いくつかの線）
    for angle in np.linspace(0, 2*np.pi, 12):
        x_end = 0.5 * np.cos(angle)
        y_end = 0.5 * np.sin(angle)
        z_end = 1
        ax.plot([0, x_end], [0, y_end], [0, z_end], 'g-', linewidth=1, alpha=0.3)
    
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.5)
    ax.set_zlim(0, 1.5)
    ax.set_xlabel('X (m)', fontsize=10)
    ax.set_ylabel('Y (m)', fontsize=10)
    ax.set_zlabel('Z (m)', fontsize=10)
    ax.set_title('ガンマ線検出の概念図', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('figures/fig5_gamma_detection.png', dpi=300, bbox_inches='tight')
    print("ガンマ線検出の概念図を保存しました: figures/fig5_gamma_detection.png")
    plt.close()

def plot_poisson_distribution():
    """ポアソン分布の例"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # ポアソン分布（λ=400）
    try:
        from scipy.stats import poisson
        k = np.arange(350, 450)
        lambda_val = 400
        poisson_vals = poisson.pmf(k, lambda_val)
    except ImportError:
        # scipyがない場合は、より狭い範囲で計算
        import math
        k = np.arange(380, 420)
        lambda_val = 400
        poisson_vals = []
        for ki in k:
            # 対数を使って計算（オーバーフロー回避）
            log_prob = ki * np.log(lambda_val) - lambda_val - sum(np.log(np.arange(1, int(ki) + 1)))
            poisson_vals.append(np.exp(log_prob))
        poisson_vals = np.array(poisson_vals)
    
    ax.bar(k, poisson_vals, width=1, alpha=0.7, color='blue', edgecolor='black')
    ax.axvline(lambda_val, color='red', linestyle='--', linewidth=2, label=f'平均 = {lambda_val}')
    
    ax.set_xlabel('検出数 k', fontsize=12)
    ax.set_ylabel('確率 P(k; λ)', fontsize=12)
    ax.set_title(f'ポアソン分布（λ = {lambda_val}）', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('figures/fig5_poisson.png', dpi=300, bbox_inches='tight')
    print("ポアソン分布の例を保存しました: figures/fig5_poisson.png")
    plt.close()

# ============================================
# メイン関数
# ============================================

def main():
    """すべての図を生成"""
    print("物理実験学期末試験の図を生成します...")
    
    # 大問1
    plot_graph_improvements()
    plot_loglog_example()
    plot_semilog_example()
    
    # 大問2
    plot_pipe_section()
    
    # 大問3
    plot_vernier()
    plot_multimeter()
    plot_oscilloscope()
    
    # 大問4
    plot_logic_circuit()
    plot_counter_waveform()
    
    # 大問5
    plot_gamma_detection()
    plot_poisson_distribution()
    
    print("\nすべての図の生成が完了しました！")

if __name__ == '__main__':
    main()
