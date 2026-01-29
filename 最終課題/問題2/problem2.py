"""
問題2: 2準位系のエントロピーと温度の数値計算

統計力学における2準位系のエントロピーと温度を数値計算し、
Stirling近似との比較を行う。
"""

import numpy as np
import matplotlib.pyplot as plt
from math import log
import os
import matplotlib

# 日本語フォントの設定（macOS用）
import matplotlib.font_manager as fm

# macOSで利用可能な日本語フォントを優先順位順に設定
japanese_fonts = ['Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'AppleGothic', 
                  'Yu Gothic', 'Meiryo', 'Takao', 'IPAexGothic', 'IPAPGothic', 
                  'VL PGothic', 'Noto Sans CJK JP']

# 利用可能なフォントを確認
available_fonts = [f.name for f in fm.fontManager.ttflist]
selected_font = None
for font in japanese_fonts:
    if font in available_fonts:
        selected_font = font
        break

if selected_font:
    plt.rcParams['font.family'] = selected_font
    matplotlib.rcParams['font.sans-serif'] = [selected_font] + japanese_fonts
else:
    # フォントが見つからない場合はデフォルト設定
    plt.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = japanese_fonts

# マイナス記号の文字化けを防ぐ
plt.rcParams['axes.unicode_minus'] = False

# 図の保存先ディレクトリ
FIG_DIR = 'figures'
os.makedirs(FIG_DIR, exist_ok=True)


def calculate_entropy(N, M):
    """
    エントロピー S(M) = ln C(N, M) を計算
    
    数値安定性のため、階乗を直接計算せずに
    ln C(N, M) = Σ[k=1 to M] ln(N - k + 1) - Σ[k=1 to M] ln k
    を使用する。
    
    Parameters:
    -----------
    N : int
        粒子数
    M : int
        励起状態の粒子数
        
    Returns:
    --------
    float
        エントロピー S(M)
    """
    if M == 0 or M == N:
        return 0.0
    
    # ln C(N, M) = Σ[k=1 to M] ln(N - k + 1) - Σ[k=1 to M] ln k
    sum1 = sum(log(N - k + 1) for k in range(1, M + 1))
    sum2 = sum(log(k) for k in range(1, M + 1))
    
    return sum1 - sum2


def calculate_entropy_array(N):
    """
    すべてのMについてエントロピーを計算
    
    Parameters:
    -----------
    N : int
        粒子数
        
    Returns:
    --------
    numpy.ndarray
        M=0からM=Nまでのエントロピーの配列
    """
    S = np.zeros(N + 1)
    for M in range(N + 1):
        S[M] = calculate_entropy(N, M)
    return S


def stirling_entropy(x):
    """
    Stirling近似によるエントロピー密度
    
    s_approx(x) = -[x ln x + (1 - x) ln(1 - x)]
    
    Parameters:
    -----------
    x : float or numpy.ndarray
        正規化エネルギー (0 < x < 1)
        
    Returns:
    --------
    float or numpy.ndarray
        正規化エントロピー
    """
    x = np.asarray(x)
    # x = 0 または x = 1 の場合は 0 を返す
    result = np.zeros_like(x)
    mask = (x > 0) & (x < 1)
    result[mask] = -(x[mask] * np.log(x[mask]) + (1 - x[mask]) * np.log(1 - x[mask]))
    return result


def calculate_temperature(S, N):
    """
    エントロピーから温度を数値的に計算
    
    中心差分法を使用:
    T(M) ≈ 2 / [S(M+1) - S(M-1)]
    
    Parameters:
    -----------
    S : numpy.ndarray
        エントロピーの配列（M=0からM=Nまで）
    N : int
        粒子数
        
    Returns:
    --------
    numpy.ndarray
        温度の配列（M=1からM=N-1まで）
    numpy.ndarray
        対応するMの配列
    """
    T = np.zeros(N - 1)
    M_values = np.arange(1, N)
    
    for i, M in enumerate(M_values):
        dS = S[M + 1] - S[M - 1]
        if abs(dS) < 1e-10:  # S(M+1) = S(M-1) の場合（無限大温度）
            T[i] = np.inf
        else:
            T[i] = 2.0 / dS
    
    return T, M_values


def stirling_temperature(x):
    """
    Stirling近似による温度
    
    T_th(x) = [ln((1-x)/x)]^(-1)
    
    Parameters:
    -----------
    x : float or numpy.ndarray
        正規化エネルギー
        
    Returns:
    --------
    float or numpy.ndarray
        温度
    """
    x = np.asarray(x)
    result = np.zeros_like(x)
    # x = 0.5 で無限大になる点に注意
    mask = (x > 0) & (x < 1) & (x != 0.5)
    result[mask] = 1.0 / np.log((1 - x[mask]) / x[mask])
    # x = 0.5 の場合は無限大
    result[x == 0.5] = np.inf
    return result


def plot_entropy():
    """
    課題2, 3: エントロピーのプロットとStirling近似との比較
    """
    N_values = [20, 50, 100]
    colors = ['blue', 'red', 'green']
    linestyles = ['-', '--', '-.']
    
    plt.figure(figsize=(10, 7))
    
    # 数値計算結果のプロット
    for N, color, ls in zip(N_values, colors, linestyles):
        S = calculate_entropy_array(N)
        M = np.arange(N + 1)
        x = M / N  # 正規化エネルギー
        s = S / N  # 正規化エントロピー
        
        plt.plot(x, s, color=color, linestyle=ls, linewidth=2, 
                label=f'N = {N} (数値計算)', alpha=0.8)
    
    # Stirling近似の理論曲線
    x_theory = np.linspace(0.01, 0.99, 1000)
    s_theory = stirling_entropy(x_theory)
    plt.plot(x_theory, s_theory, 'k-', linewidth=2, 
            label='Stirling近似 (N → ∞)', alpha=0.7)
    
    plt.xlabel('正規化エネルギー $x = E/E_0 = M/N$', fontsize=14)
    plt.ylabel('正規化エントロピー $s = S/N$', fontsize=14)
    plt.title('2準位系のエントロピー', fontsize=16)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1)
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, 'entropy_plot.png'), dpi=300, bbox_inches='tight')
    print(f"エントロピーのプロットを保存: {FIG_DIR}/entropy_plot.png")
    plt.close()


def plot_temperature():
    """
    課題4, 5: 温度のプロットとStirling近似との比較
    """
    N_values = [20, 50, 100]
    colors = ['blue', 'red', 'green']
    linestyles = ['-', '--', '-.']
    
    plt.figure(figsize=(12, 7))
    
    # 数値計算結果のプロット
    for N, color, ls in zip(N_values, colors, linestyles):
        S = calculate_entropy_array(N)
        T, M_values = calculate_temperature(S, N)
        x = M_values / N  # 正規化エネルギー
        
        # 無限大温度を除外してプロット
        finite_mask = np.isfinite(T)
        plt.plot(x[finite_mask], T[finite_mask], 'o', color=color, 
                markersize=4, alpha=0.6, label=f'N = {N} (数値計算)')
        plt.plot(x[finite_mask], T[finite_mask], color=color, 
                linestyle=ls, linewidth=1.5, alpha=0.8)
    
    # Stirling近似の理論曲線
    x_theory = np.linspace(0.01, 0.49, 500)
    T_theory_left = stirling_temperature(x_theory)
    finite_mask_left = np.isfinite(T_theory_left)
    plt.plot(x_theory[finite_mask_left], T_theory_left[finite_mask_left], 
            'k-', linewidth=2, label='Stirling近似 (N → ∞)', alpha=0.7)
    
    x_theory_right = np.linspace(0.51, 0.99, 500)
    T_theory_right = stirling_temperature(x_theory_right)
    finite_mask_right = np.isfinite(T_theory_right)
    plt.plot(x_theory_right[finite_mask_right], T_theory_right[finite_mask_right], 
            'k-', linewidth=2, alpha=0.7)
    
    plt.xlabel('正規化エネルギー $x = E/E_0 = M/N$', fontsize=14)
    plt.ylabel('温度 $T$', fontsize=14)
    plt.title('2準位系の温度', fontsize=16)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1)
    plt.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    plt.axvline(x=0.5, color='gray', linestyle='--', linewidth=1, alpha=0.5, 
               label='$x = 0.5$ (無限大温度)')
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, 'temperature_plot.png'), dpi=300, bbox_inches='tight')
    print(f"温度のプロットを保存: {FIG_DIR}/temperature_plot.png")
    plt.close()


def plot_convergence():
    """
    エントロピー最大値の収束性を示す図
    """
    N_values = np.arange(10, 201, 10)  # N = 10, 20, ..., 200
    s_max_values = []
    s_theory = np.log(2)  # Stirling近似の理論値
    
    for N in N_values:
        S = calculate_entropy_array(N)
        s_max = np.max(S) / N
        s_max_values.append(s_max)
    
    plt.figure(figsize=(10, 6))
    plt.plot(N_values, s_max_values, 'o-', color='blue', linewidth=2, 
            markersize=6, label='数値計算結果')
    plt.axhline(y=s_theory, color='red', linestyle='--', linewidth=2, 
               label=f'Stirling近似の理論値 ($s = \\ln 2 \\approx {s_theory:.6f}$)')
    plt.xlabel('粒子数 $N$', fontsize=14)
    plt.ylabel('正規化エントロピーの最大値 $s_{\\max}$', fontsize=14)
    plt.title('エントロピー最大値の粒子数依存性', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, 'entropy_convergence.png'), dpi=300, bbox_inches='tight')
    print(f"エントロピー収束性のプロットを保存: {FIG_DIR}/entropy_convergence.png")
    plt.close()


def plot_temperature_convergence():
    """
    温度の収束性を示す図（特定のx値でのN依存性）
    """
    x_values = [0.3, 0.4, 0.6, 0.7]  # 異なる正規化エネルギーでの温度
    N_values = np.arange(20, 201, 10)  # N = 20, 30, ..., 200
    
    plt.figure(figsize=(12, 7))
    
    for x in x_values:
        T_numerical = []
        T_theory = stirling_temperature(x)
        
        for N in N_values:
            M = int(round(x * N))
            if M < 1 or M >= N:
                T_numerical.append(np.nan)
                continue
            
            S = calculate_entropy_array(N)
            T, M_vals = calculate_temperature(S, N)
            
            # Mに最も近いインデックスを見つける
            idx = np.argmin(np.abs(M_vals - M))
            if idx < len(T) and np.isfinite(T[idx]):
                T_numerical.append(T[idx])
            else:
                T_numerical.append(np.nan)
        
        # 数値計算結果をプロット
        valid_mask = ~np.isnan(T_numerical)
        plt.plot(N_values[valid_mask], np.array(T_numerical)[valid_mask], 
                'o-', linewidth=2, markersize=5, 
                label=f'$x = {x}$ (数値計算)')
        
        # 理論値を水平線で表示
        if np.isfinite(T_theory):
            plt.axhline(y=T_theory, linestyle='--', linewidth=1.5, alpha=0.7,
                       label=f'$x = {x}$ (Stirling近似, $T \\approx {T_theory:.3f}$)')
    
    plt.xlabel('粒子数 $N$', fontsize=14)
    plt.ylabel('温度 $T$', fontsize=14)
    plt.title('温度の粒子数依存性（異なる正規化エネルギーでの収束）', fontsize=16)
    plt.legend(fontsize=10, ncol=2)
    plt.grid(True, alpha=0.3)
    plt.yscale('symlog')  # 対称対数スケールで正負の温度を表示
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, 'temperature_convergence.png'), dpi=300, bbox_inches='tight')
    print(f"温度収束性のプロットを保存: {FIG_DIR}/temperature_convergence.png")
    plt.close()


def generate_numerical_table():
    """
    数値計算結果の表を生成（LaTeX形式）
    """
    N_values = [20, 50, 100, 200]
    results = []
    
    for N in N_values:
        S = calculate_entropy_array(N)
        M_max = np.argmax(S)
        x_max = M_max / N
        s_max = S[M_max] / N
        s_theory = np.log(2)
        error = abs(s_max - s_theory) / s_theory * 100
        
        results.append({
            'N': N,
            'M_max': M_max,
            'x_max': x_max,
            's_max': s_max,
            's_theory': s_theory,
            'error_percent': error
        })
    
    # LaTeX表形式で出力
    table_content = """
\\begin{table}[H]
\\centering
\\caption{エントロピー最大値の数値計算結果}
\\label{tab:entropy_max}
\\begin{tabular}{cccccc}
\\hline
$N$ & $M_{\\max}$ & $x_{\\max}$ & $s_{\\max}$ (数値) & $s_{\\max}$ (理論) & 相対誤差 [\\%] \\\\
\\hline
"""
    
    for r in results:
        table_content += f"{r['N']} & {r['M_max']} & {r['x_max']:.3f} & {r['s_max']:.6f} & {r['s_theory']:.6f} & {r['error_percent']:.3f} \\\\\n"
    
    table_content += """\\hline
\\end{tabular}
\\end{table}
"""
    
    # ファイルに保存
    with open(os.path.join(FIG_DIR, 'numerical_table.tex'), 'w', encoding='utf-8') as f:
        f.write(table_content)
    
    print(f"数値計算結果の表を保存: {FIG_DIR}/numerical_table.tex")
    
    return results


def main():
    """
    メイン処理
    """
    print("=" * 60)
    print("2準位系のエントロピーと温度の数値計算")
    print("=" * 60)
    
    # 課題1: エントロピーの計算（可視化のみなので計算は関数内で実行）
    print("\n課題1: エントロピーの数値計算")
    print("各Nについてエントロピーを計算中...")
    
    # 課題2, 3: エントロピーのプロット
    print("\n課題2, 3: エントロピーのプロットとStirling近似との比較")
    plot_entropy()
    
    # エントロピー最大値の収束性
    print("\nエントロピー最大値の収束性のプロット")
    plot_convergence()
    
    # 課題4: 温度の計算
    print("\n課題4: 温度の数値計算")
    print("各Nについて温度を計算中...")
    
    # 課題5: 温度のプロット
    print("\n課題5: 温度のプロットとStirling近似との比較")
    plot_temperature()
    
    # 温度の収束性
    print("\n温度の収束性のプロット")
    plot_temperature_convergence()
    
    # エントロピーの最大値の確認
    print("\nエントロピーの最大値の確認:")
    for N in [20, 50, 100]:
        S = calculate_entropy_array(N)
        M_max = np.argmax(S)
        x_max = M_max / N
        s_max = S[M_max] / N
        print(f"N = {N}: M = {M_max}, x = {x_max:.3f}, s_max = {s_max:.6f}")
    
    # 数値計算結果の表を生成
    print("\n数値計算結果の表を生成中...")
    generate_numerical_table()
    
    print("\n計算完了！")
    print(f"図は {FIG_DIR}/ ディレクトリに保存されました。")


if __name__ == '__main__':
    main()
