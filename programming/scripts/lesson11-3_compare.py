import numpy as np
import matplotlib.pyplot as plt

# 日本語フォントの設定
plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False

# 初期条件
x0_list = [0.7, 1.0, 2.0, 3.0]
colors = ['blue', 'red', 'green', 'orange']
labels = ['r0=0.7', 'r0=1.0', 'r0=2.0', 'r0=3.0']

# 初期角運動量を計算
Lz0_list = [x0 * 1.0 for x0 in x0_list]  # Lz = m * (x * vy - y * vx) = x * 1.0

print("=== 角運動量の保存精度の比較 ===\n")

# 角運動量の誤差を比較
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i in range(4):
    # オイラー法のデータ
    try:
        data_euler = np.loadtxt(f'lesson11-1_case{i+1}.dat')
        t_euler = data_euler[:, 0]
        Lz_euler = data_euler[:, 1]
        Lz_error_euler = np.abs(Lz_euler - Lz0_list[i])
    except FileNotFoundError:
        print(f"警告: lesson11-1_case{i+1}.dat が見つかりません。")
        continue
    
    # ルンゲ・クッタ法のデータ
    try:
        data_rk4 = np.loadtxt(f'lesson11-3_case{i+1}.dat')
        t_rk4 = data_rk4[:, 0]
        Lz_rk4 = data_rk4[:, 1]
        Lz_error_rk4 = np.abs(Lz_rk4 - Lz0_list[i])
    except FileNotFoundError:
        print(f"警告: lesson11-3_case{i+1}.dat が見つかりません。")
        continue
    
    # 最大誤差と標準偏差を計算
    max_error_euler = np.max(Lz_error_euler) if len(Lz_error_euler) > 0 else 0.0
    max_error_rk4 = np.max(Lz_error_rk4) if len(Lz_error_rk4) > 0 else 0.0
    
    # 角運動量の誤差をプロット
    ax = axes[i]
    # 誤差をプロット（符号付きで表示）
    ax.plot(t_euler, Lz_euler - Lz0_list[i], color=colors[i], linestyle='--', 
            linewidth=2, label='オイラー法', alpha=0.7)
    ax.plot(t_rk4, Lz_rk4 - Lz0_list[i], color=colors[i], linestyle='-', 
            linewidth=2, label='ルンゲ・クッタ法')
    ax.set_ylabel('Lz - Lz0', fontsize=12)
    ax.set_xlabel('t', fontsize=12)
    ax.set_title(f'{labels[i]} (Lz0={Lz0_list[i]:.1f})', fontsize=12)
    
    # y軸の範囲を誤差の最大値に基づいて設定
    max_abs_error = max(max_error_euler, max_error_rk4)
    if max_abs_error > 0:
        # 誤差が見えるように適切な範囲を設定（対数スケールまたは線形スケール）
        if max_abs_error < 1e-10:
            # 非常に小さい誤差の場合は対数スケール
            ax.set_yscale('symlog', linthresh=1e-15)
            y_range = max(1e-15, max_abs_error * 1.5)
            ax.set_ylim(-y_range, y_range)
        else:
            # 通常の線形スケール
            y_range = max_abs_error * 1.2
            ax.set_ylim(-y_range, y_range)
    else:
        # 誤差が検出できない場合は固定範囲
        ax.set_ylim(-1e-15, 1e-15)
    
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)
    std_error_euler = np.std(Lz_error_euler) if len(Lz_error_euler) > 0 else 0.0
    std_error_rk4 = np.std(Lz_error_rk4) if len(Lz_error_rk4) > 0 else 0.0
    
    print(f"{labels[i]}:")
    print(f"  オイラー法 - 最大誤差: {max_error_euler:.10e}, 標準偏差: {std_error_euler:.10e}")
    print(f"  ルンゲ・クッタ法 - 最大誤差: {max_error_rk4:.10e}, 標準偏差: {std_error_rk4:.10e}")
    if max_error_euler > 1e-15:
        print(f"  最大誤差の減少率: {100.0 * (1.0 - max_error_rk4 / max_error_euler):.2f}%")
    if std_error_euler > 1e-15:
        print(f"  標準偏差の減少率: {100.0 * (1.0 - std_error_rk4 / std_error_euler):.2f}%")
    print()

plt.suptitle('062400506: 角運動量の保存精度の比較', fontsize=14)
plt.tight_layout()
plt.savefig('lesson11-3_Lz_comparison.png', dpi=300, bbox_inches='tight')
print("グラフを lesson11-3_Lz_comparison.png に保存しました。\n")
plt.close()

# 軌道の比較
print("=== 軌道の比較 ===\n")
fig, axes = plt.subplots(2, 2, figsize=(14, 14))
axes = axes.flatten()

for i in range(4):
    try:
        data_euler = np.loadtxt(f'lesson11-1_case{i+1}.dat')
        data_rk4 = np.loadtxt(f'lesson11-3_case{i+1}.dat')
        
        x_euler = data_euler[:, 2]
        y_euler = data_euler[:, 3]
        x_rk4 = data_rk4[:, 2]
        y_rk4 = data_rk4[:, 3]
        
        ax = axes[i]
        ax.plot(x_euler, y_euler, color=colors[i], linestyle='--', 
                linewidth=1.5, label='オイラー法', alpha=0.6)
        ax.plot(x_rk4, y_rk4, color=colors[i], linestyle='-', 
                linewidth=2, label='ルンゲ・クッタ法')
        ax.plot(x_euler[0], y_euler[0], 'o', color=colors[i], markersize=8, 
                markeredgecolor='black', markeredgewidth=1)
        ax.plot(0, 0, 'k*', markersize=12, label='原点')
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('y', fontsize=12)
        ax.set_title(f'{labels[i]}', fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.axis('equal')
        ax.legend(fontsize=9)
        
        # 各ケースに応じた適切な範囲を設定
        x_range = max(np.abs(x_euler).max(), np.abs(x_rk4).max())
        y_range = max(np.abs(y_euler).max(), np.abs(y_rk4).max())
        max_range = max(x_range, y_range) * 1.1  # 10%のマージンを追加
        
        # 最大範囲を10に制限（軌道の主要部分を見やすくするため）
        max_range = min(max_range, 10.0)
        ax.set_xlim(-max_range, max_range)
        ax.set_ylim(-max_range, max_range)
    except FileNotFoundError:
        print(f"警告: データファイルが見つかりません（case {i+1}）")
        continue

plt.suptitle('062400506: 軌道の比較', fontsize=14)
plt.tight_layout()
plt.savefig('lesson11-3_orbit_comparison.png', dpi=300, bbox_inches='tight')
print("グラフを lesson11-3_orbit_comparison.png に保存しました。\n")
plt.close()

# 軌道の精度比較（周期後の位置の誤差）
print("=== 軌道の精度比較（最初と最後の位置の比較）===\n")
for i in range(4):
    try:
        data_euler = np.loadtxt(f'lesson11-1_case{i+1}.dat')
        data_rk4 = np.loadtxt(f'lesson11-3_case{i+1}.dat')
        
        # 最初の位置
        x0_euler = data_euler[0, 2]
        y0_euler = data_euler[0, 3]
        x0_rk4 = data_rk4[0, 2]
        y0_rk4 = data_rk4[0, 3]
        
        # 最後の位置
        xf_euler = data_euler[-1, 2]
        yf_euler = data_euler[-1, 3]
        xf_rk4 = data_rk4[-1, 2]
        yf_rk4 = data_rk4[-1, 3]
        
        # 原点からの距離
        r0_euler = np.sqrt(x0_euler**2 + y0_euler**2)
        rf_euler = np.sqrt(xf_euler**2 + yf_euler**2)
        r0_rk4 = np.sqrt(x0_rk4**2 + y0_rk4**2)
        rf_rk4 = np.sqrt(xf_rk4**2 + yf_rk4**2)
        
        print(f"{labels[i]}:")
        print(f"  オイラー法 - 初期距離: {r0_euler:.10f}, 最終距離: {rf_euler:.10f}, 変化: {rf_euler - r0_euler:.10e}")
        print(f"  ルンゲ・クッタ法 - 初期距離: {r0_rk4:.10f}, 最終距離: {rf_rk4:.10f}, 変化: {rf_rk4 - r0_rk4:.10e}")
        
        # 軌道の範囲を比較
        x_euler = data_euler[:, 2]
        y_euler = data_euler[:, 3]
        x_rk4 = data_rk4[:, 2]
        y_rk4 = data_rk4[:, 3]
        
        r_euler = np.sqrt(x_euler**2 + y_euler**2)
        r_rk4 = np.sqrt(x_rk4**2 + y_rk4**2)
        
        r_min_euler = np.min(r_euler)
        r_max_euler = np.max(r_euler)
        r_min_rk4 = np.min(r_rk4)
        r_max_rk4 = np.max(r_rk4)
        
        print(f"  オイラー法 - 最小距離: {r_min_euler:.10f}, 最大距離: {r_max_euler:.10f}, 範囲: {r_max_euler - r_min_euler:.10e}")
        print(f"  ルンゲ・クッタ法 - 最小距離: {r_min_rk4:.10f}, 最大距離: {r_max_rk4:.10f}, 範囲: {r_max_rk4 - r_min_rk4:.10e}")
        print()
    except FileNotFoundError:
        continue

print("=== 比較完了 ===\n")

