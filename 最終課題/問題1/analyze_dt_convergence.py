"""
時間刻み Δt の収束性：オイラー・マルヤマ法で Δt を変え、拡散係数 D が理論に収束するか確認。
"""
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['font.family'] = 'Hiragino Sans'
plt.rcParams['axes.unicode_minus'] = False


def simulate(T, m, gamma, kB, dt, n_steps, seed):
    np.random.seed(seed)
    rx, ry = 0.0, 0.0
    vx, vy = 0.0, 0.0
    c1 = gamma / m
    c2 = np.sqrt(2.0 * gamma * kB * T / m)
    t = np.arange(n_steps + 1) * dt
    x = np.zeros(n_steps + 1)
    y = np.zeros(n_steps + 1)
    for n in range(n_steps):
        vx = vx - c1 * vx * dt + c2 * np.sqrt(dt) * np.random.normal(0, 1)
        vy = vy - c1 * vy * dt + c2 * np.sqrt(dt) * np.random.normal(0, 1)
        rx += vx * dt
        ry += vy * dt
        x[n + 1] = rx
        y[n + 1] = ry
    return t, x, y


def fit_D(t, x, y):
    n = len(t)
    i0 = n // 2
    t_f = t[i0:]
    msd = x[i0:] ** 2 + y[i0:] ** 2
    return np.mean(msd / (4.0 * t_f))


os.makedirs('figures', exist_ok=True)

kB, T, m, gamma = 1.0, 1.0, 1.0, 1.0
D_theory = kB * T / gamma
t_total = 15.0
n_runs = 30
dt_list = [0.1, 0.05, 0.03, 0.02, 0.01, 0.005, 0.002]
D_means, D_stds = [], []

for dt in dt_list:
    n_steps = int(t_total / dt)
    Ds = [fit_D(*simulate(T, m, gamma, kB, dt, n_steps, r)) for r in range(n_runs)]
    D_means.append(np.mean(Ds))
    D_stds.append(np.std(Ds))

fig, ax = plt.subplots(figsize=(8, 5))
ax.errorbar(dt_list, D_means, yerr=D_stds, fmt='bs', capsize=5, label='シミュレーション')
ax.axhline(D_theory, color='r', linestyle='--', lw=2, label=rf'理論 $D = k_B T/\gamma = {D_theory:.2f}$')
ax.set_xlabel(r'時間刻み $\Delta t$')
ax.set_ylabel('拡散係数 $D$')
ax.set_title(r'$\Delta t$ 依存性：総時間 $t = {:.1f}$ 固定、$n={}$ 試行'.format(t_total, n_runs))
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xscale('log')
plt.tight_layout()
plt.savefig('figures/dt_convergence.png', dpi=150)
plt.close()
print("dt_convergence.png を保存しました。")
