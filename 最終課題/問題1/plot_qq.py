"""
Q-Q プロット：正規分布・運動エネルギー分布の分位点比較。
理論分位点 vs サンプル分位点が直線に乗れば、理論分布と整合的。
"""
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os
from scipy import stats

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False

os.makedirs('data', exist_ok=True)
os.makedirs('figures', exist_ok=True)


def simulate_brownian_motion(T, m, gamma, kB=1.0, dt=0.01, n_steps=1000, seed=None):
    if seed is not None:
        np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    coeff1 = gamma / m
    coeff2 = np.sqrt(2.0 * gamma * kB * T / m)
    vx_arr, vy_arr = [], []
    for n in range(n_steps + 1):
        vx_arr.append(vx)
        vy_arr.append(vy)
        if n == n_steps:
            break
        eta_x = np.random.normal(0, 1)
        eta_y = np.random.normal(0, 1)
        vx = vx - coeff1 * vx * dt + coeff2 * np.sqrt(dt) * eta_x
        vy = vy - coeff1 * vy * dt + coeff2 * np.sqrt(dt) * eta_y
        rx += vx * dt
        ry += vy * dt
    E = 0.5 * m * (np.array(vx_arr) ** 2 + np.array(vy_arr) ** 2)
    return E


# 正規分布 Q-Q（Box-Muller または numpy）
n_samples = 2000
path = os.path.join('data', 'normal_rand_qq.dat')
exe = './normal_rand'
if os.path.isfile(exe):
    with open(path, 'w') as f:
        subprocess.run([exe, str(n_samples)], stdout=f)
    normal_data = np.loadtxt(path)
else:
    np.random.seed(42)
    normal_data = np.random.standard_normal(n_samples)

# エネルギー
kB, T, m, gamma = 1.0, 1.0, 1.0, 1.0
n_runs = 20
energies = []
for r in range(n_runs):
    E = simulate_brownian_motion(T, m, gamma, kB=1.0, dt=0.01, n_steps=1000, seed=r)
    energies.extend(E)
energies = np.array(energies)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左: 正規分布 Q-Q
ax = axes[0]
stats.probplot(normal_data, dist='norm', plot=ax)
ax.set_title(r'正規分布の Q-Q プロット（$N(0,1)$）')
ax.grid(True, alpha=0.3)

# 右: 指数分布 Q-Q（エネルギー）
ax = axes[1]
# scipy probplot は'expon'をサポート。scale=kB*T, loc=0.
stats.probplot(energies, dist='expon', sparams=(0, kB * T), plot=ax)
ax.set_title(r'運動エネルギー分布の Q-Q プロット（指数分布 $\sim e^{-E/k_B T}$）')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figures/qq_plots.png', dpi=150)
plt.close()
print("qq_plots.png を保存しました。")
