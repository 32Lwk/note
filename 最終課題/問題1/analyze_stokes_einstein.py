"""
Stokes-Einstein 関係: D = k_B T / γ。
球形粒子では γ = 6πηa なので D = k_B T / (6πηa)。γ を変えて D(1/γ) の線形性を確認。
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
    x, y = np.zeros(n_steps + 1), np.zeros(n_steps + 1)
    for n in range(n_steps):
        vx = vx - c1 * vx * dt + c2 * np.sqrt(dt) * np.random.normal(0, 1)
        vy = vy - c1 * vy * dt + c2 * np.sqrt(dt) * np.random.normal(0, 1)
        rx += vx * dt
        ry += vy * dt
        x[n + 1], y[n + 1] = rx, ry
    return t, x, y


def fit_D(t, x, y):
    n = len(t)
    i0 = n // 2
    return np.mean((x[i0:] ** 2 + y[i0:] ** 2) / (4.0 * t[i0:]))


os.makedirs('figures', exist_ok=True)

kB, T, m = 1.0, 1.0, 1.0
dt, n_steps, n_runs = 0.01, 1000, 25
gamma_vals = np.array([0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0])
inv_gamma = 1.0 / gamma_vals
D_theory = kB * T / gamma_vals
D_sim, D_err = [], []
for g in gamma_vals:
    Ds = [fit_D(*simulate(T, m, g, kB, dt, n_steps, r)) for r in range(n_runs)]
    D_sim.append(np.mean(Ds))
    D_err.append(np.std(Ds))

fig, ax = plt.subplots(figsize=(8, 5))
ax.errorbar(inv_gamma, D_sim, yerr=D_err, fmt='bs', capsize=5, label='シミュレーション')
ax.plot(inv_gamma, D_theory, 'r--', lw=2, label=r'$D = k_B T/\gamma$')
ax.set_xlabel(r'$1/\gamma$')
ax.set_ylabel(r'拡散係数 $D$')
ax.set_title(r'Stokes–Einstein 型関係 $D = k_B T/\gamma$（球形なら $\gamma=6\pi\eta a$）')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figures/stokes_einstein.png', dpi=150)
plt.close()
print("stokes_einstein.png を保存しました。")
