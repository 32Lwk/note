#!/usr/bin/env python3
"""
問題 5-2: ポテンシャルの井戸での束縛状態
束縛状態が存在しない条件を求めるためのグラフ描画プログラム
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 日本語フォントの設定
rcParams['font.family'] = 'DejaVu Sans'

def left_side(y, lam):
    """左辺: sqrt(λ - y²) / y"""
    # y > 0 かつ y < sqrt(λ) の範囲でのみ定義
    mask = (y > 0) & (y < np.sqrt(lam))
    result = np.zeros_like(y)
    result[mask] = np.sqrt(lam - y[mask]**2) / y[mask]
    result[~mask] = np.nan
    return result

def right_side(y):
    """右辺: tan(y - π/2)"""
    return np.tan(y - np.pi/2)

def plot_intersection(lam_values):
    """異なるλ値での左辺と右辺をプロット"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()
    
    for idx, lam in enumerate(lam_values):
        ax = axes[idx]
        
        # yの範囲: 0 < y < sqrt(λ) かつ tanが定義される範囲を考慮
        y_max = min(np.sqrt(lam), 3.0)  # 適切な範囲に制限
        y = np.linspace(0.01, y_max, 1000)
        
        # 左辺
        fL = left_side(y, lam)
        
        # 右辺（tanの特異点を避ける）
        fR = right_side(y)
        # tanの特異点付近でNaNを設定（より大きな閾値を使用）
        fR = np.where(np.abs(fR) > 50, np.nan, fR)
        
        ax.plot(y, fL, 'b-', linewidth=2, label=f'左辺: $\\sqrt{{\\lambda - y^2}}/y$')
        ax.plot(y, fR, 'r--', linewidth=2, label=f'右辺: $\\tan(y - \\pi/2)$')
        
        # 交点を探す
        # 方程式: sqrt(λ - y²)/y = tan(y - π/2)
        # これを sqrt(λ - y²)/y - tan(y - π/2) = 0 として解く
        diff = fL - fR
        valid = ~(np.isnan(fL) | np.isnan(fR))
        intersection_found = False
        
        if np.sum(valid) > 1:
            valid_indices = np.where(valid)[0]
            
            # 方法1: 符号変化を探す
            for i in range(len(valid_indices) - 1):
                idx1 = valid_indices[i]
                idx2 = valid_indices[i + 1]
                
                # 符号変化があるかチェック
                if diff[idx1] * diff[idx2] < 0:
                    # 交点を線形補間で推定
                    y1, y2 = y[idx1], y[idx2]
                    d1, d2 = diff[idx1], diff[idx2]
                    if abs(d2 - d1) > 1e-10:
                        y_intersect = y1 - d1 * (y2 - y1) / (d2 - d1)
                        # 範囲内かチェック
                        if y1 <= y_intersect <= y2 and y_intersect > 0 and y_intersect < np.sqrt(lam):
                            f_intersect = np.sqrt(lam - y_intersect**2) / y_intersect
                            ax.plot(y_intersect, f_intersect, 'go', markersize=10, 
                                   label=f'交点: y ≈ {y_intersect:.3f}')
                            intersection_found = True
                            break
            
            # 方法2: 最小差を探す（符号変化がない場合のフォールバック）
            if not intersection_found:
                abs_diff = np.abs(diff[valid])
                min_idx = np.nanargmin(abs_diff)
                min_diff = abs_diff[min_idx]
                
                # より緩い閾値で交点を探す
                if min_diff < 1.0:  # 閾値を緩める
                    y_intersect = y[valid][min_idx]
                    if y_intersect > 0 and y_intersect < np.sqrt(lam):
                        f_intersect = fL[valid][min_idx]
                        ax.plot(y_intersect, f_intersect, 'go', markersize=10, 
                               label=f'近似交点: y ≈ {y_intersect:.3f} (差={min_diff:.4f})')
                        intersection_found = True
        
        ax.set_xlabel('$y = qa$', fontsize=12)
        ax.set_ylabel('関数値', fontsize=12)
        ax.set_title(f'$\\lambda = {lam:.3f}$', fontsize=14)
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=10, loc='best')
        # y軸の範囲を適切に設定（データに基づいて自動調整）
        y_data = np.concatenate([fL[~np.isnan(fL)], fR[~np.isnan(fR)]])
        if len(y_data) > 0:
            y_min, y_max = np.nanmin(y_data), np.nanmax(y_data)
            y_range = y_max - y_min
            if y_range > 0:
                ax.set_ylim(y_min - 0.1*y_range, y_max + 0.1*y_range)
            else:
                ax.set_ylim(-5, 5)
        else:
            ax.set_ylim(-5, 5)
    
    plt.tight_layout()
    plt.savefig('problem5-2_well_intersection.png', dpi=150, bbox_inches='tight')
    print("グラフを problem5-2_well_intersection.png に保存しました。")
    # 注意: plt.show()は最後に1回だけ呼ぶ（この関数内では呼ばない）
    plt.close()

def find_intersection(lam, y_start=0.01, y_end=None, tol=1e-6):
    """与えられたλに対して交点を探す（二分法）"""
    if y_end is None:
        y_end = min(np.sqrt(lam) - 0.001, 4.0)
    
    def equation(y):
        """f_L(y) - f_R(y) = 0 を解く"""
        if y <= 0 or y >= np.sqrt(lam):
            return np.nan
        fL = np.sqrt(lam - y**2) / y
        fR = np.tan(y - np.pi/2)
        # tanの特異点を避ける
        if np.abs(fR) > 100:
            return np.nan
        return fL - fR
    
    # 符号変化を探す
    n_points = 10000
    y_vals = np.linspace(y_start, y_end, n_points)
    eq_vals = []
    for y in y_vals:
        val = equation(y)
        if not np.isnan(val):
            eq_vals.append((y, val))
    
    if len(eq_vals) < 2:
        return None
    
    # 符号変化を探す
    for i in range(len(eq_vals) - 1):
        y1, val1 = eq_vals[i]
        y2, val2 = eq_vals[i+1]
        if val1 * val2 < 0:  # 符号変化あり
            # 二分法で交点を求める
            a, b = y1, y2
            for _ in range(50):
                c = (a + b) / 2
                val_c = equation(c)
                if np.isnan(val_c) or abs(val_c) < tol:
                    return c
                if val1 * val_c < 0:
                    b = c
                    val2 = val_c
                else:
                    a = c
                    val1 = val_c
            return (a + b) / 2
    
    return None

def find_critical_lambda():
    """束縛状態が存在しない臨界のλを求める"""
    # 理論的には、y = π/2 のとき λ = (π/2)² = π²/4 が臨界
    # より正確に求めるため、二分法を使用
    theoretical_critical = np.pi**2 / 4
    
    print(f"理論的な臨界値: λ = π²/4 ≈ {theoretical_critical:.6f}")
    
    # 数値的に確認
    lam_low = 0.1
    lam_high = 5.0
    tol = 1e-6
    
    print("\n数値的に臨界値を求めています...")
    for _ in range(50):
        lam_mid = (lam_low + lam_high) / 2
        intersection = find_intersection(lam_mid, y_end=min(np.sqrt(lam_mid), np.pi/2 - 0.01))
        
        if intersection is not None:
            lam_low = lam_mid
        else:
            lam_high = lam_mid
        
        if lam_high - lam_low < tol:
            break
    
    critical_lam = (lam_low + lam_high) / 2
    
    print(f"\n数値的に求めた臨界値: λ ≈ {critical_lam:.6f}")
    print(f"理論値との差: {abs(critical_lam - theoretical_critical):.6f}")
    
    print(f"\n束縛状態が存在しない臨界条件:")
    print(f"λ < π²/4 ≈ {theoretical_critical:.6f}")
    print(f"すなわち: 2mV₀a²/ħ² < π²/4")
    print(f"したがって: V₀ < (π²/4) × ħ²/(2ma²) = π²ħ²/(8ma²)")
    
    return critical_lam

def plot_detailed_analysis():
    """詳細な解析: 左辺と右辺の挙動を詳しく調べる"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # 左辺の挙動
    lam_test = 2.0
    y = np.linspace(0.01, np.sqrt(lam_test) - 0.01, 1000)
    fL = left_side(y, lam_test)
    
    ax1.plot(y, fL, 'b-', linewidth=2, label=f'左辺 ($\\lambda = {lam_test}$)')
    ax1.set_xlabel('$y$', fontsize=12)
    ax1.set_ylabel('左辺の値', fontsize=12)
    ax1.set_title('左辺: $\\sqrt{\\lambda - y^2}/y$ の挙動', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=11)
    
    # 右辺の挙動
    y2 = np.linspace(0.01, 4.0, 1000)
    fR = right_side(y2)
    fR = np.where(np.abs(fR) > 10, np.nan, fR)
    
    ax2.plot(y2, fR, 'r--', linewidth=2, label='右辺: $\\tan(y - \\pi/2)$')
    ax2.set_xlabel('$y$', fontsize=12)
    ax2.set_ylabel('右辺の値', fontsize=12)
    ax2.set_title('右辺: $\\tan(y - \\pi/2)$ の挙動', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=11)
    ax2.set_ylim(-5, 5)
    
    plt.tight_layout()
    plt.savefig('problem5-2_well_detailed.png', dpi=150, bbox_inches='tight')
    print("詳細解析グラフを problem5-2_well_detailed.png に保存しました。")
    # 注意: plt.show()は最後に1回だけ呼ぶ（この関数内では呼ばない）
    plt.close()

if __name__ == '__main__':
    print("問題 5-2: ポテンシャルの井戸での束縛状態の解析")
    print("=" * 60)
    
    # 異なるλ値でのグラフ
    # 注意: λ < π²/4 ≈ 2.47 の場合は交点が存在しない（束縛状態が存在しない）
    #       λ > π²/4 の場合は交点が存在する（束縛状態が存在する）
    lam_values = [1.0, 2.0, 2.5, 4.0]  # 交点が存在しない場合と存在する場合を含む
    plot_intersection(lam_values)
    
    # 詳細解析
    plot_detailed_analysis()
    
    # 臨界条件を求める
    critical_lam = find_critical_lambda()
    
    print("\n解析完了！")
    print("\nグラフを表示するには、保存されたPNGファイルを開くか、")
    print("以下のコマンドで画像を確認してください:")
    print("  open problem5-2_well_intersection.png")
    print("  open problem5-2_well_detailed.png")
    
    # グラフを表示（オプション - 環境によっては表示されない場合がある）
    # plt.show()

