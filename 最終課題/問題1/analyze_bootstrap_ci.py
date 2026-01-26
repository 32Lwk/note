"""
拡散係数 D のブートストラップ信頼区間。
各試行で D をフィットし、D のリストをリサンプルして 95% CI を求める。
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

kB, T, m, gamma = 1.0, 1.0, 1.0, 1.0
D_theory = kB * T / gamma
dt, n_steps, n_runs = 0.01, 1000, 50
B = 2000  # ブートストラップ反復

Ds = np.array([fit_D(*simulate(T, m, gamma, kB, dt, n_steps, r)) for r in range(n_runs)])
boot_means = []
np.random.seed(123)
for _ in range(B):
    idx = np.random.choice(n_runs, size=n_runs, replace=True)
    boot_means.append(np.mean(Ds[idx]))
boot_means = np.array(boot_means)
ci_lo, ci_hi = np.percentile(boot_means, [2.5, 97.5])
d_mean = np.mean(Ds)
d_std = np.std(Ds)
print(f"D_mean={d_mean:.4f}, D_std={d_std:.4f}, 95% CI=[{ci_lo:.4f}, {ci_hi:.4f}], D_theory={D_theory:.4f}")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
ax = axes[0]
ax.hist(boot_means, bins=50, density=True, alpha=0.7, color='steelblue', edgecolor='black')
ax.axvline(d_mean, color='red', lw=2, label=rf'平均 $\hat{{D}} = {d_mean:.4f}$')
ax.axvline(ci_lo, color='green', ls='--', lw=2, label=rf'95% CI [{ci_lo:.3f}, {ci_hi:.3f}]')
ax.axvline(ci_hi, color='green', ls='--', lw=2)
ax.axvline(D_theory, color='orange', ls=':', lw=2, label=rf'理論 $D = {D_theory:.4f}$')
ax.set_xlabel('拡散係数 $D$')
ax.set_ylabel('密度')
ax.set_title('ブートストラップ分布（$D$ の推定値）')
ax.legend()
ax.grid(True, alpha=0.3)

ax = axes[1]
ax.errorbar([0], [d_mean], yerr=[[d_mean - ci_lo], [ci_hi - d_mean]], fmt='bs', capsize=8, markersize=10, label='ブートストラップ 95% CI')
ax.axhline(D_theory, color='r', ls='--', lw=2, label=rf'理論 $D = k_B T/\gamma$')
ax.set_xlim(-0.5, 0.5)
ax.set_xticks([])
ax.set_ylabel('拡散係数 $D$')
ax.set_title('$D$ の点推定と 95% 信頼区間')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figures/bootstrap_ci.png', dpi=150)
plt.close()
print("bootstrap_ci.png を保存しました。")
