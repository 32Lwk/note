import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os
import sys
import time

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False

n_runs = int(sys.argv[1]) if len(sys.argv) > 1 else 5
T = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
m, gamma, kB = 1.0, 1.0, 1.0

os.makedirs('data', exist_ok=True)
os.makedirs('figures', exist_ok=True)

trajectories = []
for i in range(n_runs):
    output_file = os.path.join('data', f'trajectory_{i+1}.dat')
    with open(output_file, 'w') as f:
        subprocess.run(['./brownian_motion', str(T), str(m), str(gamma)], stdout=f)
    # 各試行で異なるシードを確保するため、1秒待機
    if i < n_runs - 1:
        time.sleep(1.0)
    data = np.loadtxt(output_file, comments='#')
    trajectories.append((data[:, 0], data[:, 1], data[:, 2]))

t = trajectories[0][0]
# 各試行のMSDを計算
msd_individual = []
for _, x, y in trajectories:
    msd_individual.append(x**2 + y**2)

# 平均MSDを計算
msd = np.array([np.mean([msd_individual[j][i] for j in range(n_runs)]) for i in range(len(t))])

D = kB * T / gamma
tau = m / gamma
msd_theory = (4.0 * kB * T / gamma) * (t - tau * (1.0 - np.exp(-t / tau)))
msd_diffusion = 4.0 * D * t

plt.figure(figsize=(10, 8))

# 5回の試行を個別に重ねて表示（色分け）
# より鮮明な色を使用し、確実に表示されるようにする
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']  # 明確な色を指定
for i in range(n_runs):
    # 個別試行を確実に表示するため、線の太さと透明度を調整
    # 各試行を異なる色で明確に表示（必ず表示されるようにzorder=1で設定）
    plt.plot(t, msd_individual[i], '-', linewidth=2.5, alpha=0.85, 
             color=colors[i % len(colors)], label=f'試行 {i+1}', zorder=1, solid_capstyle='round')

# 理論値と拡散極限を表示（個別試行の後、平均の前）
plt.plot(t, msd_theory, 'r--', linewidth=2.5, label='理論値（完全な式）', alpha=0.8, zorder=2)
plt.plot(t, msd_diffusion, 'b:', linewidth=2.5, label='拡散極限 (4Dt)', alpha=0.8, zorder=2)

# 平均を太い線で表示（最後に表示して前面に）
plt.plot(t, msd, 'k-', linewidth=3.5, label='平均 <r²(t)>', alpha=0.9, zorder=3)

plt.xlabel('時間 t', fontsize=12)
plt.ylabel('平均二乗変位 <r²(t)>', fontsize=12)
plt.title(f'平均二乗変位 (n={n_runs}回実行, T={T}, m={m}, γ={gamma})', fontsize=13)
plt.legend(loc='best', fontsize=10, framealpha=0.9)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join('figures', 'msd_plot.png'), dpi=150, bbox_inches='tight')
plt.close()
